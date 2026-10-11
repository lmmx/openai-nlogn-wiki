# exegenius task 0340-write-established-multiplier

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
- Bluestein's chirp identity (also: chirp identity)
- Synthetic polynomial transforms (also: Nussbaumer polynomial transforms, polynomial transforms, Nussbaumer and Quandalle)
- Polynomial ring modulo y^r + 1 (also: negacyclic polynomial ring)
  - $y$ (polynomial variable): The indeterminate of the polynomial ring, whose powers act as roots of unity.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Phase twist
- Subspace labels (also: binary label)
- Linear networks and frames (also: roles, frames, network of wires and gates, network, vertex, edge, source and sink vertices, Edge change)
- Subset-intersection network (also: three-element subset network, subset-intersection network and complex phase network, side and central wires, gather and scatter, scalar network)
- Address-field interchange (also: power-width interchange, tape procedure for interchanging address chunks, address-field interchange procedure, field interchanges)
- Address shear (also: shear of address pairs, Matrix shear)
- Rank-saving recursion (also: recursive saving)
- Gaussian dyadics
- Complex phase network (also: phase-frame identity, complex variant, orthogonal residual of an edge)
- Simultaneous butterfly layer (also: selected bits, two-point operator on selected bits)
- Transform layout (also: transform layout and packed selected-bit addition)
- Transform identity with retained permutations (also: target permutation, coordinate permutations)
- Carry propagation (also: carry scan)
- Address field (also: address chunk, chunk, target chunk, selected address bits)
- Transform axis (also: axis, remaining axes, reduction axis)
- Linear algebra basics (also: linear algebra: invertible linear operator, matrix, inverse, matrix, linear map, usual axioms)
- Bilinear map (also: bilinear product, bilinear contraction)
- Bilinear form (also: bilinear space, orthogonality, bilinear form and orthogonality, bilinear space and bilinear form)
- Binary field (also: finite field F2, F_2, finite field F_2, copy step)
- Binary change of basis (also: residual basis of directions)
- Bit procedure
- Butterfly (also: two-point butterfly map, two-point map, Butterfly operation)
- Congruence (also: congruence modulo B, modulo, modulo arithmetic)
- Centered residue
- Cyclic shift (also: controlled cyclic shift, signed shifts)
- Convolution
- Coprime (also: gcd, pairwise coprime, coprime (gcd))
- Running time cost (also: cost, linear-cost update, bit-complexity bound)
- Cost table (also: chirp and twist)
- Stable radix sort (also: label-and-sort operations)
- Destination rank (also: prefix-slot move, move, extracted records, rectangular routine, hole, destination key)
- Endpoint operator
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
- Normalized cyclic convolution
- Normalization scales (also: normalizations and known scales)
- Numerical layer (also: butterfly layers, layer)
- Opposite transform (also: opposite-sign transform)
- Padded transform box
- Payload (also: record)
- Phase factor (also: phase factors and scalar corrections)
- Polynomial ring (also: polynomial suffix)
- Matrix rank (also: rational rank, rank of a shear, Row reduction and pivots)
- Ring homomorphism and isomorphism (also: ring homomorphism and ring isomorphism)
- Schoolbook multiplication (also: the paper's construction)
- Scratch storage (also: scratch values, scratch chunk, scratch wires, forward schedule, linear-readout version)
- Tensor product (also: tensor power)
- Transform round (also: butterfly round, current recursive length, level the round processes)
- Truncation
- Exclusive or (also: XOR)
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
- Bit construction
- Complex construction
- Chinese remainder theorem (also: CRT)
- Cyclic group (also: cyclic group of order S)
- Diagonal scaling
- Eigenvalue
- Extended real numbers
- Family parameter
- Frequency domain
- Incidence
- Independence of events
- Mathematical induction (also: induction)
- Integer
- Prime number (also: prime)
- Logical bit volume
- Ring
- Orthogonal complement
- Pointwise product
- Projection along a subspace
- Root of unity (also: roots of unity)
- Stream (also: fixed track, scan, role stream, stream position)
- Tape procedure
- Schönhage–Strassen multiplication (also: Schönhage and Strassen, Schönhage–Strassen bound)

## This page

Concept: Established O(n log n) multiplier
Gloss: The known fixed-tape integer multiplier running in O(n log n) time, used here only as a black-box subroutine.
Also called: Harvey–van der Hoeven multiplier, der Hoeven

## Where the argument relies on this page

- Convolution on the remaining axes over the polynomial ring is computed by two forward synthetic transforms, a pointwise product, an opposite transform, and packed integer products. (on [Convolution over the polynomial ring](polynomial-ring-convolution.md))
- The parameters can be chosen so that every term in the cost table is $O(n(\lg n)^{1-\kappa})$ for $\kappa = 2^{-182}$, which gives the bound of the theorem.

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
- $\circledast$ (normalized cyclic convolution), bound on [Normalized cyclic convolution](normalized-cyclic-convolution.md): The operation sending two length-$s$ sequences $f$ and $g$ to their cyclic convolution divided by $s$.
- $\chi$ (chirp vector), bound on [Bluestein's chirp identity](bluestein-chirp-identity.md): The vector of chirp factors, whose entries are unit-modulus phases $\chi_m = e^{\pi i m^2/q}$.
- $m$ (chirp position), bound on [Bluestein's chirp identity](bluestein-chirp-identity.md): The integer position at which a chirp entry is taken, which may be negative or exceed q-1.
- $w$ (scaled input), bound on [Bluestein's chirp identity](bluestein-chirp-identity.md): The input vector u with each entry divided by the corresponding chirp entry.
- $\zeta$ (twist root), bound on [Phase twist](phase-twist.md): The root of unity $e^{\pi i/r}$ of order $2r$, whose powers are the twist factors.
- $j$ (coefficient position), bound on [Phase twist](phase-twist.md): The position of a coefficient in the record, running from 0 to r-1.
- $k$ (first record position), bound on [Phase twist](phase-twist.md): The position of the coefficient taken from the first record in a product.
- $l$ (second record position), bound on [Phase twist](phase-twist.md): The position of the coefficient taken from the second record in a product.
- $\sigma$ (digit scale), bound on [Normalization scales](normalization-scales.md): The power of two 2^{-b-2} by which each radix-2^b digit is multiplied when it is stored.
- $E$ (fixed bilinear space), bound on [Subspace labels](subspace-labels.md): The fixed bilinear space in which every label is a subspace.
- $\langle\xi,\eta\rangle$ (bilinear form), bound on [Subspace labels](subspace-labels.md): The bilinear form of E; two vectors are orthogonal when it is zero.
- $U^\perp$ (orthogonal complement), bound on [Subspace labels](subspace-labels.md): The set of vectors of E orthogonal to every vector of U.
- $\subseteq$ (inclusion), bound on [Subspace labels](subspace-labels.md): V is contained in U: every vector of V lies in U.
- $\supseteq$ (containment), bound on [Subspace labels](subspace-labels.md): U contains V, the same relation as V inside U.
- $\cap$ (intersection), bound on [Subspace labels](subspace-labels.md): The vectors lying in both subspaces.
- $\oplus$ (direct sum), bound on [Subspace labels](subspace-labels.md): The direct sum: each vector is uniquely a vector of the first summand plus one of the second.
- $C_U$ (label frame), bound on [Subspace labels](subspace-labels.md): The frame operator at a vertex whose label is U.
- $\lambda_0$ (kernel coefficient), bound on [Subspace labels](subspace-labels.md): A Gaussian dyadic coefficient of the translation kernel.
- $\lambda_1$ (kernel coefficient), bound on [Subspace labels](subspace-labels.md): A Gaussian dyadic coefficient of the translation kernel.
- $I$ (identity), bound on [Subspace labels](subspace-labels.md): The identity operator (or matrix).
- $v$ (basis vector), bound on [Subspace labels](subspace-labels.md): A vector of the orthonormal basis of the residual, the shift used by the kernel.
- $X_v$ (shift operator), bound on [Subspace labels](subspace-labels.md): The shift that moves a function of addresses by v.
- $x$ (address), bound on [Subspace labels](subspace-labels.md): An address, a binary point at which array entries are indexed; the letter changes meaning here.
- $f$ (function of addresses), bound on [Subspace labels](subspace-labels.md): A function of addresses; the letter changes meaning here.
- $P_U$ (projection), bound on [Subspace labels](subspace-labels.md): The projection onto U along U-perp.
- $q_U$ (phase exponent), bound on [Subspace labels](subspace-labels.md): The integer mod 4 given by the weight of the projected address.
- $\mathrm{wt}$ (Hamming weight), bound on [Subspace labels](subspace-labels.md): The number of ones in a binary vector.
- $H$ (Hadamard matrix), bound on [Subspace labels](subspace-labels.md): The normalized 2 by 2 Hadamard matrix.
- $m$ (address length), bound on [Subspace labels](subspace-labels.md): The number of address bits, so addresses lie in F_2^m.
- $\mathbb{Q}$ (rationals), bound on [Subspace labels](subspace-labels.md): The field of rational numbers.
- $h$ (ground set size), bound on [Subspace labels](subspace-labels.md): The number of elements of the ground set.
- $J$ (all-ones matrix), bound on [Subspace labels](subspace-labels.md): The h by h matrix with every entry 1.
- $\top$ (transpose), bound on [Subspace labels](subspace-labels.md): Transpose of a vector or matrix.
- $T$ (triple), bound on [Subspace labels](subspace-labels.md): A three-element subset of the ground set.
- $t_T$ (indicator vector), bound on [Subspace labels](subspace-labels.md): The 0-1 vector with entry 1 on the triple T.
- $S$ (triple), bound on [Subspace labels](subspace-labels.md): A second three-element subset, used for inner products.
- $t_S$ (indicator vector), bound on [Subspace labels](subspace-labels.md): The 0-1 vector of the triple S.
- $|A|$ (size), bound on [Subspace labels](subspace-labels.md): The number of elements of the set A.
- $\mathcal{K}$ (triples), bound on [Subset-intersection network](subset-intersection-network.md): The set of all three-element subsets of the ground set.
- $X$ (bank X), bound on [Subset-intersection network](subset-intersection-network.md): One of the two banks of scalars, indexed by triples of triples.
- $Y$ (bank Y), bound on [Subset-intersection network](subset-intersection-network.md): The second of the two banks of scalars, indexed by triples of triples.
- $\beta$ (bank index), bound on [Subset-intersection network](subset-intersection-network.md): A triple of triples that indexes one entry of a bank.
- $\xi$ (source vector), bound on [Subset-intersection network](subset-intersection-network.md): The vector of source-bank entries on one line, indexed by triples.
- $\eta$ (target vector), bound on [Subset-intersection network](subset-intersection-network.md): The vector of target-bank entries on one line, indexed by triples.
- $\mathbb{F}_2$ (binary field), bound on [Subset-intersection network](subset-intersection-network.md): The field with two elements, whose arithmetic is mod 2.
- $W_{ST}$ (side wire), bound on [Subset-intersection network](subset-intersection-network.md): The auxiliary wire attached to an ordered neighbouring pair of triples.
- $C_\ell$ (central wire), bound on [Subset-intersection network](subset-intersection-network.md): The auxiliary wire attached to one element of the ground set.
- $\ell$ (ground element), bound on [Subset-intersection network](subset-intersection-network.md): An element of the ground set, indexing a central wire.
- $I$ (identity matrix), bound on [Subset-intersection network](subset-intersection-network.md): The h by h identity matrix.
- $I$ (identity matrix), bound on [Complex phase network](complex-phase-network.md): The identity operator, which leaves every vector or function unchanged.
- $i$ (imaginary unit), bound on [Complex phase network](complex-phase-network.md): The imaginary unit, with $i^2 = -1$.
- $H$ (normalized Hadamard matrix), bound on [Complex phase network](complex-phase-network.md): The $2\times 2$ matrix with entries $\pm 1/\sqrt{2}$, a symmetric matrix squaring to $I$.
- $X$ (bit-flip matrix), bound on [Complex phase network](complex-phase-network.md): The matrix swapping the two coordinates of a vector.
- $\mathrm{diag}$ (diagonal operator), bound on [Complex phase network](complex-phase-network.md): The operator that multiplies the value at each address by a given factor.
- $\lambda$ (constant lambda), bound on [Complex phase network](complex-phase-network.md): The constant $(1+i)/2$.
- $\mu$ (constant mu), bound on [Complex phase network](complex-phase-network.md): The constant $(1-i)/2$.
- $M$ (two-point kernel), bound on [Complex phase network](complex-phase-network.md): The $2\times 2$ matrix $\lambda I+\mu X$ acting on one address bit.
- $\otimes$ (Kronecker product), bound on [Complex phase network](complex-phase-network.md): The Kronecker (tensor) product of matrices, so $H^{\otimes m}$ is the $m$-fold tensor power of $H$.
- $\mathbb{F}_2$ (binary field), bound on [Complex phase network](complex-phase-network.md): The field with two elements $0$ and $1$.
- $x$ (address), bound on [Complex phase network](complex-phase-network.md): A binary vector in $\mathbb{F}_2^m$ at which the arrays are evaluated.
- $\cdot$ (dot product), bound on [Complex phase network](complex-phase-network.md): The parity of the number of coordinates where two binary vectors are both 1.
- $\mathrm{supp}$ (support), bound on [Complex phase network](complex-phase-network.md): The set of coordinates at which a binary vector is 1.
- $\mathrm{wt}$ (Hamming weight), bound on [Complex phase network](complex-phase-network.md): The number of coordinates of a binary vector equal to 1, read as an integer.
- $P_U$ (projection onto U), bound on [Complex phase network](complex-phase-network.md): The projection onto the label $U$ for the dot product.
- $q_U$ (weight modulo 4), bound on [Complex phase network](complex-phase-network.md): The Hamming weight of $P_Ux$ modulo 4, a value in $\{0,1,2,3\}$.
- $\perp$ (orthogonal sum), bound on [Complex phase network](complex-phase-network.md): The sum of two orthogonal subspaces with trivial intersection.
- $R$ (orthogonal residual), bound on [Complex phase network](complex-phase-network.md): The subspace by which an edge's two labels differ, orthogonal to the smaller one.
- $\mathcal{B}$ (orthonormal basis), bound on [Complex phase network](complex-phase-network.md): A basis of the residual whose vectors $v$ satisfy $v\cdot v=1$ and are pairwise orthogonal.
- $v$ (binary vector), bound on [Complex phase network](complex-phase-network.md): A binary vector; the vectors of the orthonormal basis $\mathcal{B}$ are such vectors.
- $\sigma$ (binary vector), bound on [Complex phase network](complex-phase-network.md): A binary vector used in the weight identity.
- $\rho$ (binary vector), bound on [Complex phase network](complex-phase-network.md): A second binary vector used in the weight identity.
- $\varepsilon$ (edge sign), bound on [Complex phase network](complex-phase-network.md): The sign in $\{1,-1\}$ that encodes each basis vector's weight and the edge direction.
- $[b]$ (indicator), bound on [Complex phase network](complex-phase-network.md): The integer 0 or 1 representing a binary value $b$.
- $X_v$ (translation), bound on [Complex phase network](complex-phase-network.md): The operator shifting a function on addresses by the binary vector $v$.
- $\phi$ (function on addresses), bound on [Complex phase network](complex-phase-network.md): An arbitrary function on binary addresses.
- $M_v$ (basis kernel), bound on [Complex phase network](complex-phase-network.md): The kernel $\lambda I+\mu X_v$ attached to a basis vector $v$.
- $u$ (field width), bound on [Address-field interchange](address-interchange.md): The number of bits in each field.
- $V$ (stored volume), bound on [Address-field interchange](address-interchange.md): The number of stored bits in the array.
- $\tau$ (bound exponent), bound on [Address-field interchange](address-interchange.md): A fixed number below one, the exponent in the running-time bound.
- $a$ (first field), bound on [Address-field interchange](address-interchange.md): The first of the two fields being interchanged.
- $b$ (second field), bound on [Address-field interchange](address-interchange.md): The second of the two fields being interchanged.
- $\oplus$ (XOR operator), bound on [Address-field interchange](address-interchange.md): Bitwise exclusive or.
- $m$ (recursion base), bound on [Address-field interchange](address-interchange.md): A fixed base in which the field width is written, so that each recursion level divides the width by m.
- $k$ (level count), bound on [Address-field interchange](address-interchange.md): The number of recursion levels, log base m of the field width.
- $W$ (volume divisor), bound on [Address-field interchange](address-interchange.md): The number of equal pieces the volume is cut into at each level.
- $s$ (child call count), bound on [Address-field interchange](address-interchange.md): The number of calls that one call makes on smaller fields.
- $j$ (level depth), bound on [Address-field interchange](address-interchange.md): The number of levels below the top call.
- $a$ (input bit), bound on [Exclusive or](xor.md): The first of the two bits that an XOR combines.
- $b$ (input bit), bound on [Exclusive or](xor.md): The second of the two bits that an XOR combines.
- $\oplus$ (exclusive or), bound on [Exclusive or](xor.md): The XOR operation: $a \oplus b$ is the bitwise sum modulo 2 of the bits $a$ and $b$, which is 1 exactly when they differ.
- $a$ (path start vertex), bound on [Endpoint operator](endpoint-operator.md): The first of three vertices on a path through the network.
- $b$ (path middle vertex), bound on [Endpoint operator](endpoint-operator.md): The middle of three vertices on a path through the network.
- $c$ (path end vertex), bound on [Endpoint operator](endpoint-operator.md): The last of three vertices on a path through the network.
- $w$ (input role), bound on [Endpoint operator](endpoint-operator.md): An input role of the network, whose route starts at its source vertex.
- $\rho$ (role permutation), bound on [Endpoint operator](endpoint-operator.md): The signed permutation of roles realised by the scalar network, sending each input role to an output role.
- $\varepsilon_w$ (route sign), bound on [Endpoint operator](endpoint-operator.md): The scalar sign carried by the route from input role $w$.
- $m$ (field count), bound on [Address shear](address-shear.md): The number of address fields in each vector, a count.
- $b$ (digit count), bound on [Address shear](address-shear.md): The number of radix-$q$ digits in each field, a count; the letter changes meaning from earlier pages.
- $q$ (prime modulus), bound on [Address shear](address-shear.md): A fixed odd prime, the base of the digits; the letter changes meaning from the transform length.
- $H$ (address field H), bound on [Address shear](address-shear.md): The vector of $m$ fields that the shear increases.
- $D$ (address field D), bound on [Address shear](address-shear.md): The vector of $m$ fields that the shear adds and leaves unchanged.
- $M$ (shear matrix), bound on [Address shear](address-shear.md): A fixed rational $m \times m$ matrix that determines the shear.
- $a$ (rational rank), bound on [Address shear](address-shear.md): The number of interchanges that the shear with matrix $M$ needs, equal to the rational rank of $M$.
- $h$ (current value of H), bound on [Address shear](address-shear.md): The value of the single field $H$ when $m = 1$.
- $d$ (current value of D), bound on [Address shear](address-shear.md): The value of the single field $D$ when $m = 1$.
- $E_1$ (lower-triangular factor), bound on [Address shear](address-shear.md): An invertible lower-triangular rational matrix in the factorization of $M$.
- $E_2$ (lower-triangular factor), bound on [Address shear](address-shear.md): An invertible lower-triangular rational matrix in the factorization of $M$.
- $\Pi$ (partial permutation matrix), bound on [Address shear](address-shear.md): A $0/1$ matrix with exactly $a$ ones, at most one in each row and column, in the factorization of $M$.
- $i$ (row index), bound on [Address shear](address-shear.md): The row of a one in $\Pi$, which names an $H$ field.
- $j$ (column index), bound on [Address shear](address-shear.md): The column of a one in $\Pi$, which names a $D$ field.
- $D$ (axis count), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The number of axes on which the layer acts, one axis per chunk; it counts the selected bits.
- $K$ (chunk width), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The number of bits in each chunk, where a chunk is a run of consecutive address bits.
- $\rho$ (selected offset), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The position of the selected bit within each chunk, counted from the least significant end.
- $\mu$ (first value), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The first of the two values of a pair, the first input of the two-point map.
- $\nu$ (second value), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The second of the two values of a pair, the second input of the two-point map.
- $H_0$ (two-point map), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The map sending a pair of values to their half-sum and half-difference.
- $I$ (identity matrix), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The $2\times 2$ identity matrix, with ones on the diagonal and zeros elsewhere.
- $L$ (layout permutation), bound on [Transform layout](transform-layout.md): The explicit permutation of record addresses that places the selected bits in the required chunks.
- $\ell$ (log record length), bound on [Transform layout](transform-layout.md): The base-two logarithm of $r$, which is the number of address bits in a long axis.
- $d$ (axis bound), bound on [Numerical layer](numerical-layer.md): An upper bound on the number D of selected axes in one layer, a count of axes.
- $\lambda'$ (cost exponent), bound on [Numerical layer](numerical-layer.md): A fixed exponent below one in the layer cost O(V d^{\lambda'}).
- $W$ (role count), bound on [Numerical layer](numerical-layer.md): The number of roles in the network, a count of the wire roles among which rows are distributed.
- $W$ (wire count), bound on [Rank-saving recursion](rank-saving-recursion.md): The number of wires in the network, which is also the number of roles among which the rows are distributed.
- $\ell$ (call parameter), bound on [Rank-saving recursion](rank-saving-recursion.md): The parameter of a call, counting the selected axes of a numerical layer or the digits of an address field.
- $s$ (smaller-call count), bound on [Rank-saving recursion](rank-saving-recursion.md): The total number of smaller calls that one call makes.
- $\mu$ (source dimension sum), bound on [Rank-saving recursion](rank-saving-recursion.md): The sum of the dimensions of the source labels.
- $L$ (lost dimension), bound on [Rank-saving recursion](rank-saving-recursion.md): The total dimension lost along decreasing edges, where the head label is smaller than the tail label.
- $\gamma$ (cost per volume), bound on [Rank-saving recursion](rank-saving-recursion.md): The cost of a call at parameter $\ell$ divided by its volume.
- $i$ (axis index), bound on [Transform round](transform-round.md): The index of a participating axis, running over the D participating axes.
- $\ell_i$ (current axis length), bound on [Transform round](transform-round.md): The number of entries that axis i holds at the level the round processes, a power of two.
- $\beta_i$ (branch bit), bound on [Transform round](transform-round.md): The bit, 0 or 1, that the round writes on axis i to record which output of the butterfly an entry is.
- $\nu_i$ (twiddle index), bound on [Transform round](transform-round.md): The index of the twiddle on axis i, with 0 <= nu_i < ell_i/2.
- $\Lambda$ (parallel butterfly), bound on [Transform round](transform-round.md): The tensor product of the two-point map over all participating axes, applied to the selected bits in one pass.
- $\Gamma_\eta$ (recordwise twiddle), bound on [Transform round](transform-round.md): The operation that multiplies each record at an address by the power y^eta of the polynomial variable.
- $\eta$ (twiddle exponent), bound on [Transform round](transform-round.md): The exponent of y at an address, an integer taken modulo 2r.
- $b$ (log-length parameter), bound on [Cost table](cost-table.md): The rounded-up base-2 logarithm of the input length $n$.
- $p$ (working precision), bound on [Cost table](cost-table.md): The precision parameter $p = 6b$, which sets the coefficient width up to a constant factor.
- $T$ (padded box size), bound on [Cost table](cost-table.md): The power of two that sets the number of cells in the padded box.
- $V$ (logical volume), bound on [Cost table](cost-table.md): The number of logical bits in the padded box, $V = Tp$.
- $d$ (axis count), bound on [Cost table](cost-table.md): The number of axes of the padded box.
- $K$ (chunk width), bound on [Cost table](cost-table.md): The number of bits in each address chunk.
- $r$ (longest axis length), bound on [Cost table](cost-table.md): The number of cells along the longest axis of the padded box.
- $\ell$ (log axis length), bound on [Cost table](cost-table.md): The base-2 logarithm of $r$.
- $\epsilon$ (size exponent), bound on [Cost table](cost-table.md): A fixed positive rational exponent that sets $d$ and $K$.
- $c$ (chunk exponent), bound on [Cost table](cost-table.md): A fixed positive rational exponent that sets $K$ relative to $d$.
- $\tau$ (exchange exponent), bound on [Cost table](cost-table.md): A fixed rational exponent between zero and one in the cost of chunk exchanges.
- $\lambda'$ (butterfly exponent), bound on [Cost table](cost-table.md): A fixed rational exponent below one in the cost of a simultaneous butterfly round.
- $\delta$ (arithmetic exponent), bound on [Cost table](cost-table.md): A fixed rational exponent in the powers of $p$ that bound the arithmetic costs.
- $\alpha$ (line cost factor), bound on [Cost table](cost-table.md): The factor, of order $p^{1/4+\epsilon/2}$, in the cost of the Gaussian line maps.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Exact integer multiplication](exact-integer-multiplication.md): Given binary strings x and y of length n, output the 2n-bit binary representation of their product.
  Shown as: Established O(n log n) multiplier *<predicate>* Exact integer multiplication
- [Cost table](cost-table.md): The list of separate running-time terms of an algorithm, each a power of the input size, whose sum bounds the total time.
  Shown as: Established O(n log n) multiplier *<predicate>* Cost table

## Pages that build on this one

- Signed coefficient packing: Encoding polynomial coefficients, including negative ones, as one large integer by fixed-width blocks, so that polynomial multiplication becomes integer multiplication.

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
- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Transform axis](transform-axis.md)
- [Multidimensional transform](multidimensional-transform.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md)
- [Butterfly](butterfly.md)
- [Radix-digit convolution](radix-digit-convolution.md)
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

