# exegenius task 0084-write-gaussian-resampling

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
- Cyclic convolution (also: convolution modulo x^S - 1)
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

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Discrete Fourier transform](fourier-transform.md): The map sending a vector u of length q to the vector whose k-th entry is (1/q) times the sum over j of u_j times exp(−2πijk/q).
  Shown as: Gaussian resampling *<predicate>* Discrete Fourier transform
- [Multidimensional transform with power-of-two axes](multidim-transform.md): A transform on an array indexed by several coordinates, each with length a power of two, obtained as a tensor product of one-dimensional Fourier transforms.
  Shown as: Gaussian resampling *<predicate>* Multidimensional transform with power-of-two axes

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
- [Cyclic convolution](cyclic-convolution.md)
- [Radix-digit convolution](radix-digit-convolution.md)
- [Root of unity](roots-of-unity.md)
- [Polynomial ring modulo yʳ + 1](polynomial-ring.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Bluestein's chirp identity](bluestein.md)
- [Chinese-remainder axis map](crt-axis-map.md)
- [Exact recovery by rounding and carries](exact-recovery.md)
- [Fixed-tape integer multiplication with a power saving](fixed-tape-multiplication.md)

## Evidence from the sources, with the paragraph around each quote

- "Gaussian resampling then expresses each source Fourier transform through a" (paper)

  > The remaining proof places these procedures inside the multiplication reduction and accounts for every change of representation. First, the radix-digit coefficient list is placed on a product of distinct prime cyclic axes by a Chinese-remainder map that preserves convolution. Section~\ref{sec:assembly} implements this map through triangular controlled shifts and charged axis moves. Gaussian resampling then expresses each source Fourier transform through a power-of-two tensor transform. Section~\ref{sec:resampling} retains the source and target coordinate permutations in the transform identity, so they need not be executed as separate full sorts.


## Sources (read from disk as needed)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The reader cannot follow this step: "The proof builds $A$ and $B_0$ from Gaussian-weighted resampling." (The page never gives formulas for A or B_0, nor says which resampling map is meant. The reader cannot check that maps with these properties exist or that they satisfy the identity, so the identity is not followable from the page.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "An exact Fourier identity relates these sums to $P_sF_s$ and $P_tF_t$." (The identity is named but not stated. The reader cannot see which sums it applies to or how it gives the target identity.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "A correction map close to the identity is inverted by a Neumann series, which gives the contraction bounds." (The page does not say which correction map this is, in what sense it is close to the identity, or how inverting it yields the norm bounds on A and B_0.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "The factor $2^{2\alpha^2}$ absorbs the normalizations of the maps." (Since the maps A and B_0 are never defined, their normalizations are not given, so the claim that this factor absorbs them cannot be checked.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "The integer product needs pairwise coprime transform lengths" (A cited claim about the source's integer multiplication scheme. The page does not say what the integer product is or why it needs coprime lengths, and the claim plays no role in the argument that follows.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "Its usual implementation sorts twice on each coordinate." (A cited claim about another implementation. The page does not say what the sorting is, how it corresponds to P_s, P_t or the identity, or why it is the point of the identity.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "Thus Gaussian resampling expresses each source transform through a" (Presented as following from the identity. The identity uses exact maps A and B_0 that the page never gives, and the computable approximations are deferred to the sources, so the reader cannot check that the conclusion follows from this page.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- Say what $v$ denotes where it is first used (for a size or count, what it counts): "$(P_t v)_k=v_{-sk}$" (The page never says what v denotes. The only earlier bindings of v (gaussian-dyadic, frame) are different objects, and this page does not say that v is a vector of length t or a vector of any kind.)
- Explain "Neumann series" in a sentence where it is first used.

## Previous version (revise it)

It has 285 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 356 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

Gaussian resampling is a rewriting of a Fourier transform as a transform with power-of-two axis lengths, with the source and target coordinate permutations kept inside the identity. The integer product needs pairwise coprime transform lengths, while the synthetic transforms use powers of two. <cite data-source="paper">Gaussian resampling connects these two shapes.</cite>

Let $s$ be the length of the source transform, the number of coordinates it acts on. Let $t>s$ be the target length, with $\gcd(s,t)=1$. Here $F_q$ is the transform of length $q$.

$$(F_q u)_k=\frac1q\sum_{j=0}^{q-1}u_j e^{-2\pi i jk/q}.$$

Gaussian resampling rewrites each [Discrete Fourier transform](fourier-transform.md) of length $s$ as follows. Let $P_s$ and $P_t$ be the coordinate permutations $(P_s u)_j=u_{tj}$ and $(P_t v)_k=v_{-sk}$, with indices taken modulo $s$ and $t$.

Here $\alpha$ is a fixed integer parameter that sets the width of the Gaussian weights below. The maps $A:\mathbb C^s\to\mathbb C^t$ and $B_0:\mathbb C^t\to\mathbb C^s$ are contractions, that is, linear maps that never increase the maximum-modulus norm of a vector.

The claim is the identity

$$P_sF_s=2^{2\alpha^2}B_0P_tF_tA.$$

Read the left side as transforming by $F_s$ and then permuting by $P_s$. The right side maps the input to length $t$ by $A$, applies $F_t$, permutes by $P_t$, and returns to length $s$ by $B_0$. The factor $2^{2\alpha^2}$ absorbs the normalizations of the maps.

The proof builds $A$ and $B_0$ from Gaussian-weighted resampling. Each output coordinate of one resampling map is a sum over all integers $j$ of $e^{-\pi\alpha^{-2}(j-sk/t)^2}$ times an input entry, a Gaussian weight centred at $sk/t$. An exact Fourier identity relates these sums to $P_sF_s$ and $P_tF_t$. A correction map close to the identity is inverted by a Neumann series, which gives the contraction bounds.

Its usual implementation sorts twice on each coordinate. This is the point of the identity. <cite data-source="paper">We retain both permutations in the transform formula and compute that formula directly.</cite>

Thus Gaussian resampling expresses each source transform through a [Multidimensional transform with power-of-two axes](multidim-transform.md). The sources compute approximations to $A$ and $B_0$ on Gaussian dyadic inputs, with error bounds; this page states only the exact identity.

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

Write the body to `exegenius/tasks/0084-write-gaussian-resampling.answer.md` and the JSON to `exegenius/tasks/0084-write-gaussian-resampling.answer.json`, then run `exegenius submit 0084-write-gaussian-resampling` in the project directory. If submit rejects the answer, fix the answer and submit again.
