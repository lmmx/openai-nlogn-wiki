# exegenius task 0132-write-tape-interchange

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
- Gaussian dyadic numbers (also: Gaussian dyadics, Z[i,1/2] (Gaussian dyadic numbers))
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

Concept: Fast interchange of address chunks
Gloss: A fixed-tape procedure that swaps two disjoint equal-width address fields of an array in time O(V u^τ) for a fixed τ < 1, where V is the stored volume and u the field width, using XOR combinations of intermediate data.
Also called: chunk interchange, address chunks, linear-cost address update, address fields, address field, bit procedure

## This page in the argument

The step: Interchanging two equal address fields of width $u$ costs less than linear in $u$ per unit volume.
How: rank-saving recursion on a bit network whose smaller calls have total rank below the number of wires times the parameter
Why: Because the sum of these ranks is less than the number of wires times $m$, the resulting recurrence saves a power of the chunk width. (the sources say so: "An edge matrix of rank $a$ will require $a$ smaller interchanges.
Because the sum of these ranks is less than the number of wires times
$m$, the resulting recurrence saves a power of the chunk width." (paper))

Its sub-steps, in order:

- The address interchange costs $O(Vu^{\tau})$ for a fixed $\tau<1$.

It serves these steps, from the main result down:

- The integer product is computed exactly on one fixed-tape machine in $O(n(\lg n)^{1-\kappa})$ worst-case time, for $\kappa=2^{-182}$.; how: reduce exact multiplication to convolution of radix digits on distinct prime axes, compute the convolution by synthetic transforms on tape layouts, and bound the total tape cost with a power saving (on [Fixed-tape integer multiplication with a power saving](fixed-tape-multiplication.md))
- The tape operations of the algorithm cost $O(V(\lg n)^{1-\kappa})$ in total, for stored volume $V=\Theta(n)$.; how: bound the cost of each tape procedure by a fixed power of its width below linear, then choose compatible fixed rational parameters

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

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Fixed-tape machine model](fixed-tape-model.md): A multitape Turing machine with one fixed finite alphabet and a fixed finite number of one-dimensional tapes, the same for every input length.
  Shown as: Fast interchange of address chunks *<predicate>* Fixed-tape machine model
- [Address shear](address-shear.md): The address permutation that replaces the first of two address fields H by H + D, leaving D fixed, which is the endpoint operator of the bit network on arrays.
  Shown as: Fast interchange of address chunks *<predicate>* Address shear
- [Rank-saving recursion](recursive-saving.md): A recursive scheme in which an edge matrix of rank a costs a smaller calls and the total number s of smaller calls over W roles satisfies s < Wm, so that multiplying the parameter by m multiplies the cost by less than m per unit volume.
  Shown as: Fast interchange of address chunks *<predicate>* Rank-saving recursion
- [Linear network](linear-network.md): A fixed network of wires with gates that apply fixed linear maps to the values on their wires, used here to exchange two banks of values while restoring all auxiliary values.
  Shown as: Fast interchange of address chunks *<predicate>* Linear network
- [Role streams from a cyclic row split](role-streams.md): Splitting the rows of an array cyclically among the W fixed wire roles of a network, so that each role carries an equal share of the volume and gates act pointwise on matching addresses.
  Shown as: Fast interchange of address chunks *<predicate>* Role streams from a cyclic row split

## Pages that build on this one

- Fixed-tape integer multiplication with a power saving: A deterministic fixed-tape Turing machine that multiplies two n-bit integers exactly in O(n(lg n)^(1−κ)) worst-case time, for a fixed κ = 2^(−182), disproving the n log n optimality conjecture in this model.

## Other pages you may link to

- [Schonhage-Strassen optimality conjecture](schonhage-strassen-conjecture.md)
- [Power saving in the logarithmic factor](power-saving.md)
- [Gaussian dyadic numbers](gaussian-dyadic.md)
- [Subset-intersection finite network](subset-network.md)
- [Established fast multiplier](multiplier-subroutine.md)
- [Source, sink and terminal of a network](network-terminal.md)
- [Frame of a vertex](frame.md)
- [Nested subspace labels](subspace-labels.md)
- [Cyclic convolution](cyclic-convolution.md)
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
- [Quotient ring by several relations](quotient-ring.md)
- [Chinese-remainder axis map](crt-axis-map.md)
- [Fixed-tape integer multiplication with a power saving](fixed-tape-multiplication.md)

## Evidence from the sources, with the paragraph around each quote

- "The first procedure interchanges two disjoint contiguous address fields" (paper)

  > The first procedure interchanges two disjoint contiguous address fields of $u$ bits in an array whose addresses form a complete Cartesian product. Its cost is $O(Vu^\tau)$ for a fixed $\tau<1$. Although its final effect is an exact permutation, its intermediate steps form pointwise XOR combinations of data. The final permutation is exact for arbitrary initial auxiliary values.


