# exegenius task 0068-write-recursive-power-saving

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
- Bluestein's chirp identity (also: chirp identity, Bluestein conversion)
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

Concept: Recursive power saving
Gloss: The mechanism in which a network with s smaller calls on W roles and parameter m gives a recursion with cost ratio s/W < m, so that repeated recursion saves a power of the parameter.
Also called: recursive saving

## This page in the argument

The step: Both tape procedures cost $O(V)$ times a power of their parameter whose exponent is strictly below one.
How: give each procedure a fixed linear network with fewer smaller calls than roles, and iterate the resulting recursion
Why: If the number of smaller calls per role is below the parameter multiplier, repeated recursion compounds into a power saving. (the sources leave this for the reader to work out: spell it out)
Striking feature: the saving is a fixed power of the parameter, with exponent strictly below one, uniform over all widths and volumes (explain why it holds, from the method)

Its sub-steps, in order:

- The address interchange of $u$-bit fields costs $O(Vu^\tau)$ for a fixed $\tau<1$. (on [Fast address interchange](address-interchange.md))
- A simultaneous butterfly layer on $d$ chunks costs $O(Vd^{\lambda'})$ for a fixed $\lambda'<1$. (on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md))
- Each tape procedure is a fixed linear network that exchanges two banks of values and restores every auxiliary value. (on [Linear network with restored auxiliary values](linear-network-exchange.md))
- The network has $W$ roles and $s$ smaller calls with $s<Wm$.
- Multiplying the parameter by $m$ multiplies the recursive cost ratio by $s/W<m$, which is a strict power saving.

It serves these steps, from the main result down:

- Two $n$-bit integers can be multiplied exactly in $O(n(\lg n)^{1-\kappa})$ worst-case time on a deterministic multitape Turing machine, for a fixed $\kappa=2^{-182}$.; how: reduce the product to a digit convolution, compute that convolution through transform layers whose tape cost saves a power, and recover the exact product by rounding (on [Integer multiplication in O(n(lg n)^(1-κ)) time](integer-multiplication-target.md))

## Symbols already bound on earlier pages

The symbols in the names of the concepts the reader knows are listed with those concepts above.

- $n$ (input bit length), bound on [Schönhage–Strassen n log n conjecture](nlogn-conjecture.md): The number of bits in each input integer; the count of bits of each of the two integers being multiplied.
- $n$ (input length), bound on [Harvey–van der Hoeven O(n log n) multiplication](harvey-hoeven-multiplier.md): The number of bits in each input integer.
- $n$ (root order), bound on [Primitive roots of unity](roots-of-unity.md): A positive integer, the order of the root of unity.
- $\omega$ (primitive root), bound on [Primitive roots of unity](roots-of-unity.md): A complex number that is a primitive $n$-th root of unity.
- $k$ (power index), bound on [Primitive roots of unity](roots-of-unity.md): An integer exponent, the power of $\omega$ being tested against 1.
- $n$ (sequence length), bound on [Discrete Fourier transform](fourier-transform.md): The number of entries in the input sequence, which is also the number of output values.
- $a$ (input sequence), bound on [Discrete Fourier transform](fourier-transform.md): The length-$n$ list of complex numbers that the transform is applied to.
- $\omega$ (primitive root), bound on [Discrete Fourier transform](fourier-transform.md): A primitive n-th root of unity, whose powers give the points at which the transform evaluates.
- $\hat{a}$ (output sequence), bound on [Discrete Fourier transform](fourier-transform.md): The discrete Fourier transform of the input sequence, a list of n values.
- $j$ (input index), bound on [Discrete Fourier transform](fourier-transform.md): An index of an input entry, running from 0 to n-1.
- $k$ (output index), bound on [Discrete Fourier transform](fourier-transform.md): An index of an output entry, running from 0 to n-1.
- $H_0$ (two-point butterfly), bound on [Butterfly operation](butterfly-operation.md): The map sending a pair of values to its scaled sum and scaled difference.
- $u$ (first input value), bound on [Butterfly operation](butterfly-operation.md): The first of the two input values of the butterfly.
- $v$ (second input value), bound on [Butterfly operation](butterfly-operation.md): The second of the two input values of the butterfly.
- $r$ (sequence length), bound on [Cyclic convolution](cyclic-convolution.md): The number of complex coefficients in each sequence being convolved.
- $a$ (first sequence), bound on [Cyclic convolution](cyclic-convolution.md): The first input sequence, a list of r complex coefficients a_0 through a_{r-1}.
- $b$ (second sequence), bound on [Cyclic convolution](cyclic-convolution.md): The second input sequence, a list of r complex coefficients b_0 through b_{r-1}.
- $c$ (cyclic convolution), bound on [Cyclic convolution](cyclic-convolution.md): The cyclic convolution of a and b, a sequence of length r.
- $k$ (output index), bound on [Cyclic convolution](cyclic-convolution.md): The index of an output coefficient of the cyclic convolution, running from 0 to r-1.
- $j$ (summation index), bound on [Cyclic convolution](cyclic-convolution.md): The index of a term in the sum for one output coefficient, running from 0 to r-1.
- $x$ (formal variable), bound on [Cyclic convolution](cyclic-convolution.md): A formal variable (indeterminate) used to write the sequences as polynomials; it is not evaluated at any number.
- $b$ (digit width), bound on [Multiplication as convolution of digits](convolution-reduction.md): The number of bits in one digit, so that digits are taken in radix $2^b$.
- $m$ (digits per input), bound on [Multiplication as convolution of digits](convolution-reduction.md): The number of radix-$2^b$ digits in each input.
- $u$ (first input), bound on [Multiplication as convolution of digits](convolution-reduction.md): The first of the two integers being multiplied.
- $v$ (second input), bound on [Multiplication as convolution of digits](convolution-reduction.md): The second of the two integers being multiplied.
- $y$ (ring indeterminate), bound on [Polynomial ring modulo yʳ + 1](polynomial-ring-y.md): The variable of the polynomial ring whose powers serve as roots of unity in the remaining axes.
- $r$ (coefficient count), bound on [Polynomial ring modulo yʳ + 1](polynomial-ring-y.md): The number of complex coefficients in the coefficient list of one polynomial record, a power of two.
- $x$ (input sequence), bound on [Synthetic polynomial transform](synthetic-transform.md): A sequence of $2r$ ring elements, the input of the transform.
- $j$ (frequency index), bound on [Synthetic polynomial transform](synthetic-transform.md): The index of a transform output, running over the $2r$ frequencies.
- $k$ (input position), bound on [Synthetic polynomial transform](synthetic-transform.md): The index of an input entry, running over the $2r$ positions of the sequence.
- $j$ (coefficient index), bound on [Signed Kronecker packing](kronecker-packing.md): The index running over the $r$ coefficient positions of a polynomial in the ring, $0 \le j < r$.
- $f$ (packed polynomial), bound on [Signed Kronecker packing](kronecker-packing.md): An element of the ring whose integer coefficients $f_j$ are packed into an integer.
- $g$ (second polynomial), bound on [Signed Kronecker packing](kronecker-packing.md): A second element of the ring with integer coefficients $g_j$, packed in the same way as $f$.
- $M$ (coefficient bound), bound on [Signed Kronecker packing](kronecker-packing.md): A bound on the absolute value of every coefficient of $f$ and $g$.
- $B$ (packing base), bound on [Signed Kronecker packing](kronecker-packing.md): The power of two at which polynomials are evaluated to pack them into integers.
- $F$ (packed integer of f), bound on [Signed Kronecker packing](kronecker-packing.md): The integer obtained by evaluating $f$ at the packing base $B$.
- $G$ (packed integer of g), bound on [Signed Kronecker packing](kronecker-packing.md): The integer obtained by evaluating $g$ at the packing base $B$.
- $h$ (unreduced product), bound on [Signed Kronecker packing](kronecker-packing.md): The product $fg$ of $f$ and $g$ as polynomials, before reduction modulo $y^r+1$.
- $k$ (product power), bound on [Signed Kronecker packing](kronecker-packing.md): The power of $y$ indexing a coefficient $h_k$ of the unreduced product.
- $M$ (matrix), bound on [Matrix rank](matrix-rank.md): A real matrix whose rank the page computes.
- $\Omega$ (address set), bound on [Linear network with restored auxiliary values](linear-network-exchange.md): The finite set of addresses that indexes the array of values on each wire.
- $D_v$ (frame), bound on [Linear network with restored auxiliary values](linear-network-exchange.md): The invertible linear operator on arrays indexed by $\Omega$ attached to the source, gate or sink $v$.
- $A$ (rational matrix), bound on [Lower-triangular factorization](lower-triangular-factorization.md): The rational m×m matrix that is factored.
- $m$ (matrix size), bound on [Lower-triangular factorization](lower-triangular-factorization.md): The number of rows, and of columns, of the matrix A.
- $E_1$ (left lower factor), bound on [Lower-triangular factorization](lower-triangular-factorization.md): The first invertible lower-triangular factor in the factorization of A.
- $E_2$ (right lower factor), bound on [Lower-triangular factorization](lower-triangular-factorization.md): The second invertible lower-triangular factor in the factorization of A.
- $\Pi$ (partial permutation), bound on [Lower-triangular factorization](lower-triangular-factorization.md): The partial permutation matrix in the factorization, with at most one 1 in each row and column and all other entries 0.
- $a$ (rank count), bound on [Lower-triangular factorization](lower-triangular-factorization.md): The number of ones in the matrix Π, which equals the rank of A.
- $H$ (address field group H), bound on [Address shear](address-shear.md): The first of the two ordered groups of address fields, viewed as a vector over a common residue ring.
- $D$ (address field group D), bound on [Address shear](address-shear.md): The second of the two ordered groups of address fields, viewed as a vector over a common residue ring.
- $A$ (shear matrix), bound on [Address shear](address-shear.md): The rational matrix of the shear, with one row for each field of H and one column for each field of D.
- $V$ (stored bit volume), bound on [Fast address interchange](address-interchange.md): The number of stored data bits in the array.
- $u$ (field width), bound on [Fast address interchange](address-interchange.md): The number of address bits in one of the two fields being swapped.
- $\tau$ (cost exponent), bound on [Fast address interchange](address-interchange.md): A fixed exponent in the cost bound, with 0 < tau < 1.
- $N$ (coefficient count), bound on [Chinese-remainder address map](chinese-remainder-address-map.md): The number of coefficients in the list, equal to the product of the distinct primes $p_1, \dots, p_k$.
- $k$ (axis count), bound on [Chinese-remainder address map](chinese-remainder-address-map.md): The number of distinct prime cyclic axes, that is, the count of primes whose product is $N$.
- $p_i$ (axis length), bound on [Chinese-remainder address map](chinese-remainder-address-map.md): The i-th distinct prime, which is the length of the i-th cyclic axis.
- $m$ (list position), bound on [Chinese-remainder address map](chinese-remainder-address-map.md): A position in the coefficient list, taken modulo $N$.
- $q$ (prime transform length), bound on [Gaussian resampling](gaussian-resampling.md): The number of entries of the sequence that the transform acts on; here a prime.
- $u$ (input sequence), bound on [Gaussian resampling](gaussian-resampling.md): The sequence of $q$ entries that the transform acts on.
- $F_q$ (normalized Fourier transform), bound on [Gaussian resampling](gaussian-resampling.md): The normalized discrete Fourier transform of length $q$, mapping $u$ to $(F_q u)_k$.
- $N$ (transform length), bound on [Bluestein's chirp identity](bluestein-chirp.md): The number of points in the transform.
- $\omega$ (primitive root of unity), bound on [Bluestein's chirp identity](bluestein-chirp.md): A primitive $N$-th root of unity, the base of the transform.
- $\zeta$ (chirp base), bound on [Bluestein's chirp identity](bluestein-chirp.md): A square root of $\omega$, used as the base of the chirp factors.
- $x$ (input sequence), bound on [Bluestein's chirp identity](bluestein-chirp.md): The input sequence $x_0,\dots,x_{N-1}$ of values to be transformed.
- $X$ (transform), bound on [Bluestein's chirp identity](bluestein-chirp.md): The transform of $x$, the sequence of values $X_0,\dots,X_{N-1}$.
- $j$ (input index), bound on [Bluestein's chirp identity](bluestein-chirp.md): The input index, running from $0$ to $N-1$.
- $k$ (output index), bound on [Bluestein's chirp identity](bluestein-chirp.md): The output index, running from $0$ to $N-1$.
- $d$ (chunk bound), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The largest number of equal-width address chunks a layer acts on.
- $D$ (chunks in a layer), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The number of equal-width address chunks used by one layer, at most d.
- $V$ (logical volume), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The number of stored data bits, the volume on which the layer's cost is measured.
- $\lambda'$ (cost exponent), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): A fixed exponent below one in the layer's cost bound.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Linear network with restored auxiliary values](linear-network-exchange.md): A fixed linear network that exchanges banks of values with prescribed signs and restores every auxiliary value, with each gate acting on the stored array through a frame operator that cancels between edges.
  Shown as: Recursive power saving *<predicate>* Linear network with restored auxiliary values
- [Fast address interchange](address-interchange.md): A tape procedure that swaps two disjoint contiguous address fields of an array in time O(V u^τ) for width u, computed through XOR combinations of intermediate data.
  Shown as: Recursive power saving *<predicate>* Fast address interchange
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): A butterfly operation applied at once on one selected address bit of every record, with exact Gaussian dyadic intermediates and a single truncation after the layer.
  Shown as: Recursive power saving *<predicate>* Simultaneous butterfly layer

## Pages that build on this one

- Integer multiplication in O(n(lg n)^(1-κ)) time: A deterministic multitape Turing machine that multiplies two n-bit integers exactly in O(n(lg n)^(1-κ)) worst-case time for a fixed κ = 2^(-182) > 0, beating the n log n conjecture in this model.

## Other pages you may link to

- [Schönhage–Strassen n log n conjecture](nlogn-conjecture.md)
- [Harvey–van der Hoeven O(n log n) multiplication](harvey-hoeven-multiplier.md)
- [Primitive roots of unity](roots-of-unity.md)
- [Discrete Fourier transform](fourier-transform.md)
- [Butterfly operation](butterfly-operation.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Multiplication as convolution of digits](convolution-reduction.md)
- [Polynomial ring modulo yʳ + 1](polynomial-ring-y.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Signed Kronecker packing](kronecker-packing.md)
- [Matrix rank](matrix-rank.md)
- [Lower-triangular factorization](lower-triangular-factorization.md)
- [Address shear](address-shear.md)
- [Chinese-remainder address map](chinese-remainder-address-map.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein's chirp identity](bluestein-chirp.md)
- [Tensor product](tensor-product.md)
- [Exact recovery by rounding](rounding-recovery.md)
- [Integer multiplication in O(n(lg n)^(1-κ)) time](integer-multiplication-target.md)

## Evidence from the sources, with the paragraph around each quote

- "The decisive property is that the total number $s$ of smaller calls satisfies $s<Wm$." (paper)

  > The finite construction in Section~\ref{sec:finite-networks} attaches subspaces of a fixed $m$-dimensional space to its gates and terminals. The subspaces at adjacent vertices are nested. Their dimension changes count the smaller operations needed on an edge, with an additional source contribution in the bit construction. The construction uses three-element subsets: gather and scatter create coefficients depending on intersection size, and auxiliary wires cancel the unwanted coefficients. Orthogonality of the corresponding indicator vectors permits the subspace assignments. The decisive property is that the total number $s$ of smaller calls satisfies $s<Wm$.

- "This strict inequality is the source of the power saving" (paper)

  > A recursive call at parameter $mf$ therefore uses $s$ calls at parameter $f$, each on a stream of volume $V/W$. The parameter counts field digits for address interchange and selected axes for a numerical layer. After dividing cost by volume, multiplying the parameter by $m$ increases the recursive contribution by $s/W<m$. This strict inequality is the source of the power saving. The later tape and arithmetic estimates preserve it, including the work of changing numerical address coordinates. Those changes are implemented by whole-chunk moves and controlled shifts, followed by a deterministic correction of the explicitly identified exceptional addresses.


## Sources (read from disk as needed)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The reader cannot follow this step: "The recursion is applied to the [Fast address interchange](address-interchange.md)" (The page does not say what plays the roles of s, W, m or the parameter in this application, or how u relates to the parameter. The reader cannot check that the recursion's cost bound applies here.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "The recursion is also applied to a" (The cited claim is that the recursion applies to the layer on d chunks. The page does not say what the recursion's parameter, s, W or m are for this layer, so its content and role here are not stated and the reader cannot check it.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "so the cost at parameter $m^k$ is $O(V(m^k)^\theta)$ when $s \ge W$" (The page never says that the recursion has k levels for parameter m^k (the parameter divides by m at each level), nor what the base case costs. So the range of the level sum is not given and the claimed bound is not checkable.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "The levels form a geometric sum dominated by its last term" (The page says the bound holds when s >= W. At s = W the ratio s/W is 1, so theta is 0 and every level costs V. The sum is then kV, which is not dominated by its last term and is not O(V). The reader cannot verify the claim at equality.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- Say what $j$ denotes where it is first used (for a size or count, what it counts): "After $j$ levels there are $s^j$ calls" (No sentence says what j denotes. The phrase 'After j levels' only suggests that j counts levels, and no earlier page binds this meaning.)
- Explain "tape procedure" in a sentence where it is first used.

## Previous version (revise it)

It has 264 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 330 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

Recursive power saving is the mechanism that turns a linear-cost network into a tape procedure whose cost is a fixed power of its parameter, with exponent below one. Each tape procedure is realized as a [Linear network with restored auxiliary values](linear-network-exchange.md) that exchanges two banks of values and restores every auxiliary value.

Let $V$ be the number of data values a call moves, $W$ the number of roles in the network, $s$ the number of smaller calls the network makes, and $m$ the factor by which the parameter grows. Here $f$ is the parameter of a smaller call. A call at parameter $mf$ makes $s$ calls at parameter $f$, each on a stream of volume $V/W$, plus linear work on its own volume.

Iterate this. After $j$ levels there are $s^j$ calls, each on volume $V/W^j$, so the work at level $j$ is $(s/W)^j$ times $V$. Let $\theta = \log_m(s/W)$ be the exponent of the saving, so $s/W = m^\theta$. The levels form a geometric sum dominated by its last term, so the cost at parameter $m^k$ is $O(V(m^k)^\theta)$ when $s \ge W$.

The inequality $s/W<m$ is exactly $\theta<1$. <cite data-source="paper">This strict inequality is the source of the power saving</cite> If $s/W$ equalled $m$, $\theta$ would be $1$ and nothing would be saved.

The exponent $\theta$ depends only on the fixed numbers $s$, $W$ and $m$ of the network, so it is uniform. The volume $V$ cancels: each level multiplies the number of calls by $s$ and divides every call's volume by $W$, so the ratio $s/W$ is the same at every level, whatever $V$ and the parameter are.

The recursion is applied to the [Fast address interchange](address-interchange.md), where $u$ is the number of bits in each field. The recursion is also applied to a [Simultaneous butterfly layer](simultaneous-butterfly-layer.md) on $d$ chunks, where $d$ is the number of chunks. <cite data-source="paper">The parameter counts field digits for address interchange and selected axes for a numerical layer.</cite>

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

Write the body to `exegenius/tasks/0068-write-recursive-power-saving.answer.md` and the JSON to `exegenius/tasks/0068-write-recursive-power-saving.answer.json`, then run `exegenius submit 0068-write-recursive-power-saving` in the project directory. If submit rejects the answer, fix the answer and submit again.
