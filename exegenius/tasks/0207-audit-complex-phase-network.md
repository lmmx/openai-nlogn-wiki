# exegenius task 0207-audit-complex-phase-network

Project directory: `/mnt/openai-nlogn` (paths below are relative to it)

Audit one page of an explanatory wiki on behalf of a specific reader. Use only this task file: do not read the sources, other pages or any other file.

The reader knows exactly the concepts listed as known, together with what the reader profile states. Everything else that you know, the reader does not know: treat it as unknown to them, however elementary it seems to you. You are simulating that reader's lack of knowledge, so use your own knowledge only to recognise what the reader is missing.

Symbols: account for every symbol in the page's mathematics, each once, saying where the reader learns what it denotes:
- `here`: the page says what it denotes; quote the sentence that says it. A use in an example ("take $r = 4$") or a range ("a power of two $r$") does not say what $r$ denotes or counts. If the page uses the symbol before that sentence, submit records that the meaning comes too late.
- `page`: an earlier page binds it, as listed under "Symbols bound on earlier pages".
- `concept`: the name of a known concept contains it and binds it, as listed under that concept. A symbol in a known concept's name that is listed with no meaning is not known.
- `background`: standard notation the reader profile covers; say what covers it.
- `unbound`: nothing tells the reader what it denotes.
Submit checks that each symbol is in the page's mathematics, that each quote is on the page and contains the symbol, and that the named page or concept binds it.

Terms and steps: a term or step is followable if the reader knows it, the page explains it, or the page links it to another wiki page. Report every term or step on the page that the reader cannot follow:
- term: a named concept the reader does not know, which the page neither explains nor links.
- step: an inference, calculation or claim the reader cannot check from what the page gives.

Copy each quote from the page exactly, character for character, and keep it short: submit rejects quotes it cannot find on the page. Do not report anything the reader can follow. Answer with an empty list of gaps if the reader can follow the whole page.

## Reader profile

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

## Known concepts

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

## Symbols bound on earlier pages

