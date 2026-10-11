# exegenius task 0125-write-complex-phase-network

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
- Synthetic polynomial transforms (also: Nussbaumer polynomial transforms, polynomial transforms, Nussbaumer and Quandalle)
- Polynomial ring modulo y^r + 1 (also: negacyclic polynomial ring)
  - $y$ (polynomial variable): The indeterminate of the polynomial ring, whose powers act as roots of unity.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Signed coefficient packing (also: Kronecker substitution)
- Subspace labels
- Linear networks and frames (also: roles, frames)
- Subset-intersection network (also: three-element subset network, subset-intersection network and complex phase network)
- Address-field interchange (also: power-width interchange, tape procedure for interchanging address chunks)
- Gaussian dyadics
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
- Cyclic coordinate (also: last cyclic coordinate)
- Limit inferior
- Line spanned by a vector
- Multidimensional transform (also: multidimensional transforms with power-of-two axes)
- Array norm (also: norm of an array)
- Opposite transform (also: opposite-sign transform)
- Payload
- Phase factor (also: phase factors and scalar corrections)
- Polynomial ring
- Matrix rank (also: rational rank)
- Schoolbook multiplication
- Scratch storage (also: scratch values, scratch chunk, scratch wires)
- Tensor product (also: tensor power)
- Truncation
- Union bound
- Exclusive or (also: XOR)

## This page

Concept: Complex phase network
Gloss: A subset-intersection network whose frame change on each edge is a product of two-point kernels aI + bX on Gaussian dyadic values.
Also called: phase-frame identity, complex variant

## Where the argument relies on this page

- A butterfly layer on the selected bits of several axes is applied at once, in a single pass. (on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md))
- The number $s$ of smaller calls satisfies $s < Wm$, so each recursive level saves a power. (on [Rank-saving recursion](rank-saving-recursion.md))
- The parameters are chosen so that every term in the cost table is $O(n(\lg n)^{1-\kappa})$ for $\kappa = 2^{-182}$, which fits the bound of the theorem.

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

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Subset-intersection network](subset-intersection-network.md): A linear network on the three-element subsets of a ground set, whose wires carry scalars and whose gates combine them by intersection size, so that it swaps two banks while cancelling arbitrary scratch values.
  Shown as: Complex phase network *<predicate>* Subset-intersection network
- [Gaussian dyadics](gaussian-dyadics.md): Complex numbers whose real and imaginary parts are integers divided by a power of two, with the Gaussian integer part also an integer.
  Shown as: Complex phase network *<predicate>* Gaussian dyadics
- [Subspace labels](subspace-labels.md): Nondegenerate subspaces of a fixed bilinear space attached to each wire of a network, whose inclusions control how much work a change of representation costs.
  Shown as: Complex phase network *<predicate>* Subspace labels
- [Binary field](binary-field.md): The field with two elements 0 and 1, where addition is exclusive or and multiplication is AND.
  Shown as: Complex phase network *<predicate>* Binary field
- [Tensor product](tensor-product.md): The Kronecker product of two matrices, whose m-fold power applies one operator to m independent coordinates at once.
  Shown as: Complex phase network *<predicate>* Tensor product

## Pages that build on this one

- Simultaneous butterfly layer: The tensor product of the two-point map H0 applied to several selected address bits at once, computed exactly in one pass rather than one axis at a time.

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
- [Indicator vector](indicator-vector.md)
- [Line spanned by a vector](line-spanned-by-vector.md)
- [Gaussian integer](gaussian-integer.md)
- [Matrix rank](matrix-rank.md)
- [Truncation](truncation.md)
- [Payload](payload.md)
- [Union bound](union-bound.md)
- [Schoolbook multiplication](schoolbook-multiplication.md)
- [Stable radix sort](stable-radix-sort.md)
- [Destination rank](destination-rank.md)
- [Binary change of basis](binary-change-of-basis.md)
- [Phase factor](phase-factor.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Radix-digit convolution](radix-digit-convolution.md)
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
- [Cyclic convolution](cyclic-convolution.md)
- [Cyclic coordinate](cyclic-coordinate.md)
- [Bilinear map](bilinear-map.md)
- [Bilinear form](bilinear-form.md)
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
- [Ring homomorphism and isomorphism](ring-homomorphism.md)
- [Mixed-radix digits](mixed-radix-digits.md)
- [Chinese-remainder map](chinese-remainder-map.md)
- [Prime source lengths](prime-source-lengths.md)
- [Carry propagation](carry-propagation.md)
- [Convolution over the polynomial ring](polynomial-ring-convolution.md)
- [Exact coefficient recovery](recovery-and-error.md)
- [Integer multiplication below n log n](main-theorem.md)

