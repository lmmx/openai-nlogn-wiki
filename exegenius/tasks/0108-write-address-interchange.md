# exegenius task 0108-write-address-interchange

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
- Polynomial ring modulo yʳ + 1 (also: negacyclic ring, signed shift)
  - $y$ (ring indeterminate): The variable of the polynomial ring whose powers serve as roots of unity in the remaining axes.
  - $r$ (coefficient count): The number of coefficients in the coefficient list of one polynomial record, a power of two.
- Synthetic polynomial transform (also: Nussbaumer polynomial transform, synthetic transform)
- Signed Kronecker packing (also: Kronecker substitution, signed packing)
- Butterfly operation (also: two-point butterfly, H_0)
- Linear network with restored auxiliary values (also: linear network, frame)
- Lower-triangular factorization (also: Bruhat factorization with reversed order)
- Address shear (also: matrix shear)
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

## This page

Concept: Fast address interchange
Gloss: A tape procedure that swaps two disjoint contiguous address fields of an array in time O(V u^τ) for width u, computed through XOR combinations of intermediate data.
Also called: bit interchange procedure, bit procedure

## This page in the argument

The step: The address interchange of $u$-bit fields costs $O(Vu^\tau)$ for a fixed $\tau<1$.

It serves these steps, from the main result down:

- Two $n$-bit integers can be multiplied exactly in $O(n(\lg n)^{1-\kappa})$ worst-case time on a deterministic multitape Turing machine, for a fixed $\kappa=2^{-182}$.; how: reduce the product to a digit convolution, compute that convolution through transform layers whose tape cost saves a power, and recover the exact product by rounding (on [Integer multiplication in O(n(lg n)^(1-κ)) time](integer-multiplication-target.md))
- Both tape procedures cost $O(V)$ times a power of their parameter whose exponent is strictly below one.; how: give each procedure a fixed linear network with fewer smaller calls than roles, and iterate the resulting recursion (on [Recursive power saving](recursive-power-saving.md))

## Symbols already bound on earlier pages

The symbols in the names of the concepts the reader knows are listed with those concepts above.

