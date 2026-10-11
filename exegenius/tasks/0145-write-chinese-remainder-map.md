# exegenius task 0145-write-chinese-remainder-map

Project directory: `/mnt/openai-nlogn` (paths below are relative to it)

Write one page of an explanatory wiki. The wiki explains a target result from source documents to a specific reader, one concept per page, in reading order.

- Open with one or two sentences that say what the concept is and what it is for on the way to the target (the step of the argument it presents, and the pages that build on it, are listed below), so a reader arriving from a link knows at once why the page matters.
- If the page presents a step of the argument, explain how its method shows its claim. Give the reader every motivation the task marks as not stated by the sources: the sources will not.
- Explain the page's concept so that this reader can follow it using only what they already understand (listed below), what this page itself explains, and the linked prerequisite pages.
- Define any other technical term on this page, where it is first used.
- Say what each symbol denotes where you introduce it: what it stands for, and for a size or count, what it counts ("$r$, the number of complex coefficients in a record", not "a power of two $r$"). A use in an example ("take $r = 4$") does not say what $r$ denotes. Symbols listed as already bound can be used without restating them: the page shows the reader their meanings. Using one of those letters with another meaning confuses readers: pick another letter, or say on the page that the letter changes meaning here.
- Link each prerequisite page the first time you rely on it, using the exact markdown link given. You may also link the other pages listed. Submit rejects links to anything else in the wiki; external URLs are allowed.
- For each prerequisite page, say in a sentence what this page uses it for, and give that sentence as a relation: the prerequisite's id, a predicate, and the sentence copied exactly. The page shows the relation as "<this page's concept> *<predicate>* <prerequisite>", so pick a predicate that makes that a true sentence, with this page's concept as subject and the prerequisite as object: "is reduced to", "computes its transforms by", "is based on", "follows from", "bounds the cost of". If the sentence says "the transforms are reduced by X", the predicate is "reduces its transforms by", not "are reduced to". Build the predicate from the sentence's own words (other forms of a word count: "reduces" for "reduced"); the sentence must link or name the prerequisite. Pick the predicate that says what the prerequisite does for this page: "uses" says little.
- Stay accurate to the sources: read the parts you need (search for the evidence quotes). State only what the sources support or what is standard background; do not invent results, constants or attributions.
- Back each specific claim taken from a source (a result, a constant, a construction step) with the source text it rests on, right after the claim: `<cite data-source="id">text copied word for word from that source</cite>`. Readers see these as "(see p. 5)"-style references, hidden until they ask for them. Submit rejects text not found in the named source. Do not cite common background.
- Be concrete and specific. Give a small worked example where it makes the idea clearer. No filler, no rhetorical flourishes, no announcing what the page will do.
- Write mathematics in LaTeX: $...$ inline, $$...$$ on its own lines for display.
- Do not write a title heading, a prerequisites list or a sources section: those are added automatically. Use ## subheadings only if the page is long.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes (also: multitape Turing machine)
- Fixed-tape machine model (also: fixed finite-tape model)
- Exact integer multiplication
- The n log n optimality conjecture (also: Schönhage–Strassen conjecture)
- Established O(n log n) multiplier (also: Harvey–van der Hoeven multiplier)
- Radix-digit convolution
- Discrete Fourier transform (also: normalized Fourier transform, transform)
- Cyclic convolution
- Gaussian resampling (also: Harvey–van der Hoeven resampling, Gaussian weights)
- Bluestein's chirp identity (also: chirp identity)
- Synthetic polynomial transforms (also: Nussbaumer polynomial transforms, polynomial transforms, Nussbaumer and Quandalle)
- Polynomial ring modulo y^r + 1 (also: negacyclic polynomial ring)
  - $y$ (polynomial variable): The indeterminate of the polynomial ring, whose powers act as roots of unity.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Phase twist
- Signed coefficient packing (also: Kronecker substitution)
- Subspace labels
- Linear networks and frames (also: roles, frames)
- Subset-intersection network (also: three-element subset network, subset-intersection network and complex phase network)
- Address-field interchange (also: power-width interchange, tape procedure for interchanging address chunks)
- Address shear
- Rank-saving recursion (also: recursive saving)
- Gaussian dyadics
- Complex phase network (also: phase-frame identity, complex variant)
- Simultaneous butterfly layer
- Packed selected-bit addition
- Guard-width bound
- Transform layout
- Transform identity with retained permutations (also: target permutation)
- Address field (also: address chunk, chunk, target chunk)
- Transform axis (also: axis, remaining axes)
- Linear algebra basics (also: linear algebra: invertible linear operator, matrix, inverse, matrix, linear map)
- Bilinear map (also: bilinear product)
- Bilinear form (also: bilinear space, orthogonality, bilinear form and orthogonality, bilinear space and bilinear form)
- Binary field (also: finite field F2, F_2, finite field F_2)
- Binary change of basis
- Bit procedure
- Butterfly
- Congruence (also: congruence modulo B, modulo)
- Centered residue
- Linear contraction (also: contraction)
- Cyclic shift (also: controlled cyclic shift)
- Convolution
- Coprime (also: gcd, pairwise coprime, coprime (gcd))
- Running time cost (also: cost)
- Cost table
- Stable radix sort
- Destination rank
- Endpoint operator
- Gate and terminal of a network
- Gaussian integer
- Grid numerator (also: grid numerators)
- Ground set
- Indicator vector
- Modular inverse (also: invertible modulo q)
- Cyclic coordinate (also: last cyclic coordinate)
- Limit inferior
- Line spanned by a vector
- Little-o notation
- Mixed-radix digits (also: mixed-radix digit)
- Multidimensional transform (also: multidimensional transforms with power-of-two axes)
- Array norm (also: norm of an array)
- Normalized cyclic convolution
- Normalization scales (also: normalizations and known scales)
- Numerical layer
- Opposite transform (also: opposite-sign transform)
- Padded transform box
- Payload
- Phase factor (also: phase factors and scalar corrections)
- Polynomial ring
- Matrix rank (also: rational rank)
- Ring homomorphism and isomorphism (also: ring homomorphism and ring isomorphism)
- Schoolbook multiplication
- Scratch storage (also: scratch values, scratch chunk, scratch wires)
- Tensor product (also: tensor power)
- Transform round
- Truncation
- Union bound
- Exclusive or (also: XOR)

