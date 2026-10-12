# exegenius task 0168-write-bluestein-chirp

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

For these sources: The reader has an undergraduate computer science degree: big-O notation and worst-case time of Turing machines, polynomials and complex numbers, and the calculus the degree requires (limits, convergence of sequences and series, basic integrals). The same degree is taken to include introductory discrete mathematics (modular arithmetic, primes, induction, sets, graphs, recurrences) and a first course in linear algebra over the reals (vectors, subspaces, matrices, elimination, dot products), each at introductory depth. Fields in the abstract sense, tensor products, bilinear forms over general fields, Gaussian integers and the Chinese remainder theorem are not assumed.

The reader already understands these concepts:

- Big-O notation (also: O-notation)
- Multitape Turing machine (also: fixed-tape model)
- Complex numbers
- Polynomials
- Schönhage–Strassen n log n conjecture (also: n log n optimality conjecture)
- Harvey–van der Hoeven O(n log n) multiplication (also: Harvey and van der Hoeven multiplier)
- Matrix rank (also: rank)
- Discrete Fourier transform (also: Fourier transform, DFT, transform of length n)
- Primitive roots of unity (also: root of unity)
- Cyclic convolution (also: normalized cyclic convolution)
- Multiplication as convolution of digits (also: radix-digit convolution)
- Chinese-remainder address map (also: Chinese remainder map)
- Gaussian resampling (also: Gaussian gridding)
- Polynomial ring modulo yʳ + 1 (also: negacyclic ring, signed shift)
  - $y$ (ring indeterminate): The variable of the polynomial ring whose powers serve as roots of unity in the remaining axes.
  - $r$ (coefficient count): The number of coefficients in the coefficient list of one polynomial record, a power of two.
- Synthetic polynomial transform (also: Nussbaumer polynomial transform, synthetic transform)
- Signed Kronecker packing (also: Kronecker substitution, signed packing)
- Butterfly operation (also: two-point butterfly, H_0)
- Simultaneous butterfly layer (also: butterfly layer)
- Linear network with restored auxiliary values (also: linear network, frame)
- Lower-triangular factorization (also: Bruhat factorization with reversed order)
- Address shear (also: matrix shear)
- Fast address interchange (also: bit interchange procedure, bit procedure)
- Recursive power saving (also: recursive saving)
- Modular arithmetic (also: congruence, congruence modulo c, residue class, mod c arithmetic, integers modulo n)
- Prime numbers and greatest common divisors (also: primes, prime, gcd, greatest common divisor, coprime, relatively prime)
- Arithmetic modulo 2 and XOR (also: F_2, GF(2), Z/2Z, binary field, two-element field, exclusive or, parity, bitwise XOR)
- Dyadic rationals (also: binary fractions, numbers with power-of-two denominators, dyadic numbers, fixed-point binary fractions)
- Vector spaces, subspaces, bases and dimension (also: linear space, subspace, span, linear independence, basis, dimension, ordered basis)
- Linear maps, matrix operations and invertibility (also: linear transformation, linear operator, matrix product, transpose, invertible matrix, nonsingular matrix, inverse matrix, kernel, null space)
- Gaussian elimination (also: row reduction, Gauss-Jordan elimination, elimination, pivot)
- Triangular matrices (also: lower-triangular matrix, upper-triangular matrix, unit triangular matrix)
- Dot product and orthogonality in R^n (also: inner product, scalar product, orthogonal vectors, orthonormal basis, orthogonal complement)
- Permutations of a finite set (also: permutation, rearrangement, bijection of an index set, permutation matrix)
- Finite sets, subsets and intersections (also: set intersection, cardinality, subset, k-subset, binomial coefficient, power set)
- Graphs (also: undirected graph, vertices and edges, adjacency, neighbours, intersection graph, source and sink vertices of the network)
- Mathematical induction (also: induction, inductive proof, strong induction, proof by induction on n)
- Recurrence relations and divide-and-conquer recursion (also: recurrence, recursion equation, divide and conquer, recursive algorithm, cost recurrence, T(n) recurrence)
- Floor and ceiling functions (also: integer part, floor, ceiling, ⌊x⌋, ⌈x⌉)
- Logarithms base 2 (also: lg, log base 2, binary logarithm, log_2)
- Big-Omega and big-Theta notation (also: Omega notation, Theta notation, Ω, Θ, asymptotic lower bound, asymptotic tight bound)
- Limits and convergence of sequences and series (also: limit of a sequence, convergent sequence, convergent series, sum of a series, n tends to infinity)
- Geometric series (also: geometric sum, geometric progression sum, sum of powers of a ratio)
- Newton's method (also: Newton iteration, Newton-Raphson method, Newton reduction, Newton's root-finding iteration)
- Worst-case time complexity of a Turing machine (also: running time, worst-case running time, time bound, T_A(n), time on n-bit inputs)
- Tensor product

