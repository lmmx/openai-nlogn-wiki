# exegenius task 0097-write-phase-kernel

Project directory: `/home/user/e2e-run` (paths below are relative to it)

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

For these sources: The reader is a computer science undergraduate: they have taken discrete mathematics, an algorithms course (asymptotics, divide and conquer, schoolbook and Karatsuba multiplication, sorting), a first linear algebra course (vector spaces, subspaces, dimension, rank, matrices as linear maps, inverses, triangular matrices, orthogonality, bilinear forms at a basic level), calculus, elementary number theory (primes, gcd, modular arithmetic) and basic machine-level binary representation (XOR, two's complement). They have seen Turing machines with tapes only at an introductory level. They have not been taught the discrete Fourier transform or FFT as such, abstract algebra beyond basic definitions (quotient rings, finite fields as a theory), tensor products, numerical error analysis, or the specific literature on fast integer multiplication.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes
- Fixed finite-tape machine model (also: multitape Turing machine, fixed-tape model)
- Elementary stream operations
- Controlled shifts and rational scalings
- Schönhage–Strassen optimality conjecture (also: n log n conjecture)
- Established O(n log n) multiplier
- Cyclic convolution
- Multiplication as radix-digit convolution
- Discrete Fourier transform (also: Fourier transform, DFT)
- Butterflies and the fast transform (also: transform levels)
- Bluestein chirp identity (also: chirp transform)
- Polynomial ring modulo y^r + 1 (also: negacyclic ring)
  - $y$ (ring variable): The indeterminate of the polynomials; it satisfies y^r = −1 in the ring.
  - $r$ (record length): The number of complex coefficients in a polynomial of the ring, always a power of two.
- Phase twist
- Synthetic polynomial transform (also: polynomial transform)
- Retained frequency order
- Signed packing (also: Kronecker substitution)
- Fixed-point Gaussian dyadic records (also: Z[i,1/2])
- Linear exchange network with restored scratch wires (also: finite network, motif)
- Frames on wire arrays
- Matrix shear by triangular factorization (also: Bruhat factorization, lower triangular factorization)
- Schoolbook and Karatsuba multiplication (also: long multiplication, grade-school multiplication, Karatsuba, O(n^2) multiplication, n^{log_2 3} multiplication)
- Divide-and-conquer recurrences (also: master theorem, recurrence relations, recursion tree)
- Binary and radix representation (also: base-b digits, positional notation, binary expansion, bit string, most significant bit, padding with leading zeros, carry propagation)
- Two's complement integers (also: two's-complement, signed binary integers, signed fixed-width addition)
- Bitwise XOR and arithmetic mod 2 (also: XOR, exclusive or, addition in F_2, GF(2), parity, bit flip)
- Logarithms and floors/ceilings (also: lg, log base 2, ceiling, floor, iterated logarithm, log log n)
- Modular arithmetic and primes (also: congruence, residues mod n, gcd, coprime, relatively prime, prime numbers, Z/nZ, modular inverse, units mod n)
- Roots of unity (also: nth roots of unity, primitive root of unity, e^{2 pi i/n}, Euler's formula)
- Vector spaces, subspaces, dimension and rank (also: linear subspace, basis, span, linear independence, dimension, matrix rank, kernel, linear map, linear operator, direct sum)
- Matrices and linear operators (also: matrix multiplication, invertible matrix, matrix inverse, identity matrix, commuting operators, diagonal matrix, triangular matrix, lower triangular, permutation matrix)
- Gaussian elimination and triangular factorization (also: row reduction, LU decomposition, back substitution)
- Orthogonality and inner products (also: orthonormal basis, dot product, orthogonal complement, bilinear form, nondegenerate form, Euclidean norm)
- Norms and the triangle inequality (also: sup norm, max norm, infinity norm, modulus bounds, absolute value bounds)
- Permutations and bijections (also: permutation of indices, sorting a permutation, bit-reversal permutation, bijective map, inverse permutation)
- Cartesian products and multi-index arrays (also: multidimensional arrays, row-major order, lexicographic order, mixed-radix index, index tuples, array stored on a tape, rectangle, columns)
- Directed acyclic graphs and networks of gates (also: circuit, DAG, wire, gate, edges and vertices, fan-in)
- Summation, geometric series and induction (also: geometric sum, proof by induction, summation notation, telescoping sum)
- Rounding to the nearest integer and exactness (also: rounding, truncation, round to nearest, rational numbers, dyadic rational)
- Multitape Turing machine running time (also: tape head movement, scanning a tape, linear-time pass over a tape, time complexity of a Turing machine, worst-case running time)
- Integer exponentials and tuple notation (also: powers of two, tensor power notation, exponent of a constant, fixed rational exponents)

## This page

Concept: Two-point kernel C
Gloss: The matrix C = aI + bX with a = (1+i)/2, b = (1−i)/2, a square root of the bit flip, linked to the butterfly by H₀ = b·S·C·S with S = diag(1, i).
Also called: phase network kernel

## Where the argument relies on this page

- Complex network: with binary labels and the phase frames $\mathcal C_U=H^{\otimes m}\operatorname{diag}(i^{\operatorname{wt}(P_Ux)\bmod 4})H^{\otimes m}$, every edge difference is a product of one translation kernel $aI+bX_v$ (or its inverse) per vector of an orthonormal basis of the edge residual; the total number of kernels is $s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}<W_{\rm c}m$ and, after endpoint corrections, the network applies $C^{\otimes m}$ on every role. (on [Binary phase frames](phase-frames.md))
- Complex variant: the tensor product of $H_0=\frac12\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ on one bit of each of $D\le d$ address chunks (each of $K$ bits, selected at a common offset), acting coefficientwise on polynomial records with $r$ complex $p$-bit coefficients, is computed exactly followed by one truncation $Q_p$, in $O(Vd^{\lambda'})$ time with $\lambda'<1$, rather than $D$ whole-array passes. (on [Simultaneous butterfly layer](simultaneous-layer.md))
- The kernel $C=aI+bX$ satisfies $H_0=b\,\mathsf SC\mathsf S$ (with $\mathsf S=\operatorname{diag}(1,i)$), $C^2=X$ and $C^4=I$.
- A group of $e=mf$ axes is handled by the complex network: each edge residual vector is one child on $f$ axes, an arbitrary residual basis is moved into coordinate position by binary changes of basis (products of at most $m(m-1)+3m$ row additions), and inverse children use forward ones, so there are exactly $s_{\rm c}$ children.

## Symbols already bound on earlier pages

The symbols in the names of the concepts the reader knows are listed with those concepts above.

- $y$ (ring variable), bound on [Polynomial ring modulo y^r + 1](ring-y.md): The indeterminate of the polynomials, satisfying y^r = -1 in the ring.
- $r$ (record length), bound on [Polynomial ring modulo y^r + 1](ring-y.md): The number of complex coefficients in a polynomial of the ring, always a power of two.
- $n$ (bit length), bound on [Schönhage–Strassen optimality conjecture](conjecture.md): The number of bits in each of the two integers being multiplied.
- $\kappa$ (saving exponent), bound on [Schönhage–Strassen optimality conjecture](conjecture.md): A fixed positive constant by which the exponent of the logarithm in the running time is lowered.
- $p$ (fractional bits), bound on [Fixed-point Gaussian dyadic records](fixed-point.md): The number of fractional bits of the stored grid, so values are integers divided by 2^p.
- $k$ (operation count), bound on [Fixed-point Gaussian dyadic records](fixed-point.md): The number of operations applied since the layer began.
- $\Delta$ (extra reserved bits), bound on [Fixed-point Gaussian dyadic records](fixed-point.md): The number of extra bits reserved, at least the number of operations charged to the layer.
- $Q_p$ (truncation), bound on [Fixed-point Gaussian dyadic records](fixed-point.md): The single truncation that drops the bits below 2^{-p} in each real and imaginary part.
- $h$ (ground-set size), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The size of the ground set $[h]$ whose three-element subsets index the banks.
- $v$ (number of triples), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of three-element subsets of $[h]$.
- $N$ (bank size), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of wires in each data bank.
- $m$ (label-space dimension), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The dimension of the label space used later.
- $I$ (invocation count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of invocations.
- $z_{\rm b}$ (bit neighbour count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of neighbours of a fixed triple in the bit construction.
- $z_{\rm c}$ (complex neighbour count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of neighbours of a fixed triple in the complex construction.
- $c_{\rm b}$ (bit central wires), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of central wires per invocation in the bit network.
- $c_{\rm c}$ (complex central wires), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of central wires per invocation in the complex network.
- $W_{\rm b}$ (bit wire count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The total number of wires in the bit network.
- $W_{\rm c}$ (complex wire count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The total number of wires in the complex network.
- $R$ (scalar ring), bound on [Frames on wire arrays](array-frames.md): The ring of scalars carried by the wires.
- $\Omega$ (address set), bound on [Frames on wire arrays](array-frames.md): A finite set of addresses indexing every wire's array.
- $\mathsf S_\Omega$ (pointwise network), bound on [Frames on wire arrays](array-frames.md): The network obtained by applying every scalar gate pointwise at each address, acting on all wire arrays together.
- $D_v$ (frame), bound on [Frames on wire arrays](array-frames.md): An invertible R-linear operator on R^Omega assigned to a source, gate or sink v.
- $D_{\rm in}$ (input frame), bound on [Frames on wire arrays](array-frames.md): The direct sum of the source frames over the input roles.
- $D_{\rm out}$ (output frame), bound on [Frames on wire arrays](array-frames.md): The direct sum of the sink frames over the output roles.
- $\rho$ (role permutation), bound on [Frames on wire arrays](array-frames.md): The map sending each input role to its output role in a signed role permutation.
- $\varepsilon_w$ (route sign), bound on [Frames on wire arrays](array-frames.md): The scalar sign of the route from input role w.
- $q$ (sequence length), bound on [Cyclic convolution](convolution.md): The number of entries in each of the two sequences being convolved.
- $t_i$ (axis length), bound on [Cyclic convolution](convolution.md): The length of axis i of the array.
- $M$ (cyclic addresses), bound on [Cyclic convolution](convolution.md): The number of cyclic addresses on the first d-1 axes, the product of t_i for i<d.
- $T$ (total coefficients), bound on [Cyclic convolution](convolution.md): The total number of complex coefficients in an array, rM.
- $u$ (first input), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The first of the two integers being multiplied.
- $v$ (second input), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The second of the two integers being multiplied.
- $n$ (input bit length), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The number of bits in each input.
- $b$ (digit width), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The number of bits in one radix digit.
- $T$ (padded length), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): A power of two with 4n/b <= T < 8n/b.
- $S$ (convolution length), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The length of the cyclic convolution, a product of distinct odd primes with T/2 < S < T.
- $q$ (digit count), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The number of radix-2^b digits in each input.
- $u_i$ (digit of u), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The i-th radix-2^b digit of u, an integer below 2^b.
- $v_k$ (digit of v), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The k-th radix-2^b digit of v, an integer below 2^b.
- $x$ (polynomial variable), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The variable of the digit polynomials, evaluated at 2^b to recover the integers.
- $c_j$ (product coefficient), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The coefficient of x^j in the product of the digit polynomials.
- $x_d$ (last-axis variable), bound on [Phase twist](phase-twist.md): The variable of the last cyclic axis, with x_d^r = 1.
- $\zeta$ (twist phase), bound on [Phase twist](phase-twist.md): The number e^{\pi i/r}, a primitive 2r-th root of unity with \zeta^r = -1.
- $\Theta$ (twist map), bound on [Phase twist](phase-twist.md): The ring isomorphism from C[x_d]/(x_d^r-1) to the negacyclic ring sending x_d to \zeta y.
- $d$ (number of axes), bound on [Phase twist](phase-twist.md): The number of axes of the array f.
- $T$ (total entries), bound on [Phase twist](phase-twist.md): The number of entries of the array f in all.
- $M$ (number of records), bound on [Phase twist](phase-twist.md): The number of lines along the last axis, T/r.
- $\iota$ (record identification), bound on [Phase twist](phase-twist.md): Reads each line along the last axis as a polynomial in the negacyclic ring.
- $D_\pm$ (diagonal twist), bound on [Phase twist](phase-twist.md): Multiplies entry k of each line by \zeta^{\pm k}.
- $\mathcal M_r$ (ring convolution), bound on [Phase twist](phase-twist.md): The ring convolution that convolves the first d-1 axes over the negacyclic ring and includes the division by T.
- $\mathcal M_{\mathbb C}$ (normalized cyclic convolution), bound on [Phase twist](phase-twist.md): The composite D_-\iota^{-1}\mathcal M_r(\iota D_+ f,\iota D_+ g), equal to f*g/T.
- $q$ (sequence length), bound on [Discrete Fourier transform](dft.md): The number of complex entries in the sequences the transform acts on.
- $u$ (input sequence), bound on [Discrete Fourier transform](dft.md): A sequence of q complex numbers to which the transform is applied.
- $\omega$ (root of unity), bound on [Discrete Fourier transform](dft.md): The primitive q-th root of unity e^{2 pi i/q} whose powers are the transform weights.
- $t$ (transform length), bound on [Butterflies and the fast transform](butterfly.md): The number of values in the transform, a power of two.
- $z_k$ (input values), bound on [Butterflies and the fast transform](butterfly.md): The input value at position k, for 0 <= k < t.
- $k$ (input position), bound on [Butterflies and the fast transform](butterfly.md): The position of an input value, 0 <= k < t.
- $\omega_t$ (root of unity), bound on [Butterflies and the fast transform](butterfly.md): The primitive t-th root of unity e^{2 pi i/t}.
- $b$ (lowest output bit), bound on [Butterflies and the fast transform](butterfly.md): The lowest bit of the output index, 0 or 1.
- $h$ (remaining output index), bound on [Butterflies and the fast transform](butterfly.md): The output index with its lowest bit removed.
- $t$ (transform length), bound on [Synthetic polynomial transform](synthetic-transform.md): The number of ring elements along one axis of the transform, a power of two dividing 2r.
- $\omega_t$ (ring root of unity), bound on [Synthetic polynomial transform](synthetic-transform.md): The power y^{2r/t} of the ring variable, used as the root of unity of the length-t synthetic transform.
- $V$ (array volume), bound on [Elementary stream operations](stream-ops.md): The number of radix-q digits stored in the array.
- $q$ (radix), bound on [Elementary stream operations](stream-ops.md): The number of values one digit can take.
- $W$ (number of streams), bound on [Elementary stream operations](stream-ops.md): The fixed number of streams into which whole rows are dealt cyclically.
- $d$ (number of axes), bound on [Bluestein chirp identity](chirp.md): The number of axes (coordinates) of an index.
- $t_i$ (axis length), bound on [Bluestein chirp identity](chirp.md): The even number of entries along axis i.
- $s_i$ (coprime integer), bound on [Bluestein chirp identity](chirp.md): An integer coprime to t_i, scaling the frequency read along axis i.
- $T$ (total entries), bound on [Bluestein chirp identity](chirp.md): The total number of entries, the product of the t_i.
- $Q$ (target permutation), bound on [Bluestein chirp identity](chirp.md): The target permutation, reading frequency (-s_i j_i)_i at output position j.
- $a$ (chirp), bound on [Bluestein chirp identity](chirp.md): The chirp, a quadratic-phase array exp(-pi i sum s_i j_i^2/t_i).
- $t$ (transform length), bound on [Retained frequency order](frequency-order.md): The number of ring elements transformed along one axis, a power of two dividing 2r.
- $a$ (number of rounds), bound on [Retained frequency order](frequency-order.md): The number log_2 t of rounds of the fast algorithm.
- $\omega_t$ (root of unity), bound on [Retained frequency order](frequency-order.md): The power y^{2r/t} of the ring variable used as the t-th root of unity.
- $H_0$ (two-point butterfly), bound on [Retained frequency order](frequency-order.md): The 2x2 matrix (1/2)[[1,1],[1,-1]] applied to each pair of entries.
- $B_t$ (bit-reversal permutation), bound on [Retained frequency order](frequency-order.md): The permutation of records moving the entry at j to rev_a(j).
- $\mathcal H$ (parallel butterfly), bound on [Retained frequency order](frequency-order.md): The butterfly layer applying H_0 on every participating axis at once.
- $J_E$ (recordwise monomial), bound on [Retained frequency order](frequency-order.md): The operation multiplying the record at each address by y^E.
- $u_i$ (current length), bound on [Retained frequency order](frequency-order.md): The current recursive length of axis i.
- $b_i$ (branch bit), bound on [Retained frequency order](frequency-order.md): The newly written branch bit of axis i.
- $k_i$ (encoded index), bound on [Retained frequency order](frequency-order.md): The index encoded by the still unprocessed slots of axis i.
- $N$ (bit length), bound on [Established O(n log n) multiplier](hvdh-multiplier.md): The number of bits in each of the two integers being multiplied.
- $p$ (precision bits), bound on [Signed packing](signed-packing.md): The number of fractional bits in each coefficient component.
- $B_0$ (packing base), bound on [Signed packing](signed-packing.md): The power of two $2^{4p}$ at which the polynomials are evaluated.
- $A_u$ (evaluation integer), bound on [Signed packing](signed-packing.md): The signed integer obtained by evaluating the polynomial u at B_0.
- $H_j$ (numerator coefficient), bound on [Signed packing](signed-packing.md): The Gaussian integer coefficient of y^j after reduction modulo y^r+1.
- $q$ (prime), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The prime base of the field arithmetic.
- $b$ (field digits), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The number of base-$q$ digits of a field.
- $Q$ (field size), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The number of values a field can hold, Q = q^b.
- $V$ (array volume), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The number of stored data bits in the array.
- $a$ (offset), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The offset added to the target field, prepared from the control values.
- $B$ (suffix length), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The number of bits following the target field.
- $c$ (scaling integer), bound on [Controlled shifts and rational scalings](controlled-shifts.md): A fixed positive integer prime to q by which the target is multiplied.
- $A$ (shear matrix), bound on [Matrix shear by triangular factorization](matrix-shear.md): The fixed rational m by m matrix whose action AD is added to H.
- $m$ (fields per group), bound on [Matrix shear by triangular factorization](matrix-shear.md): The number of fields in each of the groups H and D.
- $a$ (rank), bound on [Matrix shear by triangular factorization](matrix-shear.md): The rank of the matrix A.
- $H$ (H group), bound on [Matrix shear by triangular factorization](matrix-shear.md): The ordered group of m fields H_1..H_m that receives the update.
- $D$ (D group), bound on [Matrix shear by triangular factorization](matrix-shear.md): The ordered group of m fields D_1..D_m that is added into H.
- $q$ (base prime), bound on [Matrix shear by triangular factorization](matrix-shear.md): A fixed odd prime; fields are residues modulo q^b.
- $b$ (digits per field), bound on [Matrix shear by triangular factorization](matrix-shear.md): The number of base-q digits in a field.
- $V$ (data volume), bound on [Matrix shear by triangular factorization](matrix-shear.md): The volume of data being processed.
- $E_1$ (left factor), bound on [Matrix shear by triangular factorization](matrix-shear.md): An invertible lower triangular factor of A.
- $E_2$ (right factor), bound on [Matrix shear by triangular factorization](matrix-shear.md): An invertible lower triangular factor of A.
- $\Pi$ (partial permutation), bound on [Matrix shear by triangular factorization](matrix-shear.md): A matrix with exactly a ones, at most one per row and column, and zeros elsewhere.
- $i$ (row index), bound on [Matrix shear by triangular factorization](matrix-shear.md): The row of a one of Pi.
- $j$ (column index), bound on [Matrix shear by triangular factorization](matrix-shear.md): The column of a one of Pi.
- $h$ (value of H_i), bound on [Matrix shear by triangular factorization](matrix-shear.md): The initial value of the field H_i.
- $d$ (value of D_j), bound on [Matrix shear by triangular factorization](matrix-shear.md): The initial value of the field D_j.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Butterflies and the fast transform](butterfly.md): A two-point averaging/differencing step H₀(u,v) = ((u+v)/2, (u−v)/2) whose repeated use over address bits, with twiddle multiplications, computes a transform in log t layers.
  Shown as: Two-point kernel C *<predicate>* Butterflies and the fast transform

## Pages that build on this one

- Binary phase frames: Frames C_U = H^{⊗m} diag(i^{wt(P_U x) mod 4}) H^{⊗m} whose edge differences are products of translation kernels aI + bX_v, one per vector of an orthonormal residual basis.

## Other pages you may link to

- [Polynomial ring modulo y^r + 1](ring-y.md)
- [Fixed finite-tape machine model](machine-model.md)
- [Schönhage–Strassen optimality conjecture](conjecture.md)
- [Fixed-point Gaussian dyadic records](fixed-point.md)
- [Linear exchange network with restored scratch wires](exchange-network.md)
- [Frames on wire arrays](array-frames.md)
- [Cyclic convolution](convolution.md)
- [Multiplication as radix-digit convolution](radix-digit-reduction.md)
- [Phase twist](phase-twist.md)
- [Discrete Fourier transform](dft.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Elementary stream operations](stream-ops.md)
- [Bluestein chirp identity](chirp.md)
- [Retained frequency order](frequency-order.md)
- [Established O(n log n) multiplier](hvdh-multiplier.md)
- [Signed packing](signed-packing.md)
- [Controlled shifts and rational scalings](controlled-shifts.md)
- [Matrix shear by triangular factorization](matrix-shear.md)
- [Contractions and bilinear contractions](contraction-maps.md)
- [Multidimensional transforms](multidim-transform.md)
- [Chinese-remainder address map](crt-map.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Retained permutation cancellation](retained-permutations.md)
- [Error tracking and exact recovery](precision-recovery.md)
- [Parameter and prime-length choice](parameter-choice.md)
- [Tensor products of subspaces](tensor-product-of-spaces.md)
- [Nested subspace labels and rank deficit](subspace-labels.md)
- [Recursive power saving](rank-recurrence.md)
- [Fast address-chunk interchange](address-interchange.md)
- [Binary phase frames](phase-frames.md)
- [Packed selected-bit addition](packed-bit-addition.md)
- [Simultaneous butterfly layer](simultaneous-layer.md)
- [Tape layout for synthetic transforms](transform-layout.md)
- [Convolution from the retained transform layout](ring-convolution.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Cost accounting and the exponent κ](cost-accounting.md)
- [Power-saving integer multiplication](main-result.md)

## Evidence from the sources, with the paragraph around each quote

- "C=H\mathsf SH=aI+bX" (paper)

  > Put \[ H_0=\frac12\begin{pmatrix}1&1\\1&-1\end{pmatrix},\qquad H=\sqrt2 H_0,\qquad \mathsf S=\operatorname{diag}(1,i),\qquad Z=\operatorname{diag}(1,-1). \] For the bit-flip matrix $X=\bigl(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\bigr)$, define \begin{equation}\label{eq:phase-C} C=H\mathsf SH=aI+bX,\qquad a=\frac{1+i}{2},\quad b=\frac{1-i}{2}. \end{equation} Direct multiplication gives \begin{equation}\label{eq:phase-basic-identities} H_0=b\mathsf SC\mathsf S,\qquad C^2=X,\qquad C^4=I,\qquad C^{-1}=bI+aX=-iZCZ. \end{equation} In particular, $C=iZC^{-1}Z$. These identities use only Gaussian dyadic coefficients. The Hadamard matrices in the definition of $\mathcal C_U$ are used to prove identities; they need not be executed by the machine.

- "H_0=b\mathsf SC\mathsf S,\qquad C^2=X" (paper)

  > Put \[ H_0=\frac12\begin{pmatrix}1&1\\1&-1\end{pmatrix},\qquad H=\sqrt2 H_0,\qquad \mathsf S=\operatorname{diag}(1,i),\qquad Z=\operatorname{diag}(1,-1). \] For the bit-flip matrix $X=\bigl(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\bigr)$, define \begin{equation}\label{eq:phase-C} C=H\mathsf SH=aI+bX,\qquad a=\frac{1+i}{2},\quad b=\frac{1-i}{2}. \end{equation} Direct multiplication gives \begin{equation}\label{eq:phase-basic-identities} H_0=b\mathsf SC\mathsf S,\qquad C^2=X,\qquad C^4=I,\qquad C^{-1}=bI+aX=-iZCZ. \end{equation} In particular, $C=iZC^{-1}Z$. These identities use only Gaussian dyadic coefficients. The Hadamard matrices in the definition of $\mathcal C_U$ are used to prove identities; they need not be executed by the machine.


## Sources (read from disk as needed)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- Say what $H$ denotes where it is first used: the page uses it before saying so in "where $H=\sqrt2\,H_0$ is the normalized Hadamard matrix"

## Previous version (revise it)

It has 279 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 348 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

The two-point kernel is a $2\times 2$ matrix that squares to the bit flip and differs from the butterfly step only by phase factors; it is the building block of the phase networks used later.

Let $a=\frac{1+i}{2}$ and $b=\frac{1-i}{2}$ be two complex constants. Let $X=\begin{pmatrix}0&1\\1&0\end{pmatrix}$ be the bit flip, which swaps the two entries of a pair $(u,v)$. The kernel is $C=aI+bX$, where $I$ is the $2\times 2$ identity. Let $\mathsf S=\operatorname{diag}(1,i)$ be the phase matrix that multiplies the second entry of a pair by $i$. Let $H_0=\frac12\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ be the matrix of the averaging and differencing step $(u,v)\mapsto\bigl(\tfrac{u+v}{2},\tfrac{u-v}{2}\bigr)$.

## Why it is a square root of the flip

Since $a^2+b^2=\frac{i}{2}-\frac{i}{2}=0$ and $2ab=1$, we get $C^2=(a^2+b^2)I+2ab\,X=X$, and therefore $C^4=X^2=I$. In terms of eigenvectors, $X$ has eigenvalue $1$ on $(1,1)$ and $-1$ on $(1,-1)$, while $C$ has eigenvalues $a+b=1$ and $a-b=i$ on the same vectors. Equivalently $C=H\mathsf SH$, where $H=\sqrt2\,H_0$ is the normalized Hadamard matrix <cite data-source="paper">C=H\mathsf SH=aI+bX</cite>. Thus $C$ applies the phase $\mathsf S$ in the basis where $X$ is diagonal, and one application of $C$ is "half" a flip.

## Link to the butterfly

The kernel $C$ is obtained from the two-point step of [Butterflies and the fast transform](butterfly.md) by conjugating with $\mathsf S$ and rescaling:
$$H_0=b\,\mathsf S\,C\,\mathsf S,\qquad C^2=X$$
<cite data-source="paper">H_0=b\mathsf SC\mathsf S,\qquad C^2=X</cite>. One can check the first identity by multiplying out: $\mathsf SC\mathsf S=\begin{pmatrix}a&ib\\ib&-a\end{pmatrix}$, and multiplying by $b$ uses $ab=\frac12$ and $ib^2=\frac12$.

The reason to prefer $C$ is that it is a combination $aI+bX$ of the identity and a bit flip. When the flip acts on one address bit of a larger array, such a combination is a translation-like kernel, and the networks built from these kernels are described on the page on binary phase frames. The coefficients $a$ and $b$ are Gaussian dyadic (real and imaginary parts are dyadic rationals), so $C$ and its inverse $C^{-1}=bI+aX$ are exact on fixed-point records. The Hadamard factors in $C=H\mathsf SH$ serve to prove identities and need not be executed by the machine.

## Answer

The answer is two files: the page body as markdown (not JSON), and a JSON object with the symbols the page binds and its relations to its prerequisite pages. In JSON strings, write each backslash of LaTeX twice (`"\\kappa"`). The JSON follows this schema:

```json
{
  "$defs": {
    "Derivation": {
      "additionalProperties": false,
      "description": "Where the page derives one of the steps the argument gives it.",
      "properties": {
        "quote": {
          "description": "The passage on this page that derives the step, copied exactly: a sentence or more,\noutside citations.",
          "type": "string"
        },
        "step": {
          "description": "The step's id, as listed under \"Steps this page derives\".",
          "type": "string"
        }
      },
      "required": [
        "step",
        "quote"
      ],
      "type": "object"
    },
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
    "derivations": {
      "default": [],
      "description": "For each step listed under \"Steps this page derives\", the passage on the page that\nderives it. Empty if the task lists none.",
      "items": {
        "$ref": "#/$defs/Derivation"
      },
      "type": "array"
    },
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

Write the body to `exegenius/tasks/0097-write-phase-kernel.answer.md` and the JSON to `exegenius/tasks/0097-write-phase-kernel.answer.json`, then run `exegenius submit 0097-write-phase-kernel` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0097-write-phase-kernel`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