- $a$ (first input sequence), bound on `convolution`: The first input sequence, of length n.
- $b$ (second input sequence), bound on `convolution`: The second input sequence, of length n.
- $i$ (input position in a), bound on `convolution`: The position of an entry of a in a product a_i b_j.
- $c$ (convolution), bound on `convolution`: The convolution of a and b, a sequence of length 2n-1.
- $u$ (field width), bound on `address-field`: The number of address bits in each of the two fields being interchanged, a count.
- $a$ (input bit), bound on `xor`: The first of the two bits that an XOR combines.
- $b$ (input bit), bound on `xor`: The second of the two bits that an XOR combines.
- $F$ (field), bound on `linear-algebra-basics`: The field of scalars over which vector spaces are taken.
- $x$ (vector), bound on `linear-algebra-basics`: A vector in a vector space over $F$.
- $c$ (scalar), bound on `linear-algebra-basics`: A scalar, an element of the field $F$.
- $m$ (coordinate count), bound on `linear-algebra-basics`: The number of coordinates in each vector of $F^m$, which is the dimension of $F^m$.
- $A$ (matrix), bound on `linear-algebra-basics`: An $m\times m$ matrix with entries in $F$.
- $I$ (identity matrix), bound on `linear-algebra-basics`: The matrix with ones on the diagonal and zeros elsewhere.
- $B$ (candidate inverse matrix), bound on `linear-algebra-basics`: A matrix that is a two-sided inverse of the matrix $A$ when $A$ is invertible.
- $v$ (vertex), bound on `linear-algebra-basics`: A vertex of the network in the paper, at which a frame is placed.
- $g$ (logical array), bound on `linear-algebra-basics`: The array of values that the network computes on, before its frame is applied.
- $M$ (matrix of a frame), bound on `linear-algebra-basics`: A matrix that determines the frame $\Phi_M$.
- $v$ (vertex), bound on `linear-network-frames`: A source, gate or sink of the network.
- $g$ (logical array), bound on `linear-network-frames`: The array a wire is meant to represent before any frame is applied.
- $G$ (pointwise linear gate), bound on `linear-network-frames`: A gate that combines its input arrays separately at each address.
- $t$ (gate input count), bound on `linear-network-frames`: The number of input arrays a gate takes.
- $w$ (input wire), bound on `linear-network-frames`: An input wire of the network.
- $r$ (output role), bound on `linear-network-frames`: An output role of the network.
- $\rho$ (role permutation), bound on `linear-network-frames`: The permutation of roles that the scalar network realises, sending input role $w$ to output role $\rho(w)$.
- $a$ (path start vertex), bound on `endpoint-operator`: The first of three vertices on a path through the network.
- $b$ (path middle vertex), bound on `endpoint-operator`: The middle of three vertices on a path through the network.
- $c$ (path end vertex), bound on `endpoint-operator`: The last of three vertices on a path through the network.
- $w$ (input role), bound on `endpoint-operator`: An input role of the network, whose route starts at its source vertex.
- $\rho$ (role permutation), bound on `endpoint-operator`: The signed permutation of roles realised by the scalar network, sending each input role to an output role.
- $x$ (sequence), bound on `limit-inferior`: A sequence of real numbers $x_1, x_2, x_3, \dots$ whose $k$-th term is $x_k$.
- $m$ (starting position), bound on `limit-inferior`: A position in the sequence from which a tail infimum is taken.
- $\varepsilon$ (tolerance), bound on `limit-inferior`: A positive real number used as a threshold for how small a term must be.
- $A$ (fixed machine), bound on `limit-inferior`: A fixed multiplication machine whose running time is studied.
- $c$ (positive constant), bound on `limit-inferior`: A positive real constant in the lower bound and its negation.
- $A$ (multiplication machine), bound on `fixed-tape-model`: A fixed Turing machine that multiplies two integers, whose running time is T_A.
- $x$ (first input), bound on `exact-integer-multiplication`: The first input, a binary string of length n.
- $b$ (log-length parameter), bound on `cost-table`: The rounded-up base-2 logarithm of the input length $n$.
- $p$ (working precision), bound on `cost-table`: The precision parameter $p = 6b$, which sets the coefficient width up to a constant factor.
- $V$ (logical volume), bound on `cost-table`: The number of logical bits in the padded box, $V = Tp$.
- $d$ (axis count), bound on `cost-table`: The number of axes of the padded box.
- $r$ (longest axis length), bound on `cost-table`: The number of cells along the longest axis of the padded box.
- $c$ (chunk exponent), bound on `cost-table`: A fixed positive rational exponent that sets $K$ relative to $d$.
- $i$ (position index), bound on `cyclic-shift`: A position in the block, numbered from 0 to L-1.
- $V$ (stored bit volume), bound on `cyclic-shift`: The number of bits held in the array being shifted.
- $v$ (vertex), bound on `network-gate-terminal`: A gate or terminal of the network, which carries the frame $D_v$.
- $u$ (field width), bound on `address-interchange`: The number of bits in each field.
- $V$ (stored volume), bound on `address-interchange`: The number of stored bits in the array.
- $a$ (first field), bound on `address-interchange`: The first of the two fields being interchanged.
- $b$ (second field), bound on `address-interchange`: The second of the two fields being interchanged.
- $m$ (recursion base), bound on `address-interchange`: A fixed base in which the field width is written, so that each recursion level divides the width by m.
- $s$ (child call count), bound on `address-interchange`: The number of calls that one call makes on smaller fields.
- $\mathbb{F}_2$ (binary field), bound on `binary-field`: The field with the two elements 0 and 1, where addition is exclusive or and multiplication is AND.
- $v$ (generating vector), bound on `line-spanned-by-vector`: A nonzero vector of E whose scalar multiples form the line.
- $\lambda$ (scalar multiplier), bound on `line-spanned-by-vector`: A scalar in K, an element of the scalar field, used to scale v.
- $a$ (real part), bound on `gaussian-integer`: The real part of a Gaussian integer, which is an integer.
- $b$ (imaginary part), bound on `gaussian-integer`: The imaginary part of a Gaussian integer, which is an integer.
- $i$ (imaginary unit), bound on `gaussian-integer`: The number whose square is $-1$.
- $P$ (matrix), bound on `tensor-product`: A matrix whose entry in row i and column j is p_{ij}.
- $\otimes$ (tensor product), bound on `tensor-product`: The operation that forms the block matrix P \otimes Q, also called the Kronecker product.
- $m$ (number of factors), bound on `tensor-product`: The number of copies of P in the power P^{\otimes m}, which is also the number of address coordinates the operator acts on.
- $m$ (matrix size), bound on `matrix-rank`: The number of rows of a square matrix M, which is also its number of columns.
- $M$ (rational matrix), bound on `matrix-rank`: A rational matrix with m rows and m columns.
- $p$ (fractional precision), bound on `truncation`: The number of fractional binary places kept, so the grid spacing is $2^{-p}$.
- $m$ (number of subsets), bound on `union-bound`: The number of subsets $E_1, \dots, E_m$ of $\Omega$ whose union is bounded.
- $w$ (key width), bound on `stable-radix-sort`: The number of bits in each key.
- $M$ (record count), bound on `stable-radix-sort`: The number of records being sorted.
- $i$ (bit index), bound on `stable-radix-sort`: The position of a key bit, counting from 0 at the least significant end; pass $i$ sorts by bit $k_i$.
- $q$ (address before the move), bound on `destination-rank`: The address of a record before the move.
- $M$ (record count), bound on `destination-rank`: The number of records in the stream.
- $m$ (selected bit count), bound on `binary-change-of-basis`: The number of selected address bits that the change acts on, which is also the size of the square matrix M.
- $M$ (change matrix), bound on `binary-change-of-basis`: The invertible m-by-m matrix over the binary field that specifies the change of basis.
- $a$ (numerator), bound on `gaussian-dyadics`: A Gaussian integer, the numerator of an element $a/2^k$ of $\mathbb{D}$.
- $b$ (second numerator), bound on `gaussian-dyadics`: A Gaussian integer, the numerator of a second element $b/2^l$ of $\mathbb{D}$.
- $q$ (transform length), bound on `discrete-fourier-transform`: The number of coordinates of each vector the transform acts on.
- $u$ (input vector), bound on `discrete-fourier-transform`: A vector of q complex numbers, the input of the transform.
- $m$ (input index), bound on `discrete-fourier-transform`: An integer index of input coordinates, running from 0 to q-1.
- $b$ (digit width), bound on `radix-digit-convolution`: The number of bits in each digit, a positive integer.
- $m$ (digit count), bound on `radix-digit-convolution`: The number of digits in each input, the count of blocks of b bits.
- $i$ (digit position), bound on `radix-digit-convolution`: The position of a digit in an input, running from 0 to m-1.
- $t$ (product coefficient position), bound on `radix-digit-convolution`: The position of a coefficient of the product polynomial, running from 0 to 2m-2.
- $s$ (axis index), bound on `multidimensional-transform`: The index of an axis, running from 1 to D.
- $M$ (entry count), bound on `multidimensional-transform`: The number of entries of the array, the product of the axis lengths.
- $X$ (input array), bound on `multidimensional-transform`: The input array, on which the transform acts.
- $m$ (input position), bound on `multidimensional-transform`: A position in the input array, with each coordinate below its axis length.
- $r$ (record length), bound on `synthetic-transforms`: The number of complex coefficients in a record, a power of two at least 2.
- $m$ (coefficient position), bound on `synthetic-transforms`: The position of a coefficient in a record, running from $0$ to $r-1$.
- $s$ (shift amount), bound on `synthetic-transforms`: The number of places a shift moves each coefficient of a record, with $0 \le s < 2r$.
- $t$ (transform length), bound on `synthetic-transforms`: The number of entries in the transform, a power of two dividing $2r$.
- $s$ (source length), bound on `gaussian-resampling`: The number of entries in the source vector, which is the length of the transform being replaced.
- $t$ (resampled length), bound on `gaussian-resampling`: The number of entries in the resampled vector, a power of two greater than s.
- $p$ (precision parameter), bound on `gaussian-resampling`: An integer precision parameter of the resampling identity.
- $M$ (backward contraction), bound on `gaussian-resampling`: A linear contraction from length-t vectors back to length-s vectors.
- $m$ (power count), bound on `polynomial-ring-mod-yr-plus-1`: A positive integer, the number of factors of a root of unity whose product is 1.
- $R$ (polynomial ring), bound on `polynomial-ring`: The quotient ring of complex polynomials in y modulo the multiples of f.
- $m$ (modulus degree), bound on `polynomial-ring`: The degree of f, which is also the number of coefficients in the representative of each element of R.
- $X$ (array of complex values), bound on `array-norm`: A finite array of complex values, the argument of the norm.
- $w$ (array entry), bound on `array-norm`: A single entry of the array X, which is a complex number.
- $m$ (input coordinate count), bound on `linear-contraction`: The number of coordinates of the input vectors of a linear map, a positive integer.
- $w$ (input vector), bound on `linear-contraction`: A vector in the input space of a linear map, with m complex coordinates.
- $m$ (modulus), bound on `congruence-modulo`: A positive integer, the modulus by which congruence is taken.
- $d$ (integer), bound on `congruence-modulo`: An integer, one of the two integers compared by congruence.
- $w$ (class member), bound on `congruence-modulo`: An integer in the residue class of d modulo m.
- $g$ (packed polynomial g), bound on `signed-packing`: A polynomial in $y$ with $r$ integer coefficients, the second input that is packed.
- $p$ (coefficient bit bound), bound on `signed-packing`: The number of bits in the magnitude bound on each coefficient, so that $|f_j| \le 2^p$.
- $B$ (block base), bound on `signed-packing`: The base $2^{4p}$ at which the polynomials are evaluated, so that each coefficient occupies a block of $4p$ bits.
- $c$ (centered residue), bound on `signed-packing`: The unique integer in $[-B/2, B/2)$ that is congruent to $f(B)\,g(B)$ modulo $B$.
- $M$ (modulus), bound on `centered-residue`: A positive integer, the modulus of the residue with respect to which the centered residue is taken.
- $m$ (integer), bound on `centered-residue`: An integer whose residue class modulo M is represented by its centered residue.
- $g$ (second input sequence), bound on `cyclic-convolution`: The second of the two sequences, of length s.
- $w$ (formal variable), bound on `cyclic-convolution`: A formal variable in which a sequence is written as a polynomial, never evaluated.
- $d$ (number of cyclic coordinates), bound on `cyclic-coordinate`: The number of cyclic coordinates of an array, a positive integer.
- $V$ (first input space), bound on `bilinear-map`: A vector space over the scalars, whose vectors form the first argument of the bilinear map.
- $U$ (output space), bound on `bilinear-map`: A vector space over the scalars, containing the outputs of the bilinear map.
- $v$ (first argument), bound on `bilinear-map`: A vector of V, the first argument of the bilinear map.
- $w$ (second argument), bound on `bilinear-map`: A vector of W, the second argument of the bilinear map.
- $X$ (vector space), bound on `bilinear-form`: The vector space on which the bilinear form is defined.
- $U$ (subspace), bound on `bilinear-form`: A subspace of $X$.
- $M$ (form matrix), bound on `bilinear-form`: The matrix of the bilinear form in the chosen coordinates.
- $\cap$ (intersection), bound on `subspace-labels`: The vectors lying in both subspaces.
- $C_U$ (label frame), bound on `subspace-labels`: The frame operator at a vertex whose label is U.
- $I$ (identity), bound on `subspace-labels`: The identity operator (or matrix).
- $v$ (basis vector), bound on `subspace-labels`: A vector of the orthonormal basis of the residual, the shift used by the kernel.
- $X_v$ (shift operator), bound on `subspace-labels`: The shift that moves a function of addresses by v.
- $x$ (address), bound on `subspace-labels`: An address, a binary point at which array entries are indexed; the letter changes meaning here.
- $P_U$ (projection), bound on `subspace-labels`: The projection onto U along U-perp.
- $q_U$ (phase exponent), bound on `subspace-labels`: The integer mod 4 given by the weight of the projected address.
- $\mathrm{wt}$ (Hamming weight), bound on `subspace-labels`: The number of ones in a binary vector.
- $H$ (Hadamard matrix), bound on `subspace-labels`: The normalized 2 by 2 Hadamard matrix.
- $m$ (address length), bound on `subspace-labels`: The number of address bits, so addresses lie in F_2^m.
- $X$ (bank X), bound on `subset-intersection-network`: One of the two banks of scalars, indexed by triples of triples.
- $\mathbb{F}_2$ (binary field), bound on `subset-intersection-network`: The field with two elements, whose arithmetic is mod 2.
- $I$ (identity matrix), bound on `subset-intersection-network`: The h by h identity matrix.