## This page

Concept: Bluestein's chirp identity
Gloss: The identity that converts a Fourier transform into a cyclic convolution by multiplying by chirp factors before and after it.
Also called: chirp identity, Bluestein conversion, chirp factors

## This page in the argument

The step: The middle transform, with its target permutation, becomes normalized cyclic convolution.
How: Bluestein's chirp identity with chirp factors before and after the transform
Why: A cyclic convolution is the form that the polynomial-ring convolution can compute. (the sources leave this for the reader to work out: spell it out)

Its sub-steps, in order:

- Bluestein's chirp identity converts the middle transform into a normalized cyclic convolution.

It serves these steps, from the main result down:

- Two $n$-bit integers can be multiplied exactly in $O(n(\lg n)^{1-\kappa})$ worst-case time on a deterministic multitape Turing machine, for a fixed $\kappa=2^{-182}$.; how: reduce the product to a digit convolution, compute that convolution through transform layers whose tape cost saves a power, and recover the exact product by rounding (on [Integer multiplication in O(n(lg n)^(1-κ)) time](integer-multiplication-target.md))

## Symbols already bound on earlier pages

The symbols in the names of the concepts the reader knows are listed with those concepts above.

- $n$ (input bit length), bound on [Schönhage–Strassen n log n conjecture](nlogn-conjecture.md): The number of bits in each input integer; the count of bits in one operand.
- $\kappa$ (exponent gap), bound on [Schönhage–Strassen n log n conjecture](nlogn-conjecture.md): A fixed positive constant, the gap $\kappa = 2^{-182}$ in the exponent of the logarithm.
- $\kappa$ (exponent gap), bound on [Harvey–van der Hoeven O(n log n) multiplication](harvey-hoeven-multiplier.md): A fixed positive constant, $2^{-182}$, by which the logarithmic exponent of the target running time falls below 1.
- $n$ (root order), bound on [Primitive roots of unity](roots-of-unity.md): The order of the root, a positive integer that counts the positions of the transform it labels.
- $\omega$ (primitive root), bound on [Primitive roots of unity](roots-of-unity.md): A primitive $n$-th root of unity, the complex number that labels the positions of a transform.
- $k$ (power exponent), bound on [Primitive roots of unity](roots-of-unity.md): An integer exponent of the root, marking which power of $\omega$ is meant.
- $j$ (earlier exponent), bound on [Primitive roots of unity](roots-of-unity.md): An integer exponent of the root, the smaller of two powers compared in the distinctness argument.
- $n$ (sequence length), bound on [Discrete Fourier transform](fourier-transform.md): The number of entries in the input and output sequences, the length of the transform; it is also the order of $\omega$.
- $a$ (input sequence), bound on [Discrete Fourier transform](fourier-transform.md): The input sequence, a list of $n$ complex numbers $a_0,\dots,a_{n-1}$.
- $\hat a$ (output sequence), bound on [Discrete Fourier transform](fourier-transform.md): The DFT of $a$, whose entries $\hat a_k$ are given by the formula below.
- $j$ (input index), bound on [Discrete Fourier transform](fourier-transform.md): The index of an input entry $a_j$, running from $0$ to $n-1$.
- $k$ (output index), bound on [Discrete Fourier transform](fourier-transform.md): The index of an output entry $\hat a_k$, running from $0$ to $n-1$.
- $p$ (coefficient polynomial), bound on [Discrete Fourier transform](fourier-transform.md): The polynomial $p(x)=\sum_{j} a_j x^j$ whose coefficient list is $a$.
- $x$ (formal variable), bound on [Discrete Fourier transform](fourier-transform.md): The formal variable of $p$, a placeholder for a number to be substituted.
- $u$ (first input value), bound on [Butterfly operation](butterfly-operation.md): The first of the two input values that the butterfly maps.
- $v$ (second input value), bound on [Butterfly operation](butterfly-operation.md): The second of the two input values that the butterfly maps.
- $H_0$ (butterfly map), bound on [Butterfly operation](butterfly-operation.md): The two-point map sending a pair of values to its half-sum and half-difference.
- $I$ (identity matrix), bound on [Butterfly operation](butterfly-operation.md): The $2\times 2$ identity matrix, which leaves every pair unchanged.
- $x$ (formal variable), bound on [Cyclic convolution](cyclic-convolution.md): A formal variable, an indeterminate not evaluated at any number, used as the placeholder of the polynomials a(x) and b(x).
- $r$ (sequence length), bound on [Cyclic convolution](cyclic-convolution.md): The number of complex coefficients in each input sequence, so both sequences have length r.
- $b$ (second input sequence), bound on [Cyclic convolution](cyclic-convolution.md): The second of the two input sequences, a list of r complex numbers.
- $c$ (cyclic convolution), bound on [Cyclic convolution](cyclic-convolution.md): The cyclic convolution of a and b, a sequence of r complex coefficients.
- $l$ (term index of b), bound on [Cyclic convolution](cyclic-convolution.md): An index running over 0 to r-1 that labels the terms of b in the reduced product.
- $b$ (digit width), bound on [Multiplication as convolution of digits](convolution-reduction.md): The number of bits in one digit, so each digit lies between 0 and 2^b-1.
- $m$ (digit count), bound on [Multiplication as convolution of digits](convolution-reduction.md): The number of digits in each input, the count of radix-2^b digits of each integer.
- $U$ (first input integer), bound on [Multiplication as convolution of digits](convolution-reduction.md): The first of the two integers being multiplied.
- $V$ (second input integer), bound on [Multiplication as convolution of digits](convolution-reduction.md): The second of the two integers being multiplied.
- $y$ (ring indeterminate), bound on [Polynomial ring modulo yʳ + 1](polynomial-ring-y.md): The variable of the polynomial ring, an indeterminate that is not evaluated at any number.
- $r$ (coefficient count), bound on [Polynomial ring modulo yʳ + 1](polynomial-ring-y.md): The number of complex coefficients in the list of one element of the ring, a power of two.
- $\theta$ (twist factor), bound on [Polynomial ring modulo yʳ + 1](polynomial-ring-y.md): A complex $2r$-th root of unity with $\theta^r=-1$, by which the phase twist multiplies the entries of a coefficient list.
- $x$ (input sequence), bound on [Synthetic polynomial transform](synthetic-transform.md): The sequence $x_0,\dots,x_{2r-1}$ of ring elements whose transform is taken.
- $t$ (input position), bound on [Synthetic polynomial transform](synthetic-transform.md): The position of an input entry $x_t$, running over $0,\dots,2r-1$.
- $s$ (frequency index), bound on [Synthetic polynomial transform](synthetic-transform.md): The index of a transform entry, running over $0,\dots,2r-1$.
- $\hat{x}$ (transform of x), bound on [Synthetic polynomial transform](synthetic-transform.md): The transform entry at frequency $s$, the sum of $y^{st}x_t$ over the input positions $t$.
- $i$ (frequency pair index), bound on [Synthetic polynomial transform](synthetic-transform.md): The index of the frequency pair $2i$ and $2i+1$, running over the $r$ pairs $0,\dots,r-1$.
- $u$ (integer exponent), bound on [Synthetic polynomial transform](synthetic-transform.md): An integer exponent of $y$ in the inverse identity.
- $z$ (second sequence), bound on [Synthetic polynomial transform](synthetic-transform.md): The second sequence $z_0,\dots,z_{2r-1}$ of ring elements, transformed the same way as $x$.
- $\hat{z}$ (transform of z), bound on [Synthetic polynomial transform](synthetic-transform.md): The transform entry at frequency $s$ of $z$, the sum of $y^{sq}z_q$ over the input positions $q$.
- $q$ (input position in z), bound on [Synthetic polynomial transform](synthetic-transform.md): The position of an entry $z_q$ of the second sequence, running over $0,\dots,2r-1$.
- $h$ (output position), bound on [Synthetic polynomial transform](synthetic-transform.md): The position of an entry of the cyclic convolution, taken modulo $2r$.
- $x\ast z$ (cyclic convolution), bound on [Synthetic polynomial transform](synthetic-transform.md): The cyclic convolution of $x$ and $z$, whose entries are $(x\ast z)_h$.
- $f$ (packed ring element), bound on [Signed Kronecker packing](kronecker-packing.md): A ring element with integer coefficients $f_j$, the first of the two elements being packed.
- $g$ (second ring element), bound on [Signed Kronecker packing](kronecker-packing.md): A ring element with integer coefficients $g_j$, the second of the two elements being packed.
- $M$ (coefficient bound), bound on [Signed Kronecker packing](kronecker-packing.md): A bound on the absolute value of every coefficient of f and g.
- $j$ (coefficient position), bound on [Signed Kronecker packing](kronecker-packing.md): An index running over the r coefficient positions of f and g, from 0 to r-1.
- $k$ (product position), bound on [Signed Kronecker packing](kronecker-packing.md): An index over the coefficient positions of the unreduced product w.
- $B$ (packing base), bound on [Signed Kronecker packing](kronecker-packing.md): A power of two, larger than 2rM^2, at which the coefficient lists are evaluated.
- $F$ (packed integer of f), bound on [Signed Kronecker packing](kronecker-packing.md): The integer obtained by evaluating f at B.
- $G$ (packed integer of g), bound on [Signed Kronecker packing](kronecker-packing.md): The integer obtained by evaluating g at B.
- $w$ (unreduced product), bound on [Signed Kronecker packing](kronecker-packing.md): The product fg before reduction modulo y^r+1, whose coefficients are w_k.
- $A$ (real matrix), bound on [Matrix rank](matrix-rank.md): The real matrix whose rank is taken.
- $\Omega$ (address set), bound on [Linear network with restored auxiliary values](linear-network-exchange.md): The finite set of addresses at which every array on the network's wires is indexed.
- $w$ (input role), bound on [Linear network with restored auxiliary values](linear-network-exchange.md): An input role, the fixed place where the network takes in one of its values.
- $\rho$ (output role map), bound on [Linear network with restored auxiliary values](linear-network-exchange.md): The map sending each input role $w$ to the output role $\rho(w)$ that carries it.
- $\varepsilon_w$ (prescribed sign), bound on [Linear network with restored auxiliary values](linear-network-exchange.md): The fixed sign, plus or minus one, that the route from input role $w$ applies.
- $D_v$ (frame), bound on [Linear network with restored auxiliary values](linear-network-exchange.md): The invertible linear operator on arrays indexed by $\Omega$ attached to the vertex $v$.
- $\alpha$ (tail vertex), bound on [Linear network with restored auxiliary values](linear-network-exchange.md): A vertex of the network, the vertex where an edge starts.
- $\beta$ (head vertex), bound on [Linear network with restored auxiliary values](linear-network-exchange.md): A vertex of the network, the vertex where an edge from $\alpha$ ends.
- $\mathrm{source}(w)$ (source vertex), bound on [Linear network with restored auxiliary values](linear-network-exchange.md): The source vertex where the input role $w$ enters the network.
- $\mathrm{sink}(\rho(w))$ (sink vertex), bound on [Linear network with restored auxiliary values](linear-network-exchange.md): The sink vertex where the output role $\rho(w)$ leaves the network.
- $\xi$ (example address), bound on [Linear network with restored auxiliary values](linear-network-exchange.md): One address in $\Omega$ at which the worked example is evaluated.
- $\lambda$ (first example value), bound on [Linear network with restored auxiliary values](linear-network-exchange.md): The value on the first wire at the address $\xi$ in the example.
- $\mu$ (second example value), bound on [Linear network with restored auxiliary values](linear-network-exchange.md): The value on the second wire at the address $\xi$ in the example.
- $A$ (input matrix), bound on [Lower-triangular factorization](lower-triangular-factorization.md): The rational m×m matrix that is factored.
- $m$ (matrix size), bound on [Lower-triangular factorization](lower-triangular-factorization.md): The number of rows of A, so A is m×m; here m replaces its earlier meaning of digits per input.
- $E_1$ (left lower-triangular factor), bound on [Lower-triangular factorization](lower-triangular-factorization.md): An invertible lower-triangular matrix, the left factor in A = E_1 Π E_2.
- $E_2$ (right lower-triangular factor), bound on [Lower-triangular factorization](lower-triangular-factorization.md): An invertible lower-triangular matrix, the right factor in A = E_1 Π E_2.
- $\Pi$ (partial permutation matrix), bound on [Lower-triangular factorization](lower-triangular-factorization.md): The matrix in the factorization with at most one 1 in each row and column and all other entries 0.
- $a$ (number of ones), bound on [Lower-triangular factorization](lower-triangular-factorization.md): The number of entries equal to 1 in Π, which equals the rank of A.
- $H$ (first address group), bound on [Address shear](address-shear.md): The first group of address fields, a vector over a common residue ring with one entry for each row of A.
- $D$ (second address group), bound on [Address shear](address-shear.md): The second group of address fields, with one entry for each column of A.
- $s$ (field index of H), bound on [Address shear](address-shear.md): An index running over the fields of H, labelling the row of a 1 in Π.
- $t$ (field index of D), bound on [Address shear](address-shear.md): An index running over the fields of D, labelling the column of a 1 in Π.
- $V$ (stored bit volume), bound on [Fast address interchange](address-interchange.md): The number of data bits the array holds.
- $u$ (field width), bound on [Fast address interchange](address-interchange.md): The number of address bits in one field.
- $\tau$ (cost exponent), bound on [Fast address interchange](address-interchange.md): A fixed exponent in the cost bound, with $0<\tau<1$.
- $W$ (wire count), bound on [Fast address interchange](address-interchange.md): The number of wires of the network, scratch wires included.
- $e$ (edge), bound on [Fast address interchange](address-interchange.md): An edge of the network, the wire segment between two consecutive vertices.
- $G_e$ (edge matrix change), bound on [Fast address interchange](address-interchange.md): The difference of the end-vertex matrices of edge e, by which the frame changes along e.
- $\beta$ (matrix size), bound on [Fast address interchange](address-interchange.md): The number of rows and columns of each matrix of the network.
- $R$ (total edge rank), bound on [Fast address interchange](address-interchange.md): The sum of the edge matrix ranks, which counts the recursive calls in one level.
- $\varphi$ (time per stored bit), bound on [Fast address interchange](address-interchange.md): The running time at width u divided by the stored bit volume.
- $C$ (level constant), bound on [Fast address interchange](address-interchange.md): A constant bounding the work of one level per stored bit.
- $\lambda$ (level cost ratio), bound on [Fast address interchange](address-interchange.md): The ratio R/W, the cost factor per level.
- $\ell$ (level count), bound on [Fast address interchange](address-interchange.md): The number of levels, each dividing the field width by beta.
- $N$ (coefficient count), bound on [Chinese-remainder address map](chinese-remainder-address-map.md): The number of coefficients in the list, which is the product of the axis lengths.
- $d$ (axis count), bound on [Chinese-remainder address map](chinese-remainder-address-map.md): The number of cyclic axes on which the list is placed.
- $q_1$ (axis prime length), bound on [Chinese-remainder address map](chinese-remainder-address-map.md): The prime length of an axis, the axes being $q_1,\dots,q_d$.
- $e$ (list position), bound on [Chinese-remainder address map](chinese-remainder-address-map.md): An index of a position in the list, running from $0$ to $N-1$.
- $X$ (first vector space), bound on [Tensor product](tensor-product.md): A complex vector space, the first factor of the tensor product.
- $Y$ (second vector space), bound on [Tensor product](tensor-product.md): A complex vector space, the second factor of the tensor product.
- $\beta$ (basis vector of X), bound on [Tensor product](tensor-product.md): A basis vector of X, one half of a basis pair of the tensor product.
- $\gamma$ (basis vector of Y), bound on [Tensor product](tensor-product.md): A basis vector of Y, the other half of a basis pair of the tensor product.
- $S$ (map on X), bound on [Tensor product](tensor-product.md): A linear map on X, the factor acting on the X-part of a pair.
- $T$ (map on Y), bound on [Tensor product](tensor-product.md): A linear map on Y, the factor acting on the Y-part of a pair.
- $D$ (selected chunk count), bound on [Tensor product](tensor-product.md): The number of address chunks, each contributing one selected address bit to the layer.
- $d$ (chunk bound), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The largest number of equal-width address chunks that one layer acts on, a count.
- $D$ (chunks per layer), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The number of selected equal-width address chunks used in one layer, a count, at most d.
- $\lambda'$ (layer exponent), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): A fixed exponent below one in the layer's cost bound, so that the cost grows in d more slowly than d itself.
- $W$ (role count), bound on [Recursive power saving](recursive-power-saving.md): The number of roles of the network, the input wires that each carry a share of the data.
- $s$ (smaller-call count), bound on [Recursive power saving](recursive-power-saving.md): The number of smaller calls that the network makes.
- $m$ (parameter multiplier), bound on [Recursive power saving](recursive-power-saving.md): The factor by which the parameter grows from a smaller call to the call above it.
- $e$ (smaller-call parameter), bound on [Recursive power saving](recursive-power-saving.md): The parameter of a smaller call.
- $L$ (level count), bound on [Recursive power saving](recursive-power-saving.md): The number of levels of recursion, counting the top call's level.
- $\ell$ (level index), bound on [Recursive power saving](recursive-power-saving.md): The index of a level, counted from the top level, which is 0.
- $\alpha$ (saving exponent), bound on [Recursive power saving](recursive-power-saving.md): The exponent of the saving, the value of $\log_m(s/W)$ that makes $s/W$ equal to $m^\alpha$.
- $q$ (prime length), bound on [Gaussian resampling](gaussian-resampling.md): The prime number that is the length of the sequence z, the count of its complex entries.
- $z$ (input sequence), bound on [Gaussian resampling](gaussian-resampling.md): The sequence of q complex numbers that the transform acts on; on the synthetic transform page the same letter names a second sequence.
- $F_q$ (normalized transform), bound on [Gaussian resampling](gaussian-resampling.md): The normalized discrete Fourier transform of length q.
- $s$ (source transform length), bound on [Gaussian resampling](gaussian-resampling.md): The length of the source transform, the count of entries of the sequences it acts on.
- $t$ (target transform length), bound on [Gaussian resampling](gaussian-resampling.md): The length of the target transform, a power of two, which is the count of its entries.
- $F_s$ (normalized source transform), bound on [Gaussian resampling](gaussian-resampling.md): The normalized discrete Fourier transform of length s.
- $F_t$ (normalized target transform), bound on [Gaussian resampling](gaussian-resampling.md): The normalized discrete Fourier transform of length t.
- $P_s$ (source permutation), bound on [Gaussian resampling](gaussian-resampling.md): The coordinate permutation of the outputs of the source transform.
- $P_t$ (target permutation), bound on [Gaussian resampling](gaussian-resampling.md): The coordinate permutation of the outputs of the target transform.
- $c$ (identity constant), bound on [Gaussian resampling](gaussian-resampling.md): A power of two that is the same for all s and t, the constant factor of the identity.
- $L_1$ (first contraction), bound on [Gaussian resampling](gaussian-resampling.md): A linear contraction from the space of length-s sequences to the space of length-t sequences.
- $L_2$ (second contraction), bound on [Gaussian resampling](gaussian-resampling.md): A linear contraction from the space of length-t sequences to the space of length-s sequences.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Gaussian resampling](gaussian-resampling.md): An identity that expresses a Fourier transform of length given by a prime as a multidimensional transform with power-of-two axis lengths, with the source and target permutations kept in the identity.
  Shown as: Bluestein's chirp identity *<predicate>* Gaussian resampling