## Evidence from the sources

- "The complex phase network of Proposition 8" (paper)

## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The reader cannot follow this step: "The reason is the weight identity with the correction term $-2|\mathrm{supp}(z) \cap \mathrm{supp}(w)|$" (The weight identity is named but not stated or derived, so the mod-4 relation for q_V(x) - q_U(x) cannot be checked from the page.)
- The reader cannot follow this step: "Since $v \cdot v = 1$, $\mathrm{wt}(v)$ is odd" (This needs v·v = wt(v) mod 2 for binary vectors, which the page does not give or justify.)
- The reader cannot follow this step: "where the sign also carries the edge direction" (How the sign epsilon depends on the edge direction is not specified; only its existence is argued.)
- The reader cannot follow this step: "tensored over the coordinates in the support of $v$ turns the character $(-1)^{v\cdot x}$ into a translation" (The claim that a tensor product of two-point kernels over the support of v turns the character into a translation is asserted, not calculated.)
- The reader cannot follow this step: "Each entry of $C_U$ and of its inverse is therefore a Gaussian integer divided by $2^m$" (The inverse of C_U is never given in closed form, so the claim that its entries are Gaussian integers over 2^m cannot be checked from the page.)
- Say what $\mathbb{F}_2$ denotes where it is first used (for a size or count, what it counts): "Here $x \in \mathbb{F}_2^m$ is a binary address, and $m$ is the number of its coordinates." (The field with two elements is never named or explained; the page only says that x is a binary address.)
- Say what $I$ denotes where it is first used: the page uses it before saying so in "where $I$ is the identity."
- Say what $C_V$ denotes where it is first used (for a size or count, what it counts): "For an edge from label $U$ to label $V$, the frame change is $C_V C_U^{-1}$, where $V$ is the head label." (C_V is the frame at a vertex labelled V; the page defines C_U for a general label, but never says that C_V is the same matrix with V in place of U.)
- Say what $V$ denotes where it is first used: the page uses it before saying so in "where $V$ is the head label."
- Say what $\cdot$ denotes where it is first used (for a size or count, what it counts): "Each $v \in B$ is a binary vector with $v \cdot v = 1$." (The inner product of two binary vectors is used but never defined, and the reader profile does not cover it.)
- Say what $\mathrm{supp}$ denotes where it is first used: the page uses it before saying so in "where $\mathrm{supp}(z)$ is the set of coordinates at which $z$ is 1."
- Say what $z$ denotes where it is first used: the page uses it before saying so in "where $\mathrm{supp}(z)$ is the set of coordinates at which $z$ is 1."
- Say what $w$ denotes where it is first used (for a size or count, what it counts): "If $z\cdot w = 0$, the intersection has even size, so the weight is additive modulo 4." (Nothing says what w is (a binary vector, presumably), and it is never introduced.)
- Say what $\perp$ denotes where it is first used (for a size or count, what it counts): "Let $E$ be the orthogonal residual of the edge, so that $V = U \perp E$ on an increasing edge." (The page uses the perpendicular sign for the orthogonal sum but never says what it denotes.)
- Say what $f$ denotes where it is first used (for a size or count, what it counts): "The translation $X_v$ is defined by $(X_v f)(x) = f(x+v)$." (f is an unspecified function on addresses; the page never says what it ranges over.)
- Say what $\mathrm{diag}$ denotes where it is first used: the page uses it before saying so in "where $\mathrm{diag}_x(i^{q_U(x)})$ multiplies the value at each address $x$ by $i^{q_U(x)}$"
- Say what $\otimes$ denotes where it is first used: the page uses it before saying so in "and $H^{\otimes m}$ is the $m$-fold tensor power of $H$."
- "finite field F_2" is the concept [Binary field](binary-field.md), now a prerequisite: link it where the term is used.
- "tensor power" is the concept [Tensor product](tensor-product.md), now a prerequisite: link it where the term is used.

