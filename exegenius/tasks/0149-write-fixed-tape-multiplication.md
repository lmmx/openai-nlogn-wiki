# exegenius task 0149-write-fixed-tape-multiplication

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
- Chinese-remainder axis map (also: Chinese-remainder address map)
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

Concept: Fixed-tape integer multiplication with a power saving
Gloss: A deterministic fixed-tape Turing machine that multiplies two n-bit integers exactly in O(n(lg n)^(1−κ)) worst-case time, for a fixed κ = 2^(−182), disproving the n log n optimality conjecture in this model.
Also called: main theorem

## This page in the argument

The step: The integer product is computed exactly on one fixed-tape machine in $O(n(\lg n)^{1-\kappa})$ worst-case time, for $\kappa=2^{-182}$.
How: reduce exact multiplication to convolution of radix digits on distinct prime axes, compute the convolution by synthetic transforms on tape layouts, and bound the total tape cost with a power saving
Why: Scanning the stored bits at each transform level already costs $\Theta(n\log n)$, so savings in both movement and arithmetic are needed. (the sources say so: "We therefore need savings in both movement and arithmetic." (paper))
Striking feature: the logarithmic factor is reduced by a power $(\lg n)^{-\kappa}$ for a fixed $\kappa>0$, so the bound is below $n\log n$ (explain why it holds, from the method)

Its sub-steps, in order:

- Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients. (on [Radix-digit convolution](radix-digit-convolution.md))
- The radix-digit coefficient list is placed on distinct prime cyclic axes by a Chinese-remainder map that preserves convolution. (on [Chinese-remainder axis map](crt-axis-map.md))
- Each prime-length Fourier transform is expressed through a tensor transform with power-of-two axis lengths, keeping the source and target permutations inside the identity. (on [Gaussian resampling](gaussian-resampling.md))
- Bluestein's chirp identity turns the middle transform, with its target permutation, into normalized cyclic convolution. (on [Bluestein's chirp identity](bluestein.md))
- Normalized cyclic convolution on the power-of-two axes is computed over the polynomial ring $\mathbb C[y]/(y^r+1)$ by synthetic transforms and packed polynomial products. (on [Synthetic polynomial transform](synthetic-transform.md))
- The recovered coefficient error is strictly below $1/2$, so rounding and carry propagation give the exact binary product. (on [Exact recovery by rounding and carries](exact-recovery.md))
- The tape operations of the algorithm cost $O(V(\lg n)^{1-\kappa})$ in total, for stored volume $V=\Theta(n)$.

## Symbols already bound on earlier pages

The symbols in the names of the concepts the reader knows are listed with those concepts above.