- [Cyclic convolution](cyclic-convolution.md): The product of two sequences in which indices are taken modulo a fixed length, so each coefficient of the result is a sum of products over residues.
  Shown as: Bluestein's chirp identity *<predicate>* Cyclic convolution

## Pages that build on this one

- Exact recovery by rounding: The step in which the approximate convolution coefficients are rounded to integers, provided the error is strictly below 1/2, and carries are then propagated to give the exact binary product.
- Integer multiplication in O(n(lg n)^(1-κ)) time: A deterministic multitape Turing machine that multiplies two n-bit integers exactly in O(n(lg n)^(1-κ)) worst-case time for a fixed κ = 2^(-182) > 0, beating the n log n conjecture in this model.

## Other pages you may link to

- [Schönhage–Strassen n log n conjecture](nlogn-conjecture.md)
- [Harvey–van der Hoeven O(n log n) multiplication](harvey-hoeven-multiplier.md)
- [Primitive roots of unity](roots-of-unity.md)
- [Discrete Fourier transform](fourier-transform.md)
- [Butterfly operation](butterfly-operation.md)
- [Multiplication as convolution of digits](convolution-reduction.md)
- [Polynomial ring modulo yʳ + 1](polynomial-ring-y.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Signed Kronecker packing](kronecker-packing.md)
- [Matrix rank](matrix-rank.md)
- [Linear network with restored auxiliary values](linear-network-exchange.md)
- [Lower-triangular factorization](lower-triangular-factorization.md)
- [Address shear](address-shear.md)
- [Fast address interchange](address-interchange.md)
- [Chinese-remainder address map](chinese-remainder-address-map.md)
- [Tensor product](tensor-product.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Recursive power saving](recursive-power-saving.md)
- [Exact recovery by rounding](rounding-recovery.md)
- [Integer multiplication in O(n(lg n)^(1-κ)) time](integer-multiplication-target.md)