## Pages in the wiki

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
- [Ring homomorphism and isomorphism](ring-homomorphism.md)
- [Mixed-radix digits](mixed-radix-digits.md)
- [Chinese-remainder map](chinese-remainder-map.md)
- [Prime source lengths](prime-source-lengths.md)
- [Carry propagation](carry-propagation.md)
- [Convolution over the polynomial ring](polynomial-ring-convolution.md)
- [Exact coefficient recovery](recovery-and-error.md)
- [Integer multiplication below n log n](main-theorem.md)

## Page to audit (`complex-phase-network`)

````markdown
# Complex phase network

The complex phase network is a [subset-intersection network](subset-intersection-network.md) whose wires carry arrays of complex values, and whose frame change on each edge is a product of two-point kernels. It supplies the frame identity that the [simultaneous butterfly layer](simultaneous-butterfly-layer.md) uses to apply a butterfly on several address bits at once, one step toward the [main theorem](main-theorem.md).

The complex phase network is obtained from the [subset-intersection network](subset-intersection-network.md) by replacing each wire's scalar with an array of complex values, and it changes the frame of those arrays along each edge by a product of two-point kernels. The network takes its addresses from the [binary field](binary-field.md). Here $\mathbb{F}_2$ is the field with two elements $0$ and $1$, and $x \in \mathbb{F}_2^m$ denotes an address, where $m$ is the number of coordinates of $x$. Here $x$ is not the input string of earlier pages.