- $n$ (input bit length), bound on [Schönhage–Strassen n log n conjecture](nlogn-conjecture.md): The number of bits in each input integer.
- $\kappa$ (exponent gap), bound on [Schönhage–Strassen n log n conjecture](nlogn-conjecture.md): A fixed positive constant, $2^{-182}$, by which the logarithmic exponent of the target running time falls below 1.
- $\kappa$ (power-saving constant), bound on [Harvey–van der Hoeven O(n log n) multiplication](harvey-hoeven-multiplier.md): The fixed constant $\kappa>0$ in the target's bound $O(n(\lg n)^{1-\kappa})$, with value $2^{-182}$.
- $n$ (root order), bound on [Primitive roots of unity](roots-of-unity.md): The order of the root, a positive integer that counts the positions of the transform it labels.
- $\omega$ (primitive root), bound on [Primitive roots of unity](roots-of-unity.md): A primitive $n$-th root of unity, the complex number that labels the positions of a transform.
- $k$ (power exponent), bound on [Primitive roots of unity](roots-of-unity.md): An integer exponent of the root, marking which power of $\omega$ is meant.
- $j$ (earlier exponent), bound on [Primitive roots of unity](roots-of-unity.md): An integer exponent of the root, the smaller of two powers compared in the distinctness argument.
- $n$ (input length), bound on [Discrete Fourier transform](fourier-transform.md): The length of the input sequence, the number of its entries, so the roots are the $n$-th roots of unity.
- $a$ (input sequence), bound on [Discrete Fourier transform](fourier-transform.md): The input sequence $a=(a_0,\dots,a_{n-1})$, a list of $n$ complex numbers.
- $j$ (input index), bound on [Discrete Fourier transform](fourier-transform.md): An index running from $0$ to $n-1$ over the input entries.
- $k$ (output index), bound on [Discrete Fourier transform](fourier-transform.md): An index running from $0$ to $n-1$ over the output entries.
- $\hat a$ (output sequence), bound on [Discrete Fourier transform](fourier-transform.md): The output sequence of $n$ complex numbers, whose entries are the transform of $a$.
- $x$ (formal variable), bound on [Discrete Fourier transform](fourier-transform.md): A formal variable, a placeholder for a number substituted into the polynomial $p$.
- $p$ (coefficient polynomial), bound on [Discrete Fourier transform](fourier-transform.md): The polynomial whose coefficient list is $a$, so that $a_j$ is the coefficient of $x^j$.
- $u$ (first input value), bound on [Butterfly operation](butterfly-operation.md): One of the two input values that the butterfly operation maps.
- $v$ (second input value), bound on [Butterfly operation](butterfly-operation.md): The other of the two input values that the butterfly operation maps.
- $H_0$ (butterfly operation), bound on [Butterfly operation](butterfly-operation.md): The two-point map sending $(u,v)$ to $\left(\frac{u+v}{2}, \frac{u-v}{2}\right)$.
- $r$ (sequence length), bound on [Cyclic convolution](cyclic-convolution.md): The number of complex coefficients in each input sequence, which is also the length of their cyclic convolution.
- $b$ (second input sequence), bound on [Cyclic convolution](cyclic-convolution.md): The second input sequence, a list of r complex numbers.
- $c$ (cyclic convolution), bound on [Cyclic convolution](cyclic-convolution.md): The length-r sequence a convolved with b cyclically, whose k-th entry is the sum over j of a_j b_((k-j) mod r).
- $l$ (second-sequence index), bound on [Cyclic convolution](cyclic-convolution.md): An index of a term of b, running over the residues 0 to r-1 in the reduction argument.
- $x$ (formal variable), bound on [Cyclic convolution](cyclic-convolution.md): An indeterminate used to write sequences as polynomials; it is not evaluated at any number.
- $b$ (digit width), bound on [Multiplication as convolution of digits](convolution-reduction.md): The number of bits in one digit, so that digits are taken in radix $2^b$.
- $m$ (digits per input), bound on [Multiplication as convolution of digits](convolution-reduction.md): The number of radix-$2^b$ digits in each input.
- $u$ (first input), bound on [Multiplication as convolution of digits](convolution-reduction.md): The first of the two integers being multiplied.
- $v$ (second input), bound on [Multiplication as convolution of digits](convolution-reduction.md): The second of the two integers being multiplied.
- $y$ (ring variable), bound on [Polynomial ring modulo yʳ + 1](polynomial-ring-y.md): The variable of the polynomial ring modulo $y^r+1$, whose powers serve as roots of unity in the remaining axes.
- $r$ (coefficient count), bound on [Polynomial ring modulo yʳ + 1](polynomial-ring-y.md): The number of complex coefficients in the coefficient list of one polynomial record, a power of two.
- $\theta$ (twist factor), bound on [Polynomial ring modulo yʳ + 1](polynomial-ring-y.md): A complex $2r$-th root of unity with $\theta^r=-1$, whose powers multiply the entries of a coefficient list in the phase twist.
- $x$ (input sequence), bound on [Synthetic polynomial transform](synthetic-transform.md): The sequence of ring elements $x_0$ through $x_{2r-1}$ to which the transform is applied.
- $t$ (input position), bound on [Synthetic polynomial transform](synthetic-transform.md): The index of an input entry, running from 0 to $2r-1$.
- $s$ (frequency index), bound on [Synthetic polynomial transform](synthetic-transform.md): The index of an output frequency, running from 0 to $2r-1$.
- $i$ (half-transform index), bound on [Synthetic polynomial transform](synthetic-transform.md): The index, running from 0 to $r-1$, that labels the even outputs $\hat x_{2i}$ and the odd outputs $\hat x_{2i+1}$.
- $z$ (second sequence), bound on [Synthetic polynomial transform](synthetic-transform.md): A second sequence of ring elements, transformed by the same rule as $x$.
- $q$ (position in z), bound on [Synthetic polynomial transform](synthetic-transform.md): The index of an entry of $z$, summed over together with $t$.
- $h$ (convolution position), bound on [Synthetic polynomial transform](synthetic-transform.md): The output position of the cyclic convolution $x\ast z$, taken modulo $2r$.
- $j$ (coefficient index), bound on [Signed Kronecker packing](kronecker-packing.md): The index running over the $r$ coefficient positions of a polynomial in the ring, $0 \le j < r$.
- $f$ (packed polynomial), bound on [Signed Kronecker packing](kronecker-packing.md): An element of the ring whose integer coefficients $f_j$ are packed into an integer.
- $g$ (second polynomial), bound on [Signed Kronecker packing](kronecker-packing.md): A second element of the ring with integer coefficients $g_j$, packed in the same way as $f$.
- $M$ (coefficient bound), bound on [Signed Kronecker packing](kronecker-packing.md): A bound on the absolute value of every coefficient of $f$ and $g$.
- $B$ (packing base), bound on [Signed Kronecker packing](kronecker-packing.md): The power of two at which polynomials are evaluated to pack them into integers.
- $F$ (packed integer of f), bound on [Signed Kronecker packing](kronecker-packing.md): The integer obtained by evaluating $f$ at the packing base $B$.
- $G$ (packed integer of g), bound on [Signed Kronecker packing](kronecker-packing.md): The integer obtained by evaluating $g$ at the packing base $B$.
- $h$ (unreduced product), bound on [Signed Kronecker packing](kronecker-packing.md): The product $fg$ of $f$ and $g$ as polynomials, before reduction modulo $y^r+1$.
- $k$ (product power), bound on [Signed Kronecker packing](kronecker-packing.md): The power of $y$ indexing a coefficient $h_k$ of the unreduced product.
- $M$ (matrix), bound on [Matrix rank](matrix-rank.md): A real matrix, the matrix whose rank is taken.
- $p$ (pivot), bound on [Matrix rank](matrix-rank.md): The nonzero pivot entry, the top-left entry after reordering rows and columns.
- $S$ (smaller matrix), bound on [Matrix rank](matrix-rank.md): The matrix left after the pivot's row and column are deleted, which is smaller than the original.
- $\Omega$ (address set), bound on [Linear network with restored auxiliary values](linear-network-exchange.md): The finite set of addresses at which each wire of the network holds a value.
- $w$ (input role), bound on [Linear network with restored auxiliary values](linear-network-exchange.md): An input wire of the network, identified by its fixed role.
- $\rho$ (output role map), bound on [Linear network with restored auxiliary values](linear-network-exchange.md): The map sending an input role to the output role where its value leaves the network.
- $\varepsilon_w$ (route sign), bound on [Linear network with restored auxiliary values](linear-network-exchange.md): The prescribed sign, attached to input role w, with which its value is carried to the output.
- $D_v$ (frame), bound on [Linear network with restored auxiliary values](linear-network-exchange.md): The invertible linear operator on arrays indexed by the address set that is the frame of vertex v.
- $u$ (edge tail vertex), bound on [Linear network with restored auxiliary values](linear-network-exchange.md): A vertex of the network, the tail of an edge; here u no longer denotes a butterfly input.
- $v$ (edge head vertex), bound on [Linear network with restored auxiliary values](linear-network-exchange.md): A vertex of the network, a source, gate or sink, which carries a frame.
- $\mathrm{source}$ (source vertex map), bound on [Linear network with restored auxiliary values](linear-network-exchange.md): The map sending an input role to the source vertex where that role enters the network.
- $\mathrm{sink}$ (sink vertex map), bound on [Linear network with restored auxiliary values](linear-network-exchange.md): The map sending an output role to the sink vertex where that role leaves the network.
- $a$ (address), bound on [Linear network with restored auxiliary values](linear-network-exchange.md): One address of the address set, at which the example's two wires are read; here a no longer denotes a first sequence.
- $x$ (first wire value), bound on [Linear network with restored auxiliary values](linear-network-exchange.md): The value on the first wire at address a in the example; here x no longer denotes a formal variable.
- $y$ (second wire value), bound on [Linear network with restored auxiliary values](linear-network-exchange.md): The value on the second wire at address a in the example; here y no longer denotes a ring indeterminate.
- $X_a$ (first bank value), bound on [Linear network with restored auxiliary values](linear-network-exchange.md): The value of the first bank at address a.
- $Y_a$ (second bank value), bound on [Linear network with restored auxiliary values](linear-network-exchange.md): The value of the second bank at address a.
- $A$ (rational matrix), bound on [Lower-triangular factorization](lower-triangular-factorization.md): The rational m×m matrix that is factored.
- $m$ (matrix size), bound on [Lower-triangular factorization](lower-triangular-factorization.md): The number of rows, and of columns, of the matrix A.
- $E_1$ (left lower factor), bound on [Lower-triangular factorization](lower-triangular-factorization.md): The first invertible lower-triangular factor in the factorization of A.
- $E_2$ (right lower factor), bound on [Lower-triangular factorization](lower-triangular-factorization.md): The second invertible lower-triangular factor in the factorization of A.
- $\Pi$ (partial permutation), bound on [Lower-triangular factorization](lower-triangular-factorization.md): The partial permutation matrix in the factorization, with at most one 1 in each row and column and all other entries 0.
- $a$ (rank count), bound on [Lower-triangular factorization](lower-triangular-factorization.md): The number of ones in the matrix Π, which equals the rank of A.
- $H$ (first address group), bound on [Address shear](address-shear.md): The first ordered group of address fields, which the shear changes; one entry for each row of A.
- $D$ (second address group), bound on [Address shear](address-shear.md): The second ordered group of address fields, which the shear leaves unchanged; one entry for each column of A.
- $s$ (field index of H), bound on [Address shear](address-shear.md): An index running over the fields of H, selecting the field H_s that a 1 of Pi pairs with a field of D.
- $t$ (field index of D), bound on [Address shear](address-shear.md): An index running over the fields of D, selecting the field D_t that a 1 of Pi pairs with a field of H.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Address shear](address-shear.md): The permutation (H, D) ↦ (H + AD, D) on two ordered groups of address fields, which is performed with as many pairwise interchanges as the rank of A.
  Shown as: Fast address interchange *<predicate>* Address shear
