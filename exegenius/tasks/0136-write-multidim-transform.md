# exegenius task 0136-write-multidim-transform

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
- Tensor product
- Source, sink and terminal of a network (also: terminal, source and sink of the network)

## This page

Concept: Multidimensional transform with power-of-two axes
Gloss: A transform on an array indexed by several coordinates, each with length a power of two, obtained as a tensor product of one-dimensional Fourier transforms.
Also called: power-of-two tensor transform

## Where the argument relies on this page

- Each prime-length Fourier transform is expressed through a tensor transform with power-of-two axis lengths, keeping the source and target permutations inside the identity. (on [Gaussian resampling](gaussian-resampling.md))
- Gaussian resampling expresses each source Fourier transform through a power-of-two tensor transform.

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

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Discrete Fourier transform](fourier-transform.md): The map sending a vector u of length q to the vector whose k-th entry is (1/q) times the sum over j of u_j times exp(−2πijk/q).
  Shown as: Multidimensional transform with power-of-two axes *<predicate>* Discrete Fourier transform
- [Tensor product](tensor-product.md): The tensor product V ⊗ W of vector spaces is the space spanned by pairs of basis vectors, and the tensor product of linear maps acts on each factor separately, so one-dimensional operations on several coordinates combine into one operation on the product space.
  Shown as: Multidimensional transform with power-of-two axes *<predicate>* Tensor product

## Pages that build on this one

- Gaussian resampling: A rewriting of a Fourier transform of prime length as a transform with power-of-two axis lengths, with source and target coordinate permutations kept inside the transform identity.

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

- "transforms whose axis lengths are powers of two" (paper)

  > Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients. Our starting point is the Gaussian-resampling reduction of Harvey and van der Hoeven \cite{HarveyHoeven2021}: it replaces the Fourier transforms needed for this convolution by multidimensional transforms whose axis lengths are powers of two. After a further conversion to convolution, one coordinate is stored as the coefficient list of a polynomial modulo $y^r+1$, with $r$ a power of two. Powers of $y$ then serve as roots of unity in the remaining axes, and multiplication by such a root is a signed shift of the coefficient list. These are the synthetic polynomial transforms of Nussbaumer and Quandalle and Nussbaumer~\cite{NussbaumerQuandalle1978,Nussbaumer1980}.


## Sources (read from disk as needed)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- Say what $\ell$ denotes where it is first used: the page uses it before saying so in "Here $j_\ell$ and $k_\ell$ are the input and output indices along axis $\ell$"

## Previous version (revise it)

It has 267 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 333 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

A multidimensional transform with power-of-two axes is the [Discrete Fourier transform](fourier-transform.md) applied along every coordinate of an array whose coordinate lengths are powers of two. [Gaussian resampling](gaussian-resampling.md) uses it in place of prime-length transforms. Harvey and van der Hoeven's reduction replaces the Fourier transforms needed for convolution by multidimensional transforms <cite data-source="paper">whose axis lengths are powers of two</cite>.

Let $d$ be the number of axes, and for each axis $\ell = 1,\dots,d$ let $r_\ell$, a power of two, be the number of entries along that axis. Here $j_\ell$ and $k_\ell$ are the input and output indices along axis $\ell$, both ranging over $0,\dots,r_\ell-1$. Let $A$ be the input array, with entries $A_{j_1\cdots j_d}$, and $B$ the transformed array, with entries $B_{k_1\cdots k_d}$. The letters $A$, $B$, $j$ and $k$ take these meanings here.

The transform applies one [Discrete Fourier transform](fourier-transform.md) on each axis, and is built with the [tensor product](tensor-product.md) of these one-axis maps, so each map acts only along its own axis. The map for axis $\ell$ has entry $\frac{1}{r_\ell}\exp(-2\pi\mathrm{i}\,j_\ell k_\ell/r_\ell)$ in row $k_\ell$ and column $j_\ell$. The entry of a tensor product of matrices is the product of the factor entries, so the entry in row $(k_1,\dots,k_d)$ and column $(j_1,\dots,j_d)$ is the product over $\ell$ below, with the factors $1/r_\ell$ multiplying to $1/(r_1\cdots r_d)$. Applying this matrix to $A$ gives $B$:

$$B_{k_1\cdots k_d}=\frac{1}{r_1\cdots r_d}\sum_{j_1=0}^{r_1-1}\cdots\sum_{j_d=0}^{r_d-1}A_{j_1\cdots j_d}\prod_{\ell=1}^{d}\exp\Big(-\frac{2\pi\mathrm{i}\,j_\ell k_\ell}{r_\ell}\Big).$$

Each factor of the product depends on one axis only, so the sum over $j_1$ can be taken first, then $j_2$, and so on. Each step is the length-$r_\ell$ transform applied to every line of entries along axis $\ell$, so the axes can be processed one at a time, in any order.

Take $d=2$ and $r_1=r_2=2$. The length-2 transform sends $(u_0,u_1)$ to $((u_0+u_1)/2,(u_0-u_1)/2)$, since $\exp(-\pi\mathrm{i})=-1$. For $A_{00}=1$, $A_{01}=2$, $A_{10}=3$, $A_{11}=4$, the formula gives $B_{00}=5/2$, $B_{01}=-1/2$, $B_{10}=-1$ and $B_{11}=0$.

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

Write the body to `exegenius/tasks/0136-write-multidim-transform.answer.md` and the JSON to `exegenius/tasks/0136-write-multidim-transform.answer.json`, then run `exegenius submit 0136-write-multidim-transform` in the project directory. If submit rejects the answer, fix the answer and submit again.
