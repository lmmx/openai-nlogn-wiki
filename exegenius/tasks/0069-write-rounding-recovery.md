# exegenius task 0069-write-rounding-recovery

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

Concept: Exact recovery by rounding
Gloss: The step in which the approximate convolution coefficients are rounded to integers, provided the error is strictly below 1/2, and carries are then propagated to give the exact binary product.
Also called: exact recovery

## This page in the argument

The step: The exact product is recovered: the source permutation cancels, and the coefficient error is below $1/2$, so rounding and carries give the binary product.
How: cancel the retained source permutation, then round the approximate coefficients and propagate carries
Why: Rounding recovers the integer coefficients only once the error is strictly below one half. (the sources leave this for the reader to work out: spell it out)

Its sub-steps, in order:

- The source permutation retained during resampling cancels across the forward transforms, their product, and the opposite transform.
- The recovered coefficient error is strictly below $1/2$, and carries are propagated to give the exact binary product.

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
- $V$ (call volume), bound on [Recursive power saving](recursive-power-saving.md): The number of data values a call moves.
- $W$ (role count), bound on [Recursive power saving](recursive-power-saving.md): The number of roles in the network, which divides the volume passed to each smaller call.
- $s$ (smaller call count), bound on [Recursive power saving](recursive-power-saving.md): The number of smaller calls the network makes.
- $m$ (parameter factor), bound on [Recursive power saving](recursive-power-saving.md): The factor by which the parameter grows from a call to the larger call that makes it.
- $f$ (smaller parameter), bound on [Recursive power saving](recursive-power-saving.md): The parameter of a smaller call.
- $\theta$ (saving exponent), bound on [Recursive power saving](recursive-power-saving.md): The exponent of the power saving, $\log_m(s/W)$.
- $u$ (field width), bound on [Recursive power saving](recursive-power-saving.md): The number of bits in each field swapped by the address interchange.
- $d$ (chunk count), bound on [Recursive power saving](recursive-power-saving.md): The number of chunks on which the butterfly layer acts.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Synthetic polynomial transform](synthetic-transform.md): A transform over a polynomial ring in which the roots of unity are powers of y, so that each transform stage uses only signed shifts and butterfly additions.
  Shown as: Exact recovery by rounding *<predicate>* Synthetic polynomial transform
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): A butterfly operation applied at once on one selected address bit of every record, with exact Gaussian dyadic intermediates and a single truncation after the layer.
  Shown as: Exact recovery by rounding *<predicate>* Simultaneous butterfly layer
- [Signed Kronecker packing](kronecker-packing.md): Encoding a polynomial with bounded signed coefficients as an integer by evaluating it at a large power of two, so that polynomial products become integer products.
  Shown as: Exact recovery by rounding *<predicate>* Signed Kronecker packing
- [Bluestein's chirp identity](bluestein-chirp.md): The identity that converts a Fourier transform into a cyclic convolution by multiplying by chirp factors before and after it.
  Shown as: Exact recovery by rounding *<predicate>* Bluestein's chirp identity

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
- [Matrix rank](matrix-rank.md)
- [Linear network with restored auxiliary values](linear-network-exchange.md)
- [Lower-triangular factorization](lower-triangular-factorization.md)
- [Address shear](address-shear.md)
- [Fast address interchange](address-interchange.md)
- [Chinese-remainder address map](chinese-remainder-address-map.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Tensor product](tensor-product.md)
- [Recursive power saving](recursive-power-saving.md)
- [Integer multiplication in O(n(lg n)^(1-κ)) time](integer-multiplication-target.md)

## Evidence from the sources, with the paragraph around each quote

- "proves that the recovered coefficient error is strictly below $1/2$" (paper)

  > Finally, the source permutation retained during resampling cancels across the two forward source transforms, their pointwise product, and the opposite-sign transform. Section~\ref{sec:assembly} removes the known normalizations and digit scales, proves that the recovered coefficient error is strictly below $1/2$, and propagates carries to obtain the exact binary product. A compatible choice of rational parameters makes all terms in its cost table fit Theorem~\ref{thm:main}. Figure~\ref{fig:multiplication-flow} summarizes these reductions.


## Sources (read from disk as needed)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The reader cannot follow this step: "The source permutation cancels across the two forward source transforms, their pointwise product, and the transform with the opposite sign" (The page never says what the source permutation is, what the two forward source transforms are, or which transforms are meant by the transform with the opposite sign. The reader cannot check that the permutation cancels.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "Removing the known normalizations and digit scales then leaves the convolution of the digits as integer coefficients." (The page does not state what the normalizations or digit scales are, nor why removing them leaves exactly the digit convolution with integer coefficients.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "Its error is controlled by the single truncation after each" (The page asserts the error is controlled by one truncation per layer and must be bounded after all layers, but never says what the truncation error is or computes the bound.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "since carries undo the evaluation at a power of two" (The page does not show how the packing is an evaluation at a power of two or why carry propagation exactly undoes it.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "each recovered coefficient has error below one half (cited)" (This cited bound is the justification for rounding, but the page does not say what the error is or how the truncation bound yields one half for each coefficient. The cited claim stands in for how the recovery itself works, and the page does not give its content beyond the bare statement.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.

## Previous version (revise it)

It has 304 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 380 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

Exact recovery by rounding is the final step that turns approximate convolution coefficients into the exact binary product. It has two parts: the reordering of source coordinates retained during resampling cancels, and then each approximate coefficient is rounded to an integer and the carries are propagated.

Exact recovery by rounding works on the output of the [Synthetic polynomial transform](synthetic-transform.md) run in the opposite direction: its input is the array of approximate coefficients. Exact recovery by rounding is based on the normalized cyclic convolution that [Bluestein's chirp identity](bluestein-chirp.md) produces, so the known normalizations of that convolution must be removed first.

The source permutation cancels across the two forward source transforms, their pointwise product, and the transform with the opposite sign. Removing the known normalizations and digit scales then leaves the convolution of the digits as integer coefficients.

Its error is controlled by the single truncation after each [simultaneous butterfly layer](simultaneous-butterfly-layer.md) in the transforms, so the error must be bounded after all layers. Exact recovery by rounding inverts the [Signed Kronecker packing](kronecker-packing.md), since carries undo the evaluation at a power of two.

The true coefficients are integers. If a computed coefficient lies strictly within distance $1/2$ of its true integer, that integer is the unique nearest integer, so rounding returns it exactly. The threshold matters: at distance $1/2$ two integers are equally close, and rounding can pick the wrong one. The paper's assembly section establishes this for the product: each recovered coefficient has error below one half <cite data-source="paper">proves that the recovered coefficient error is strictly below $1/2$</cite>.

For example, take the coefficient list $(3,5)$ in base $2$, which stands for $3+5\cdot 2=13$. Suppose the computed values are $2.9$ and $5.2$. Rounding gives $3$ and $5$. Propagating carries: $3=1+2\cdot 1$ writes digit $1$ and carries $1$; $5+1=6=0+2\cdot 3$ writes digit $0$ and carries $3$; $3=1+2\cdot 1$ writes digit $1$ and carries $1$; the last carry is $1$ and is written as digit $1$. The digits from low to high, $1,0,1,1$, give $1101_2=13$.

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

Write the body to `exegenius/tasks/0069-write-rounding-recovery.answer.md` and the JSON to `exegenius/tasks/0069-write-rounding-recovery.answer.json`, then run `exegenius submit 0069-write-rounding-recovery` in the project directory. If submit rejects the answer, fix the answer and submit again.