- [Linear network with restored auxiliary values](linear-network-exchange.md): A fixed linear network that exchanges banks of values with prescribed signs and restores every auxiliary value, with each gate acting on the stored array through a frame operator that cancels between edges.
  Shown as: Fast address interchange *<predicate>* Linear network with restored auxiliary values

## Pages that build on this one

- Chinese-remainder address map: A rearrangement that places a digit sequence on a product of distinct prime cyclic axes while preserving convolution, implemented with address interchanges.
- Recursive power saving: The mechanism in which a network with s smaller calls on W roles and parameter m gives a recursion with cost ratio s/W < m, so that repeated recursion saves a power of the parameter.
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
- [Chinese-remainder address map](chinese-remainder-address-map.md)
- [Tensor product](tensor-product.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Recursive power saving](recursive-power-saving.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein's chirp identity](bluestein-chirp.md)
- [Exact recovery by rounding](rounding-recovery.md)
- [Integer multiplication in O(n(lg n)^(1-κ)) time](integer-multiplication-target.md)

## Evidence from the sources, with the paragraph around each quote

- "The first procedure interchanges two disjoint contiguous address fields" (paper)

  > The first procedure interchanges two disjoint contiguous address fields of $u$ bits in an array whose addresses form a complete Cartesian product. Its cost is $O(Vu^\tau)$ for a fixed $\tau<1$. Although its final effect is an exact permutation, its intermediate steps form pointwise XOR combinations of data. The final permutation is exact for arbitrary initial auxiliary values.


## Sources (read from disk as needed)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- Cite or cut this step: "Lower-triangular updates cost $O(V)$." (The page asserts the O(V) cost of applying the lower-triangular factors without saying how those updates act on the stored bits.). It is inside reasoning added for an earlier step, so do not explain it further: cite the source for it, or remove the claim.
- The reader cannot follow this step: "whose gates act on the stored array and restore every auxiliary value. (cited)" (The page says the procedure runs the cited network but does not say how the network's gates realise the field interchange. The role of the cited network in the procedure is asserted, not explained.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- Cite or cut this step: "So each level makes $s$ recursive calls, each on volume $V/W$." (The page does not explain why each edge gives one recursive call, or why each call's volume is V/W, so the reader cannot check the count or the volume.). It is inside reasoning added for an earlier step, so do not explain it further: cite the source for it, or remove the claim.
- Cite or cut this step: "After $t$ levels, $u=c^t$." (The page says each level divides the field width by c, which would make the width shrink as c^(-t) from the starting width. It never gives the starting width or the base case, so u = c^t cannot be checked from what the page gives.). It is inside reasoning added for an earlier step, so do not explain it further: cite the source for it, or remove the claim.
- Cite or cut this step: "Each level's time per stored bit is at most $s/W$ times the previous level's plus a constant." (The reader cannot derive this recurrence from the page: it needs the recursive call count, the call volume, and the per-level overhead, none of which is worked out here. The later geometric-sum bound depends on it.). It is inside reasoning added for an earlier step, so do not explain it further: cite the source for it, or remove the claim.
- Say what $t$ denotes where it is first used (for a size or count, what it counts): "After $t$ levels, $u=c^t$." (The page uses t as a number of levels but never says it denotes that. The earlier page synthetic-transform binds t as an input position, so the reader has no stated meaning here.)
- Explain "layer" in a sentence where it is first used.

## Previous version (revise it)

It has 254 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 317 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

Fast address interchange is a tape procedure that swaps two disjoint contiguous address fields of an array, and its cost bound lets the recursion in [Recursive power saving](recursive-power-saving.md) save a power. An address field is a block of consecutive address bits.

$V$ is the stored bit volume: the number of data bits the array holds. $u$ is the width of each field: the number of address bits in one field. The letter $u$ changes meaning here. $\tau$ is a fixed exponent with $0<\tau<1$. <cite data-source="paper">Its cost is $O(Vu^\tau)$ for a fixed $\tau<1$.</cite>

The procedure is applied to each [Address shear](address-shear.md) that a layer produces. A shear $(H,D)\mapsto(H+AD,D)$ adds to $H$ a combination of $D$ given by the rational matrix $A$. Write $A=E_1\Pi E_2$ with $E_1,E_2$ invertible and lower-triangular, and $\Pi$ a partial permutation matrix. Invertible factors preserve rank, so $\Pi$ has $\operatorname{rank} A$ ones. Lower-triangular updates cost $O(V)$. Each one of $\Pi$ is an interchange of an $H$ field with a $D$ field, so a shear takes as many interchanges as its rank.

It runs the [Linear network with restored auxiliary values](linear-network-exchange.md), whose gates act on the stored array and restore every auxiliary value. <cite data-source="paper">The final permutation is exact for arbitrary initial auxiliary values.</cite>

Each level divides the field width by a fixed integer $c\ge 2$. The swap is three updates, $D\leftarrow D-H$, $H\leftarrow H+D$, $D\leftarrow H-D$, sending $(H,D)$ to $(D,H)$. Only the middle one is a shear. The network has $W$ wires and total edge rank $s$, the sum of its edge matrix ranks. <cite data-source="paper">An edge matrix of rank $a$ will require $a$ smaller interchanges.</cite> So each level makes $s$ recursive calls, each on volume $V/W$.

Each level's time per stored bit is at most $s/W$ times the previous level's plus a constant. After $t$ levels, $u=c^t$. The geometric sum $1+s/W+\cdots+(s/W)^t$ is $O(c^{t\tau})$ when $s/W<c^\tau$, so the cost is $O(Vu^\tau)$.

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

Write the body to `exegenius/tasks/0108-write-address-interchange.answer.md` and the JSON to `exegenius/tasks/0108-write-address-interchange.answer.json`, then run `exegenius submit 0108-write-address-interchange` in the project directory. If submit rejects the answer, fix the answer and submit again.