Let $I$ be the identity matrix and $i$ the imaginary unit. Let $H = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$ be the normalized Hadamard matrix. Let $X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ be the bit-flip matrix, which swaps the two coordinates of a vector.

$\mathrm{diag}_x(c(x))$ is the diagonal operator on functions of $x$ that multiplies the value at each $x$ by $c(x)$, and $\mathrm{diag}(1,i)$ is the $2\times 2$ diagonal matrix with entries $1$ and $i$. Set $\lambda = \frac{1+i}{2}$ and $\mu = \frac{1-i}{2}$. The two-point kernel is $M = H\,\mathrm{diag}(1,i)\,H = \lambda I + \mu X$. Since $\lambda^2+\mu^2=0$ and $2\lambda\mu=1$, squaring gives $M^2 = X$. Also $H^2 = I$, and $M^{-1} = \mu I + \lambda X$, because $(\lambda I+\mu X)(\mu I+\lambda X) = 2\lambda\mu I + (\lambda^2+\mu^2)X = I$.

The complex phase network is indexed by [subspace labels](subspace-labels.md), with one binary label at each vertex. Each label $U$ is a subspace of $\mathbb{F}_2^m$.

For binary vectors $u, v \in \mathbb{F}_2^m$, the dot product $u\cdot v$ is the parity of $|\mathrm{supp}(u)\cap\mathrm{supp}(v)|$, where $\mathrm{supp}(u)$ is the set of coordinates at which $u$ is 1. Let $\mathrm{wt}(v)$ be the Hamming weight of a binary vector $v$, the number of its coordinates equal to $1$, read as an integer. Thus $v\cdot v$ is the parity of $\mathrm{wt}(v)$. Let $P_U$ be the projection onto $U$ for this dot product. For a label $U$, let $q_U(x)$ be the Hamming weight of $P_Ux$ modulo 4, a value in $\{0,1,2,3\}$.