- "Calls to the established O(n log n)" (paper)

## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The reader cannot follow this step: "Its running time on $N$-bit inputs is, which is $O(N\log N)$ for $N\ge 2$, because $\log(2N)=\log N+1$" (The running time is never stated (the sentence reads 'is, which is'), and the identity log(2N) = log N + 1 needs a logarithm base the page does not give, so the claim cannot be checked.)
- The reader cannot follow this step: "so the construction never calls itself" (The reason given, that the multiplier is not the new algorithm, is only asserted; the reader cannot check that the construction never calls itself from what the page gives, and the sentence ends in a dangling 'and.')
- Say what $\log$ denotes where it is first used (for a size or count, what it counts): "The established $O(n\log n)$ multiplier solves" (The page never says what log denotes or which base it uses, and logarithms are not in the reader profile.)

## Previous version (revise it)

It has 203 words. Fix the problems by restructuring rather than appending: keep the rewrite within 253 words, a quarter more, unless a problem cannot be fixed without more. Pages that grow with every repair stop being self-contained explanations of one concept.

The established $O(n\log n)$ multiplier solves [exact integer multiplication](exact-integer-multiplication.md). Here $N$ is the number of bits in each input, and the multiplier runs in $O(N\log N)$ time on two $N$-bit inputs. The [main theorem](main-theorem.md) is proved by a construction that calls this multiplier as a subroutine, so its cost is one term of the new algorithm's [cost table](cost-table.md).

