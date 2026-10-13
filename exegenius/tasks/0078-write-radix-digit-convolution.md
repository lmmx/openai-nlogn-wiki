# exegenius task 0078-write-radix-digit-convolution

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
- Cyclic convolution (also: convolution modulo x^S - 1)
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

Concept: Radix-digit convolution
Gloss: Writing each n-bit input as a polynomial in 2^b with about n/b nonnegative digits, so that integer multiplication becomes a convolution whose coefficients are bounded by a fixed power of two.
Also called: radix-2^b digit polynomials

## This page in the argument

The step: Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients.

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

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Cyclic convolution](cyclic-convolution.md): The product of two coefficient lists in the ring of polynomials modulo x^S − 1, in which exponents wrap around modulo S.
  Shown as: Radix-digit convolution *<predicate>* Cyclic convolution

## Pages that build on this one

- Exact recovery by rounding and carries: Recovering the exact integer coefficients of a convolution by rounding the computed values, whose error is below one half, and then propagating carries in radix 2^b.
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
- [Discrete Fourier transform](fourier-transform.md)
- [Multidimensional transform with power-of-two axes](multidim-transform.md)
- [Root of unity](roots-of-unity.md)
- [Polynomial ring modulo yʳ + 1](polynomial-ring.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein's chirp identity](bluestein.md)
- [Chinese-remainder axis map](crt-axis-map.md)
- [Exact recovery by rounding and carries](exact-recovery.md)
- [Fixed-tape integer multiplication with a power saving](fixed-tape-multiplication.md)

## Evidence from the sources, with the paragraph around each quote

- "Splitting the inputs into radix digits reduces multiplication to" (paper)

  > Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients. Our starting point is the Gaussian-resampling reduction of Harvey and van der Hoeven \cite{HarveyHoeven2021}: it replaces the Fourier transforms needed for this convolution by multidimensional transforms whose axis lengths are powers of two. After a further conversion to convolution, one coordinate is stored as the coefficient list of a polynomial modulo $y^r+1$, with $r$ a power of two. Powers of $y$ then serve as roots of unity in the remaining axes, and multiplication by such a root is a signed shift of the coefficient list. These are the synthetic polynomial transforms of Nussbaumer and Quandalle and Nussbaumer~\cite{NussbaumerQuandalle1978,Nussbaumer1980}.


## Sources (read from disk as needed)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- Explain "zero padding" in a sentence where it is first used.

## Previous version (revise it)

It has 266 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 332 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

Radix-digit convolution rewrites the product of two $n$-bit integers as a product of two polynomials with small nonnegative coefficients, which is the first step toward computing integer products on a fixed-tape machine.

Fix a digit width $b$, the number of bits in each radix digit. Let $m = \lceil n/b \rceil$ be the number of digits in each input. The digit $u_i$, for $0 \le i \le m-1$, is the $i$-th radix digit of the first input, and $v_i$ is the $i$-th radix digit of the second input, each in $\{0,\dots,2^b-1\}$. Let $t$ be a formal variable. The polynomial $U(t)$ has the digits of the first input as coefficients. The polynomial $V(t)$ has the digits of the second input as coefficients, so that $U(t) = \sum_{i=0}^{m-1} u_i t^i$ and $V(t) = \sum_{i=0}^{m-1} v_i t^i$.

Evaluating at $t = 2^b$ recovers the inputs, since $U(2^b) = \sum_i u_i 2^{bi}$, and evaluation respects products. The product of the inputs is therefore $U(2^b)V(2^b) = W(2^b)$, where the product polynomial is $W(t) = U(t)V(t)$. Its $k$-th coefficient $w_k$ is the sum of $u_i v_j$ over $i+j=k$, which is a convolution of the two digit lists.

Each $w_k$ is a sum of at most $m$ products $u_i v_j$, each below $2^{2b}$, so $0 \le w_k < m\,2^{2b}$. The coefficients are therefore short nonnegative integers whose bound depends only on $b$ and $m$.

Computing $W$ from the two digit lists is a [Cyclic convolution](cyclic-convolution.md) of length at least $2m-1$ with zero padding, so the integer product is reduced to a cyclic convolution.

For example, take $b = 4$ and $n = 8$, so $m = 2$. The integers $75 = 11 + 4\cdot 16$ and $38 = 6 + 2\cdot 16$ give $U(t) = 11 + 4t$ and $V(t) = 6 + 2t$, so $W(t) = 66 + 46t + 8t^2$. At $t = 16$ this gives $66 + 736 + 2048 = 2850 = 75 \cdot 38$, and every coefficient lies below $m\,2^{2b} = 512$.

The point of the reduction is that a convolution of short coefficients can be computed by transforms, and the carries are handled afterwards by [Exact recovery by rounding and carries](exact-recovery.md).

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

Write the body to `exegenius/tasks/0078-write-radix-digit-convolution.answer.md` and the JSON to `exegenius/tasks/0078-write-radix-digit-convolution.answer.json`, then run `exegenius submit 0078-write-radix-digit-convolution` in the project directory. If submit rejects the answer, fix the answer and submit again.