The complex phase network computes its frames by the [tensor power](tensor-product.md) $H^{\otimes m}$ of $H$, where $\otimes$ is the Kronecker product. The frame at a vertex with label $U$ is
$$C_U = H^{\otimes m}\,\mathrm{diag}_x\big(i^{q_U(x)}\big)\,H^{\otimes m}.$$
Since $(H^{\otimes m})^2 = I$, the inverse is $C_U^{-1} = H^{\otimes m}\,\mathrm{diag}_x\big(i^{-q_U(x)}\big)\,H^{\otimes m}$. Each entry of $H^{\otimes m}$ is $\pm 2^{-m/2}$, so each entry of $C_U$ is $2^{-m}$ times a sum of terms $\pm i^{q_U(x)}$, and the same holds for $C_U^{-1}$. The complex phase network has coefficients in [Gaussian dyadics](gaussian-dyadics.md): each entry of $C_U$ and of its inverse is a Gaussian integer divided by $2^m$.

On an edge from label $U$ to label $V$, where $V$ is the head label, the frame change is $C_V C_U^{-1}$, and $C_V$ is given by the same formula with $V$ in place of $U$. Since diagonal operators multiply pointwise and $(H^{\otimes m})^2 = I$,
$$C_V C_U^{-1} = H^{\otimes m}\,\mathrm{diag}_x\big(i^{q_V(x)-q_U(x)}\big)\,H^{\otimes m}.$$