## Evidence from the sources, with the paragraph around each quote

- "Bluestein's chirp identity converts the middle transform" (paper)

  > Next, Bluestein's chirp identity converts the middle transform, including its target permutation, into normalized cyclic convolution. A phase twist changes the last cyclic coordinate into a polynomial modulo $y^r+1$; its negative wrap gives precisely the original cyclic wrap after the twist is removed. Sections~\ref{sec:synthetic-layouts} and~\ref{sec:exact-ring-products} compute convolution on the remaining axes over this polynomial ring. The two forward synthetic transforms retain the same frequency order through their pointwise product, and the opposite transform consumes that order. Their polynomial products use signed packing and the established $O(n\log n)$ multiplier as an ordinary subroutine.


## Sources (read from disk as needed)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- $\alpha$ means wrapped coefficient here, but tail vertex on [Linear network with restored auxiliary values](linear-network-exchange.md), which this page builds on: On bluestein-chirp, the wrapped coefficient alpha clashes with the tail vertex alpha of linear-network-exchange. Use another letter for the wrapped coefficient (e.g. gamma).

## Previous version (revise it)

It has 277 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 346 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

Bluestein's chirp identity rewrites a Fourier transform as a [normalized cyclic convolution](cyclic-convolution.md) that is bracketed by multiplications by chirps, where a chirp is a factor whose exponent is quadratic in an index. It turns the middle transform into a form that the polynomial ring can compute.