## This page

Concept: Chinese-remainder map
Gloss: A relabeling of coefficient positions by mixed-radix digits for pairwise coprime lengths, which turns one cyclic convolution into a multidimensional cyclic convolution.
Also called: Agarwal–Cooley map, coefficient layout, generator

## This page in the argument

The step: The radix-digit coefficients are placed on distinct prime cyclic axes by a map that preserves convolution.
How: relabel the coefficients by mixed-radix digits for the coprime axis lengths
Why: Mixed-radix relabeling turns one cyclic convolution into a multidimensional one whose axis lengths are pairwise coprime. (the sources leave this for the reader to work out: spell it out)

Its sub-steps, in order:

- The radix-digit coefficient list is placed on prime cyclic axes by a Chinese-remainder map that preserves convolution.

It serves these steps, from the main result down:

- Exact multiplication of two $n$-bit integers runs in $O(n(\lg n)^{1-\kappa})$ time on one deterministic fixed-tape machine, with $\kappa = 2^{-182}$.; how: reduce exact multiplication to radix-digit convolution, compute that convolution with fast tape transforms, and check that the output is exact (on [Integer multiplication below n log n](main-theorem.md))

## Symbols already bound on earlier pages

The symbols in the names of the concepts the reader knows are listed with those concepts above.