Write $A \perp B$ when $A$ and $B$ are subspaces with $A\cap B = 0$, every vector of $A$ is orthogonal to every vector of $B$, and $A+B$ is their sum. On an increasing edge $V = U \perp R$, and on a decreasing edge $U = V \perp R$, where $R$ is the orthogonal residual of the edge. Let $\mathcal{B}$ be an orthonormal basis of $R$, with vectors $v$ satisfying $v\cdot v = 1$ and $v\cdot w = 0$ for distinct $v, w \in \mathcal{B}$. A zero residual has the empty basis.

For binary vectors $\sigma, \rho$, the coordinates in both supports are counted by both weights but are $0$ in $\sigma+\rho$, so $\mathrm{wt}(\sigma+\rho) = \mathrm{wt}(\sigma)+\mathrm{wt}(\rho)-2|\mathrm{supp}(\sigma)\cap\mathrm{supp}(\rho)|$, with the sum taken coordinatewise over $\mathbb{F}_2$. So if $\sigma\cdot\rho = 0$, then $\mathrm{wt}(\sigma+\rho) \equiv \mathrm{wt}(\sigma)+\mathrm{wt}(\rho) \pmod 4$, because the last term is then a multiple of 4.

Let $x$ be an address on an increasing edge. The projection onto $R$ is $P_Rx = \sum_{v\in\mathcal{B}}(v\cdot x)\,v$, and $P_Vx = P_Ux + P_Rx$ with $P_Ux\cdot P_Rx = 0$, because $U\perp R$. The weight identity gives $\mathrm{wt}(P_Vx)\equiv\mathrm{wt}(P_Ux)+\mathrm{wt}(P_Rx)$ modulo 4. The summands $(v\cdot x)\,v$ are pairwise orthogonal, so applying the identity one summand at a time gives $\mathrm{wt}(P_Rx)\equiv\sum_{v\in\mathcal{B}}[v\cdot x]\,\mathrm{wt}(v)$ modulo 4, where $[b]\in\{0,1\}$ is the integer representative of $b\in\mathbb{F}_2$. Hence
$$q_V(x)-q_U(x)\equiv\sum_{v\in\mathcal{B}}\mathrm{wt}(v)\,[v\cdot x] \pmod 4,$$
and the right side is negated on a decreasing edge, where the roles of $U$ and $V$ swap.