The identity is applied to the middle transform produced by [Gaussian resampling](gaussian-resampling.md). That transform's target permutation $P_t$ is the reordering of its output indices that the next stage needs; this page sets it aside and uses the plain order.

Start from the plain transform $\hat a_k=\sum_{j=0}^{n-1}a_j\,\omega^{jk}$ for $k=0,\dots,n-1$, where $\omega=e^{2\pi i/n}$. Let $\zeta=e^{\pi i/n}$, so that $\zeta^2=\omega$ and $\zeta^n=-1$; $\zeta$ is the chirp base, and its powers are the chirp factors. Since $2jk=j^2+k^2-(k-j)^2$, we have $\omega^{jk}=\zeta^{j^2}\zeta^{k^2}\zeta^{-(k-j)^2}$, and therefore
$$\hat a_k=\zeta^{k^2}\sum_{j=0}^{n-1}\bigl(\zeta^{j^2}a_j\bigr)\,\zeta^{-(k-j)^2}.$$

The factors $\zeta^{j^2}$ before the sum and $\zeta^{k^2}$ after it are the chirps. Write $\nu$ for an integer offset. The sum is a convolution that pairs $\zeta^{j^2}a_j$ with the chirp $\zeta^{-\nu^2}$ at offset $\nu=k-j$. It is cyclic when $n$ is even, because the chirp then has period $n$:
$$\zeta^{-(\nu+n)^2}=\zeta^{-\nu^2}\,\omega^{-\nu n}\,\zeta^{-n^2}=\zeta^{-\nu^2},$$
since $\omega^{-\nu n}=1$ and $\zeta^{-n^2}=(\zeta^n)^{-n}=(-1)^n=1$. So the transform is computed by multiplying by chirps, convolving cyclically, and multiplying again. For $n=2$, $\omega=-1$, $\zeta=i$, the formula at $k=1$ gives $i(-ia_0+ia_1)=a_0-a_1$, the value the definition gives.

The cyclic form matters because of the polynomial ring. Let $\sigma$ be a coefficient position, from $0$ to $n-1$. In $\mathbb C[y]/(y^r+1)$ with $r=n$, a product term past the top coefficient picks up a minus sign, since $y^r=-1$. A phase twist removes this sign: multiply the coefficient of $y^\sigma$ by $\zeta^\sigma$ before the product, and by $\zeta^{-\sigma}$ after it. Let $\alpha$ be the coefficient at $y^{\sigma+n}$ in the twisted product. That term wraps to $-\alpha\zeta^{-\sigma}y^\sigma$ after the untwist, and $-\alpha\zeta^{-\sigma}=\alpha\zeta^{-(\sigma+n)}$ because $\zeta^n=-1$, which is the untwisted term moved to $y^\sigma$. The ring therefore computes a cyclic convolution <cite data-source="paper">its negative wrap gives precisely the original cyclic wrap after the twist is removed</cite>.

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

Write the body to `exegenius/tasks/0168-write-bluestein-chirp.answer.md` and the JSON to `exegenius/tasks/0168-write-bluestein-chirp.answer.json`, then run `exegenius submit 0168-write-bluestein-chirp` in the project directory. If submit rejects the answer, fix the answer and submit again.
