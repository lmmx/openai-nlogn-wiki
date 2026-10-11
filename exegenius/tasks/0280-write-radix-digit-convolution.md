# exegenius task 0280-write-radix-digit-convolution

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
- Exact integer multiplication (also: exact multiplication)
- Discrete Fourier transform (also: normalized Fourier transform, transform, Fourier transform, normalized form, frequency order)
- Synthetic polynomial transforms (also: Nussbaumer polynomial transforms, polynomial transforms, Nussbaumer and Quandalle)
- Polynomial ring modulo y^r + 1 (also: negacyclic polynomial ring)
  - $y$ (polynomial variable): The indeterminate of the polynomial ring, whose powers act as roots of unity.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Linear networks and frames (also: roles, frames, network of wires and gates, network, vertex, edge, source and sink vertices, Edge change)
- Address field (also: address chunk, chunk, target chunk, selected address bits)
- Transform axis (also: axis, remaining axes, reduction axis)
- Linear algebra basics (also: linear algebra: invertible linear operator, matrix, inverse, matrix, linear map, usual axioms)
- Butterfly (also: two-point butterfly map, two-point map, Butterfly operation)
- Cyclic shift (also: controlled cyclic shift, signed shifts)
- Convolution
- Coprime (also: gcd, pairwise coprime, coprime (gcd))
- Running time cost (also: cost, linear-cost update, bit-complexity bound)
- Stable radix sort (also: label-and-sort operations)
- Destination rank (also: prefix-slot move, move, extracted records, rectangular routine, hole, destination key)
- Gate and terminal of a network (also: gate applied pointwise, pointwise linear gate, sink)
- Ground set (also: finite set)
- Indicator vector
- Little-o notation (also: limit as lambda tends to infinity)
- Multidimensional transform (also: multidimensional transforms with power-of-two axes)
- Array norm (also: norm of an array, coefficient bound)
- Payload (also: record)
- Phase factor (also: phase factors and scalar corrections)
- Polynomial ring (also: polynomial suffix)
- Matrix rank (also: rational rank, rank of a shear, Row reduction and pivots)
- Ring homomorphism and isomorphism (also: ring homomorphism and ring isomorphism)
- Schoolbook multiplication (also: the paper's construction)
- Truncation
- Address (also: binary addresses)
- Array (also: disk array)
- Logical array (also: logical array and stored array)
- Logarithm (also: logarithm lg)
- Base-2 logarithm (also: logarithm and ceiling)
- Bijection
- Permutation
- Eigenvalue
- Incidence
- Mathematical induction (also: induction)
- Integer
- Prime number (also: prime)
- Ring
- Pointwise product
- Root of unity (also: roots of unity)
- Stream (also: fixed track, scan, role stream, stream position)
- Schönhage–Strassen multiplication (also: Schönhage and Strassen, Schönhage–Strassen bound)

## This page

Concept: Radix-digit convolution
Gloss: Writing both integers as polynomials in a power of two whose coefficients are their digits, so that their product is a polynomial convolution of short coefficients.

## This page in the argument

The step: Exact multiplication of two $n$-bit integers reduces to a convolution of short integer coefficients obtained by splitting each input into radix digits.
How: split each input into radix digits and convolve
Why: Short coefficients keep each convolution cheap, so the cost comes from the transforms rather than from the digits. (the sources leave this for the reader to work out: spell it out)

Its sub-steps, in order:

- Exact multiplication of $n$-bit integers reduces to convolution of short integer coefficients.

It serves these steps, from the main result down:

- Exact multiplication of two $n$-bit integers runs in $O(n(\lg n)^{1-\kappa})$ time on one deterministic fixed-tape machine, with $\kappa = 2^{-182}$.; how: reduce exact multiplication to radix-digit convolution, compute that convolution with fast tape transforms, and recover the exact product (on [Integer multiplication below n log n](main-theorem.md))

## Symbols already bound on earlier pages

The symbols in the names of the concepts the reader knows are listed with those concepts above.

- $x$ (first input), bound on [Exact integer multiplication](exact-integer-multiplication.md): The first input, a binary string of length n.
- $y$ (second input), bound on [Exact integer multiplication](exact-integer-multiplication.md): The second input, a binary string of length n.
- $\mathrm{val}$ (binary value), bound on [Exact integer multiplication](exact-integer-multiplication.md): The function giving the nonnegative integer value of a binary string, with the leftmost bit most significant.
- $\mathrm{bin}_k$ (padded binary representation), bound on [Exact integer multiplication](exact-integer-multiplication.md): The function giving the binary representation of an integer padded on the left with zeros to a fixed length k.
- $k$ (padded length), bound on [Exact integer multiplication](exact-integer-multiplication.md): The number of bits in the padded binary string, so it counts the bit positions of the representation.
- $z$ (integer to encode), bound on [Exact integer multiplication](exact-integer-multiplication.md): A nonnegative integer less than $2^k$, which is written in binary by the padded representation.
- $\#$ (separator), bound on [Exact integer multiplication](exact-integer-multiplication.md): A separator symbol that marks where the first input ends and the second begins.
- $a$ (first input sequence), bound on [Convolution](convolution.md): The first input sequence, of length n.
- $b$ (second input sequence), bound on [Convolution](convolution.md): The second input sequence, of length n.
- $n$ (sequence length), bound on [Convolution](convolution.md): The number of entries in each input sequence.
- $k$ (output position), bound on [Convolution](convolution.md): The position of an entry of the output sequence c.
- $i$ (input position in a), bound on [Convolution](convolution.md): The position of an entry of a in a product a_i b_j.
- $j$ (input position in b), bound on [Convolution](convolution.md): The position of an entry of b in a product a_i b_j.
- $c$ (convolution), bound on [Convolution](convolution.md): The convolution of a and b, a sequence of length 2n-1.
- $p$ (fractional precision), bound on [Truncation](truncation.md): The number of fractional binary places kept, so the grid spacing is $2^{-p}$.
- $Q_p$ (truncation to precision p), bound on [Truncation](truncation.md): The operator that truncates each real and imaginary coefficient part of an array toward zero to the grid $2^{-p}\mathbb{Z}$.
- $z$ (input array), bound on [Truncation](truncation.md): An array of complex coefficients that is truncated by $Q_p$.
- $w$ (key width), bound on [Stable radix sort](stable-radix-sort.md): The number of bits in each key.
- $M$ (record count), bound on [Stable radix sort](stable-radix-sort.md): The number of records being sorted.
- $k$ (key), bound on [Stable radix sort](stable-radix-sort.md): The key of a record, written as a string of $w$ bits.
- $i$ (bit index), bound on [Stable radix sort](stable-radix-sort.md): The position of a key bit, counting from 0 at the least significant end; pass $i$ sorts by bit $k_i$.
- $q$ (address before the move), bound on [Destination rank](destination-rank.md): The address of a record before the move.
- $q'$ (address after the move), bound on [Destination rank](destination-rank.md): The address of the same record after the move.
- $\operatorname{rank}$ (stream rank), bound on [Destination rank](destination-rank.md): The position of a record among the records in stream order, written as a function of its address.
- $h$ (chunk index), bound on [Destination rank](destination-rank.md): The index of one of the three address chunks, taking values 1, 2 or 3.
- $q_h$ (current chunk value), bound on [Destination rank](destination-rank.md): The current value of chunk h of the address q.
- $q'_h$ (destination chunk value), bound on [Destination rank](destination-rank.md): The value that chunk h of the address takes after the move.
- $\sigma_h$ (record stride), bound on [Destination rank](destination-rank.md): The amount by which the rank changes when chunk h rises by one with the other chunks fixed.
- $M$ (record count), bound on [Destination rank](destination-rank.md): The number of records in the stream.
- $A_{\mathrm{rect}}$ (integer bit bound), bound on [Destination rank](destination-rank.md): A bit-size bound for the integers the rectangular routine handles.
- $R$ (polynomial ring), bound on [Polynomial ring](polynomial-ring.md): The quotient ring of complex polynomials in y modulo the multiples of f.
- $f$ (modulus polynomial), bound on [Polynomial ring](polynomial-ring.md): The fixed monic polynomial with complex coefficients by which the ring is reduced.
- $m$ (modulus degree), bound on [Polynomial ring](polynomial-ring.md): The degree of f, which is also the number of coefficients in the representative of each element of R.
- $X$ (array of complex values), bound on [Array norm](array-norm.md): A finite array of complex values, the argument of the norm.
- $w$ (array entry), bound on [Array norm](array-norm.md): A single entry of the array X, which is a complex number.
- $\|X\|$ (array norm), bound on [Array norm](array-norm.md): The largest modulus of the entries of the array X, a nonnegative real number.
- $\varphi$ (function being bounded), bound on [Little-o notation](little-o-notation.md): A map from the positive reals to the positive reals, the function that the little-o statement bounds.
- $\psi$ (comparison function), bound on [Little-o notation](little-o-notation.md): A map from the positive reals to the positive reals, positive for all large arguments, against which the function being bounded is compared.
- $\lambda$ (limit variable), bound on [Little-o notation](little-o-notation.md): The real point at which both functions are evaluated, taken to infinity in the limit.
- $\beta$ (first integer), bound on [Coprime](coprime.md): One of the two integers whose greatest common divisor is taken, not both zero.
- $\gamma$ (second integer), bound on [Coprime](coprime.md): The second of the two integers whose greatest common divisor is taken, not both zero.
- $M$ (family size), bound on [Coprime](coprime.md): The number of integers in a family of integers, which counts the members of the family.
- $\lambda_i$ (family member), bound on [Coprime](coprime.md): The i-th integer of a family of integers, for an index i from 1 to M.
- $Q$ (source ring), bound on [Ring homomorphism and isomorphism](ring-homomorphism.md): The ring from which the ring homomorphism $\varphi$ starts.
- $Q'$ (target ring), bound on [Ring homomorphism and isomorphism](ring-homomorphism.md): The ring into which the ring homomorphism $\varphi$ sends elements of $Q$.
- $\varphi$ (ring homomorphism), bound on [Ring homomorphism and isomorphism](ring-homomorphism.md): A map from the ring $Q$ to the ring $Q'$ that preserves sums, products and the identity.
- $\xi$ (ring element), bound on [Ring homomorphism and isomorphism](ring-homomorphism.md): An arbitrary element of the source ring $Q$.
- $\eta$ (ring element), bound on [Ring homomorphism and isomorphism](ring-homomorphism.md): A second arbitrary element of the source ring $Q$.
- $w$ (indeterminate), bound on [Ring homomorphism and isomorphism](ring-homomorphism.md): The variable of the example ring $Q=\mathbb{C}[w]/(w^2-1)$, whose square is $1$.
- $\lambda$ (constant coefficient), bound on [Ring homomorphism and isomorphism](ring-homomorphism.md): The complex coefficient of $1$ in an element $\lambda+\mu w$ of $Q$.
- $\mu$ (linear coefficient), bound on [Ring homomorphism and isomorphism](ring-homomorphism.md): The complex coefficient of $w$ in an element $\lambda+\mu w$ of $Q$.
- $\psi$ (evaluation at one), bound on [Ring homomorphism and isomorphism](ring-homomorphism.md): The ring homomorphism from $Q$ to $\mathbb{C}$ that sends $w$ to $1$, which is not bijective.
- $u$ (field width), bound on [Address field](address-field.md): The number of address bits in each of the two fields being interchanged, a count.
- $L$ (block length), bound on [Cyclic shift](cyclic-shift.md): The number of positions in the block that a cyclic shift rotates.
- $i$ (position index), bound on [Cyclic shift](cyclic-shift.md): A position in the block, numbered from 0 to L-1.
- $k$ (offset), bound on [Cyclic shift](cyclic-shift.md): The integer, taken modulo L, by which the cyclic shift rotates the block.
- $V$ (stored bit volume), bound on [Cyclic shift](cyclic-shift.md): The number of bits held in the array being shifted.
- $F$ (field), bound on [Linear algebra basics](linear-algebra-basics.md): The field of scalars over which vector spaces are taken.
- $x$ (vector), bound on [Linear algebra basics](linear-algebra-basics.md): A vector in a vector space over $F$.
- $y$ (vector), bound on [Linear algebra basics](linear-algebra-basics.md): A second vector in a vector space over $F$.
- $c$ (scalar), bound on [Linear algebra basics](linear-algebra-basics.md): A scalar, an element of the field $F$.
- $m$ (coordinate count), bound on [Linear algebra basics](linear-algebra-basics.md): The number of coordinates in each vector of $F^m$, which is the dimension of $F^m$.
- $T$ (linear map), bound on [Linear algebra basics](linear-algebra-basics.md): A linear map between vector spaces over $F$.
- $A$ (matrix), bound on [Linear algebra basics](linear-algebra-basics.md): An $m\times m$ matrix with entries in $F$.
- $I$ (identity matrix), bound on [Linear algebra basics](linear-algebra-basics.md): The matrix with ones on the diagonal and zeros elsewhere.
- $S$ (candidate inverse), bound on [Linear algebra basics](linear-algebra-basics.md): A linear map that is a two-sided inverse of the operator $T$ when $T$ is invertible.
- $B$ (candidate inverse matrix), bound on [Linear algebra basics](linear-algebra-basics.md): A matrix that is a two-sided inverse of the matrix $A$ when $A$ is invertible.
- $v$ (vertex), bound on [Linear algebra basics](linear-algebra-basics.md): A vertex of the network in the paper, at which a frame is placed.
- $D_v$ (frame), bound on [Linear algebra basics](linear-algebra-basics.md): The invertible linear operator on arrays attached to vertex $v$.
- $g$ (logical array), bound on [Linear algebra basics](linear-algebra-basics.md): The array of values that the network computes on, before its frame is applied.
- $M$ (matrix of a frame), bound on [Linear algebra basics](linear-algebra-basics.md): A matrix that determines the frame $\Phi_M$.
- $\Phi_M$ (matrix frame), bound on [Linear algebra basics](linear-algebra-basics.md): The frame on arrays determined by the matrix $M$.
- $v$ (vertex), bound on [Linear networks and frames](linear-network-frames.md): A source, gate or sink of the network.
- $D_v$ (frame of a vertex), bound on [Linear networks and frames](linear-network-frames.md): An invertible linear operator on arrays, the frame at vertex $v$.
- $g$ (logical array), bound on [Linear networks and frames](linear-network-frames.md): The array a wire is meant to represent before any frame is applied.
- $G$ (pointwise linear gate), bound on [Linear networks and frames](linear-network-frames.md): A gate that combines its input arrays separately at each address.
- $t$ (gate input count), bound on [Linear networks and frames](linear-network-frames.md): The number of input arrays a gate takes.
- $g_1,\dots,g_t$ (gate input arrays), bound on [Linear networks and frames](linear-network-frames.md): The logical input arrays of a gate.
- $c_j$ (input weight), bound on [Linear networks and frames](linear-network-frames.md): The fixed weight of input j in a gate, the same at every address.
- $w$ (input wire), bound on [Linear networks and frames](linear-network-frames.md): An input wire of the network.
- $f_w$ (supplied input array), bound on [Linear networks and frames](linear-network-frames.md): The supplied physical array on input wire $w$.
- $\mathrm{source}(w)$ (source vertex), bound on [Linear networks and frames](linear-network-frames.md): The source vertex of wire $w$.
- $g_w$ (logical input array), bound on [Linear networks and frames](linear-network-frames.md): The logical array of input wire $w$, equal to $D_{\mathrm{source}(w)}^{-1} f_w$.
- $r$ (output role), bound on [Linear networks and frames](linear-network-frames.md): An output role of the network.
- $\mathrm{sink}(r)$ (sink vertex), bound on [Linear networks and frames](linear-network-frames.md): The sink vertex of output role $r$.
- $\rho$ (role permutation), bound on [Linear networks and frames](linear-network-frames.md): The permutation of roles that the scalar network realises, sending input role $w$ to output role $\rho(w)$.
- $\varepsilon_w$ (scalar sign), bound on [Linear networks and frames](linear-network-frames.md): The fixed sign multiplied onto the value carried from input role $w$.
- $h$ (ground set size), bound on [Ground set](ground-set.md): The number of elements of the ground set $[h]$.
- $v$ (vertex), bound on [Gate and terminal of a network](network-gate-terminal.md): A gate or terminal of the network, which carries the frame $D_v$.
- $h$ (ground-set size), bound on [Indicator vector](indicator-vector.md): The number of elements in the ground set $[h] = \{1, \dots, h\}$, which is 100 in the construction.
- $T$ (triple), bound on [Indicator vector](indicator-vector.md): A three-element subset of the ground set $[h]$.
- $t_T$ (triple indicator vector), bound on [Indicator vector](indicator-vector.md): The indicator vector of the triple $T$: the 0-1 vector with entry 1 exactly at the positions of the elements of $T$.
- $\mathbb{Q}$ (rational numbers), bound on [Matrix rank](matrix-rank.md): The field of rational numbers, the fractions p/q with integers p and q nonzero.
- $m$ (matrix size), bound on [Matrix rank](matrix-rank.md): The number of rows of a square matrix M, which is also its number of columns.
- $M$ (rational matrix), bound on [Matrix rank](matrix-rank.md): A rational matrix with m rows and m columns.
- $\operatorname{rank}_{\mathbb{Q}}(M)$ (matrix rank), bound on [Matrix rank](matrix-rank.md): The number of linearly independent rows of M over the rationals, which equals the number of linearly independent columns.
- $\zeta$ (phase factor), bound on [Phase factor](phase-factor.md): A complex number of modulus one, the factor multiplied into coefficients.
- $\alpha$ (real part), bound on [Phase factor](phase-factor.md): The real part of the complex number z.
- $\beta$ (imaginary part), bound on [Phase factor](phase-factor.md): The imaginary part of the complex number z.
- $q$ (transform length), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The number of coordinates of each vector the transform acts on.
- $\omega$ (primitive root of unity), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The primitive q-th root of unity, with \omega^q = 1.
- $u$ (input vector), bound on [Discrete Fourier transform](discrete-fourier-transform.md): A vector of q complex numbers, the input of the transform.
- $j$ (input index), bound on [Discrete Fourier transform](discrete-fourier-transform.md): An integer index of input coordinates, running from 0 to q-1.
- $\ell$ (output index), bound on [Discrete Fourier transform](discrete-fourier-transform.md): An integer index of output coordinates, running from 0 to q-1.
- $m$ (input index), bound on [Discrete Fourier transform](discrete-fourier-transform.md): An integer index of input coordinates, running from 0 to q-1.
- $F_q$ (discrete Fourier transform), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The map of length q sending a vector of q complex numbers to its transform.
- $F_q^+$ (positive-sign transform), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The transform of length q with the positive sign, which replaces omega by its inverse.
- $L$ (linear map), bound on [Discrete Fourier transform](discrete-fourier-transform.md): A generic linear map from vectors to vectors, tested for the contraction property.
- $D$ (number of axes), bound on [Transform axis](transform-axis.md): The number of axes of an array, which is the number of coordinates in each address.
- $t_i$ (axis length), bound on [Transform axis](transform-axis.md): The length of axis $i$: the number of values that coordinate of an address takes.
- $x_i$ (axis coordinate), bound on [Transform axis](transform-axis.md): The coordinate of an address along axis $i$, an integer with $0 \le x_i < t_i$.
- $D$ (axis count), bound on [Multidimensional transform](multidimensional-transform.md): The number of transform axes, a positive integer.
- $s$ (axis index), bound on [Multidimensional transform](multidimensional-transform.md): The index of an axis, running from 1 to D.
- $t_s$ (axis length), bound on [Multidimensional transform](multidimensional-transform.md): The number of coordinates along axis s, a power of two.
- $M$ (entry count), bound on [Multidimensional transform](multidimensional-transform.md): The number of entries of the array, the product of the axis lengths.
- $X$ (input array), bound on [Multidimensional transform](multidimensional-transform.md): The input array, on which the transform acts.
- $Y$ (output array), bound on [Multidimensional transform](multidimensional-transform.md): The output array, the transformed array.
- $m$ (input position), bound on [Multidimensional transform](multidimensional-transform.md): A position in the input array, with each coordinate below its axis length.
- $h$ (output position), bound on [Multidimensional transform](multidimensional-transform.md): A position in the output array, with each coordinate below its axis length.
- $\mathcal{F}$ (multidimensional transform), bound on [Multidimensional transform](multidimensional-transform.md): The map from the input array to the output array.
- $r$ (record length), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The number of complex coefficients in a record, a power of two at least 2.
- $R_r$ (record ring), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The ring of polynomials with complex coefficients in which $y^r$ is identified with $-1$; records are its elements.
- $y$ (polynomial variable), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The formal variable of the polynomial ring $R_r$.
- $c_m$ (coefficient of a record), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The complex coefficient of $y^m$ in a record.
- $m$ (coefficient position), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The position of a coefficient in a record, running from $0$ to $r-1$.
- $s$ (shift amount), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The number of places a shift moves each coefficient of a record, with $0 \le s < 2r$.
- $t$ (transform length), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The number of entries in the transform, a power of two dividing $2r$.
- $\omega_t$ (polynomial root of unity), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The primitive $t$-th root of unity $y^{2r/t}$ in $R_r$, used in place of the complex root.
- $h$ (input list), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The list of $t$ records $(h_0,\dots,h_{t-1})$ that the transform takes as input.
- $Z$ (output list), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The list of $t$ records $(Z_0,\dots,Z_{t-1})$ that the transform returns.
- $z$ (ring element), bound on [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md): A single element of the polynomial ring modulo y^r+1, a polynomial with complex coefficients.
- $k$ (coefficient position), bound on [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md): The position of a coefficient in a record, running from 0 to r-1.
- $z_k$ (k-th coefficient), bound on [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md): The coefficient of y^k in the representative z of degree less than r.
- $\zeta$ (root of unity), bound on [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md): A complex number that some positive integer power of it equals 1.
- $m$ (power count), bound on [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md): A positive integer, the number of factors of a root of unity whose product is 1.
- $H_0$ (butterfly map), bound on [Butterfly](butterfly.md): The two-point map sending a pair of values to their half-sum and half-difference.
- $\xi$ (first input value), bound on [Butterfly](butterfly.md): The first of the two values that the butterfly takes as input.
- $\eta$ (second input value), bound on [Butterfly](butterfly.md): The second of the two values that the butterfly takes as input.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Exact integer multiplication](exact-integer-multiplication.md): Given binary strings x and y of length n, output the 2n-bit binary representation of their product.
  Shown as: Radix-digit convolution *<predicate>* Exact integer multiplication