Each $\mathrm{wt}(v)$ is odd, since $v\cdot v = 1$. Define $\varepsilon_v\in\{1,-1\}$ by $\varepsilon_v\equiv\mathrm{wt}(v)$ modulo 4 on an increasing edge and $\varepsilon_v\equiv-\mathrm{wt}(v)$ on a decreasing edge, so the sign carries the edge direction. Then $i^{q_V(x)-q_U(x)} = \prod_{v\in\mathcal{B}} i^{\varepsilon_v[v\cdot x]}$.

For one $v$, write $\varepsilon = \varepsilon_v$. The function $i^{\varepsilon[v\cdot x]}$ equals
$$\frac{1+i\varepsilon}{2}+\frac{1-i\varepsilon}{2}(-1)^{v\cdot x},$$
since both sides are $1$ when $v\cdot x = 0$ and both equal $i\varepsilon$ when $v\cdot x = 1$. The sign $(-1)^{v\cdot x}$ is a product of single-coordinate signs over $\mathrm{supp}(v)$, and $H\,\mathrm{diag}(1,-1)\,H = X$ on each such coordinate. The translation $X_v$ is defined by $(X_v\phi)(x) = \phi(x+v)$, where $\phi$ is a function on addresses. Conjugating by $H^{\otimes m}$ therefore gives
$$H^{\otimes m}\,\mathrm{diag}_x\big(i^{\varepsilon[v\cdot x]}\big)\,H^{\otimes m} = \tfrac{1+i\varepsilon}{2}\,I + \tfrac{1-i\varepsilon}{2}\,X_v.$$
Write $M_v = \lambda I + \mu X_v$. This is $M_v$ when $\varepsilon = 1$ and $\mu I + \lambda X_v = M_v^{-1}$ when $\varepsilon = -1$, since $X_v^2 = I$.

Diagonal operators multiply pointwise, so $H^{\otimes m}\mathrm{diag}(F)H^{\otimes m}\cdot H^{\otimes m}\mathrm{diag}(G)H^{\otimes m} = H^{\otimes m}\mathrm{diag}(FG)H^{\otimes m}$. Hence the frame change on the edge is a product of one kernel $M_v^{\pm 1}$ for each $v \in \mathcal{B}$. Along a route of edges the intermediate frames cancel, so telescoping gives $M^{\otimes m}$ on every role.

Take $m=1$ and the labels $\{0\}$ and $\mathbb{F}_2$. For $\{0\}$, $q_{\{0\}}(x)=0$, so $C_{\{0\}} = I$. For $\mathbb{F}_2$, $P_{\mathbb{F}_2}$ is the identity, so $q_{\mathbb{F}_2}(x)=x$ and $C_{\mathbb{F}_2}=M$. The edge from $\{0\}$ to $\mathbb{F}_2$ is increasing, with residual $R=\mathbb{F}_2$ and basis $\mathcal{B}=\{1\}$, since $\mathrm{wt}(1)=1$ gives $\varepsilon=1$. Its frame change is $C_{\mathbb{F}_2}C_{\{0\}}^{-1} = M = \lambda I+\mu X_1$. Here $X_1 = X$, which swaps the two values of $\phi$.
````

## Answer

The answer is one JSON object following this schema:

