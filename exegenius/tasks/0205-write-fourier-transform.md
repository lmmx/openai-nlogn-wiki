# exegenius task 0205-write-fourier-transform

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

Concept: Discrete Fourier transform
Gloss: The map sending a vector u of length q to the vector whose k-th entry is (1/q) times the sum over j of u_j times exp(−2πijk/q).
Also called: Fourier transform, twiddle step

## Where the argument relies on this page

- Each prime-length Fourier transform is expressed through a tensor transform with power-of-two axis lengths, keeping the source and target permutations inside the identity. (on [Gaussian resampling](gaussian-resampling.md))
- Gaussian resampling expresses each source Fourier transform through a power-of-two tensor transform.
- Bluestein's chirp identity turns the middle transform, with its target permutation, into normalized cyclic convolution. (on [Bluestein's chirp identity](bluestein.md))

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

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Cyclic convolution](cyclic-convolution.md): The product of two coefficient lists in the ring of polynomials modulo x^S − 1, in which exponents wrap around modulo S.
  Shown as: Discrete Fourier transform *<predicate>* Cyclic convolution

## Pages that build on this one

- Tensor product: The tensor product V ⊗ W of vector spaces is the space spanned by pairs of basis vectors, and the tensor product of linear maps acts on each factor separately, so one-dimensional operations on several coordinates combine into one operation on the product space.
- Multidimensional transform with power-of-two axes: A transform on an array indexed by several coordinates, each with length a power of two, obtained as a tensor product of one-dimensional Fourier transforms.
- Root of unity: A number whose some positive integer power equals one; here powers of y in the polynomial ring play this role.
- Gaussian resampling: A rewriting of a Fourier transform of prime length as a transform with power-of-two axis lengths, with source and target coordinate permutations kept inside the transform identity.
- Bluestein's chirp identity: An identity writing a Fourier transform as a cyclic convolution sandwiched between pointwise multiplications by chirp sequences exp(−πi s j² / t).

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
- [Quotient ring by several relations](quotient-ring.md)
- [Chinese-remainder axis map](crt-axis-map.md)
- [Fixed-tape integer multiplication with a power saving](fixed-tape-multiplication.md)

## Evidence from the sources, with the paragraph around each quote

- "replaces the Fourier transforms needed for" (paper)

  > Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients. Our starting point is the Gaussian-resampling reduction of Harvey and van der Hoeven \cite{HarveyHoeven2021}: it replaces the Fourier transforms needed for this convolution by multidimensional transforms whose axis lengths are powers of two. After a further conversion to convolution, one coordinate is stored as the coefficient list of a polynomial modulo $y^r+1$, with $r$ a power of two. Powers of $y$ then serve as roots of unity in the remaining axes, and multiplication by such a root is a signed shift of the coefficient list. These are the synthetic polynomial transforms of Nussbaumer and Quandalle and Nussbaumer~\cite{NussbaumerQuandalle1978,Nussbaumer1980}.


## Sources (read from disk as needed)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- $r$ means summation index here, but record length on [Simultaneous butterfly layer H₀](butterfly-layer.md), which builds on this page: Rename the second summation index (for example to t), since r is the power-of-two coefficient count on the roots-of-unity, polynomial-ring and butterfly-layer pages.
- $r$ means summation index here, but reduced length on [Root of unity](roots-of-unity.md), which builds on this page: Rename the second summation index (for example to t), since r is the reduced length on the roots-of-unity page.
- $r$ means summation index here, but coefficient count on [Polynomial ring modulo yʳ + 1](polynomial-ring.md), which builds on this page: Rename the second summation index (for example to t), since r is the coefficient count on the polynomial-ring page.

## Previous version (revise it)

It has 219 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 273 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

The discrete Fourier transform is the linear map that turns a vector into its Fourier coefficients. It matters because it turns [cyclic convolution](cyclic-convolution.md) into entrywise products.

Let $u=(u_0,\dots,u_{q-1})$ be a complex vector of length $q$, where $q$ is the number of entries of $u$. The letter $u$ here is not the first input of earlier pages. Let $\omega=\exp(-2\pi i/q)$ be a [primitive $q$-th root of unity](roots-of-unity.md), so $\omega^q=1$ and no smaller positive power of $\omega$ equals $1$.

The transform of $u$, written $\hat u$, has entries $\hat u_k$, where $j$ indexes the entries of $u$ and $k$ indexes those of $\hat u$, each from $0$ to $q-1$, given by

$$\hat u_k=\frac1q\sum_{j=0}^{q-1}u_j\,\omega^{jk},$$

Let $a$ and $b$ be vectors of length $q$. Let $c$ be their cyclic convolution, $c_l=\sum_{j+r\equiv l\ (\mathrm{mod}\ q)}a_j b_r$, where $r$ is a second summation index and $l$ indexes the entries of $c$. Each product $a_jb_r$ appears in $c_l$ for $l\equiv j+r$, and $\omega^{lk}=\omega^{(j+r)k}$ because $\omega^q=1$. Hence

$$\sum_{l=0}^{q-1}c_l\,\omega^{lk}=\sum_{j,r}a_jb_r\,\omega^{(j+r)k}=\Big(\sum_j a_j\omega^{jk}\Big)\Big(\sum_r b_r\omega^{rk}\Big).$$

Here $\hat a$, $\hat b$ and $\hat c$ are the transforms of $a$, $b$ and $c$, each defined by the formula above. Each bracket on the right is $q$ times a transform, and $\hat c_k=\frac1q\sum_l c_l\,\omega^{lk}$, so $\hat c_k=q\,\hat a_k\,\hat b_k$. The transform turns cyclic convolution into entrywise products, up to the factor $q$.

For $q$ a power of two, the fast Fourier transform (FFT) of Cooley and Tukey computes $\hat u$ in $O(q\log q)$ operations: it splits $u$ into its even- and odd-indexed entries and transforms each half at length $q/2$. Let $N(q)$ count the operations on length $q$; splitting gives $N(q)=2N(q/2)+O(q)$, which solves to $O(q\log q)$.

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

Write the body to `exegenius/tasks/0205-write-fourier-transform.answer.md` and the JSON to `exegenius/tasks/0205-write-fourier-transform.answer.json`, then run `exegenius submit 0205-write-fourier-transform` in the project directory. If submit rejects the answer, fix the answer and submit again.