## Sources (read from disk as needed)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The reader cannot follow this step: "Since $s/W<m$, a fixed $\tau<1$ with $s/W<m^{\tau}$ exists." (s/W < m does not imply s/W < m^tau for a fixed tau < 1. For example, s/W = m - 1 gives m - 1 > m^tau for large m. The page would need a bound of the form s/W <= m^tau, which it neither states nor derives.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step. It is inside reasoning added for an earlier step. If it is part of how this page's own step of the argument works (see "This page in the argument"), develop it here; if it concerns a result that step uses, say what the result states and cite it.
- The reader cannot follow this step: "Each call makes $s$ calls on streams of volume $V/W$, so $F_0=O(1)$ and $F_d\le (s/W)F_{d-1}+O(1)$." (The page never says that the s smaller calls are interchanges of width m^(d-1), only that they act on streams of volume V/W. It does not say why the outer updates add O(1) per unit volume, nor why F_0 = O(1) for the width-one base case.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step. It is inside reasoning added for an earlier step. If it is part of how this page's own step of the argument works (see "This page in the argument"), develop it here; if it concerns a result that step uses, say what the result states and cite it.
- The reader cannot follow this step: "a forward, inverse, forward schedule returns every auxiliary wire to its starting value" (The reader cannot check this because the action of a forward invocation is never stated. The conclusion 'So the shear is exact for any initial auxiliary contents' also needs the page to say that the shear is the forward invocation, which it does not say.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step. It is inside reasoning added for an earlier step. If it is part of how this page's own step of the argument works (see "This page in the argument"), develop it here; if it concerns a result that step uses, say what the result states and cite it.
- Say what $\leftarrow$ denotes where it is first used (for a size or count, what it counts): "$D\leftarrow D-H$, then $H\leftarrow H+D$" (The page says the updates replace one field by a sum or difference, but never says what the arrow denotes.)
- "wire streams" is the concept [Role streams from a cyclic row split](role-streams.md), now a prerequisite: link it where the term is used.

## Previous version (revise it)

It has 325 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 406 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

Fast interchange of address chunks is a procedure that runs on a [Fixed-tape machine model](fixed-tape-model.md) and swaps two disjoint, equal-width address fields of an array. The multiplication algorithm uses it to rearrange its tape layouts, so that the tape cost per unit of stored data falls below linear in the field width.

Let $H$ and $D$ be the two address fields, and let $u$ be their common width, the number of bits in each. Let $V$ be the stored volume, the number of data units in the array. The interchange costs $O(Vu^{\tau})$ for a fixed exponent $\tau<1$ that sets the saving <cite data-source="paper">Its cost is $O(Vu^\tau)$ for a fixed $\tau<1$</cite>.

The interchange reduces to three updates, and the middle one is the [Address shear](address-shear.md), which replaces $H$ by $H+D$ and leaves $D$ fixed: $D\leftarrow D-H$, then $H\leftarrow H+D$, then $D\leftarrow H-D$ send $(H,D)$ to $(D,H)$. The outer two updates cost linear time.

The shear is carried by a bit network, a [Linear network](linear-network.md) whose wires each carry one bit. An edge matrix of rank $a$ costs $a$ smaller calls, and $s$ is the sum of these ranks over all edges. Each smaller call acts on one of the $W$ wire streams, of volume $V/W$. The network satisfies $s<Wm$, where $m$ is the matrix size; the paper checks this for an explicit bit network <cite data-source="paper">supplies these conditions with $W=W_{\rm b}$ and $s=s_{\rm b}$</cite>. The shear is computed by a [Rank-saving recursion](recursive-saving.md) on that network.

Let $F_d$ be the time per unit volume for an interchange of width $m^d$, where $d$ is the recursion depth. Each call makes $s$ calls on streams of volume $V/W$, so $F_0=O(1)$ and $F_d\le (s/W)F_{d-1}+O(1)$. Unrolling gives $F_d=O\left(1+(s/W)+\cdots+(s/W)^d\right)$. Since $s/W<m$, a fixed $\tau<1$ with $s/W<m^{\tau}$ exists. If $s/W\le 1$ the sum is at most $d+1$; if $s/W>1$ it is $O((s/W)^d)$. Either way $F_d=O(m^{d\tau})$, which is $O(u^{\tau})$ per unit volume for $u=m^d$.

Over bits, $H+D$ is XOR, so each shear is a pointwise XOR of data. The auxiliary wires may start with arbitrary contents. A forward invocation adds one bank into the other and changes nothing else, and a forward, inverse, forward schedule returns every auxiliary wire to its starting value. So the shear is exact for any initial auxiliary contents.

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

Write the body to `exegenius/tasks/0132-write-tape-interchange.answer.md` and the JSON to `exegenius/tasks/0132-write-tape-interchange.answer.json`, then run `exegenius submit 0132-write-tape-interchange` in the project directory. If submit rejects the answer, fix the answer and submit again.