## Previous version (revise it)

It has 753 words. Fix the problems by restructuring rather than appending: keep the rewrite within 941 words, a quarter more, unless a problem cannot be fixed without more. Pages that grow with every repair stop being self-contained explanations of one concept.

The complex phase network is obtained from the [subset-intersection network](subset-intersection-network.md) by replacing each wire's scalar with an array of complex values, and it changes the frame of those arrays along each edge by a product of two-point kernels. It supplies the frame identity that the [simultaneous butterfly layer](simultaneous-butterfly-layer.md) uses to apply a butterfly on several address bits at once, one step toward the [main theorem](main-theorem.md).

The constants are $a = (1+i)/2$ and $b = (1-i)/2$. Here $x \in \mathbb{F}_2^m$ is a binary address, and $m$ is the number of its coordinates.

Let $H = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$ be the normalized Hadamard matrix. Let $X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ be the bit-flip matrix, which swaps the two coordinates of a vector. <cite data-source="paper">where X interchanges the two coordinates</cite>

The two-point kernel is $C = H\,\mathrm{diag}(1, i)\,H = aI + bX$, where $I$ is the identity. Since $a^2+b^2=0$ and $2ab=1$, squaring gives $C^2 = X$. Also $C^{-1} = bI + aX$, because $(aI+bX)(bI+aX) = I$.

The complex phase network is indexed by [subspace labels](subspace-labels.md), with one binary label at each vertex. <cite data-source="paper">Use the complex scalar network and binary labels.</cite> A label $U$ is a subspace of $\mathbb{F}_2^m$. The frame at a vertex with label $U$ is the matrix $C_U$ defined below.

Let $\mathrm{wt}(x)$ be the Hamming weight of a binary vector $x$, the number of its coordinates equal to 1, read as an integer. Let $P_U$ be the projection onto $U$ over $\mathbb{F}_2$. <cite data-source="paper">The projection here is over F2</cite> For a label $U$, let $q_U(x)$ be the Hamming weight of $P_U x$ modulo 4, so that $q_U(x) = \mathrm{wt}(P_U x) \pmod 4$. <cite data-source="paper">qU (x) = wt(PU x)</cite>

For a label $U$, the frame is
$$C_U = H^{\otimes m}\,\mathrm{diag}_x\big(i^{q_U(x)}\big)\,H^{\otimes m},$$
where $\mathrm{diag}_x(i^{q_U(x)})$ multiplies the value at each address $x$ by $i^{q_U(x)}$, and $H^{\otimes m}$ is the $m$-fold tensor power of $H$. <cite data-source="paper">The use of H in this definition is an identity of matrices. Each entry of CU and its inverse is a</cite> Each entry of $C_U$ and of its inverse is therefore a Gaussian integer divided by $2^m$, so $C_U$ and its inverse preserve arrays of Gaussian dyadic values.

For an edge from label $U$ to label $V$, the frame change is $C_V C_U^{-1}$, where $V$ is the head label. <cite data-source="paper">On an edge from label U to label</cite>