- $D_v$ (frame), bound on [Linear networks and frames](linear-network-frames.md): The invertible linear operator on arrays attached to vertex $v$ of a network, so that the stored array at $v$ is $D_v g$.
- $g$ (logical array), bound on [Linear networks and frames](linear-network-frames.md): The array a wire is meant to represent before any frame is applied.
- $G$ (pointwise gate), bound on [Linear networks and frames](linear-network-frames.md): A fixed linear map that combines the entries of several wires at each address.
- $n$ (input length), bound on [Fixed-tape machine model](fixed-tape-model.md): The number of bits in each of the two input integers.
- $A$ (fixed machine), bound on [Fixed-tape machine model](fixed-tape-model.md): A fixed multiplication machine, whose alphabet and tape count do not depend on the input.
- $T_A$ (running time), bound on [Fixed-tape machine model](fixed-tape-model.md): The worst-case running time of machine A as a function of the input length n.
- $c_A$ (lower-bound constant), bound on [Fixed-tape machine model](fixed-tape-model.md): A positive constant, depending on machine A, in the eventual lower bound T_A(n) >= c_A n log n.
- $N_A$ (threshold input length), bound on [Fixed-tape machine model](fixed-tape-model.md): The input length from which the lower bound for machine A holds.
- $x$ (first input string), bound on [Exact integer multiplication](exact-integer-multiplication.md): A binary string of length n, the first input to the product.
- $y$ (second input string), bound on [Exact integer multiplication](exact-integer-multiplication.md): A binary string of length n, the second input to the product.
- $n$ (input length), bound on [Exact integer multiplication](exact-integer-multiplication.md): The number of bits in each input string.
- $n$ (input length), bound on [The n log n optimality conjecture](n-log-n-conjecture.md): The number of bits in each of the two input integers.
- $A$ (multiplication machine), bound on [The n log n optimality conjecture](n-log-n-conjecture.md): A fixed Turing machine that computes exact products.
- $T_A$ (running time), bound on [The n log n optimality conjecture](n-log-n-conjecture.md): The worst-case running time of A on inputs of two n-bit integers, as a number of steps.
- $c_A$ (lower-bound constant), bound on [The n log n optimality conjecture](n-log-n-conjecture.md): A positive constant in the lower bound that must hold for machine A.
- $N_A$ (threshold length), bound on [The n log n optimality conjecture](n-log-n-conjecture.md): The input length from which the lower bound for machine A must hold.
- $\lg n$ (binary logarithm), bound on [The n log n optimality conjecture](n-log-n-conjecture.md): The base-2 logarithm of n, rounded up to an integer and never below 1.
- $\kappa$ (saving exponent), bound on [The n log n optimality conjecture](n-log-n-conjecture.md): The specific positive constant by which the main theorem's running time falls below n lg n.
- $N$ (input bit length), bound on [Established O(n log n) multiplier](established-multiplier.md): The number of bits in each of the two binary inputs of the multiplier.
- $u$ (field width), bound on [Address-field interchange](address-interchange.md): The number of bits in each address field.
- $V$ (stored volume), bound on [Address-field interchange](address-interchange.md): The number of stored bits in the array.
- $\tau$ (width exponent), bound on [Address-field interchange](address-interchange.md): A fixed number below one in the cost bound $O(V u^{\tau})$.
- $x$ (first field), bound on [Address-field interchange](address-interchange.md): The value of the first field, a block of bits at matching positions.
- $y$ (second field), bound on [Address-field interchange](address-interchange.md): The value of the second field, a block of bits at matching positions.
- $\oplus$ (bitwise XOR), bound on [Address-field interchange](address-interchange.md): Bitwise exclusive or of two blocks of bits.
- $\mathbb{D}$ (Gaussian dyadics), bound on [Gaussian dyadics](gaussian-dyadics.md): The set of numbers $a/2^k$, with $a$ a Gaussian integer and $k \ge 0$ an integer.
- $a$ (Gaussian integer numerator), bound on [Gaussian dyadics](gaussian-dyadics.md): A Gaussian integer, the numerator of a Gaussian dyadic over a power of two.
- $k$ (denominator exponent), bound on [Gaussian dyadics](gaussian-dyadics.md): A non-negative integer, so that $2^k$ is the denominator.
- $q$ (transform length), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The number of coordinates of each vector the transform acts on, a positive integer.
- $\omega$ (primitive root of unity), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The complex number $e^{-2\pi i/q}$, a primitive $q$-th root of unity.
- $u$ (input vector), bound on [Discrete Fourier transform](discrete-fourier-transform.md): A vector of $q$ complex numbers, the input to the transform.
- $j$ (input index), bound on [Discrete Fourier transform](discrete-fourier-transform.md): An index of the input coordinates, running from 0 to q-1.
- $k$ (output index), bound on [Discrete Fourier transform](discrete-fourier-transform.md): An index of the output coordinates, running from 0 to q-1.
- $F_q$ (Fourier transform), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The discrete Fourier transform of length q, the map sending u to F_q u.
- $F_q^+$ (positive-sign transform), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The same map with the positive sign in the exponent, with omega replaced by its inverse.
- $n$ (input length), bound on [Radix-digit convolution](radix-digit-convolution.md): The number of bits in each input.
- $b$ (digit width), bound on [Radix-digit convolution](radix-digit-convolution.md): The number of bits in each digit.
- $q$ (digits per input), bound on [Radix-digit convolution](radix-digit-convolution.md): The number of radix-$2^b$ digits in each input.
- $x$ (first input), bound on [Radix-digit convolution](radix-digit-convolution.md): The first input, a binary string of $n$ bits.
- $y$ (second input), bound on [Radix-digit convolution](radix-digit-convolution.md): The second input, a binary string of $n$ bits.
- $x_i$ (digit of x), bound on [Radix-digit convolution](radix-digit-convolution.md): The digit of $x$ at position $i$, of weight $(2^b)^i$.
- $y_i$ (digit of y), bound on [Radix-digit convolution](radix-digit-convolution.md): The digit of $y$ at position $i$, of weight $(2^b)^i$.
- $i$ (digit position), bound on [Radix-digit convolution](radix-digit-convolution.md): The position of a digit, running from $0$ to $q-1$.
- $j$ (coefficient position), bound on [Radix-digit convolution](radix-digit-convolution.md): The position of a product coefficient, running from $0$ to $2q-2$.
- $z$ (formal variable), bound on [Radix-digit convolution](radix-digit-convolution.md): A formal variable in which each input is written as a polynomial whose coefficients are its digits.
- $c_j$ (product coefficient), bound on [Radix-digit convolution](radix-digit-convolution.md): The integer coefficient of $z^j$ in the product of the two digit polynomials.
- $r$ (record length), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The number of complex coefficients in a record, a power of two at least 2.
- $R_r$ (record ring), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The ring of polynomials with complex coefficients in which $y^r$ is identified with $-1$.
- $y$ (polynomial variable), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The polynomial variable whose powers serve as the roots of unity.
- $c_i$ (record coefficient), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The coefficient of $y^i$ in the record being shifted.
- $i$ (coefficient position), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The position of a coefficient in a record, from 0 to r-1.
- $a$ (shift amount), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The number of places a signed shift moves each coefficient, an integer with 0 \le a < 2r.
- $t$ (transform length), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The number of entries in the transform, a power of two dividing 2r.
- $\omega_t$ (transform root), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The primitive t-th root of unity $y^{2r/t}$ in the record ring.
- $z$ (transform input), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The input list of t records to be transformed.
- $Z$ (transform output), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The transform of the input z, a list of t entries.
- $j$ (output index), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The index of an entry of the transform, from 0 to t-1.
- $k$ (input index), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The index of an entry of the input, from 0 to t-1.
- $q$ (transform length), bound on [Gaussian resampling](gaussian-resampling.md): the number of entries of the vector that a transform of length q acts on.
- $F_q$ (normalized transform), bound on [Gaussian resampling](gaussian-resampling.md): the normalized discrete Fourier transform of length q.
- $s$ (source length), bound on [Gaussian resampling](gaussian-resampling.md): the number of entries in the source vector, which is the length of the transform being replaced.
- $t$ (resampled length), bound on [Gaussian resampling](gaussian-resampling.md): the power-of-two number of entries in the resampled vector, greater than s.
- $\theta$ (relative gap), bound on [Gaussian resampling](gaussian-resampling.md): the relative gap t/s - 1 between the two lengths.
- $\alpha$ (Gaussian width), bound on [Gaussian resampling](gaussian-resampling.md): a positive integer parameter that sets the width of the Gaussian weights.
- $p$ (precision), bound on [Gaussian resampling](gaussian-resampling.md): a positive integer precision parameter of the approximations.
- $P_s$ (source reordering), bound on [Gaussian resampling](gaussian-resampling.md): the permutation of length-s vectors that reorders their entries by multiplying each position by t modulo s.
- $P_t$ (target reordering), bound on [Gaussian resampling](gaussian-resampling.md): the permutation of length-t vectors that reorders their entries by multiplying each position by -s modulo t.
- $A$ (forward contraction), bound on [Gaussian resampling](gaussian-resampling.md): the linear contraction from length-s vectors to length-t vectors that appears in the identity.
- $B$ (backward contraction), bound on [Gaussian resampling](gaussian-resampling.md): the linear contraction from length-t vectors to length-s vectors that appears in the identity.
- $y$ (polynomial variable), bound on [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md): The indeterminate of the polynomial ring, whose powers act as roots of unity.
- $r$ (record length), bound on [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md): The number of complex coefficients in a polynomial record, a power of two.
- $R_r$ (polynomial ring), bound on [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md): The ring $\mathbb{C}[y]/(y^r+1)$ studied on this page.
- $z$ (ring element), bound on [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md): An element of the ring, written as a polynomial with complex coefficients.
- $z_k$ (coefficient), bound on [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md): The k-th complex coefficient of the representative of z, for 0 <= k < r.
- $s$ (shift amount), bound on [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md): The number of positions by which the coefficient list moves under multiplication by y^s, with 0 <= s < r.
- $y$ (indeterminate), bound on [Signed coefficient packing](signed-packing.md): The indeterminate of the polynomial ring, the variable in which the packed polynomials are written.
- $r$ (coefficient count), bound on [Signed coefficient packing](signed-packing.md): The number of coefficients of each polynomial being packed.
- $j$ (coefficient index), bound on [Signed coefficient packing](signed-packing.md): The index of a coefficient, running from 0 to r-1.
- $p$ (coefficient bit bound), bound on [Signed coefficient packing](signed-packing.md): The number of bits in the magnitude bound on each coefficient, so every coefficient has magnitude at most 2^p.
- $f$ (packed polynomial), bound on [Signed coefficient packing](signed-packing.md): A polynomial in y with r integer coefficients, packed as the integer f(B).
- $g$ (second packed polynomial), bound on [Signed coefficient packing](signed-packing.md): A second polynomial in y with r integer coefficients, multiplied with f by one integer product.
- $B$ (block base), bound on [Signed coefficient packing](signed-packing.md): The base 2^{4p} of the integer encoding, one block of 4p bits per coefficient.
- $h$ (product polynomial), bound on [Signed coefficient packing](signed-packing.md): The ordinary polynomial product fg, whose coefficients are read back from the integer product.
- $c$ (centered residue), bound on [Signed coefficient packing](signed-packing.md): The unique integer in [-B/2, B/2) congruent to f(B)g(B) modulo B, which is the next coefficient of h.
- $s$ (sequence length), bound on [Cyclic convolution](cyclic-convolution.md): The number of entries in each of the two input sequences.
- $f$ (first input sequence), bound on [Cyclic convolution](cyclic-convolution.md): The first of the two sequences of length s being convolved.
- $g$ (second input sequence), bound on [Cyclic convolution](cyclic-convolution.md): The second of the two sequences of length s being convolved.
- $\ast$ (cyclic convolution), bound on [Cyclic convolution](cyclic-convolution.md): The operation that maps two length-s sequences to their cyclic convolution, a sequence of length s.
- $k$ (output position), bound on [Cyclic convolution](cyclic-convolution.md): An index in the range 0 to s-1 naming an entry of the cyclic convolution.
- $j$ (summation index), bound on [Cyclic convolution](cyclic-convolution.md): The index running over the entries of f in the cyclic convolution sum.
- $x$ (formal variable), bound on [Cyclic convolution](cyclic-convolution.md): The indeterminate of the polynomial associated with a sequence, whose power x^j stands for position j.
- $E$ (fixed bilinear space), bound on [Subspace labels](subspace-labels.md): The fixed bilinear space that contains every label, with bilinear form $\langle\cdot,\cdot\rangle$.
- $m$ (ambient dimension), bound on [Subspace labels](subspace-labels.md): The dimension of $E$, which counts the coordinates of a vector of $E$.
- $U$ (label), bound on [Subspace labels](subspace-labels.md): A nondegenerate subspace of $E$ attached to a gate or terminal.
- $V$ (head label), bound on [Subspace labels](subspace-labels.md): The label at the head of an edge, whose tail label is $U$.
- $C_U$ (label frame), bound on [Subspace labels](subspace-labels.md): The frame at a vertex whose label is $U$.
- $h$ (ground set size), bound on [Subspace labels](subspace-labels.md): The number of elements of the ground set on which triples are taken.
- $J$ (all-one matrix), bound on [Subspace labels](subspace-labels.md): The $h\times h$ matrix whose entries are all $1$.
- $T$ (triple), bound on [Subspace labels](subspace-labels.md): A three-element subset of the ground set.
- $t_T$ (triple indicator vector), bound on [Subspace labels](subspace-labels.md): The indicator vector of a triple $T$ in $\mathbb{Q}^h$, with a one in each coordinate of an element of $T$ and zero elsewhere.
- $S$ (other triple), bound on [Subspace labels](subspace-labels.md): Another triple of the ground set, compared with $T$ through the form.
- $h$ (ground set size), bound on [Subset-intersection network](subset-intersection-network.md): The number of elements in the ground set $[h]$, from which the triples are drawn.
- $\mathcal{K}$ (set of triples), bound on [Subset-intersection network](subset-intersection-network.md): The set of all three-element subsets of $[h]$.
- $a$ (bank index), bound on [Subset-intersection network](subset-intersection-network.md): An index $a=(a_1,a_2,a_3)$ of one entry of a bank, a triple of triples.
- $X$ (source bank), bound on [Subset-intersection network](subset-intersection-network.md): One of the two banks of values, with entries $x_a$, that the network exchanges.
- $Y$ (target bank), bound on [Subset-intersection network](subset-intersection-network.md): The other of the two banks of values, with entries $y_a$, that the network exchanges.
- $t_T$ (indicator vector), bound on [Subset-intersection network](subset-intersection-network.md): The $0/1$ vector of a triple $T$, with a $1$ in the coordinate of each element of $T$.
- $S$ (neighbouring triple), bound on [Subset-intersection network](subset-intersection-network.md): A triple that is a neighbour of the other triple $T$ when they share exactly one element.
- $T$ (neighbouring triple), bound on [Subset-intersection network](subset-intersection-network.md): A triple, here the triple whose indicator vector is $t_T$.
- $A_{ST}$ (side wire), bound on [Subset-intersection network](subset-intersection-network.md): The auxiliary wire attached to an ordered neighbouring pair $(S,T)$.
- $C_i$ (central wire), bound on [Subset-intersection network](subset-intersection-network.md): The auxiliary wire attached to an element $i$ of the ground set.
- $i$ (ground element), bound on [Subset-intersection network](subset-intersection-network.md): An element of the ground set $[h]$, one coordinate of an indicator vector.
- $H$ (Hadamard matrix), bound on [Complex phase network](complex-phase-network.md): The normalized $2\times 2$ Hadamard matrix.
- $X$ (bit-flip matrix), bound on [Complex phase network](complex-phase-network.md): The $2\times 2$ matrix that swaps the two coordinates of a vector.
- $C$ (two-point kernel), bound on [Complex phase network](complex-phase-network.md): The two-point kernel $H\,\mathrm{diag}(1, i)\,H$, which equals $aI + bX$.
- $a$ (kernel coefficient a), bound on [Complex phase network](complex-phase-network.md): The constant $(1+i)/2$ in the kernel $C = aI + bX$.
- $b$ (kernel coefficient b), bound on [Complex phase network](complex-phase-network.md): The constant $(1-i)/2$ in the kernel $C = aI + bX$.
- $m$ (address length), bound on [Complex phase network](complex-phase-network.md): The number of coordinates of a binary address, so that $\mathbb{F}_2^m$ is the address space.
- $x$ (binary address), bound on [Complex phase network](complex-phase-network.md): A binary address, a vector in $\mathbb{F}_2^m$.
- $U$ (subspace label), bound on [Complex phase network](complex-phase-network.md): A binary label, which is a subspace of $\mathbb{F}_2^m$.
- $C_U$ (label frame), bound on [Complex phase network](complex-phase-network.md): The frame matrix of a vertex with label $U$.
- $P_U$ (label projection), bound on [Complex phase network](complex-phase-network.md): The projection onto the label $U$ over $\mathbb{F}_2$.
- $\mathrm{wt}$ (Hamming weight), bound on [Complex phase network](complex-phase-network.md): The number of coordinates equal to 1 of a binary vector, read as an integer.
- $q_U$ (label phase exponent), bound on [Complex phase network](complex-phase-network.md): The Hamming weight of $P_U x$ modulo 4, the exponent of $i$ in the frame of label $U$.
- $V$ (head label), bound on [Complex phase network](complex-phase-network.md): The label at the head of an edge.
- $E$ (orthogonal residual), bound on [Complex phase network](complex-phase-network.md): The orthogonal residual of an edge, the part of $V$ orthogonal to $U$.
- $B$ (residual basis), bound on [Complex phase network](complex-phase-network.md): An orthonormal basis of the residual $E$ of an edge.
- $v$ (residual basis vector), bound on [Complex phase network](complex-phase-network.md): A vector of the residual basis $B$.
- $\varepsilon$ (edge sign), bound on [Complex phase network](complex-phase-network.md): The sign in $\{1,-1\}$ congruent to $\mathrm{wt}(v)$ modulo 4, which includes the edge direction.
- $X_v$ (translation by v), bound on [Complex phase network](complex-phase-network.md): The translation operator on arrays indexed by $\mathbb{F}_2^m$, shifting the argument by $v$.
- $u$ (pair value (first)), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The first of the two values of a pair that the two-point map takes as input.
- $v$ (pair value (second)), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The second of the two values of a pair that the two-point map takes as input.
- $H_0$ (two-point map), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The map sending a pair of values to their half-sum and half-difference.
- $D$ (axis count), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The number of axes on which the layer acts, which is also the number of address chunks it transforms.
- $K$ (chunk width), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The number of address bits in each chunk.
- $\rho$ (selected offset), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The position, counted from the least significant end, of the selected bit within each chunk.
- $K$ (chunk width), bound on [Transform layout](transform-layout.md): The number of address bits in each consecutive chunk, a count of bits.
- $D$ (participating axes), bound on [Transform layout](transform-layout.md): The number of participating axes, each contributing one chunk, a count.
- $\rho$ (selected offset), bound on [Transform layout](transform-layout.md): The position, counted from the least significant bit of a chunk, of the bit selected in every chunk.
- $s$ (smaller call count), bound on [Rank-saving recursion](rank-saving-recursion.md): The number of smaller calls that one call makes.
- $W$ (wire count), bound on [Rank-saving recursion](rank-saving-recursion.md): The number of wires in the network, which is also the number of roles among which the rows of an array are distributed.
- $m$ (label dimension), bound on [Rank-saving recursion](rank-saving-recursion.md): The dimension of the fixed ambient space in which the labels are subspaces.
- $V$ (data volume), bound on [Rank-saving recursion](rank-saving-recursion.md): The number of stored data bits in the array that a call works on.
- $f$ (call parameter), bound on [Rank-saving recursion](rank-saving-recursion.md): The parameter of a call, which counts the digits of the field being interchanged or the selected axes of a numerical layer.
- $N$ (source dimension), bound on [Rank-saving recursion](rank-saving-recursion.md): The sum of the dimensions of the labels at the sources of the network.
- $L$ (lost dimension), bound on [Rank-saving recursion](rank-saving-recursion.md): The total dimension lost along the decreasing edges of the network.
- $g$ (normalized cost), bound on [Rank-saving recursion](rank-saving-recursion.md): The function giving the cost of a call at parameter f divided by its volume.
- $\tau$ (power-saving exponent), bound on [Rank-saving recursion](rank-saving-recursion.md): The exponent of the power saving, the logarithm to base m of s/W.
- $p$ (precision), bound on [Guard-width bound](guard-width-bound.md): The number of fractional bits carried by each input coefficient.
- $D$ (selected axes), bound on [Guard-width bound](guard-width-bound.md): The number of selected axes in one layer.
- $d$ (axis bound), bound on [Guard-width bound](guard-width-bound.md): An upper bound on the number D of selected axes in one layer.
- $\Delta$ (guard count), bound on [Guard-width bound](guard-width-bound.md): The number of extra fractional bits reserved for one layer.
- $C_0$ (depth constant), bound on [Guard-width bound](guard-width-bound.md): A fixed constant of the network, equal to 128 m B^2.
- $C_1$ (depth exponent), bound on [Guard-width bound](guard-width-bound.md): The exponent of d in the guard count, equal to 20 for the stated construction.
- $B$ (per-level growth bound), bound on [Guard-width bound](guard-width-bound.md): A fixed count, s plus 64(W+m+1)^3, that bounds how much the depth grows at each recursive level.
- $W$ (wire count), bound on [Guard-width bound](guard-width-bound.md): The number of wires in the complex network.
- $m$ (label dimension), bound on [Guard-width bound](guard-width-bound.md): The dimension of the label space of the complex network.
- $s$ (smaller-call count), bound on [Guard-width bound](guard-width-bound.md): The total number of smaller calls made by the network.
- $\ell$ (depth), bound on [Guard-width bound](guard-width-bound.md): The number of arithmetic operations on a chain that computes a value from an input coefficient.
- $u$ (first coefficient), bound on [Guard-width bound](guard-width-bound.md): The first of the two coefficients that the two-point map combines.
- $v$ (second coefficient), bound on [Guard-width bound](guard-width-bound.md): The second of the two coefficients that the two-point map combines.
- $H$ (address field H), bound on [Address shear](address-shear.md): The first of the two address fields, a vector of m fields, which the shear updates.
- $D$ (address field D), bound on [Address shear](address-shear.md): The second of the two address fields, a vector of m fields, which the shear reads and leaves unchanged.
- $m$ (fields per vector), bound on [Address shear](address-shear.md): The number of fields in each of the vectors H and D.
- $b$ (digits per field), bound on [Address shear](address-shear.md): The number of radix-q digits in each field.
- $q$ (radix prime), bound on [Address shear](address-shear.md): A fixed odd prime, the base of the digits.
- $M$ (shear matrix), bound on [Address shear](address-shear.md): A fixed rational m by m matrix that determines the shear.
- $a$ (rational rank), bound on [Address shear](address-shear.md): The number of interchanges used for the shear with matrix M, equal to the rank of M over the rational numbers.
- $V$ (stored bit volume), bound on [Address shear](address-shear.md): The number of stored bits in the array.
- $h$ (value of H), bound on [Address shear](address-shear.md): The current value of H when m = 1.
- $d$ (value of D), bound on [Address shear](address-shear.md): The current value of D when m = 1.
- $X$ (control chunk), bound on [Packed selected-bit addition](packed-bit-addition.md): The address chunk whose selected bits are XORed into the target chunk $W$.
- $W$ (target chunk), bound on [Packed selected-bit addition](packed-bit-addition.md): The address chunk whose selected bits receive the XOR and are updated by the procedure.
- $T$ (scratch chunk), bound on [Packed selected-bit addition](packed-bit-addition.md): The third address chunk, whose initial value is arbitrary and which is used as temporary space.
- $L$ (chunk width), bound on [Packed selected-bit addition](packed-bit-addition.md): The number of address bits in each of the chunks $X$ and $W$.
- $f$ (segments per chunk), bound on [Packed selected-bit addition](packed-bit-addition.md): The number of $K$-bit segments into which each chunk is cut, so that each segment holds one selected bit.
- $K$ (segment width), bound on [Packed selected-bit addition](packed-bit-addition.md): The number of bits in each segment of a chunk.
- $\rho$ (first selected position), bound on [Packed selected-bit addition](packed-bit-addition.md): The position of the first selected bit, counted from $0$ at the least significant end.
- $E$ (exceptional addresses), bound on [Packed selected-bit addition](packed-bit-addition.md): The set of addresses at which the parallel segment updates may carry, and which the correction handles.
- $\tau$ (interchange exponent), bound on [Packed selected-bit addition](packed-bit-addition.md): The fixed exponent, between $0$ and $1$, in the time bound of the address-field interchange.
- $V$ (stream volume), bound on [Packed selected-bit addition](packed-bit-addition.md): The number of bits in the stream on which the procedure runs.
- $q$ (vector length), bound on [Transform identity with retained permutations](transform-identity.md): The number of entries of a vector to which the normalized transform F_q applies.
- $u$ (input vector), bound on [Transform identity with retained permutations](transform-identity.md): A complex vector whose length is set by the transform applied to it.
- $v$ (second vector), bound on [Transform identity with retained permutations](transform-identity.md): A complex vector whose length is set by the transform applied to it.
- $F_q$ (normalized transform), bound on [Transform identity with retained permutations](transform-identity.md): The normalized discrete Fourier transform of length q.
- $j$ (entry index), bound on [Transform identity with retained permutations](transform-identity.md): An index of an entry of a vector, running from 0 to q-1 in the sum defining F_q.
- $k$ (output index), bound on [Transform identity with retained permutations](transform-identity.md): An index of an entry of a transformed vector, taken modulo q.
- $\Pi$ (coordinate permutation), bound on [Transform identity with retained permutations](transform-identity.md): A rearrangement of the entries of a vector.
- $s$ (source length), bound on [Transform identity with retained permutations](transform-identity.md): The number of entries of the source vectors, the length of the source axis.
- $t$ (target length), bound on [Transform identity with retained permutations](transform-identity.md): The number of entries of the target vectors, the length of the target axis.
- $P_s$ (source permutation), bound on [Transform identity with retained permutations](transform-identity.md): The coordinate permutation of length-s vectors given by (P_s u)_j = u_{tj}.
- $P_t$ (target permutation), bound on [Transform identity with retained permutations](transform-identity.md): The coordinate permutation of length-t vectors given by (P_t v)_k = v_{-sk}.
- $p$ (precision), bound on [Transform identity with retained permutations](transform-identity.md): The precision, which fixes the grid 2^{-p} on which approximate values are stored.
- $\alpha$ (integer parameter), bound on [Transform identity with retained permutations](transform-identity.md): A fixed integer parameter of the identity, with 2 <= alpha < p.
- $\theta$ (relative gap), bound on [Transform identity with retained permutations](transform-identity.md): The ratio t/s minus one, which measures how far apart the two lengths are.
- $A$ (source map), bound on [Transform identity with retained permutations](transform-identity.md): A linear contraction from length-s vectors to length-t vectors.
- $B_0$ (target map), bound on [Transform identity with retained permutations](transform-identity.md): A linear contraction from length-t vectors to length-s vectors.
- $q$ (transform length), bound on [Bluestein's chirp identity](bluestein-chirp-identity.md): The number of entries in each input and output vector of the transform.
- $u$ (input vector), bound on [Bluestein's chirp identity](bluestein-chirp-identity.md): The input vector of the transform, with entries $u_0$ through $u_{q-1}$.
- $j$ (input position), bound on [Bluestein's chirp identity](bluestein-chirp-identity.md): An index into the input vector, an integer from 0 to q-1.
- $k$ (output position), bound on [Bluestein's chirp identity](bluestein-chirp-identity.md): An index into the output vector, an integer from 0 to q-1.
- $F_q$ (transform), bound on [Bluestein's chirp identity](bluestein-chirp-identity.md): The discrete Fourier transform of length q, normalized by 1/q.
- $\cdot$ (coordinatewise product), bound on [Bluestein's chirp identity](bluestein-chirp-identity.md): The product of two vectors of length q taken entry by entry.
- $\ast$ (cyclic convolution), bound on [Bluestein's chirp identity](bluestein-chirp-identity.md): The cyclic convolution of two vectors of length q.
- $x$ (first operand), bound on [Bluestein's chirp identity](bluestein-chirp-identity.md): The first of the two vectors of length q in the cyclic convolution.
- $y$ (second operand), bound on [Bluestein's chirp identity](bluestein-chirp-identity.md): The second of the two vectors of length q in the cyclic convolution.
- $a$ (chirp), bound on [Bluestein's chirp identity](bluestein-chirp-identity.md): The chirp vector, whose entry at each integer m is e^{\pi i m^2/q}.
- $m$ (integer argument), bound on [Bluestein's chirp identity](bluestein-chirp-identity.md): The integer at which the chirp entry a_m is evaluated.
- $\zeta$ (twist root), bound on [Phase twist](phase-twist.md): A root of unity of order $2r$, namely $e^{\pi i/r}$, whose powers are the twist factors.
- $j$ (coefficient position), bound on [Phase twist](phase-twist.md): The position of a coefficient in a record, counted from 0.
- $k$ (first term position), bound on [Phase twist](phase-twist.md): The position of the coefficient taken from the first record in a product.
- $l$ (second term position), bound on [Phase twist](phase-twist.md): The position of the coefficient taken from the second record in a product.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Cyclic convolution](cyclic-convolution.md): The product of two sequences in which indices wrap around modulo the sequence length.
  Shown as: Chinese-remainder map *<predicate>* Cyclic convolution
- [Radix-digit convolution](radix-digit-convolution.md): Writing both integers as polynomials in a power of two whose coefficients are their digits, so that their product is a polynomial convolution of short coefficients.
  Shown as: Chinese-remainder map *<predicate>* Radix-digit convolution
- [Mixed-radix digits](mixed-radix-digits.md): The digits of an integer written in a positional system whose place values use a separate length for each place, so that the digit at each place ranges over its own length.
  Shown as: Chinese-remainder map *<predicate>* Mixed-radix digits
- [Ring homomorphism and isomorphism](ring-homomorphism.md): A map between rings that preserves addition and multiplication; it is an isomorphism when it is also bijective, so that the two rings have the same structure.
  Shown as: Chinese-remainder map *<predicate>* Ring homomorphism and isomorphism

## Pages that build on this one

- Prime source lengths: Distinct odd primes chosen close to the powers of two that are the padded axis lengths, so that their product fills a fixed fraction of the padded box.
- Integer multiplication below n log n: A deterministic fixed-tape machine that multiplies two n-bit integers exactly in O(n (lg n)^(1−κ)) time with κ = 2^−182, which disproves the n log n optimality conjecture in this model.

## Other pages you may link to

- [Convolution](convolution.md)
- [Transform axis](transform-axis.md)
- [Address field](address-field.md)
- [Exclusive or](xor.md)
- [Linear algebra basics](linear-algebra-basics.md)
- [Linear networks and frames](linear-network-frames.md)
- [Endpoint operator](endpoint-operator.md)
- [Limit inferior](limit-inferior.md)
- [Fixed-tape machine model](fixed-tape-model.md)
- [Running time cost](running-time-cost.md)
- [Exact integer multiplication](exact-integer-multiplication.md)
- [The n log n optimality conjecture](n-log-n-conjecture.md)
- [Cost table](cost-table.md)
- [Established O(n log n) multiplier](established-multiplier.md)
- [Cyclic shift](cyclic-shift.md)
- [Ground set](ground-set.md)
- [Gate and terminal of a network](network-gate-terminal.md)
- [Scratch storage](scratch-storage.md)
- [Address-field interchange](address-interchange.md)
- [Bit procedure](bit-procedure.md)
- [Binary field](binary-field.md)
- [Indicator vector](indicator-vector.md)
- [Line spanned by a vector](line-spanned-by-vector.md)
- [Gaussian integer](gaussian-integer.md)
- [Tensor product](tensor-product.md)
- [Matrix rank](matrix-rank.md)
- [Truncation](truncation.md)
- [Payload](payload.md)
- [Union bound](union-bound.md)
- [Schoolbook multiplication](schoolbook-multiplication.md)
- [Stable radix sort](stable-radix-sort.md)
- [Destination rank](destination-rank.md)
- [Binary change of basis](binary-change-of-basis.md)
- [Phase factor](phase-factor.md)
- [Gaussian dyadics](gaussian-dyadics.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Multidimensional transform](multidimensional-transform.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md)
- [Butterfly](butterfly.md)
- [Opposite transform](opposite-transform.md)
- [Polynomial ring](polynomial-ring.md)
- [Array norm](array-norm.md)
- [Grid numerator](grid-numerator.md)
- [Linear contraction](linear-contraction.md)
- [Congruence](congruence-modulo.md)
- [Signed coefficient packing](signed-packing.md)
- [Centered residue](centered-residue.md)
- [Cyclic coordinate](cyclic-coordinate.md)
- [Bilinear map](bilinear-map.md)
- [Bilinear form](bilinear-form.md)
- [Subspace labels](subspace-labels.md)
- [Subset-intersection network](subset-intersection-network.md)
- [Complex phase network](complex-phase-network.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Transform layout](transform-layout.md)
- [Numerical layer](numerical-layer.md)
- [Rank-saving recursion](rank-saving-recursion.md)
- [Transform round](transform-round.md)
- [Padded transform box](padded-transform-box.md)
- [Normalized cyclic convolution](normalized-cyclic-convolution.md)
- [Normalization scales](normalization-scales.md)
- [Little-o notation](little-o-notation.md)
- [Guard-width bound](guard-width-bound.md)
- [Coprime](coprime.md)
- [Modular inverse](modular-inverse.md)
- [Address shear](address-shear.md)
- [Packed selected-bit addition](packed-bit-addition.md)
- [Transform identity with retained permutations](transform-identity.md)
- [Bluestein's chirp identity](bluestein-chirp-identity.md)
- [Phase twist](phase-twist.md)
- [Prime source lengths](prime-source-lengths.md)
- [Carry propagation](carry-propagation.md)
- [Convolution over the polynomial ring](polynomial-ring-convolution.md)
- [Exact coefficient recovery](recovery-and-error.md)
- [Integer multiplication below n log n](main-theorem.md)

## Evidence from the sources

- "a Chinese-remainder map that preserves convolution" (paper)

## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The reader cannot follow this step: "these are all $S$ monomial basis elements of the target" (The page does not say that the monomials with exponents below each s_i form a basis of the target ring, so the reader cannot check that the S powers are all of them.)
- The reader cannot follow this step: "Then $b_i = a_i + \mu_i \sum_{j<i} a_j P_j \pmod{s_i}$." (The page does not show that Phi(x^k) = Phi(x)^k has x_i-exponent mu_i k, which must be reduced modulo s_i before the k = sum a_j P_j substitution gives this formula.)
- The reader cannot follow this step: "In the main argument it is the step that places the coefficients of a" (The claim refers to a main argument that is not on this page and is not linked, so the reader cannot check it.)
- The reader cannot follow this step: "In the main argument the axis lengths are distinct primes" (The claim about the axis lengths in the main argument cannot be checked from this page.)
- Say what $m$ denotes where it is first used (for a size or count, what it counts): "The power $\Phi(x)^m$ equals $1$ exactly when $s_i \mid m$ for every $i$" (Nothing says what m denotes or what range it takes; it is only used as an exponent.)
- "mixed-radix digit" is the concept [Mixed-radix digits](mixed-radix-digits.md), now a prerequisite: link it where the term is used.
- "ring homomorphism and ring isomorphism" is the concept [Ring homomorphism and isomorphism](ring-homomorphism.md), now a prerequisite: link it where the term is used.

## Previous version (revise it)

It has 700 words. Fix the problems by restructuring rather than appending: keep the rewrite within 875 words, a quarter more, unless a problem cannot be fixed without more. Pages that grow with every repair stop being self-contained explanations of one concept.

The Chinese-remainder map is a relabeling of coefficient positions that turns one [cyclic convolution](cyclic-convolution.md) into a multidimensional cyclic convolution. In the main argument it is the step that places the coefficients of a [radix-digit convolution](radix-digit-convolution.md) on distinct prime cyclic axes, so that each axis can be transformed separately. It is also called the Agarwal–Cooley map. <cite data-source="paper">Cooley used the Chinese remainder theorem to convert one cyclic convolution into multidimensional</cite>

Let $d$ be the number of cyclic axes. Where $s_i$ is the number of positions on axis $i$, the lengths $s_1, \dots, s_d$ are pairwise coprime, meaning any two of them have greatest common divisor $1$. Let $S = s_1 s_2 \cdots s_d$ be the total number of positions, which is the length of the one-dimensional cyclic convolution being replaced. <cite data-source="paper">The transform lengths needed for the integer product are pairwise coprime</cite>

A cyclic convolution of length $S$ indexes its positions by the integers modulo $S$. The Chinese remainder theorem says that when $S$ factors into pairwise coprime lengths, an integer modulo $S$ is determined by its residue modulo each factor. The map below is that splitting, written out with explicit coordinates.

For each axis $i$, let $P_i = s_1 s_2 \cdots s_{i-1}$ be the product of the lengths before it, with $P_1 = 1$ as an empty product. <cite data-source="paper">Here Pi denotes an integer prefix product</cite> Let $\mu_i$ be an inverse of $P_i$ modulo $s_i$, so that $\mu_i P_i \equiv 1 \pmod{s_i}$. It exists because $P_i$ is a product of lengths coprime to $s_i$.

Write $x$ for the indeterminate of the one-dimensional ring, so that $\mathbb{C}[x]/(x^S-1)$ is the ring of polynomials in which $x^S$ is replaced by $1$. Multiplying two such polynomials wraps exponents modulo $S$, which is exactly cyclic convolution of their coefficient lists. The target is the multidimensional ring $\mathbb{C}[x_1,\dots,x_d]/(x_1^{s_1}-1,\dots,x_d^{s_d}-1)$, where $x_i$ is the indeterminate of axis $i$ and $x_i^{s_i}$ is replaced by $1$. A multidimensional cyclic convolution is the product in this ring, where the exponent on each axis wraps modulo that axis's length.

Define $\Phi$ on the generator by $\Phi(x) = \prod_{i=1}^d x_i^{\mu_i}$, and extend it to polynomials as a ring homomorphism. This is well defined: the exponent of $x_i$ in $\Phi(x)^S$ is $\mu_i S$, which is divisible by $s_i$, so $\Phi(x)^S = 1$ in the target. The power $\Phi(x)^m$ equals $1$ exactly when $s_i \mid m$ for every $i$, because each $\mu_i$ is invertible modulo $s_i$. Since the $s_i$ are pairwise coprime, this happens exactly when $S \mid m$. So $\Phi(x)$ has order $S$, its powers are $S$ distinct monomials, and these are all $S$ monomial basis elements of the target. <cite data-source="paper">through all target basis monomials exactly once.</cite> <cite data-source="paper">Hence Φ is an isomorphism and preserves cyclic</cite> Because $\Phi$ is a ring isomorphism, the map preserves [cyclic convolution](cyclic-convolution.md) of length $S$: the product of two coefficient polynomials maps to the product of their images, which is a multidimensional cyclic convolution on the axes $s_1, \dots, s_d$.

Let $k$ be an ordinary coefficient index, with $0 \le k < S$. Let $a_j$ be the mixed-radix digit of $k$ on axis $j$, with $0 \le a_j < s_j$. <cite data-source="paper">Every ordinary coefficient index has a unique mixed-radix expression</cite>, $k = \sum_{j=1}^{d} a_j P_j$.

Let $b_i$ be the coordinate of $\Phi(x^k)$ on axis $i$, so $\Phi(x^k) = \prod_i x_i^{b_i}$. Then $b_i = a_i + \mu_i \sum_{j<i} a_j P_j \pmod{s_i}$. <cite data-source="paper">The coordinate of Φ(xk ) in axis i is</cite> <cite data-source="paper">Indeed terms with j > i are divisible by si</cite> Terms with $j > i$ vanish modulo $s_i$ because $P_j$ contains the factor $s_i$. The $j = i$ term gives $\mu_i P_i a_i \equiv a_i$, and the terms with $j < i$ remain.

So the coefficient at index $k$ is stored at the address $(b_1, \dots, b_d)$ on the axes.

Take $d = 2$, $s_1 = 3$, $s_2 = 5$, so $S = 15$. Then $P_1 = 1$, $P_2 = 3$, $\mu_1 = 1$, and $\mu_2 = 2$ because $3 \cdot 2 = 6 \equiv 1 \pmod 5$. So $\Phi(x) = x_1 x_2^2$. The index $k = 7$ has digits $a_1 = 1$ and $a_2 = 2$, since $7 = 1 + 3 \cdot 2$. Its coordinates are $b_1 = a_1 = 1$ and $b_2 = a_2 + \mu_2 a_1 P_1 = 2 + 2 \cdot 1 \cdot 1 \equiv 4 \pmod 5$. Directly, $\Phi(x)^7 = x_1^7 x_2^{14} = x_1 x_2^4$, since $7 \equiv 1 \pmod 3$ and $14 \equiv 4 \pmod 5$. So index $7$ is stored at address $(1, 4)$ on the $3 \times 5$ grid.

In the main argument the axis lengths are distinct primes, which are pairwise coprime, so this construction applies. <cite data-source="paper">First, the radix-digit coefficient list is placed on a product of distinct</cite> prime cyclic axes.

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

Write the body to `exegenius/tasks/0145-write-chinese-remainder-map.answer.md` and the JSON to `exegenius/tasks/0145-write-chinese-remainder-map.answer.json`, then run `exegenius submit 0145-write-chinese-remainder-map` in the project directory. If submit rejects the answer, fix the answer and submit again.