- $n$ (input length), bound on [Fixed-tape machine model](fixed-tape-model.md): The number of bits in each input; the worst-case time is measured as a function of it.
- $\kappa$ (power-saving constant), bound on [Fixed-tape machine model](fixed-tape-model.md): A fixed constant equal to $2^{-182}$ that does not depend on $n$.
- $n$ (integer length), bound on [Schonhage-Strassen optimality conjecture](schonhage-strassen-conjecture.md): The number of bits in each of the two integers being multiplied.
- $\kappa$ (power-saving exponent gap), bound on [Schonhage-Strassen optimality conjecture](schonhage-strassen-conjecture.md): A fixed constant with κ > 0, so that the target's time bound has exponent 1 − κ on lg n.
- $\kappa$ (saving parameter), bound on [Power saving in the logarithmic factor](power-saving.md): A fixed number greater than 0 that sets the size of the saving in the bound.
- $z$ (Gaussian dyadic number), bound on [Gaussian dyadic numbers](gaussian-dyadic.md): A complex number whose real and imaginary parts are both dyadic rationals.
- $a$ (real part), bound on [Gaussian dyadic numbers](gaussian-dyadic.md): The real part of the Gaussian dyadic number $z$, a dyadic rational.
- $b$ (imaginary part), bound on [Gaussian dyadic numbers](gaussian-dyadic.md): The imaginary part of the Gaussian dyadic number $z$, a dyadic rational.
- $m$ (numerator), bound on [Gaussian dyadic numbers](gaussian-dyadic.md): The integer numerator of a dyadic rational $m/2^k$.
- $k$ (denominator exponent), bound on [Gaussian dyadic numbers](gaussian-dyadic.md): The non-negative integer exponent such that $2^k$ is the denominator of a dyadic rational $m/2^k$.
- $\mathcal{G}$ (Gaussian dyadic set), bound on [Gaussian dyadic numbers](gaussian-dyadic.md): The set of all Gaussian dyadic numbers.
- $u$ (first input), bound on [Gaussian dyadic numbers](gaussian-dyadic.md): A Gaussian dyadic number used as the first input of the butterfly $H_0$.
- $v$ (second input), bound on [Gaussian dyadic numbers](gaussian-dyadic.md): A Gaussian dyadic number used as the second input of the butterfly $H_0$.
- $p$ (fractional bit count), bound on [Gaussian dyadic numbers](gaussian-dyadic.md): The number of fractional bits in the fixed-point grid, counting the binary digits after the binary point of each stored part.
- $x$ (first bank value), bound on [Linear network](linear-network.md): The value of the first bank, held on one wire in the example.
- $y$ (second bank value), bound on [Linear network](linear-network.md): The value of the second bank, held on one wire in the example.
- $i$ (row index), bound on [Role streams from a cyclic row split](role-streams.md): The position of a row among the rows that share its prefix, counted from 0.
- $W$ (number of roles), bound on [Role streams from a cyclic row split](role-streams.md): The number of roles, which is the number of fixed wire places in the network.
- $V$ (padded node volume), bound on [Role streams from a cyclic row split](role-streams.md): The number of bits the node holds once its rows are padded.
- $R$ (padded row count), bound on [Role streams from a cyclic row split](role-streams.md): The number of rows of one prefix after padding, a multiple of W.
- $h$ (ground-set size), bound on [Subset-intersection finite network](subset-network.md): The number of elements of the ground set $[h]$, which counts the elements the triples are drawn from.
- $\mathcal{T}$ (triple family), bound on [Subset-intersection finite network](subset-network.md): The set of all three-element subsets of $[h]$.
- $T$ (triple), bound on [Subset-intersection finite network](subset-network.md): A three-element subset of $[h]$ in the family $\mathcal T$, used as an index of scalars.
- $S$ (triple), bound on [Subset-intersection finite network](subset-network.md): A three-element subset of $[h]$ in $\mathcal T$, which indexes one bank-X scalar and one bank-Y scalar.
- $X$ (bank X), bound on [Subset-intersection finite network](subset-network.md): The bank holding the bank-X scalars $x_S$, one for each triple $S$.
- $Y$ (bank Y), bound on [Subset-intersection finite network](subset-network.md): The bank holding the bank-Y scalars $y_S$, one for each triple $S$.
- $x_S$ (bank-X scalar), bound on [Subset-intersection finite network](subset-network.md): The bank-X scalar held at triple $S$, on one wire.
- $y_S$ (bank-Y scalar), bound on [Subset-intersection finite network](subset-network.md): The bank-Y scalar held at triple $S$, on one wire.
- $A_{ST}$ (side wire), bound on [Subset-intersection finite network](subset-network.md): The scratch wire for an ordered neighbouring pair $(S,T)$, which receives a copy of $x_T$.
- $C_i$ (central wire), bound on [Subset-intersection finite network](subset-network.md): The scratch wire for element $i$ of $[h]$, which gathers the $x_T$ over triples $T$ containing $i$.
- $C_\ast$ (total central wire), bound on [Subset-intersection finite network](subset-network.md): The extra scratch wire of the complex version, which gathers the sum of all $x_T$.
- $D_v$ (vertex frame), bound on [Frame of a vertex](frame.md): The frame of a vertex v, an invertible linear operator on arrays indexed by the common address set; D_u is the frame of u.
- $u$ (edge tail vertex), bound on [Frame of a vertex](frame.md): A vertex at the tail of an edge, where the edge goes from u to v.
- $v$ (edge head vertex), bound on [Frame of a vertex](frame.md): A vertex at the head of an edge, where the edge goes from u to v.
- $g$ (logical array), bound on [Frame of a vertex](frame.md): The array a wire carries in its logical interpretation, before the frame is applied.
- $t$ (gate input count), bound on [Frame of a vertex](frame.md): The number of input arrays of a pointwise linear gate.
- $c_i$ (gate coefficient), bound on [Frame of a vertex](frame.md): The fixed scalar by which a pointwise linear gate multiplies its i-th input array.
- $i$ (input index), bound on [Frame of a vertex](frame.md): The index of an input array of a pointwise linear gate, running from 1 to t.
- $H$ (first address field), bound on [Address shear](address-shear.md): The first of the two address fields, a vector of residues, which the shear replaces by H + D.
- $D$ (second address field), bound on [Address shear](address-shear.md): The second of the two address fields, a vector of residues, which the shear adds to H and leaves fixed.
- $q$ (modulus), bound on [Address shear](address-shear.md): The fixed modulus q of the residue ring Z/qZ in which the entries of H and D lie.
- $E$ (fixed label space), bound on [Nested subspace labels](subspace-labels.md): The fixed space in which every label lies, a space of dimension m.
- $m$ (label space dimension), bound on [Nested subspace labels](subspace-labels.md): The dimension of E, the number of independent directions in E.
- $x$ (vertex), bound on [Nested subspace labels](subspace-labels.md): A vertex of the network, which is a gate or terminal.
- $L$ (label), bound on [Nested subspace labels](subspace-labels.md): The label L(x), a subspace of E attached to the vertex x.
- $y$ (head vertex), bound on [Nested subspace labels](subspace-labels.md): The vertex at which an edge from x ends.
- $P_U$ (orthogonal projection), bound on [Nested subspace labels](subspace-labels.md): The orthogonal projection onto a subspace U of E.
- $q$ (address field width), bound on [Nested subspace labels](subspace-labels.md): The number of bits in each of the two equal address fields being interchanged.
- $s$ (smaller call count), bound on [Nested subspace labels](subspace-labels.md): The total number of smaller calls, which is the sum of the drops over all edges.
- $a$ (edge rank), bound on [Rank-saving recursion](recursive-saving.md): The rank of an edge matrix, which counts the smaller calls that edge costs.
- $s$ (smaller call count), bound on [Rank-saving recursion](recursive-saving.md): The total number of smaller calls over all roles, which is the count the recursion's cost is measured by.
- $u$ (field width), bound on [Fast interchange of address chunks](tape-interchange.md): The common width of the two address fields, the number of bits in each.
- $V$ (stored volume), bound on [Fast interchange of address chunks](tape-interchange.md): The number of data units held in the array, the stored volume.
- $\tau$ (width exponent), bound on [Fast interchange of address chunks](tape-interchange.md): A fixed exponent with $\tau<1$ that sets the power saving below linear in the field width.
- $F_d$ (time per unit volume), bound on [Fast interchange of address chunks](tape-interchange.md): The time per unit volume for an interchange of width $m^d$ at recursion depth $d$.
- $d$ (recursion depth), bound on [Fast interchange of address chunks](tape-interchange.md): The number of levels of recursion below the top call, so that the width is $m^d$.
- $x$ (formal variable), bound on [Cyclic convolution](cyclic-convolution.md): A formal variable, the symbol whose powers mark the positions of the coefficients of a list.
- $S$ (list length), bound on [Cyclic convolution](cyclic-convolution.md): The number of coefficients in each list, which counts the coefficient positions and sets the wraparound modulus.
- $i$ (first index), bound on [Cyclic convolution](cyclic-convolution.md): An index of the first list's coefficients, running over $\{0,\dots,S-1\}$.
- $j$ (second index), bound on [Cyclic convolution](cyclic-convolution.md): An index of the second list's coefficients, running over $\{0,\dots,S-1\}$.
- $k$ (output index), bound on [Cyclic convolution](cyclic-convolution.md): An index of the cyclic product's coefficients, running over $\{0,\dots,S-1\}$.
- $c$ (cyclic product), bound on [Cyclic convolution](cyclic-convolution.md): The list of $S$ coefficients of the cyclic convolution of $a$ and $b$.
- $b$ (digit width), bound on [Radix-digit convolution](radix-digit-convolution.md): The number of bits in each radix digit.
- $m$ (digit count), bound on [Radix-digit convolution](radix-digit-convolution.md): The number of radix digits in each input, $\lceil n/b \rceil$.
- $u_i$ (first input digit), bound on [Radix-digit convolution](radix-digit-convolution.md): The $i$-th radix digit of the first input, an integer in $\{0,\dots,2^b-1\}$.
- $v_i$ (second input digit), bound on [Radix-digit convolution](radix-digit-convolution.md): The $i$-th radix digit of the second input, an integer in $\{0,\dots,2^b-1\}$.
- $t$ (formal variable), bound on [Radix-digit convolution](radix-digit-convolution.md): A formal variable whose powers mark the coefficient positions of the digit polynomials.
- $U$ (first digit polynomial), bound on [Radix-digit convolution](radix-digit-convolution.md): The polynomial $U(t)$ whose coefficients are the digits of the first input.
- $V$ (second digit polynomial), bound on [Radix-digit convolution](radix-digit-convolution.md): The polynomial $V(t)$ whose coefficients are the digits of the second input.
- $W$ (product polynomial), bound on [Radix-digit convolution](radix-digit-convolution.md): The product $U(t)V(t)$, whose value at $t = 2^b$ is the integer product of the inputs.
- $w_k$ (product coefficient), bound on [Radix-digit convolution](radix-digit-convolution.md): The $k$-th coefficient of $W$, the sum of $u_i v_j$ over $i+j=k$.
- $u$ (input vector), bound on [Discrete Fourier transform](fourier-transform.md): The complex vector $u=(u_0,\dots,u_{q-1})$ whose transform is taken.
- $q$ (vector length), bound on [Discrete Fourier transform](fourier-transform.md): The length of $u$, which counts the entries of $u$ and of its transform.
- $\omega$ (primitive root of unity), bound on [Discrete Fourier transform](fourier-transform.md): The number $\exp(-2\pi i/q)$, a primitive $q$-th root of unity, so that $\omega^q=1$.
- $\hat u$ (transform of u), bound on [Discrete Fourier transform](fourier-transform.md): The transform of $u$, the vector whose $k$-th entry is $\frac1q\sum_j u_j\omega^{jk}$.
- $k$ (transform index), bound on [Discrete Fourier transform](fourier-transform.md): The index of an entry of the transform $\hat u$, running from $0$ to $q-1$.
- $j$ (input index), bound on [Discrete Fourier transform](fourier-transform.md): The index of an entry of $u$, running from $0$ to $q-1$.
- $l$ (convolution index), bound on [Discrete Fourier transform](fourier-transform.md): The index of an entry of the cyclic convolution $c$, running from $0$ to $q-1$.
- $\alpha$ (even-entry transform), bound on [Discrete Fourier transform](fourier-transform.md): The normalized transform, of length $q/2$, of the even-indexed entries of $u$.
- $\beta$ (odd-entry transform), bound on [Discrete Fourier transform](fourier-transform.md): The normalized transform, of length $q/2$, of the odd-indexed entries of $u$.
- $T$ (operation count), bound on [Discrete Fourier transform](fourier-transform.md): The number of operations the transform takes on a vector of length $q$.
- $E$ (first vector space), bound on [Tensor product](tensor-product.md): The first vector space, the first factor of the tensor product.
- $F$ (second vector space), bound on [Tensor product](tensor-product.md): The second vector space, the second factor of the tensor product.
- $e_i$ (basis vector of E), bound on [Tensor product](tensor-product.md): The i-th basis vector of E.
- $f_j$ (basis vector of F), bound on [Tensor product](tensor-product.md): The j-th basis vector of F.
- $p$ (dimension of E), bound on [Tensor product](tensor-product.md): The number of basis vectors of E, so E has dimension p.
- $q$ (dimension of F), bound on [Tensor product](tensor-product.md): The number of basis vectors of F, so F has dimension q.
- $S$ (linear map on E), bound on [Tensor product](tensor-product.md): A linear map of E, the factor that S acts on in the tensor product.
- $T$ (linear map on F), bound on [Tensor product](tensor-product.md): A linear map of F, the factor that T acts on in the tensor product.
- $H_0$ (two-point butterfly), bound on [Tensor product](tensor-product.md): The map sending a pair (u,v) to ((u+v)/2,(u-v)/2).
- $D$ (selected bit count), bound on [Tensor product](tensor-product.md): The number of selected address bits that the butterfly layer acts on.
- $d$ (number of axes), bound on [Multidimensional transform with power-of-two axes](multidim-transform.md): The number of axes of the array, which counts the coordinates it is indexed by.
- $r_\ell$ (axis length), bound on [Multidimensional transform with power-of-two axes](multidim-transform.md): The number of entries along axis $\ell$, a power of two.
- $\ell$ (axis index), bound on [Multidimensional transform with power-of-two axes](multidim-transform.md): The index of an axis, running from 1 to d.
- $A$ (input array), bound on [Multidimensional transform with power-of-two axes](multidim-transform.md): The array to be transformed, with entries indexed by $j_1,\dots,j_d$.
- $B$ (transformed array), bound on [Multidimensional transform with power-of-two axes](multidim-transform.md): The result of the transform, with entries indexed by $k_1,\dots,k_d$.
- $j$ (input index), bound on [Multidimensional transform with power-of-two axes](multidim-transform.md): The index along an axis of the input array, $j_\ell$ being the index along axis $\ell$.
- $k$ (output index), bound on [Multidimensional transform with power-of-two axes](multidim-transform.md): The index along an axis of the transformed array, $k_\ell$ being the index along axis $\ell$.
- $H_0$ (butterfly layer), bound on [Simultaneous butterfly layer H₀](butterfly-layer.md): The simultaneous butterfly layer, the two-point butterfly applied at once to one selected address bit of every chunk.
- $d$ (chunk count), bound on [Simultaneous butterfly layer H₀](butterfly-layer.md): The number of equal-width address chunks on which the layer acts, each with one selected bit.
- $r$ (record length), bound on [Simultaneous butterfly layer H₀](butterfly-layer.md): The number of complex coefficients in a polynomial record.
- $\lambda'$ (cost exponent), bound on [Simultaneous butterfly layer H₀](butterfly-layer.md): A fixed exponent below one that sets the layer's cost bound.
- $r$ (coefficient count), bound on [Root of unity](roots-of-unity.md): The number of complex coefficients of a reduced polynomial, which is a power of two.
- $y$ (polynomial variable), bound on [Root of unity](roots-of-unity.md): The formal variable of the polynomial ring modulo y^r+1, whose powers are the roots of unity on this page.
- $p$ (power exponent), bound on [Root of unity](roots-of-unity.md): The exponent of a power of y being multiplied, with 0 < p < r.
- $y$ (polynomial variable), bound on [Polynomial ring modulo yʳ + 1](polynomial-ring.md): The formal variable of the ring, whose powers act as roots of unity on the remaining axes.
- $r$ (coefficient count), bound on [Polynomial ring modulo yʳ + 1](polynomial-ring.md): The number of complex coefficients in each polynomial record, which is a power of two.
- $a_i$ (ring coefficient), bound on [Polynomial ring modulo yʳ + 1](polynomial-ring.md): The i-th complex coefficient of an element of the ring, the coefficient of y^i.
- $i$ (coefficient index), bound on [Polynomial ring modulo yʳ + 1](polynomial-ring.md): The index of a coefficient of a ring element, running from 0 to r-1.
- $k$ (shift amount), bound on [Polynomial ring modulo yʳ + 1](polynomial-ring.md): The number of places each coefficient moves when the element is multiplied by y^k.
- $j$ (twiddle exponent), bound on [Synthetic polynomial transform](synthetic-transform.md): The exponent of a twiddle factor $y^j$, an integer ranging over $0,\dots,2r-1$.
- $A$ (packed polynomial), bound on [Signed coefficient packing](signed-packing.md): The polynomial $A(x)$ whose coefficients are packed into one integer.
- $x$ (formal variable), bound on [Signed coefficient packing](signed-packing.md): The formal variable in which the polynomial $A(x)$ is written.
- $i$ (coefficient index), bound on [Signed coefficient packing](signed-packing.md): The index of a coefficient, running from $0$ to $m-1$.
- $m$ (coefficient count), bound on [Signed coefficient packing](signed-packing.md): The number of coefficients of $A$.
- $b$ (slot width), bound on [Signed coefficient packing](signed-packing.md): The number of bits in each slot, which holds one coefficient.
- $a_i$ (coefficient), bound on [Signed coefficient packing](signed-packing.md): The integer coefficient of $x^i$ in $A(x)$.
- $N_A$ (packed integer of A), bound on [Signed coefficient packing](signed-packing.md): The integer $A(2^b)$ whose bit slots hold the coefficients of $A$.
- $B$ (second polynomial), bound on [Signed coefficient packing](signed-packing.md): The second polynomial, whose coefficients are packed into $N_B$.
- $N_B$ (packed integer of B), bound on [Signed coefficient packing](signed-packing.md): The integer $B(2^b)$ whose bit slots hold the coefficients of $B$.
- $p$ (shared denominator exponent), bound on [Exact recovery by rounding and carries](exact-recovery.md): The exponent $p \ge 1$ such that all the real parts have denominator $2^p$.
- $L$ (position count), bound on [Exact recovery by rounding and carries](exact-recovery.md): The number of carry positions processed, a count of positions at least as large as the number of coefficients.
- $e_k$ (radix digit), bound on [Exact recovery by rounding and carries](exact-recovery.md): The digit at position $k$, the remainder of the carried sum modulo $2^b$.
- $T$ (digit value), bound on [Exact recovery by rounding and carries](exact-recovery.md): The number represented by the digits, $T = \sum_{k<L} e_k 2^{bk}$.
- $C$ (final carry), bound on [Exact recovery by rounding and carries](exact-recovery.md): The carry left over after the last position $L-1$.
- $R$ (exact product), bound on [Exact recovery by rounding and carries](exact-recovery.md): The exact product of the two integer inputs, written as the sum of the coefficients weighted by powers of $2^b$.
- $s$ (source length), bound on [Gaussian resampling](gaussian-resampling.md): The length of the source transform, the number of coordinates it acts on.
- $t$ (target length), bound on [Gaussian resampling](gaussian-resampling.md): The target length, the number of coordinates of the longer transform.
- $\alpha$ (Gaussian width), bound on [Gaussian resampling](gaussian-resampling.md): A fixed integer that sets the width of the Gaussian weights.
- $F_q$ (normalized transform), bound on [Gaussian resampling](gaussian-resampling.md): The normalized Fourier transform of length $q$, mapping a vector of length $q$ to one of length $q$.
- $P_s$ (source permutation), bound on [Gaussian resampling](gaussian-resampling.md): The coordinate permutation of length-$s$ vectors that sends $u$ to the vector with entries $u_{tj}$.
- $P_t$ (target permutation), bound on [Gaussian resampling](gaussian-resampling.md): The coordinate permutation of length-$t$ vectors that sends $v$ to the vector with entries $v_{-sk}$.
- $v$ (target vector), bound on [Gaussian resampling](gaussian-resampling.md): A vector of length $t$, the input to the target permutation $P_t$.
- $G$ (Gaussian map), bound on [Gaussian resampling](gaussian-resampling.md): The map from length $s$ to length $t$ whose $k$-th output is a Gaussian-weighted sum centred at $sk/t$.
- $T$ (dual Gaussian map), bound on [Gaussian resampling](gaussian-resampling.md): The map from length $s$ to length $t$ that weights each input $u_j$ by a Gaussian centred at $tj/s$.
- $E$ (weight map), bound on [Gaussian resampling](gaussian-resampling.md): The diagonal map on length-$s$ vectors that multiplies entry $j$ by $e^{\pi\alpha^2\beta_j^2}$.
- $q_j$ (nearest index), bound on [Gaussian resampling](gaussian-resampling.md): The integer nearest $tj/s$, rounding ties up, which is the target coordinate that $C$ selects for index $j$.
- $\beta_j$ (rounding offset), bound on [Gaussian resampling](gaussian-resampling.md): The signed distance $tj/s-q_j$ from $tj/s$ to its nearest integer, with absolute value at most $\tfrac12$.
- $C$ (selection map), bound on [Gaussian resampling](gaussian-resampling.md): The map from length $t$ to length $s$ that selects the coordinates $v_{q_j}$.
- $N$ (near-identity map), bound on [Gaussian resampling](gaussian-resampling.md): The composite map $CTE$ on length-$s$ vectors, which is close to the identity.
- $I$ (identity map), bound on [Gaussian resampling](gaussian-resampling.md): The identity map on vectors, the operator with $Iu=u$.
- $R$ (first contraction), bound on [Gaussian resampling](gaussian-resampling.md): The contraction $R=\tfrac12 G$ from length $s$ to length $t$.
- $Q$ (second contraction), bound on [Gaussian resampling](gaussian-resampling.md): The contraction $Q=2^{1-2\alpha^2}EN^{-1}C$ from length $t$ back to length $s$.
- $c_p$ (chirp value), bound on [Bluestein's chirp identity](bluestein.md): The chirp value $\exp(-\pi i p^2/q)$ at the integer $p$, a unit complex number.
- $p$ (chirp index), bound on [Bluestein's chirp identity](bluestein.md): The integer at which the chirp is evaluated, which may be negative.
- $s_i$ (axis length), bound on [Chinese-remainder axis map](crt-axis-map.md): The length of axis $i$, which counts the positions on that axis.
- $P_i$ (earlier length product), bound on [Chinese-remainder axis map](crt-axis-map.md): The product of the lengths of the axes before axis $i$, which counts the positions on those axes.
- $\mu_i$ (inverse of P_i), bound on [Chinese-remainder axis map](crt-axis-map.md): The inverse of $P_i$ modulo $s_i$, an integer with $\mu_iP_i\equiv1\pmod{s_i}$.
- $x_i$ (axis variable), bound on [Chinese-remainder axis map](crt-axis-map.md): The variable of axis $i$ in the target ring.
- $\Phi$ (axis map), bound on [Chinese-remainder axis map](crt-axis-map.md): The algebra map sending $x$ to $\prod_i x_i^{\mu_i}$.
- $a_j$ (axis digit), bound on [Chinese-remainder axis map](crt-axis-map.md): The digit of the coefficient index $k$ on axis $j$, the coefficient of $P_j$ in its mixed-radix expansion.
- $b_i$ (target exponent), bound on [Chinese-remainder axis map](crt-axis-map.md): The exponent of $x_i$ in $\Phi(x^k)$, reduced to lie between $0$ and $s_i-1$.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Fixed-tape machine model](fixed-tape-model.md): A multitape Turing machine with one fixed finite alphabet and a fixed finite number of one-dimensional tapes, the same for every input length.
  Shown as: Fixed-tape integer multiplication with a power saving *<predicate>* Fixed-tape machine model
- [Power saving in the logarithmic factor](power-saving.md): A bound of the form n times (lg n) raised to the power 1 − κ for a fixed κ > 0, which is smaller than n log n by a polynomial factor in log n.
  Shown as: Fixed-tape integer multiplication with a power saving *<predicate>* Power saving in the logarithmic factor
- [Fast interchange of address chunks](tape-interchange.md): A fixed-tape procedure that swaps two disjoint equal-width address fields of an array in time O(V u^τ) for a fixed τ < 1, where V is the stored volume and u the field width, using XOR combinations of intermediate data.
  Shown as: Fixed-tape integer multiplication with a power saving *<predicate>* Fast interchange of address chunks
- [Simultaneous butterfly layer H₀](butterfly-layer.md): The map H₀(u,v) = ((u+v)/2, (u−v)/2) applied at once to a selected coordinate bit of every chunk, a two-point butterfly acting coefficientwise on polynomial records.
  Shown as: Fixed-tape integer multiplication with a power saving *<predicate>* Simultaneous butterfly layer H₀
- [Synthetic polynomial transform](synthetic-transform.md): A discrete Fourier transform whose roots of unity are powers of y in the polynomial ring, so that each twiddle multiplication is a signed shift and the transform is computed by simultaneous butterfly layers.
  Shown as: Fixed-tape integer multiplication with a power saving *<predicate>* Synthetic polynomial transform
- [Gaussian resampling](gaussian-resampling.md): A rewriting of a Fourier transform of prime length as a transform with power-of-two axis lengths, with source and target coordinate permutations kept inside the transform identity.
  Shown as: Fixed-tape integer multiplication with a power saving *<predicate>* Gaussian resampling
- [Bluestein's chirp identity](bluestein.md): An identity writing a Fourier transform as a cyclic convolution sandwiched between pointwise multiplications by chirp sequences exp(−πi s j² / t).
  Shown as: Fixed-tape integer multiplication with a power saving *<predicate>* Bluestein's chirp identity
- [Chinese-remainder axis map](crt-axis-map.md): The bijection sending a coefficient index written in mixed radix with pairwise coprime lengths to coordinates on a product of cyclic axes, which turns one cyclic convolution into a multidimensional one.
  Shown as: Fixed-tape integer multiplication with a power saving *<predicate>* Chinese-remainder axis map
- [Radix-digit convolution](radix-digit-convolution.md): Writing each n-bit input as a polynomial in 2^b with about n/b nonnegative digits, so that integer multiplication becomes a convolution whose coefficients are bounded by a fixed power of two.
  Shown as: Fixed-tape integer multiplication with a power saving *<predicate>* Radix-digit convolution
- [Signed coefficient packing](signed-packing.md): Encoding a polynomial with signed integer coefficients as one integer by placing coefficients at fixed bit offsets, so that a polynomial product becomes an integer product.
  Shown as: Fixed-tape integer multiplication with a power saving *<predicate>* Signed coefficient packing
- [Established fast multiplier](multiplier-subroutine.md): The known deterministic O(n log n) multiplication algorithm of Harvey and van der Hoeven, used as a black-box subroutine on shorter integers.
  Shown as: Fixed-tape integer multiplication with a power saving *<predicate>* Established fast multiplier
- [Exact recovery by rounding and carries](exact-recovery.md): Recovering the exact integer coefficients of a convolution by rounding the computed values, whose error is below one half, and then propagating carries in radix 2^b.
  Shown as: Fixed-tape integer multiplication with a power saving *<predicate>* Exact recovery by rounding and carries

## Other pages you may link to

- [Schonhage-Strassen optimality conjecture](schonhage-strassen-conjecture.md)
- [Gaussian dyadic numbers](gaussian-dyadic.md)
- [Linear network](linear-network.md)
- [Role streams from a cyclic row split](role-streams.md)
- [Subset-intersection finite network](subset-network.md)
- [Source, sink and terminal of a network](network-terminal.md)
- [Frame of a vertex](frame.md)
- [Address shear](address-shear.md)
- [Nested subspace labels](subspace-labels.md)
- [Rank-saving recursion](recursive-saving.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Discrete Fourier transform](fourier-transform.md)
- [Tensor product](tensor-product.md)
- [Multidimensional transform with power-of-two axes](multidim-transform.md)
- [Order of an element](order-of-element.md)
- [Root of unity](roots-of-unity.md)
- [Polynomial ring modulo yʳ + 1](polynomial-ring.md)
- [Operator norm of a linear map](operator-norm.md)
- [Quotient ring by several relations](quotient-ring.md)

## Evidence from the sources, with the paragraph around each quote

- "We give a deterministic algorithm that multiplies two $n$-bit integers" (paper)

  > \documentclass[11pt]{article} \usepackage[T1]{fontenc} \usepackage{lmodern,microtype} \usepackage{amsmath,amssymb,amsthm,mathrsfs,mathtools,booktabs,array,longtable} \usepackage[margin=1in]{geometry} \usepackage{tikz} \usetikzlibrary{positioning,arrows.meta} \usepackage[hyphens]{url} \usepackage{hyperref} \hypersetup{colorlinks=true,linkcolor=blue!45!black,citecolor=blue!45!black,urlcolor=blue!45!black,pdftitle={Integer multiplication below n log n},pdfauthor={OpenAI}} \pdfinfoomitdate=1 \pdftrailerid{} \pdfsuppressptexinfo=15 \newtheorem{theorem}{Theorem} \newtheorem{lemma}[theorem]{Lemma} \newtheorem{proposition}[theorem]{Proposition} \newtheorem{corollary}[theorem]{Corollary} \theoremstyle{definition} \newtheorem{definition}[theorem]{Definition} \newtheorem{remark}[theorem]{Remark} \newcommand{\norm}[1]{\lVert#1\rVert_\infty} \title{Integer multiplication below \texorpdfstring{$n\log n$}{n log n}} \author{OpenAI} \date{September 23, 2026} \begin{document} \maketitle \begin{abstract} We give a deterministic algorithm that multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ worst-case time, with $\kappa=2^{-182}$, on one fixed finite-alphabet Turing machine with a fixed finite number of one-dimensional tapes. The algorithm is exact for every input length and disproves the $n\log n$ optimality conjecture of Sch\"onhage and Strassen in this model. \end{abstract} \tableofcontents \clearpage \section{Introduction}


## Sources (read from disk as needed)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The reader cannot follow this step: "The computed values keep $p$ bits after each rounding, the precision, which is of order $\lg n$." (The page asserts that the precision p is of order lg n but never says why the rounding precision must grow like lg n or how it is chosen.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step. It is inside reasoning added for an earlier step. If it is part of how this page's own step of the argument works (see "This page in the argument"), develop it here; if it concerns a result that step uses, say what the result states and cite it.
- The reader cannot follow this step: "Undoing the digit scales leaves an error of a constant times $b\,2^{-3b/4}$ for the digit width $b$." (The error bound b 2^(-3b/4) is presented as the result of undoing the digit scales, but no calculation is shown and it is not marked as cited. The reader cannot check it, and the scaling is not explained.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step. It is inside reasoning added for an earlier step. If it is part of how this page's own step of the argument works (see "This page in the argument"), develop it here; if it concerns a result that step uses, say what the result states and cite it.
- The reader cannot follow this step: "since the coefficient error is below $1/2$" (The page never says how b is chosen relative to n, nor how the p-bit rounding error combines with the b 2^(-3b/4) term. So the claim that the total error is below 1/2 does not follow from what the page gives.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "with $V=\Theta(n)$" (The page states that the stored volume V is Theta(n) without saying how the array size is set from the input length.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step. It is inside reasoning added for an earlier step. If it is part of how this page's own step of the argument works (see "This page in the argument"), develop it here; if it concerns a result that step uses, say what the result states and cite it.
- The reader cannot follow this step: "each displayed power there is at most $1-2\kappa$ (cited)" (The cited bound refers to a cost table and its displayed powers, but the page does not say what the table contains or which operations it charges, so the reader cannot tell what the bound covers.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step. It is inside reasoning added for an earlier step. If it is part of how this page's own step of the argument works (see "This page in the argument"), develop it here; if it concerns a result that step uses, say what the result states and cite it.
- The reader cannot follow this step: "so the total is $O(Vp^{1-\kappa})$" (The page combines the cited table bound with the cited log absorption into one total, but does not say how many terms there are or why combining them keeps the exponent at 1 - kappa.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step. It is inside reasoning added for an earlier step. If it is part of how this page's own step of the argument works (see "This page in the argument"), develop it here; if it concerns a result that step uses, say what the result states and cite it.
- The reader cannot follow this step: "Each recursion level multiplies the cost by $s/W$" (The page does not say why each recursion level multiplies the cost by s/W, and gives no link or argument for this factor.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step. It is inside reasoning added for an earlier step. If it is part of how this page's own step of the argument works (see "This page in the argument"), develop it here; if it concerns a result that step uses, say what the result states and cite it.
- The reader cannot follow this step: "So the level costs form a geometric series with ratio $(s/W)m^{-\tau}<1$, dominated by its first term." (The page asserts that the ratio (s/W) m^(-tau) is below 1 without any inequality relating s, W, m and tau, and m is unbound. The geometric-series domination also needs the ratio to stay bounded away from 1, which is not shown.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step. It is inside reasoning added for an earlier step. If it is part of how this page's own step of the argument works (see "This page in the argument"), develop it here; if it concerns a result that step uses, say what the result states and cite it.
- The reader cannot follow this step: "the smallest slack is $2^{-181}$" (The page uses slack without defining it and says its smallest value is 2^(-181), so kappa is half of it. The reader cannot tell what slack measures or why its smallest value is that, and the cited claim does not say.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step. It is inside reasoning added for an earlier step. If it is part of how this page's own step of the argument works (see "This page in the argument"), develop it here; if it concerns a result that step uses, say what the result states and cite it.
- Say what $m$ denotes where it is first used (for a size or count, what it counts): "while the width falls by a factor $m$" (The page uses m as the factor by which the width falls at each recursion level. The earlier pages bind m only to other objects (label space dimension, coefficient count, digit count), and none of them tells the reader that m is this factor.)

## Previous version (revise it)

It has 418 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 522 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

Fixed-tape integer multiplication with a power saving is a deterministic algorithm that multiplies two integers exactly. It is the main result that disproves the [Schonhage-Strassen optimality conjecture](schonhage-strassen-conjecture.md) in the fixed-tape model. It runs on one [Fixed-tape machine model](fixed-tape-model.md).

Let $n$ be the number of bits in each input. The worst-case time is $O(n(\lg n)^{1-\kappa})$ with $\kappa=2^{-182}$ <cite data-source="paper">$\kappa=2^{-182}$</cite>. It achieves a [Power saving in the logarithmic factor](power-saving.md), so its time is smaller than $n\log n$ by a power of $\lg n$.

It reduces multiplication to convolution through [Radix-digit convolution](radix-digit-convolution.md). It places its coefficients on axes by the [Chinese-remainder axis map](crt-axis-map.md), which preserves the convolution. It rewrites its prime-length transforms by [Gaussian resampling](gaussian-resampling.md). It reduces the middle transform by [Bluestein's chirp identity](bluestein.md) to cyclic convolution. It computes its transforms by a [Synthetic polynomial transform](synthetic-transform.md) over the ring $\mathbb C[y]/(y^r+1)$. Each transform is built from simultaneous layers of [Simultaneous butterfly layer H₀](butterfly-layer.md) on polynomial records. It packs signed coefficients by [Signed coefficient packing](signed-packing.md), so that polynomial products become integer products. It calls the [Established fast multiplier](multiplier-subroutine.md) as a black box on shorter integers. It recovers the exact binary product by [Exact recovery by rounding and carries](exact-recovery.md), since the coefficient error is below $1/2$.

The coefficient error is the difference between a computed coefficient and its true integer value. The computed values keep $p$ bits after each rounding, the precision, which is of order $\lg n$. Undoing the digit scales leaves an error of a constant times $b\,2^{-3b/4}$ for the digit width $b$. Below $1/2$ for $b$ beyond a fixed cutoff, the nearest integer is the true coefficient <cite data-source="paper">The strict error below $1/2$ makes the nearest integer to</cite>.

It carries out its address rearrangements by [Fast interchange of address chunks](tape-interchange.md). Here $u$ is the number of bits in each interchanged address field, and $\tau$ is a fixed exponent below one. A swap on stored volume $V$ costs $O(Vu^{\tau})$ time <cite data-source="paper">$O(Vu^\tau)$</cite>.

Exactness alone does not bound the time. The arithmetic and multiplier calls are charged in the same cost table, and each displayed power there is at most $1-2\kappa$ <cite data-source="paper">Each of the seven displayed powers is at most $1-2\kappa$</cite>. A fixed power of $\log p$ is absorbed by $p^{\kappa}$ <cite data-source="paper">Any fixed power of $\log p$ is at most $p^\kappa$ eventually</cite>, so the total is $O(Vp^{1-\kappa})$ with $V=\Theta(n)$ and $p$ of order $\lg n$, which is $O(n(\lg n)^{1-\kappa})$.

Each swap costs a power $u^{\tau}$ of its width, not $u$. Each recursion level multiplies the cost by $s/W$, where $s$ is the total number of smaller calls and $W$ the number of roles, while the width falls by a factor $m$. So the level costs form a geometric series with ratio $(s/W)m^{-\tau}<1$, dominated by its first term. The exponents are fixed rationals such as $\tau=1-2^{-50}$, and the smallest slack is $2^{-181}$, so $\kappa$ is half of it <cite data-source="paper">Thus $\min_i g_i=2^{-181}=2\kappa$</cite>.

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

Write the body to `exegenius/tasks/0149-write-fixed-tape-multiplication.answer.md` and the JSON to `exegenius/tasks/0149-write-fixed-tape-multiplication.answer.json`, then run `exegenius submit 0149-write-fixed-tape-multiplication` in the project directory. If submit rejects the answer, fix the answer and submit again.