Let $E$ be the orthogonal residual of the edge, so that $V = U \perp E$ on an increasing edge. Let $B$ be an orthonormal basis of $E$. Each $v \in B$ is a binary vector with $v \cdot v = 1$. <cite data-source="paper">Each v has norm one, so wt(v) is odd.</cite> Since $v \cdot v = 1$, $\mathrm{wt}(v)$ is odd, so for each $v$ there is a sign $\varepsilon \in \{1,-1\}$ with $\mathrm{wt}(v) \equiv \varepsilon \pmod 4$, where the sign also carries the edge direction. Then $q_V(x) - q_U(x) = \sum_{v\in B} \mathrm{wt}(v)\,[v\cdot x] \pmod 4$, where $[v\cdot x]$ is 1 when $v\cdot x = 1$ and 0 otherwise, and the right side is negated on a decreasing edge. <cite data-source="paper">and B is an orthonormal basis of E, it follows that</cite> The reason is the weight identity <cite data-source="paper">wt(z + w) = wt(z) + wt(w)</cite> with the correction term $-2|\mathrm{supp}(z) \cap \mathrm{supp}(w)|$, where $\mathrm{supp}(z)$ is the set of coordinates at which $z$ is 1. If $z\cdot w = 0$, the intersection has even size, so the weight is additive modulo 4.

For each $v \in B$, the factor is $i^{\varepsilon[v\cdot x]} = \frac{1+i\varepsilon}{2} + \frac{1-i\varepsilon}{2}(-1)^{v\cdot x}$, since both sides equal 1 when $v\cdot x = 0$, and the right side equals $i\varepsilon$ when $v\cdot x = 1$. <cite data-source="paper">The identity H diag(1, −1)H = X</cite> tensored over the coordinates in the support of $v$ turns the character $(-1)^{v\cdot x}$ into a translation. The translation $X_v$ is defined by $(X_v f)(x) = f(x+v)$. <cite data-source="paper">Here (Xv f )(x) = f (x + v).</cite> So the factor is $\frac{1+i\varepsilon}{2}I + \frac{1-i\varepsilon}{2}X_v$. This is $aI + bX_v$ for $\varepsilon = 1$, and $bI + aX_v$ for $\varepsilon = -1$, which is the inverse of $aI + bX_v$ by the same computation as for $C$, using $X_v^2 = I$.

The frame change on the edge is therefore a product, over $v \in B$, of one such kernel, each $aI + bX_v$ or its inverse. <cite data-source="paper">is a product of one translation kernel aI + bXv</cite> Along a route of edges the intermediate frames cancel, so the composite change depends only on its endpoints. <cite data-source="paper">phase frames gives C ⊗m on every role</cite> <cite data-source="paper">All these numbers are fixed, independently of any eventual input length.</cite>

The complex phase network has coefficients in [Gaussian dyadics](gaussian-dyadics.md): each entry of $C_U$ and of its inverse is a Gaussian integer divided by $2^m$. <cite data-source="paper">below have Gaussian dyadic coefficients.</cite>

Take $m=1$ and the two labels $\{0\}$ and $\mathbb{F}_2$. For $\{0\}$, $q_{\{0\}}(x)=0$, so $C_{\{0\}} = H\,I\,H = I$. For $\mathbb{F}_2$, $P_{\mathbb{F}_2}$ is the identity, so $q_{\mathbb{F}_2}(x) = x$ and $C_{\mathbb{F}_2} = C$. The edge from $\{0\}$ to $\mathbb{F}_2$ has residual $E = \mathbb{F}_2$ with orthonormal basis $B = \{1\}$, because $\mathrm{wt}(1) = 1$ and $\varepsilon = 1$. Its frame change is $C_{\mathbb{F}_2} C_{\{0\}}^{-1} = C = aI + bX_1$. Here $X_1 = X$, since $X_1$ maps $f(x)$ to $f(x+1)$, which swaps the two values of $f$.

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

Write the body to `exegenius/tasks/0125-write-complex-phase-network.answer.md` and the JSON to `exegenius/tasks/0125-write-complex-phase-network.answer.json`, then run `exegenius submit 0125-write-complex-phase-network` in the project directory. If submit rejects the answer, fix the answer and submit again.