The source calls it <cite data-source="paper">the fixed-tape integer multiplier of Harvey and van</cite> der Hoeven. A fixed-tape machine is a Turing machine whose alphabet and number of tapes do not depend on the input length. Its running time on $N$-bit inputs is <cite data-source="paper">O(N log(2N )) on N -bit inputs</cite>, which is $O(N\log N)$ for $N\ge 2$, because $\log(2N)=\log N+1$.

For example, take $N=4$, $x=1011$ (value $11$) and $y=0110$ (value $6$). The product is $66$, so the multiplier outputs the $2N$-bit string $01000010$.

The construction packs each polynomial's coefficients into one large integer, multiplies two such integers with this multiplier, and unpacks the result (see [signed coefficient packing](signed-packing.md)). The proof states this step as <cite data-source="paper">with an established integer multiplier.</cite>

The multiplier is not the new algorithm, so the construction never calls itself: it makes only ordinary subroutine calls to this multiplier, and <cite data-source="paper">they do not invoke the improved theorem recursively</cite>. Each call is charged the multiplier's $O(N\log N)$ cost on its own inputs, taken as given, and these charges are summed in the cost table.

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

Write the body to `exegenius/tasks/0340-write-established-multiplier.answer.md` and the JSON to `exegenius/tasks/0340-write-established-multiplier.answer.json`, then run `exegenius submit 0340-write-established-multiplier` in the project directory. If submit rejects the answer, fix the answer and submit again.