```json
{
  "$defs": {
    "Anchor": {
      "description": "Where the reader learns what a symbol denotes.",
      "oneOf": [
        {
          "additionalProperties": false,
          "description": "This page says what the symbol denotes. A use in an example (\"take $r = 4$\") does not.",
          "properties": {
            "kind": {
              "const": "here",
              "type": "string"
            },
            "quote": {
              "description": "The sentence that says it, copied exactly from the page.",
              "type": "string"
            }
          },
          "required": [
            "kind",
            "quote"
          ],
          "type": "object"
        },
        {
          "additionalProperties": false,
          "description": "An earlier page binds it: one listed under \"Symbols bound on earlier pages\".",
          "properties": {
            "kind": {
              "const": "page",
              "type": "string"
            },
            "page": {
              "description": "Id of that page.",
              "type": "string"
            }
          },
          "required": [
            "kind",
            "page"
          ],
          "type": "object"
        },
        {
          "additionalProperties": false,
          "description": "The name of a known concept contains it and binds it, as listed under the known\nconcepts.",
          "properties": {
            "concept": {
              "description": "Id of that concept.",
              "type": "string"
            },
            "kind": {
              "const": "concept",
              "type": "string"
            }
          },
          "required": [
            "kind",
            "concept"
          ],
          "type": "object"
        },
        {
          "additionalProperties": false,
          "description": "Standard notation the reader profile covers, such as $n$ for an input size.",
          "properties": {
            "kind": {
              "const": "background",
              "type": "string"
            },
            "note": {
              "description": "What in the reader profile covers it.",
              "type": "string"
            }
          },
          "required": [
            "kind",
            "note"
          ],
          "type": "object"
        },
        {
          "additionalProperties": false,
          "description": "Nothing tells the reader what it denotes.",
          "properties": {
            "kind": {
              "const": "unbound",
              "type": "string"
            },
            "note": {
              "description": "What the reader cannot tell.",
              "type": "string"
            },
            "quote": {
              "description": "Where it is first used, copied exactly from the page.",
              "type": "string"
            }
          },
          "required": [
            "kind",
            "quote",
            "note"
          ],
          "type": "object"
        }
      ]
    },
    "Gap": {
      "additionalProperties": false,
      "properties": {
        "kind": {
          "$ref": "#/$defs/GapKind"
        },
        "note": {
          "description": "Why this reader cannot follow it.",
          "type": "string"
        },
        "quote": {
          "description": "The passage on the page where the gap occurs, copied exactly (a phrase or one sentence).",
          "type": "string"
        },
        "term": {
          "description": "The term, or a short label for the step.",
          "type": "string"
        }
      },
      "required": [
        "term",
        "quote",
        "kind",
        "note"
      ],
      "type": "object"
    },
    "GapKind": {
      "oneOf": [
        {
          "const": "term",
          "description": "A named concept the reader does not know, which the page neither explains nor links.",
          "type": "string"
        },
        {
          "const": "step",
          "description": "An inference, calculation or claim the reader cannot check from what the page gives.",
          "type": "string"
        }
      ]
    },
    "SymbolUse": {
      "additionalProperties": false,
      "properties": {
        "anchor": {
          "$ref": "#/$defs/Anchor"
        },
        "symbol": {
          "description": "The symbol in LaTeX, as it appears in the page's mathematics, without dollar signs.",
          "type": "string"
        }
      },
      "required": [
        "symbol",
        "anchor"
      ],
      "type": "object"
    }
  },
  "additionalProperties": false,
  "properties": {
    "gaps": {
      "description": "Every term or step the reader cannot follow; empty if the reader can follow them all.",
      "items": {
        "$ref": "#/$defs/Gap"
      },
      "type": "array"
    },
    "symbols": {
      "description": "Every symbol in the page's mathematics, each once, with where the reader learns what\nit denotes. Empty only if the page has no mathematics.",
      "items": {
        "$ref": "#/$defs/SymbolUse"
      },
      "type": "array"
    }
  },
  "required": [
    "symbols",
    "gaps"
  ],
  "title": "AuditAnswer",
  "type": "object"
}
```

Write the answer to `exegenius/tasks/0207-audit-complex-phase-network.answer.json`, then run `exegenius submit 0207-audit-complex-phase-network` in the project directory. If submit rejects the answer, fix the answer and submit again.