- [Discrete Fourier transform](discrete-fourier-transform.md): The map sending a vector of q values to its q values weighted by powers of a q-th root of unity, normalized by 1/q.
  Shown as: Radix-digit convolution *<predicate>* Discrete Fourier transform
- [Butterfly](butterfly.md): The two-point map H0(u, v) = ((u + v)/2, (u − v)/2) applied to a pair of values, the elementary step of a Fourier-type transform.
  Shown as: Radix-digit convolution *<predicate>* Butterfly

## Pages that build on this one

- Gaussian resampling: A technique that replaces a Fourier transform of arbitrary length by transforms whose axis lengths are powers of two, using Gaussian weights to move between the two sets of frequencies.
- Carry propagation: Converting the recovered integer radix-digit coefficients into a binary string by adding each coefficient to a carry from the previous position.
- Chinese-remainder map: A relabeling of coefficient positions by mixed-radix digits for pairwise coprime lengths, which turns one cyclic convolution into a multidimensional cyclic convolution.
- Integer multiplication below n log n: A deterministic fixed-tape machine that multiplies two n-bit integers exactly in O(n (lg n)^(1−κ)) time with κ = 2^−182, which disproves the n log n optimality conjecture in this model.

## Other pages you may link to

- [Logarithm](logarithm.md)
- [Base-2 logarithm](base-two-logarithm.md)
- [Integer](integer.md)
- [Ring](ring.md)
- [Root of unity](root-of-unity.md)
- [Stream](stream.md)
- [Prime number](prime-number.md)
- [Pointwise product](pointwise-product.md)
- [Running time cost](running-time-cost.md)
- [Schönhage–Strassen multiplication](schonhage-strassen.md)
- [Convolution](convolution.md)
- [Truncation](truncation.md)
- [Payload](payload.md)
- [Bijection](bijection.md)
- [Permutation](permutation.md)
- [Schoolbook multiplication](schoolbook-multiplication.md)
- [Mathematical induction](mathematical-induction.md)
- [Stable radix sort](stable-radix-sort.md)
- [Destination rank](destination-rank.md)
- [Polynomial ring](polynomial-ring.md)
- [Array norm](array-norm.md)
- [Little-o notation](little-o-notation.md)
- [Coprime](coprime.md)
- [Ring homomorphism and isomorphism](ring-homomorphism.md)
- [Address](address.md)
- [Address field](address-field.md)
- [Cyclic shift](cyclic-shift.md)
- [Array](array.md)
- [Linear algebra basics](linear-algebra-basics.md)
- [Linear networks and frames](linear-network-frames.md)
- [Logical array](logical-array.md)
- [Ground set](ground-set.md)
- [Gate and terminal of a network](network-gate-terminal.md)
- [Incidence](incidence.md)
- [Eigenvalue](eigenvalue.md)
- [Indicator vector](indicator-vector.md)
- [Matrix rank](matrix-rank.md)
- [Phase factor](phase-factor.md)
- [Transform axis](transform-axis.md)
- [Multidimensional transform](multidimensional-transform.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Gaussian dyadics](gaussian-dyadics.md)
- [Gaussian integer](gaussian-integer.md)
- [Two-point kernel](two-point-kernel.md)
- [Tensor product](tensor-product.md)
- [Bilinear map](bilinear-map.md)
- [Ceiling function](ceiling-function.md)
- [Carry propagation](carry-propagation.md)
- [Grid numerator](grid-numerator.md)
- [Congruence](congruence-modulo.md)
- [Binary field](binary-field.md)
- [Binary change of basis](binary-change-of-basis.md)
- [Bit network](bit-network.md)
- [Bilinear form](bilinear-form.md)
- [Orthogonal complement](orthogonal-complement.md)
- [Line spanned by a vector](line-spanned-by-vector.md)
- [Centered residue](centered-residue.md)
- [Chinese remainder theorem](chinese-remainder-theorem.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Cyclic coordinate](cyclic-coordinate.md)
- [Bézout's identity](bezout-identity.md)
- [Big-Theta notation](big-theta-notation.md)
- [Cyclic group](cyclic-group.md)
- [Modular inverse](modular-inverse.md)
- [Diagonal scaling](diagonal-scaling.md)
- [Extended real numbers](extended-reals.md)
- [Limit inferior](limit-inferior.md)
- [The n log n optimality conjecture](n-log-n-conjecture.md)
- [Fixed-tape machine model](fixed-tape-model.md)
- [Family parameter](family-parameter.md)
- [Frequency domain](frequency-domain.md)
- [Opposite transform](opposite-transform.md)
- [Transform identity with retained permutations](transform-identity.md)
- [Padded transform box](padded-transform-box.md)
- [Logical bit volume](logical-bit-volume.md)
- [Normalized cyclic convolution](normalized-cyclic-convolution.md)
- [Bluestein's chirp identity](bluestein-chirp-identity.md)
- [Phase twist](phase-twist.md)
- [Normalization scales](normalization-scales.md)
- [Independence of events](independence.md)
- [Projection along a subspace](projection-along-subspace.md)
- [Subspace labels](subspace-labels.md)
- [Subset-intersection network](subset-intersection-network.md)
- [Bit construction](bit-construction.md)
- [Complex phase network](complex-phase-network.md)
- [Scratch storage](scratch-storage.md)
- [Address-field interchange](address-interchange.md)
- [Tape procedure](tape-procedure.md)
- [Exclusive or](xor.md)
- [Bit procedure](bit-procedure.md)
- [Endpoint operator](endpoint-operator.md)
- [Address shear](address-shear.md)
- [Complex construction](complex-construction.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Transform layout](transform-layout.md)
- [Numerical layer](numerical-layer.md)
- [Rank-saving recursion](rank-saving-recursion.md)
- [Transform round](transform-round.md)
- [Cost table](cost-table.md)
- [Established O(n log n) multiplier](established-multiplier.md)
- [Signed coefficient packing](signed-packing.md)
- [Convolution over the polynomial ring](polynomial-ring-convolution.md)
- [Supremum](supremum.md)
- [Linear contraction](linear-contraction.md)
- [Guard-width bound](guard-width-bound.md)
- [Union bound](union-bound.md)
- [Packed selected-bit addition](packed-bit-addition.md)
- [Telescoping identity](telescoping-identity.md)
- [Mixed-radix digits](mixed-radix-digits.md)
- [Chinese-remainder map](chinese-remainder-map.md)
- [Prime source lengths](prime-source-lengths.md)
- [Exact coefficient recovery](recovery-and-error.md)
- [Integer multiplication below n log n](main-theorem.md)

## Evidence from the sources

- "Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients" (paper)

## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The reader cannot follow this step: "The paper takes, so that $2^b \ge n$." (The sentence does not say which b the paper takes, so the reader cannot check that 2^b >= n for the b that is used.)
- The reader cannot follow this step: "Since $b = \lceil \log_2 n \rceil < \log_2 n + 1$, each coefficient has $O(\log n)$ bits." (The equation b = ceil(log2 n) is used here, but no earlier sentence chooses b this way, so the reader cannot check it.)
- The reader cannot follow this step: "Why the split lowers cost." (The page never states the cost of the unsplit multiplication, so the reader cannot check that the split lowers cost.)
- The reader cannot follow this step: "The cost lies in moving data." (The page does not say why the cost is data movement rather than arithmetic, so the reader cannot check this claim.)
- The reader cannot follow this step: "so one level costs time proportional to the stored bits" (The page does not explain why a tape pass that writes each entry to a new address takes time proportional to the stored bits, so the reader cannot check this cost.)
- The reader cannot follow this step: "The paper's count of this cost is that" (The page ends before giving the count, so the reader is given no bound on the cost of the transform.)
- "Butterfly operation" is the concept [Butterfly](butterfly.md), now a prerequisite: link it where the term is used.

## Previous version (revise it)

It has 681 words. Fix the problems by restructuring rather than appending: keep the rewrite within 851 words, a quarter more, unless a problem cannot be fixed without more. Pages that grow with every repair stop being self-contained explanations of one concept.

Radix-digit convolution is a reduction of [exact integer multiplication](exact-integer-multiplication.md) that writes each input as a polynomial in a power of two whose coefficients are its digits, so that the product becomes a convolution of short integer coefficients. It is the first step of the argument for [Integer multiplication below n log n](main-theorem.md): the [Chinese-remainder map](chinese-remainder-map.md) and [carry propagation](carry-propagation.md) pages build on the coefficients it produces.

The paper states the reduction in one sentence: <cite data-source="paper">Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients.</cite>

**Digits.** Let $x$ and $y$ be the two binary strings, each of $n$ bits. Fix a digit width $b \ge 1$. The digit width is the number of bits in each digit. Cut each input into blocks of $b$ bits, counting from the least significant end and padding the last block with leading zeros. Each block is a digit in base $2^b$, the radix. Let $m = \lceil n/b \rceil$ be the number of digits in each input.

The paper takes <cite data-source="paper">b = ⌈log2 n⌉</cite>, so that $2^b \ge n$.

Let $i$ be the position of a digit, running from $0$ to $m-1$. Let $x_i$ be the digit of $x$ at position $i$, with weight $(2^b)^i$, so that $x = \sum_{i=0}^{m-1} x_i (2^b)^i$. The digits $y_i$ of $y$ are defined the same way.

**Polynomials.** Let $z$ be a formal variable. Write $X(z) = \sum_{i=0}^{m-1} x_i z^i$ and $Y(z) = \sum_{i=0}^{m-1} y_i z^i$. Substituting $z = 2^b$ returns the inputs: $X(2^b) = x$ and $Y(2^b) = y$.

Let $t$ be the position of a product coefficient, running from $0$ to $2m-2$. Let $c_t$ be the integer coefficient of $z^t$ in the product $X(z)Y(z)$. Then
$$c_t = \sum_i x_i\, y_{t-i},$$
summed over the $i$ with $0 \le i \le m-1$ and $0 \le t-i \le m-1$. This sum is the convolution of the digit sequences $(x_i)$ and $(y_i)$. Substituting $z = 2^b$ gives $xy = \sum_t c_t (2^b)^t$, so the product is recovered from the $c_t$. The $c_t$ are not yet binary digits, since a coefficient can exceed $2^b-1$.

**Coefficient size.** Each $c_t$ is a sum of at most $m$ products $x_i y_{t-i}$, and each product is at most $(2^b-1)^2$. So $0 \le c_t \le m(2^b-1)^2$. <cite data-source="paper">Every product coefficient obeys</cite> this bound, and it gives $c_t < 2^{3b}$. Because $b \ge 1$ and $n$ is an integer, $m = \lceil n/b \rceil \le n \le 2^b$. Hence $c_t \le 2^b \cdot (2^b)^2 = 2^{3b}$, and the strict inequality holds because $(2^b-1)^2 < 2^{2b}$. Each coefficient therefore fits in $3b$ bits. Since $b = \lceil \log_2 n \rceil < \log_2 n + 1$, each coefficient has $O(\log n)$ bits.

**Example.** Take $n = 4$. Then $b = 2$ and $m = 2$. Let $x = 1101$ (value 13) and $y = 1011$ (value 11). Splitting into base-4 digits from the least significant end gives $x_0 = 1$, $x_1 = 3$, $y_0 = 3$ and $y_1 = 2$. The coefficients are $c_0 = x_0 y_0 = 3$, $c_1 = x_0 y_1 + x_1 y_0 = 2 + 9 = 11$ and $c_2 = x_1 y_1 = 6$. Check: $3 + 11 \cdot 4 + 6 \cdot 16 = 143 = 13 \cdot 11$. The coefficient $c_1 = 11$ is larger than a digit, so the sequence is not yet the binary product. [Carry propagation](carry-propagation.md) converts it into one.

**Why the split lowers cost.** Arithmetic on one coefficient is cheap, since it works on $O(\log n)$-bit numbers. The cost lies in moving data. The $2m-1$ coefficients occupy $(2m-1) \cdot 3b$ stored bits. Since $m \ge n/b$ and $m \le n/b + 1$, this is between $6n - 3b$ and $6n + 3b$ bits, which is $\Theta(n)$ because $b = O(\log n)$.

The convolution is computed with [Fourier transforms](discrete-fourier-transform.md). A transform proceeds in transform levels, where each level is one pass of address rearrangements and butterfly operations over the whole array. On a tape, a pass reads the array in order and writes each entry back at its new address, so one level costs time proportional to the stored bits. Each level therefore scans all $\Theta(n)$ stored bits, even though each coefficient is small. The paper's count of this cost is that <cite data-source="paper">Scanning an array of Θ(n) stored bits at each of Θ(log n) transform levels already costs Θ(n log n).</cite> <cite data-source="paper">We therefore need savings in both movement and arithmetic.</cite>

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

Write the body to `exegenius/tasks/0280-write-radix-digit-convolution.answer.md` and the JSON to `exegenius/tasks/0280-write-radix-digit-convolution.answer.json`, then run `exegenius submit 0280-write-radix-digit-convolution` in the project directory. If submit rejects the answer, fix the answer and submit again.
