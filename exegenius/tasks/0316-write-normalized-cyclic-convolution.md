# exegenius task 0316-write-normalized-cyclic-convolution

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
- Exact integer multiplication (also: exact multiplication)
- The n log n optimality conjecture (also: Schönhage–Strassen conjecture, the conjecture)
- Radix-digit convolution
- Discrete Fourier transform (also: normalized Fourier transform, transform, Fourier transform, normalized form, frequency order)
- Cyclic convolution
- Gaussian resampling (also: Harvey–van der Hoeven resampling, Gaussian weights, Gaussian line map, Gaussian corrections, target)
- Synthetic polynomial transforms (also: Nussbaumer polynomial transforms, polynomial transforms, Nussbaumer and Quandalle)
- Polynomial ring modulo y^r + 1 (also: negacyclic polynomial ring)
  - $y$ (polynomial variable): The indeterminate of the polynomial ring, whose powers act as roots of unity.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Linear networks and frames (also: roles, frames, network of wires and gates, network, vertex, edge, source and sink vertices, Edge change)
- Gaussian dyadics
- Transform identity with retained permutations (also: target permutation, coordinate permutations)
- Carry propagation (also: carry scan)
- Address field (also: address chunk, chunk, target chunk, selected address bits)
- Transform axis (also: axis, remaining axes, reduction axis)
- Linear algebra basics (also: linear algebra: invertible linear operator, matrix, inverse, matrix, linear map, usual axioms)
- Bilinear map (also: bilinear product, bilinear contraction)
- Bilinear form (also: bilinear space, orthogonality, bilinear form and orthogonality, bilinear space and bilinear form)
- Binary field (also: finite field F2, F_2, finite field F_2, copy step)
- Binary change of basis (also: residual basis of directions)
- Butterfly (also: two-point butterfly map, two-point map, Butterfly operation)
- Congruence (also: congruence modulo B, modulo, modulo arithmetic)
- Centered residue
- Cyclic shift (also: controlled cyclic shift, signed shifts)
- Convolution
- Coprime (also: gcd, pairwise coprime, coprime (gcd))
- Running time cost (also: cost, linear-cost update, bit-complexity bound)
- Stable radix sort (also: label-and-sort operations)
- Destination rank (also: prefix-slot move, move, extracted records, rectangular routine, hole, destination key)
- Gate and terminal of a network (also: gate applied pointwise, pointwise linear gate, sink)
- Gaussian integer
- Grid numerator (also: grid numerators)
- Ground set (also: finite set)
- Indicator vector
- Modular inverse (also: invertible modulo q, unit modulo M_i)
- Two-point kernel (also: kernel)
- Cyclic coordinate (also: last cyclic coordinate)
- Limit inferior
- Line spanned by a vector
- Little-o notation (also: limit as lambda tends to infinity)
- Multidimensional transform (also: multidimensional transforms with power-of-two axes)
- Array norm (also: norm of an array, coefficient bound)
- Opposite transform (also: opposite-sign transform)
- Padded transform box
- Payload (also: record)
- Phase factor (also: phase factors and scalar corrections)
- Polynomial ring (also: polynomial suffix)
- Matrix rank (also: rational rank, rank of a shear, Row reduction and pivots)
- Ring homomorphism and isomorphism (also: ring homomorphism and ring isomorphism)
- Schoolbook multiplication (also: the paper's construction)
- Tensor product (also: tensor power)
- Truncation
- Address (also: binary addresses)
- Array (also: disk array)
- Logical array (also: logical array and stored array)
- Logarithm (also: logarithm lg)
- Base-2 logarithm (also: logarithm and ceiling)
- Ceiling function
- Bézout's identity (also: Bezout's identity)
- Big-Theta notation
- Bijection
- Permutation
- Bit network (also: the paper's bit network)
- Chinese remainder theorem (also: CRT)
- Cyclic group (also: cyclic group of order S)
- Diagonal scaling
- Eigenvalue
- Extended real numbers
- Family parameter
- Frequency domain
- Incidence
- Mathematical induction (also: induction)
- Integer
- Prime number (also: prime)
- Logical bit volume
- Ring
- Orthogonal complement
- Pointwise product
- Root of unity (also: roots of unity)
- Stream (also: fixed track, scan, role stream, stream position)
- Schönhage–Strassen multiplication (also: Schönhage and Strassen, Schönhage–Strassen bound)

## This page

Concept: Normalized cyclic convolution
Gloss: A cyclic convolution divided by the transform length, the normalization for which a Fourier transform turns convolution into pointwise product.

## Where the argument relies on this page

- The middle transform, including its target permutation, becomes a normalized cyclic convolution. (on [Bluestein's chirp identity](bluestein-chirp-identity.md))
- Convolution on the remaining axes over the polynomial ring is computed by two forward synthetic transforms, a pointwise product, an opposite transform, and packed integer products. (on [Convolution over the polynomial ring](polynomial-ring-convolution.md))

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
- $b$ (digit width), bound on [Radix-digit convolution](radix-digit-convolution.md): The number of bits in each digit, a positive integer.
- $m$ (digit count), bound on [Radix-digit convolution](radix-digit-convolution.md): The number of digits in each input, the count of blocks of b bits.
- $i$ (digit position), bound on [Radix-digit convolution](radix-digit-convolution.md): The position of a digit in an input, running from 0 to m-1.
- $x_i$ (digit of x), bound on [Radix-digit convolution](radix-digit-convolution.md): The digit of the first input x at position i, with weight (2^b)^i.
- $z$ (formal variable), bound on [Radix-digit convolution](radix-digit-convolution.md): A formal variable in which each input is written as a polynomial.
- $t$ (product coefficient position), bound on [Radix-digit convolution](radix-digit-convolution.md): The position of a coefficient of the product polynomial, running from 0 to 2m-2.
- $c_t$ (product coefficient), bound on [Radix-digit convolution](radix-digit-convolution.md): The integer coefficient of z^t in the product of the two digit polynomials.
- $s$ (source length), bound on [Gaussian resampling](gaussian-resampling.md): The number of entries in the source vector, which is the length of the transform being replaced.
- $t$ (resampled length), bound on [Gaussian resampling](gaussian-resampling.md): The number of entries in the resampled vector, a power of two greater than s.
- $\theta$ (relative gap), bound on [Gaussian resampling](gaussian-resampling.md): The relative gap t/s - 1 between the two lengths.
- $\alpha$ (width parameter), bound on [Gaussian resampling](gaussian-resampling.md): An integer that sets how wide the Gaussian weights are.
- $p$ (precision parameter), bound on [Gaussian resampling](gaussian-resampling.md): An integer precision parameter of the resampling identity.
- $P_s$ (length-s permutation), bound on [Gaussian resampling](gaussian-resampling.md): The permutation of length-s vectors that sends each position m to the position tm mod s.
- $P_t$ (length-t permutation), bound on [Gaussian resampling](gaussian-resampling.md): The permutation of length-t vectors defined by sending each position m to the position -sm mod t.
- $L$ (forward contraction), bound on [Gaussian resampling](gaussian-resampling.md): A linear contraction from length-s vectors to length-t vectors.
- $M$ (backward contraction), bound on [Gaussian resampling](gaussian-resampling.md): A linear contraction from length-t vectors back to length-s vectors.
- $S$ (first Gaussian map), bound on [Gaussian resampling](gaussian-resampling.md): A Gaussian-weighted map from length-s vectors to length-t vectors, used in the proof.
- $T$ (second Gaussian map), bound on [Gaussian resampling](gaussian-resampling.md): A second Gaussian-weighted map from length-s vectors to length-t vectors, used in the proof.
- $N$ (near-identity map), bound on [Gaussian resampling](gaussian-resampling.md): A map built from T and Gaussian corrections that lies within 1/2 of the identity.
- $\mathbb{D}$ (Gaussian dyadics), bound on [Gaussian dyadics](gaussian-dyadics.md): The set of Gaussian dyadics.
- $a$ (numerator), bound on [Gaussian dyadics](gaussian-dyadics.md): A Gaussian integer, the numerator of an element $a/2^k$ of $\mathbb{D}$.
- $k$ (denominator power), bound on [Gaussian dyadics](gaussian-dyadics.md): The number of factors of two in the denominator of an element of $\mathbb{D}$.
- $b$ (second numerator), bound on [Gaussian dyadics](gaussian-dyadics.md): A Gaussian integer, the numerator of a second element $b/2^l$ of $\mathbb{D}$.
- $l$ (second denominator power), bound on [Gaussian dyadics](gaussian-dyadics.md): The number of factors of two in the denominator of the second element $b/2^l$.
- $a$ (real part), bound on [Gaussian integer](gaussian-integer.md): The real part of a Gaussian integer, which is an integer.
- $b$ (imaginary part), bound on [Gaussian integer](gaussian-integer.md): The imaginary part of a Gaussian integer, which is an integer.
- $i$ (imaginary unit), bound on [Gaussian integer](gaussian-integer.md): The number whose square is $-1$.
- $\mathbb{Z}[i]$ (Gaussian integers), bound on [Gaussian integer](gaussian-integer.md): The set of all Gaussian integers.
- $P$ (matrix), bound on [Tensor product](tensor-product.md): A matrix whose entry in row i and column j is p_{ij}.
- $Q$ (second matrix), bound on [Tensor product](tensor-product.md): A second matrix, which is copied once for each entry of P in the tensor product P \otimes Q.
- $\otimes$ (tensor product), bound on [Tensor product](tensor-product.md): The operation that forms the block matrix P \otimes Q, also called the Kronecker product.
- $m$ (number of factors), bound on [Tensor product](tensor-product.md): The number of copies of P in the power P^{\otimes m}, which is also the number of address coordinates the operator acts on.
- $\beta$ (bilinear map), bound on [Bilinear map](bilinear-map.md): A map sending each pair of vectors, one from V and one from W, to a vector in U.
- $V$ (first input space), bound on [Bilinear map](bilinear-map.md): A vector space over the scalars, whose vectors form the first argument of the bilinear map.
- $W$ (second input space), bound on [Bilinear map](bilinear-map.md): A vector space over the scalars, whose vectors form the second argument of the bilinear map.
- $U$ (output space), bound on [Bilinear map](bilinear-map.md): A vector space over the scalars, containing the outputs of the bilinear map.
- $v$ (first argument), bound on [Bilinear map](bilinear-map.md): A vector of V, the first argument of the bilinear map.
- $w$ (second argument), bound on [Bilinear map](bilinear-map.md): A vector of W, the second argument of the bilinear map.
- $Q_0$ (radix), bound on [Carry propagation](carry-propagation.md): The number of values a digit can take, equal to 2 raised to the digit width b.
- $d_j$ (output digit), bound on [Carry propagation](carry-propagation.md): The j-th base-Q_0 digit of the output, an integer from 0 to Q_0 minus 1.
- $\gamma_j$ (carry), bound on [Carry propagation](carry-propagation.md): The amount carried into position j from the lower positions.
- $h$ (summed position), bound on [Carry propagation](carry-propagation.md): The position of an already processed coefficient, running over the summation range 0 to j minus 1.
- $m$ (modulus), bound on [Congruence](congruence-modulo.md): A positive integer, the modulus by which congruence is taken.
- $d$ (integer), bound on [Congruence](congruence-modulo.md): An integer, one of the two integers compared by congruence.
- $e$ (integer), bound on [Congruence](congruence-modulo.md): An integer, the other of the two integers compared by congruence.
- $w$ (class member), bound on [Congruence](congruence-modulo.md): An integer in the residue class of d modulo m.
- $\mathbb{F}_2$ (binary field), bound on [Binary field](binary-field.md): The field with the two elements 0 and 1, where addition is exclusive or and multiplication is AND.
- $m$ (selected bit count), bound on [Binary change of basis](binary-change-of-basis.md): The number of selected address bits that the change acts on, which is also the size of the square matrix M.
- $\mathbf b$ (selected bit column), bound on [Binary change of basis](binary-change-of-basis.md): The column vector of the m selected address bits, each an element of the binary field.
- $M$ (change matrix), bound on [Binary change of basis](binary-change-of-basis.md): The invertible m-by-m matrix over the binary field that specifies the change of basis.
- $\mathrm{GL}(m,\mathbb F_2)$ (invertible matrices), bound on [Binary change of basis](binary-change-of-basis.md): The set of invertible m-by-m matrices over the binary field.
- $\mathbf a$ (selected address), bound on [Binary change of basis](binary-change-of-basis.md): An address of the m selected bits, viewed as a column vector over the binary field.
- $P_M$ (address permutation), bound on [Binary change of basis](binary-change-of-basis.md): The permutation of addresses that moves the value at each address a to M a.
- $X$ (vector space), bound on [Bilinear form](bilinear-form.md): The vector space on which the bilinear form is defined.
- $\mathbb{K}$ (scalar field), bound on [Bilinear form](bilinear-form.md): The field of scalars over which the vector space is taken.
- $\xi$ (vector), bound on [Bilinear form](bilinear-form.md): A vector of $X$.
- $\eta$ (vector), bound on [Bilinear form](bilinear-form.md): A vector of $X$.
- $\langle \cdot,\cdot\rangle$ (bilinear form), bound on [Bilinear form](bilinear-form.md): The bilinear form, which assigns a scalar to each pair of vectors.
- $U$ (subspace), bound on [Bilinear form](bilinear-form.md): A subspace of $X$.
- $U^\perp$ (orthogonal complement), bound on [Bilinear form](bilinear-form.md): The set of vectors of $X$ orthogonal to every vector of $U$.
- $M$ (form matrix), bound on [Bilinear form](bilinear-form.md): The matrix of the bilinear form in the chosen coordinates.
- $J$ (all-one matrix), bound on [Bilinear form](bilinear-form.md): The matrix all of whose entries are 1.
- $t_T$ (triple indicator vector), bound on [Bilinear form](bilinear-form.md): The indicator vector of the triple $T$, with entries 1 at the positions of $T$ and 0 elsewhere.
- $\xi_1$ (first coordinate), bound on [Bilinear form](bilinear-form.md): The first coordinate of a vector $\xi$ in $\mathbb{Q}^2$.
- $\xi_2$ (second coordinate), bound on [Bilinear form](bilinear-form.md): The second coordinate of a vector $\xi$ in $\mathbb{Q}^2$.
- $K$ (scalar field), bound on [Line spanned by a vector](line-spanned-by-vector.md): The field of scalars over which the vector space E is taken.
- $E$ (vector space), bound on [Line spanned by a vector](line-spanned-by-vector.md): The vector space over K in which the line lies.
- $v$ (generating vector), bound on [Line spanned by a vector](line-spanned-by-vector.md): A nonzero vector of E whose scalar multiples form the line.
- $\lambda$ (scalar multiplier), bound on [Line spanned by a vector](line-spanned-by-vector.md): A scalar in K, an element of the scalar field, used to scale v.
- $\langle v\rangle$ (line spanned by v), bound on [Line spanned by a vector](line-spanned-by-vector.md): The set of all scalar multiples of v, a one-dimensional subspace of E.
- $M$ (modulus), bound on [Centered residue](centered-residue.md): A positive integer, the modulus of the residue with respect to which the centered residue is taken.
- $m$ (integer), bound on [Centered residue](centered-residue.md): An integer whose residue class modulo M is represented by its centered residue.
- $f$ (first input sequence), bound on [Cyclic convolution](cyclic-convolution.md): The first of the two sequences, of length s.
- $g$ (second input sequence), bound on [Cyclic convolution](cyclic-convolution.md): The second of the two sequences, of length s.
- $w$ (formal variable), bound on [Cyclic convolution](cyclic-convolution.md): A formal variable in which a sequence is written as a polynomial, never evaluated.
- $\ast$ (cyclic convolution), bound on [Cyclic convolution](cyclic-convolution.md): The cyclic convolution operation, whose result f \ast g is the sequence with entries (f \ast g)_k.
- $\Phi$ (coefficient layout map), bound on [Cyclic convolution](cyclic-convolution.md): The map of the paper's Section 9.3 from a cyclic convolution to a multidimensional one.
- $QFt$ (middle transform), bound on [Cyclic convolution](cyclic-convolution.md): The middle factor of the paper's transform, a Fourier-type transform given by equation (35).
- $d$ (number of cyclic coordinates), bound on [Cyclic coordinate](cyclic-coordinate.md): The number of cyclic coordinates of an array, a positive integer.
- $\ell$ (coordinate index), bound on [Cyclic coordinate](cyclic-coordinate.md): The index naming one cyclic coordinate, running from 1 to d.
- $L_\ell$ (cyclic length), bound on [Cyclic coordinate](cyclic-coordinate.md): The number of positions along cyclic coordinate ℓ before indices wrap around.
- $\beta$ (integer to invert), bound on [Modular inverse](modular-inverse.md): The integer whose inverse modulo $M$ is sought.
- $M$ (modulus), bound on [Modular inverse](modular-inverse.md): A positive integer, the modulus of the congruence.
- $\mu$ (modular inverse), bound on [Modular inverse](modular-inverse.md): The integer with $\beta\mu$ congruent to $1$ modulo $M$.
- $\nu$ (multiple of the modulus), bound on [Modular inverse](modular-inverse.md): The integer with $\beta\mu - 1 = \nu M$ in a solution of the congruence.
- $S$ (product of the lengths), bound on [Modular inverse](modular-inverse.md): The product $M_1 M_2 \cdots$ of all the lengths, the order of the cyclic group.
- $M_i$ (axis length), bound on [Modular inverse](modular-inverse.md): The $i$-th of the pairwise coprime lengths, the number of entries along one cyclic axis.
- $\pi_i$ (prefix product), bound on [Modular inverse](modular-inverse.md): The product of the lengths before the $i$-th, so $\pi_1 = 1$.
- $\mu_i$ (exponent of an axis), bound on [Modular inverse](modular-inverse.md): The inverse of $\pi_i$ modulo $M_i$, used as the exponent of $\xi_i$.
- $\xi$ (cyclic generator), bound on [Modular inverse](modular-inverse.md): A generator of a cyclic group of order $S$, which the map sends to $\prod_i \xi_i^{\mu_i}$.
- $\xi_i$ (axis generator), bound on [Modular inverse](modular-inverse.md): A generator of the cyclic group of order $M_i$ on the $i$-th axis.
- $x$ (sequence), bound on [Limit inferior](limit-inferior.md): A sequence of real numbers $x_1, x_2, x_3, \dots$ whose $k$-th term is $x_k$.
- $k$ (term index), bound on [Limit inferior](limit-inferior.md): The position of a term in the sequence $x$.
- $m$ (starting position), bound on [Limit inferior](limit-inferior.md): A position in the sequence from which a tail infimum is taken.
- $y$ (tail infimum), bound on [Limit inferior](limit-inferior.md): The smallest term of the sequence at or after position $m$, written $y_m$.
- $\varepsilon$ (tolerance), bound on [Limit inferior](limit-inferior.md): A positive real number used as a threshold for how small a term must be.
- $n$ (input length), bound on [Limit inferior](limit-inferior.md): The number of bits in each input, which is the index of the running-time function.
- $A$ (fixed machine), bound on [Limit inferior](limit-inferior.md): A fixed multiplication machine whose running time is studied.
- $T_A$ (running time), bound on [Limit inferior](limit-inferior.md): The worst-case running time of machine $A$ on inputs of $n$ bits, as a function of $n$.
- $c$ (positive constant), bound on [Limit inferior](limit-inferior.md): A positive real constant in the lower bound and its negation.
- $N$ (input length threshold), bound on [Limit inferior](limit-inferior.md): A threshold on input length, below which the bound is not required.
- $\kappa$ (exponent saving), bound on [The n log n optimality conjecture](n-log-n-conjecture.md): A specific positive constant; the main theorem's time bound has logarithmic exponent $1-\kappa$.
- $n$ (input bit length), bound on [Fixed-tape machine model](fixed-tape-model.md): The number of bits in each of the two input integers.
- $T_A$ (running time), bound on [Fixed-tape machine model](fixed-tape-model.md): The running time of machine A as a function of the input length n.
- $A$ (multiplication machine), bound on [Fixed-tape machine model](fixed-tape-model.md): A fixed Turing machine that multiplies two integers, whose running time is T_A.
- $c_A$ (lower-bound constant), bound on [Fixed-tape machine model](fixed-tape-model.md): A positive constant, depending on machine A, in the lower bound T_A(n) >= c_A n log n.
- $N_A$ (threshold input length), bound on [Fixed-tape machine model](fixed-tape-model.md): The input length from which the lower bound for machine A holds.
- $\Psi$ (generic linear map), bound on [Transform identity with retained permutations](transform-identity.md): A linear map whose norm bound defines a contraction.
- $F_s$ (length-s transform), bound on [Transform identity with retained permutations](transform-identity.md): The normalized discrete Fourier transform of length s, that is F_q at q = s.
- $F_t$ (length-t transform), bound on [Transform identity with retained permutations](transform-identity.md): The normalized discrete Fourier transform of length t, that is F_q at q = t.
- $w$ (second vector), bound on [Transform identity with retained permutations](transform-identity.md): A second complex vector of length q, paired with u in the permutation and product formulas.
- $B_0$ (backward contraction), bound on [Transform identity with retained permutations](transform-identity.md): The linear contraction from length-t vectors to length-s vectors that appears in the identity.
- $S$ (Gaussian map S), bound on [Transform identity with retained permutations](transform-identity.md): A Gaussian-weighted map from length-s vectors to length-t vectors, used in the source's resampling identity.
- $T$ (Gaussian map T), bound on [Transform identity with retained permutations](transform-identity.md): A second Gaussian-weighted map from length-s vectors to length-t vectors, used in the source's resampling identity.
- $N$ (near-identity operator), bound on [Transform identity with retained permutations](transform-identity.md): The map from length-s vectors to themselves given by selecting, applying T and scaling, which is close to the identity.
- $\Gamma$ (coordinate selection), bound on [Transform identity with retained permutations](transform-identity.md): The map from length-t vectors to length-s vectors that picks the coordinates nearest to tj/s.
- $\Lambda$ (diagonal scaling), bound on [Transform identity with retained permutations](transform-identity.md): A diagonal map on length-s vectors, with the Gaussian weights on its diagonal.
- $L$ (left inverse of T), bound on [Transform identity with retained permutations](transform-identity.md): The map Lambda N^{-1} Gamma from length-t vectors to length-s vectors, which is a left inverse of T.
- $\Pi$ (coordinate permutation), bound on [Transform identity with retained permutations](transform-identity.md): A permutation that rearranges the entries of a vector.
- $\cdot$ (entrywise product), bound on [Transform identity with retained permutations](transform-identity.md): The product of two vectors of the same length taken entry by entry.
- $R$ (retained source permutation), bound on [Transform identity with retained permutations](transform-identity.md): The source permutation that is kept in the formula instead of being executed, and cancels across the convolution.
- $\nu$ (axis index), bound on [Padded transform box](padded-transform-box.md): The index of an axis, running from 1 to d.
- $d$ (axis count), bound on [Padded transform box](padded-transform-box.md): The number of axes of the transform, the count of coordinate directions along which the data is laid out.
- $w_\nu$ (valid length), bound on [Padded transform box](padded-transform-box.md): The number of data entries along axis nu, the valid length of that axis.
- $M_\nu$ (padded length), bound on [Padded transform box](padded-transform-box.md): The padded length of axis nu, at least its valid length, to which the axis is padded with zero entries.
- $Q$ (box size), bound on [Padded transform box](padded-transform-box.md): The number of entries of the padded transform box, the product of the padded lengths of all axes.
- $\mathbf{e}$ (box address), bound on [Padded transform box](padded-transform-box.md): An address naming one entry of the padded box, a tuple of one coordinate per axis.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Cyclic convolution](cyclic-convolution.md): The product of two sequences in which indices wrap around modulo the sequence length.
  Shown as: Normalized cyclic convolution *<predicate>* Cyclic convolution
- [Discrete Fourier transform](discrete-fourier-transform.md): The map sending a vector of q values to its q values weighted by powers of a q-th root of unity, normalized by 1/q.
  Shown as: Normalized cyclic convolution *<predicate>* Discrete Fourier transform
- [Transform identity with retained permutations](transform-identity.md): The Gaussian resampling identity in which the source and target coordinate permutations are kept as part of the formula, so that they cancel across a convolution instead of being executed as sorts.
  Shown as: Normalized cyclic convolution *<predicate>* Transform identity with retained permutations
- [Gaussian resampling](gaussian-resampling.md): A technique that replaces a Fourier transform of arbitrary length by transforms whose axis lengths are powers of two, using Gaussian weights to move between the two sets of frequencies.
  Shown as: Normalized cyclic convolution *<predicate>* Gaussian resampling

## Pages that build on this one

- Bluestein's chirp identity: An identity that rewrites a Fourier transform as a cyclic convolution multiplied by chirp factors, so that it can be computed with convolution.
- Normalization scales: The known powers of two and transform lengths by which a computed product is multiplied to undo the normalizing factors of the transforms and the digit scaling.

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
- [Exact integer multiplication](exact-integer-multiplication.md)
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
- [Butterfly](butterfly.md)
- [Radix-digit convolution](radix-digit-convolution.md)
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
- [Padded transform box](padded-transform-box.md)
- [Logical bit volume](logical-bit-volume.md)
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

- "Here ∗ denotes cyclic convolution on the" (paper)

## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- [Transform identity with retained permutations](transform-identity.md) is now a prerequisite: link it where "target permutation" is used: "including its target permutation"
- Explain "middle transform" inline where it is used: "rewrites the middle transform" (its concept depends on this page, so it cannot be a prerequisite)
- The reader cannot follow this step: "The source states the rule for the unnormalized product, writing the length as $S$:" (The page gives the rule F_s(f*g) = s(F_s f)(F_s g) only by citing a source; its one numerical example checks it for s = 2 alone, so the reader cannot check the general rule from the page.)
- The reader cannot follow this step: "so the transform step reduces to one cyclic convolution and two pointwise phase multiplications" (The reader cannot tell what the transform step is or why it reduces to one cyclic convolution and two pointwise multiplications; the page does not derive this.)
- Say what $s$ denotes where it is first used: the page uses it before saying so in "For sequences $f$ and $g$ of length $s$, the entries of $f \ast g$ are"
- "target" is the concept [Gaussian resampling](gaussian-resampling.md), now a prerequisite: link it where the term is used.

## Previous version (revise it)

It has 382 words. Fix the problems by restructuring rather than appending: keep the rewrite within 477 words, a quarter more, unless a problem cannot be fixed without more. Pages that grow with every repair stop being self-contained explanations of one concept.

A normalized cyclic convolution is a scaling of the [Cyclic convolution](cyclic-convolution.md) $f \ast g$ by $1/s$. Its purpose is to make a [Discrete Fourier transform](discrete-fourier-transform.md) turn convolution into a pointwise product. On the way to the target, [Bluestein's chirp identity](bluestein-chirp-identity.md) rewrites the middle transform, including its target permutation, as a normalized cyclic convolution.

For sequences $f$ and $g$ of length $s$, the entries of $f \ast g$ are
$$(f \ast g)_k = \sum_{j=0}^{s-1} f_j\, g_{(k-j) \bmod s}, \qquad 0 \le k \le s-1,$$
where $f_j$ is the entry of $f$ at position $j$, and the index $(k-j) \bmod s$ wraps around modulo $s$.

We write $f \circledast g$ for the normalized cyclic convolution of $f$ and $g$, the cyclic convolution $f \ast g$ divided by $s$.
$$f \circledast g = \frac{1}{s}\,(f \ast g).$$

Let $F_s$ be the normalized discrete Fourier transform of length $s$, which is the $F_q$ of the transform page with $q = s$. A normalized cyclic convolution is turned into pointwise products by the [Discrete Fourier transform](discrete-fourier-transform.md) $F_s$, as the rule below states. The source states the rule for the unnormalized product, writing the length as $S$: <cite data-source="paper">The normalized convolution rule is Fs (u ∗ v) = S(Fs u) · (Fs v), while Fs+ Fs = I/S.</cite>

With $S = s$, the rule says $F_s(f \ast g) = s\,(F_s f)(F_s g)$. Dividing both sides by $s$ gives the form used here:
$$F_s(f \circledast g)_k = (F_s f)_k\,(F_s g)_k, \qquad 0 \le k \le s-1.$$
That is, the transform of the normalized product is the pointwise product of the transforms of $f$ and $g$, meaning entry $k$ of one multiplied by entry $k$ of the other.

Take $s = 2$, $f = (1, 2)$ and $g = (3, 4)$. Then $(f \ast g)_0 = 1 \cdot 3 + 2 \cdot 4 = 11$ and $(f \ast g)_1 = 1 \cdot 4 + 2 \cdot 3 = 10$, so $f \circledast g = (11/2,\ 5)$. For $s = 2$ the transform is $F_2 u = \left(\frac{u_0 + u_1}{2},\ \frac{u_0 - u_1}{2}\right)$, so $F_2 f = (3/2,\ -1/2)$ and $F_2 g = (7/2,\ -1/2)$, whose entrywise product is $(21/4,\ 1/4)$. Directly, $F_2(f \circledast g) = \left(\frac{11/2 + 5}{2},\ \frac{11/2 - 5}{2}\right) = (21/4,\ 1/4)$, as the rule predicts.

This is the step the source uses. It states that <cite data-source="paper">The factor QFt in (35) can be computed from a cyclic convolution and two pointwise phase multiplications.</cite> so the transform step reduces to one cyclic convolution and two pointwise phase multiplications.

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

Write the body to `exegenius/tasks/0316-write-normalized-cyclic-convolution.answer.md` and the JSON to `exegenius/tasks/0316-write-normalized-cyclic-convolution.answer.json`, then run `exegenius submit 0316-write-normalized-cyclic-convolution` in the project directory. If submit rejects the answer, fix the answer and submit again.
