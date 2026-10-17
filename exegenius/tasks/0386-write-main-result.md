# exegenius task 0386-write-main-result

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
- Multidimensional transforms
- Chinese-remainder address map (also: Agarwal–Cooley map)
- Gaussian resampling
- Bluestein chirp identity (also: chirp transform)
- Retained permutation cancellation
- Polynomial ring modulo y^r + 1 (also: negacyclic ring)
  - $y$ (ring variable): The indeterminate of the polynomials; it satisfies y^r = −1 in the ring.
  - $r$ (record length): The number of complex coefficients in a polynomial of the ring, always a power of two.
- Phase twist
- Synthetic polynomial transform (also: polynomial transform)
- Retained frequency order
- Signed packing (also: Kronecker substitution)
- Fixed-point Gaussian dyadic records (also: Z[i,1/2])
- Error tracking and exact recovery (also: synthetic transform error, source transform error)
- Linear exchange network with restored scratch wires (also: finite network, motif)
- Frames on wire arrays
- Nested subspace labels and rank deficit (also: rank saving)
- Recursive power saving
- Matrix shear by triangular factorization (also: Bruhat factorization, lower triangular factorization)
- Fast address-chunk interchange (also: chunk swap, tape interchange, costly recursive primitive)
- Two-point kernel C (also: phase network kernel)
- Binary phase frames
- Packed selected-bit addition (also: exceptional addresses)
- Simultaneous butterfly layer (also: parallel butterfly layer)
- Tape layout for synthetic transforms
- Convolution from the retained transform layout
- Parameter and prime-length choice
- The multiplication algorithm
- Cost accounting and the exponent κ
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
- Contractions and bilinear contractions (also: contraction, bilinear contraction)
- Tensor products of subspaces (also: tensor product of subspaces, tensor product)

## This page

Concept: Power-saving integer multiplication
Gloss: A deterministic fixed-tape Turing machine multiplying two n-bit integers exactly in O(n(lg n)^{1−κ}) time with κ = 2^{−182}, disproving the n log n optimality conjecture in this model.
Also called: multiplication in O(n (lg n)^(1-κ))

## This page in the argument

The step: A single deterministic Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ worst-case time with $\kappa=2^{-182}$, disproving the $n\log n$ optimality conjecture of Sch\"onhage and Strassen in this model.
How: Build two power-saving tape procedures (chunk interchange and simultaneous butterfly layer) from fixed finite linear networks; use them to accelerate the synthetic polynomial transforms and ring convolution; use Gaussian resampling with retained permutations and chirps to reduce the prime-length cyclic convolution of the radix-digit coefficients to those power-of-two transforms; assemble the exact product with a proof that the error is below $1/2$; and total the cost to show a power of $\log n$ is saved.
Why: Scanning an array of $\Theta(n)$ stored bits at each of $\Theta(\log n)$ transform levels already costs $\Theta(n\log n)$, so the logarithmic factor can only be beaten by cheaper address movement and cheaper butterfly arithmetic. (the sources say so: "We therefore need savings in both movement and arithmetic." (paper))
Striking feature: The power saving $\kappa=2^{-182}$ is astronomically small, yet strictly positive, so the algorithm's running time is $o(n\log n)$ through all input lengths. (explain why it holds, from the method)

Its sub-steps, in order:

- Both tape primitives (the interchange of two address chunks of $u$ digits and the simultaneous butterfly layer on up to $d$ axes) cost the volume times a power below one of their width, because a call at parameter $mf$ makes $s$ calls at parameter $f$ on streams of volume $V/W$ with $s<Wm$, so the cost per unit volume grows by $s/W<m$ per factor $m$ of the parameter. (on [Recursive power saving](rank-recurrence.md))
- Synthetic transforms over $\mathcal R_r$ on $d-1$ axes of lengths $t_i\in\{2^{\ell-1},2^\ell\}$ with outputs kept in a retained layout $LB$ cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$ with error less than $\sqrt2\ell\,2^{-p}$. (on [Tape layout for synthetic transforms](transform-layout.md))
- Normalized cyclic convolution over the polynomial ring $\mathbb C[y]/(y^r+1)$ on the remaining $d-1$ axes is computed from two forward synthetic transforms in retained order, $M$ pointwise polynomial products and the opposite transform, in $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}+\log(rp)])$ time with error less than $\sqrt2\,M(3\ell+1)2^{-p}$. (on [Convolution from the retained transform layout](ring-convolution.md))
- The Fourier transforms of pairwise coprime prime lengths $s_i$ that the integer product needs are computed through power-of-two lengths $t_i$ by Gaussian resampling and Bluestein chirps, with the source and target coordinate permutations left inside the transform identities, so that none is executed as a sort. (on [Retained permutation cancellation](retained-permutations.md))
- The exact $2n$-bit product of the two inputs is obtained from the radix-digit convolution by the chain: radix digits, Chinese-remainder address map to a product of prime cyclic axes, two forward source transforms (resampling and chirps), pointwise product, opposite transform, rescaling, rounding, and carry propagation, with total error below $1/2$. (on [The multiplication algorithm](multiplication-algorithm.md))
- The total time of the machine is $O(n(\lg n)^{1-\kappa})$ with $\kappa=2^{-182}$: after dividing each cost by $V=Tp=\Theta(n)$ the dominant terms are powers of $p$ below one, with minimum margin $2^{-181}=2\kappa$. (on [Cost accounting and the exponent κ](cost-accounting.md))

## Symbols already bound on earlier pages

The symbols in the names of the concepts the reader knows are listed with those concepts above.

- $y$ (ring variable), bound on [Polynomial ring modulo y^r + 1](ring-y.md): The indeterminate of the polynomials; it satisfies y^r = -1 in the ring.
- $r$ (record length), bound on [Polynomial ring modulo y^r + 1](ring-y.md): The number of complex coefficients in a polynomial of the ring, always a power of two.
- $n$ (bit length), bound on [Schönhage–Strassen optimality conjecture](conjecture.md): The number of bits in each of the two integers being multiplied.
- $\kappa$ (power saving), bound on [Schönhage–Strassen optimality conjecture](conjecture.md): A fixed positive constant, the amount by which the exponent of the logarithm is lowered.
- $p$ (fractional bits), bound on [Fixed-point Gaussian dyadic records](fixed-point.md): The number of fractional bits of the grid on which stored values lie.
- $k$ (depth), bound on [Fixed-point Gaussian dyadic records](fixed-point.md): The number of operations in sequence since the layer began that produced a value.
- $\Delta$ (reserved extra bits), bound on [Fixed-point Gaussian dyadic records](fixed-point.md): The number of extra bits reserved, at least the maximal depth reached in the layer.
- $Q_p$ (truncation), bound on [Fixed-point Gaussian dyadic records](fixed-point.md): The truncation that drops the bits below 2^{-p} in each real and imaginary part, returning a record to the p-bit grid.
- $X$ (first data bank), bound on [Linear exchange network with restored scratch wires](exchange-network.md): One of the two data banks, with entries X_a.
- $Y$ (second data bank), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The other data bank, with entries Y_a.
- $a$ (bank index), bound on [Linear exchange network with restored scratch wires](exchange-network.md): A triple of three-element subsets of [h] indexing the entries of the banks.
- $h$ (ground-set size), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The size of the ground set [h] whose three-element subsets index the banks.
- $\mathcal T$ (triple set), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The set of three-element subsets of [h].
- $v$ (number of triples), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of three-element subsets of [h].
- $N$ (bank size), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of values in each data bank.
- $m$ (label-space dimension), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The dimension of the label space used on later pages.
- $I$ (invocation count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of invocations over all three stages.
- $z_{\rm b}$ (bit neighbour count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of neighbours of a fixed triple in the bit construction.
- $z_{\rm c}$ (complex neighbour count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of neighbours of a fixed triple in the complex construction.
- $c_{\rm b}$ (bit central wires), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of central wires per invocation in the bit network.
- $c_{\rm c}$ (complex central wires), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of central wires per invocation in the complex network.
- $W_{\rm b}$ (bit wire count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The total number of wires in the bit network.
- $W_{\rm c}$ (complex wire count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The total number of wires in the complex network.
- $R$ (scalar ring), bound on [Frames on wire arrays](array-frames.md): The ring of scalars carried by the wires.
- $\Omega$ (address set), bound on [Frames on wire arrays](array-frames.md): A finite set of addresses indexing every array.
- $\mathsf S_\Omega$ (pointwise network), bound on [Frames on wire arrays](array-frames.md): The network acting on all the wire arrays together, each gate applied at every address separately.
- $D_v$ (frame), bound on [Frames on wire arrays](array-frames.md): The invertible R-linear operator on R^Omega assigned to the source, gate or sink v.
- $t$ (gate input count), bound on [Frames on wire arrays](array-frames.md): The number of input arrays of the gate G.
- $\rho$ (role permutation), bound on [Frames on wire arrays](array-frames.md): The map sending each input role w to its output role rho(w) in a signed role permutation.
- $\varepsilon_w$ (role sign), bound on [Frames on wire arrays](array-frames.md): The scalar sign carried by the route from input role w.
- $q$ (sequence length), bound on [Cyclic convolution](convolution.md): The number of entries in each of the two sequences being convolved.
- $d$ (axis count), bound on [Cyclic convolution](convolution.md): The number of axes of an array, counting the d-1 cyclic axes plus the coefficient axis.
- $t_i$ (axis length), bound on [Cyclic convolution](convolution.md): The length of cyclic axis i.
- $M$ (address count), bound on [Cyclic convolution](convolution.md): The number of cyclic addresses of an array, the product of the axis lengths.
- $T$ (coefficient count), bound on [Cyclic convolution](convolution.md): The total number of complex coefficients in an array.
- $u$ (first input), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The first of the two n-bit integers being multiplied.
- $v$ (second input), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The second of the two n-bit integers being multiplied (not the number of triples).
- $b$ (digit bits), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The number of bits in one radix-2^b digit.
- $T$ (padded length), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The padded length, a power of two with 4n/b <= T < 8n/b.
- $S$ (convolution length), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The length of the cyclic convolution, with T/2<S<T.
- $q$ (digit count), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The number of digits in each input, not the sequence length of the convolution page.
- $x$ (polynomial variable), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The indeterminate of the digit polynomials, evaluated at 2^b to recover the integers.
- $c_j$ (product coefficient), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The coefficient of x^j in the product of the two digit polynomials.
- $f$ (first array), bound on [Phase twist](phase-twist.md): The first complex array being convolved.
- $g$ (second array), bound on [Phase twist](phase-twist.md): The second complex array being convolved with f.
- $d$ (axis count), bound on [Phase twist](phase-twist.md): The number of axes of the arrays.
- $x_d$ (last-axis variable), bound on [Phase twist](phase-twist.md): The variable of the last cyclic axis.
- $\mathcal R_r$ (negacyclic ring), bound on [Phase twist](phase-twist.md): The ring of polynomials modulo y^r+1.
- $\zeta$ (twist root), bound on [Phase twist](phase-twist.md): The primitive 2r-th root of unity e^{\pi i/r}, with zeta^r=-1.
- $\Theta$ (twist map), bound on [Phase twist](phase-twist.md): The ring isomorphism from the cyclic ring to the negacyclic ring sending x_d to zeta y.
- $k$ (coefficient index), bound on [Phase twist](phase-twist.md): An index of a coefficient (not an operation count).
- $l$ (second coefficient index), bound on [Phase twist](phase-twist.md): An index of a coefficient of the second factor.
- $j$ (wrapped position), bound on [Phase twist](phase-twist.md): The position k+l reduced modulo r.
- $h$ (wrap indicator), bound on [Phase twist](phase-twist.md): Zero or one according to whether k+l wrapped past r.
- $\iota$ (record reading), bound on [Phase twist](phase-twist.md): The map reading each line along the last axis as a polynomial in R_r.
- $D_\pm$ (diagonal twist), bound on [Phase twist](phase-twist.md): The maps multiplying entry k of each line by zeta^{+-k}.
- $\mathcal M_r$ (ring convolution), bound on [Phase twist](phase-twist.md): Normalized convolution of the first d-1 axes over R_r, including division by T.
- $\mathcal M_{\mathbb C}$ (complex convolution), bound on [Phase twist](phase-twist.md): The normalized complex cyclic convolution of two arrays.
- $\|f\|$ (sup norm), bound on [Phase twist](phase-twist.md): The largest modulus of a scalar coefficient of f.
- $q$ (sequence length), bound on [Discrete Fourier transform](dft.md): The number of entries of a sequence.
- $u$ (input sequence), bound on [Discrete Fourier transform](dft.md): A sequence of q complex numbers to be transformed.
- $\omega$ (primitive root), bound on [Discrete Fourier transform](dft.md): The primitive q-th root of unity e^{2\pi i/q}.
- $t$ (transform length), bound on [Butterflies and the fast transform](butterfly.md): The number of positions in the sequence being transformed, a power of two.
- $z_k$ (input value), bound on [Butterflies and the fast transform](butterfly.md): The input value at position k of the sequence being transformed.
- $m$ (output index), bound on [Butterflies and the fast transform](butterfly.md): The index of an output of the transform.
- $b$ (lowest bit), bound on [Butterflies and the fast transform](butterfly.md): The lowest bit of the output index m.
- $h$ (remaining index), bound on [Butterflies and the fast transform](butterfly.md): The output index m with its lowest bit removed.
- $t$ (transform length), bound on [Synthetic polynomial transform](synthetic-transform.md): The number of ring elements along one axis, a power of two dividing 2r.
- $e$ (two-adic exponent), bound on [Synthetic polynomial transform](synthetic-transform.md): The exponent of 2 in j when j is written as 2^e times an odd number.
- $V$ (array volume), bound on [Elementary stream operations](stream-ops.md): The number of digits stored in the array.
- $\beta$ (radix), bound on [Elementary stream operations](stream-ops.md): The number of values one digit can take.
- $W$ (stream count), bound on [Elementary stream operations](stream-ops.md): The fixed number of streams into which rows are dealt.
- $P$ (prefix count), bound on [Elementary stream operations](stream-ops.md): The number of prefix values of the array in item 4.
- $R$ (row count), bound on [Elementary stream operations](stream-ops.md): The number of rows in item 4; here R is not the scalar ring.
- $B$ (row length), bound on [Elementary stream operations](stream-ops.md): The number of entries per row in item 4.
- $\boldsymbol j$ (index tuple), bound on [Bluestein chirp identity](chirp.md): The tuple of indices (j_1,...,j_d), one per axis, locating an entry of an array.
- $\boldsymbol t$ (axis lengths), bound on [Bluestein chirp identity](chirp.md): The tuple (t_1,...,t_d) of axis lengths, where t_i is the even number of entries along axis i.
- $s_i$ (coprime multiplier), bound on [Bluestein chirp identity](chirp.md): An integer coprime to the axis length t_i.
- $F_{\boldsymbol t}$ (normalized transform), bound on [Bluestein chirp identity](chirp.md): The normalized multidimensional discrete Fourier transform with axis lengths t.
- $\boldsymbol k$ (input position), bound on [Bluestein chirp identity](chirp.md): The index tuple of an input entry.
- $\boldsymbol f$ (frequency), bound on [Bluestein chirp identity](chirp.md): The tuple of frequencies labelling an output entry of the transform.
- $Q$ (target permutation), bound on [Bluestein chirp identity](chirp.md): The permutation reordering the output so that position j holds the entry of frequency (-s_i j_i)_i.
- $a$ (chirp), bound on [Bluestein chirp identity](chirp.md): The chirp, a phase quadratic in the index.
- $N$ (factor bit length), bound on [Established O(n log n) multiplier](hvdh-multiplier.md): The number of bits in each of the two integers given to the established multiplier.
- $B_0$ (packing base), bound on [Signed packing](signed-packing.md): The base 2^{4p} at which the polynomials are evaluated.
- $A_u$ (signed evaluation integer), bound on [Signed packing](signed-packing.md): The integer obtained by evaluating the integer-coefficient polynomial u at B_0.
- $\gamma_j$ (carry), bound on [Signed packing](signed-packing.md): The carry, in {-1,0}, into block j when forming A_u.
- $d_j$ (block), bound on [Signed packing](signed-packing.md): The residue of u_j plus the carry modulo B_0, the j-th block of 4p bits of A_u.
- $h_j$ (product coefficient), bound on [Signed packing](signed-packing.md): The coefficient of y^j in the ordinary product h=ac of integer polynomials.
- $\rho_j$ (extraction carry), bound on [Signed packing](signed-packing.md): The carry into block j during extraction, in {0,1}.
- $H_j$ (reduced coefficient), bound on [Signed packing](signed-packing.md): The Gaussian integer coefficient of y^j after reduction modulo y^r+1.
- $q$ (prime radix), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The radix of the stored digits, a prime (not a sequence length).
- $b$ (field digit count), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The number of base-q digits of a field.
- $Q$ (field value count), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The number of values a field can take.
- $y$ (field value), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The value of the target field, an integer from 0 to Q-1 (not the ring variable).
- $a$ (offset), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The offset added to the target field, prepared from the control values.
- $B$ (suffix digit count), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The number of digits following the target field.
- $c$ (scaling multiplier), bound on [Controlled shifts and rational scalings](controlled-shifts.md): A fixed positive integer prime to q by which the field is multiplied.
- $j$ (wrap count), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The number of times cy wraps past Q.
- $y'$ (scaled position), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The position cy - jQ to which the block at position y is sent.
- $c'$ (unit denominator), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The positive integer denominator of a rational unit, prime to q.
- $q$ (field base), bound on [Matrix shear by triangular factorization](matrix-shear.md): A fixed odd prime, the base of the digits.
- $b$ (digits per field), bound on [Matrix shear by triangular factorization](matrix-shear.md): The number of base-q digits in one field.
- $a$ (rank), bound on [Matrix shear by triangular factorization](matrix-shear.md): The rank of the matrix A.
- $m$ (fields per group), bound on [Matrix shear by triangular factorization](matrix-shear.md): The number of fields in each of the groups H and D.
- $I$ (identity matrix), bound on [Two-point kernel C](phase-kernel.md): The 2x2 identity matrix.
- $X$ (bit flip), bound on [Two-point kernel C](phase-kernel.md): The 2x2 matrix swapping the two entries of a pair.
- $a$ (kernel constant), bound on [Two-point kernel C](phase-kernel.md): The complex constant (1+i)/2.
- $b$ (kernel coefficient), bound on [Two-point kernel C](phase-kernel.md): The complex coefficient (1-i)/2 of the bit flip in the kernel.
- $C$ (two-point kernel), bound on [Two-point kernel C](phase-kernel.md): The matrix aI + bX.
- $\mathsf S$ (phase matrix), bound on [Two-point kernel C](phase-kernel.md): The diagonal matrix diag(1, i) multiplying the second entry of a pair by i.
- $H_0$ (averaging step), bound on [Two-point kernel C](phase-kernel.md): The matrix of the two-point averaging and differencing step.
- $H$ (Hadamard matrix), bound on [Two-point kernel C](phase-kernel.md): The normalized Hadamard matrix sqrt(2) H_0.
- $L$ (linear map), bound on [Contractions and bilinear contractions](contraction-maps.md): A linear map whose norm bound is being defined.
- $\mathcal M$ (bilinear map), bound on [Contractions and bilinear contractions](contraction-maps.md): A map linear in each of its two operands.
- $u'$ (computed input), bound on [Contractions and bilinear contractions](contraction-maps.md): The computed input that replaces the exact input u.
- $f'$ (computed first operand), bound on [Contractions and bilinear contractions](contraction-maps.md): The computed operand replacing f.
- $g'$ (computed second operand), bound on [Contractions and bilinear contractions](contraction-maps.md): The computed operand replacing g.
- $F_q$ (normalized transform), bound on [Contractions and bilinear contractions](contraction-maps.md): The normalized discrete Fourier transform on sequences of q entries.
- $f$ (first operand), bound on [Contractions and bilinear contractions](contraction-maps.md): The first operand of the bilinear map.
- $g$ (second operand), bound on [Contractions and bilinear contractions](contraction-maps.md): The second operand of the bilinear map.
- $i$ (axis index), bound on [Multidimensional transforms](multidim-transform.md): The index of an axis of the array, from 1 to d.
- $q_i$ (axis position count), bound on [Multidimensional transforms](multidim-transform.md): The number of positions along axis i.
- $j$ (index tuple), bound on [Multidimensional transforms](multidim-transform.md): The tuple of coordinates (j_1,...,j_d) of an entry of the array.
- $k$ (output index tuple), bound on [Multidimensional transforms](multidim-transform.md): An output index tuple shaped like j.
- $G_i$ (axis operator), bound on [Multidimensional transforms](multidim-transform.md): An operator on sequences of length q_i, applied to every line along axis i.
- $\delta$ (time-bound slack), bound on [Multidimensional transforms](multidim-transform.md): A fixed constant with 0<delta<1/8 that sets the slack in the exponent 3/2+delta of p in the time bound.
- $\alpha$ (resampling parameter), bound on [Multidimensional transforms](multidim-transform.md): An integer resampling parameter with 2<=alpha<sqrt p.
- $\boldsymbol s$ (source lengths), bound on [Multidimensional transforms](multidim-transform.md): The tuple of source axis lengths (s_1,...,s_d).
- $\boldsymbol t$ (padded lengths), bound on [Multidimensional transforms](multidim-transform.md): The tuple of padded power-of-two axis lengths (t_1,...,t_d).
- $\gamma$ (scalar exponent), bound on [Multidimensional transforms](multidim-transform.md): The total exponent 2d alpha^2 of the power of two multiplying the tensored identity.
- $R$ (source permutation), bound on [Multidimensional transforms](multidim-transform.md): The tensor product of the source index permutations P_{s_i}; here not the scalar ring.
- $Q$ (padded permutation), bound on [Multidimensional transforms](multidim-transform.md): The tensor product of the index permutations P_{t_i}.
- $\mathcal A$ (input map), bound on [Multidimensional transforms](multidim-transform.md): The tensor product of the one-dimensional input maps A_i.
- $\mathcal B_0$ (output map), bound on [Multidimensional transforms](multidim-transform.md): The tensor product of the one-dimensional output maps B_{0,i}.
- $P_{s_i}$ (source axis permutation), bound on [Multidimensional transforms](multidim-transform.md): The index permutation of source axis i.
- $P_{t_i}$ (padded axis permutation), bound on [Multidimensional transforms](multidim-transform.md): The index permutation of padded axis i.
- $A_i$ (axis input map), bound on [Multidimensional transforms](multidim-transform.md): The linear input map of axis i.
- $B_{0,i}$ (axis output map), bound on [Multidimensional transforms](multidim-transform.md): The linear output map of axis i.
- $F_{q_i}$ (axis transform), bound on [Multidimensional transforms](multidim-transform.md): The one-dimensional normalized discrete Fourier transform of length q_i.
- $F_{\boldsymbol q}$ (multidimensional transform), bound on [Multidimensional transforms](multidim-transform.md): The tensor product of the axis transforms F_{q_i}.
- $X_i$ (axis operator X), bound on [Multidimensional transforms](multidim-transform.md): An operator on axis i.
- $Y_i$ (axis operator Y), bound on [Multidimensional transforms](multidim-transform.md): An operator on axis i.
- $d$ (axis count), bound on [Chinese-remainder address map](crt-map.md): The number of prime cyclic axes, with no coefficient axis counted.
- $s_i$ (axis length), bound on [Chinese-remainder address map](crt-map.md): The length of prime cyclic axis i; the s_i are pairwise coprime.
- $P_i$ (prefix product), bound on [Chinese-remainder address map](crt-map.md): The product of the axis lengths s_j with j<i.
- $\mu_i$ (coordinate exponent), bound on [Chinese-remainder address map](crt-map.md): The inverse of P_i modulo s_i, the exponent of x_i in the image of x.
- $\Phi$ (address map), bound on [Chinese-remainder address map](crt-map.md): The ring isomorphism sending x to the product of x_i^{mu_i}.
- $x_i$ (axis variable), bound on [Chinese-remainder address map](crt-map.md): The variable of axis i in the multi-axis ring.
- $k$ (coefficient index), bound on [Chinese-remainder address map](crt-map.md): A single coefficient index, an exponent of x; not an output index tuple as on the multidimensional-transform page.
- $a_j$ (mixed-radix digit), bound on [Chinese-remainder address map](crt-map.md): The digit of k of weight P_j, with 0<=a_j<s_j.
- $j$ (digit index), bound on [Chinese-remainder address map](crt-map.md): The index of an axis before axis i, in the product defining P_i, and later the index of a mixed-radix digit.
- $b_i$ (axis coordinate), bound on [Chinese-remainder address map](crt-map.md): The axis-i coordinate of Phi(x^k).
- $\ell$ (address bits), bound on [Chinese-remainder address map](crt-map.md): The number of address bits of an axis of length r.
- $T$ (padded record count), bound on [Chinese-remainder address map](crt-map.md): The number of padded records, the product of the padded axis lengths t_i.
- $\tau$ (interchange exponent), bound on [Chinese-remainder address map](crt-map.md): A fixed exponent below 1 in the chunk-interchange cost.
- $i$ (axis index), bound on [Chinese-remainder address map](crt-map.md): The index of a prime cyclic axis, from 1 to d.
- $t_i$ (padded axis length), bound on [Chinese-remainder address map](crt-map.md): The length of axis i after zero padding, a power of two between r/2 and r.
- $s$ (source length), bound on [Gaussian resampling](gaussian-resampling.md): The length of the Fourier transform being re-expressed, coprime to t.
- $t$ (transform length), bound on [Gaussian resampling](gaussian-resampling.md): The larger length, a power of two, of the transform through which the length-s transform is expressed.
- $\alpha$ (width parameter), bound on [Gaussian resampling](gaussian-resampling.md): The integer width parameter of the Gaussian weights, with 2<=alpha<sqrt p.
- $\theta$ (relative gap), bound on [Gaussian resampling](gaussian-resampling.md): The relative gap t/s-1 between the target and source lengths.
- $j$ (coordinate index), bound on [Gaussian resampling](gaussian-resampling.md): A single integer coordinate index.
- $k$ (coordinate index), bound on [Gaussian resampling](gaussian-resampling.md): A single integer coordinate index.
- $q_j$ (nearest coordinate), bound on [Gaussian resampling](gaussian-resampling.md): The integer nearest to tj/s.
- $\beta_j$ (rounding offset), bound on [Gaussian resampling](gaussian-resampling.md): The signed distance tj/s-q_j from tj/s to the nearest integer.
- $E$ (Neumann error), bound on [Gaussian resampling](gaussian-resampling.md): The map N-I, whose norm is small.
- $K$ (series term count), bound on [Gaussian resampling](gaussian-resampling.md): The number of terms of the Neumann series that are kept.
- $\beta$ (unit), bound on [Retained permutation cancellation](retained-permutations.md): A unit modulo q, an integer coprime to q, used as the multiplier of the index permutation R_beta.
- $R_\beta$ (index scaling), bound on [Retained permutation cancellation](retained-permutations.md): The permutation of a length-q vector sending z to the vector with entries z_{beta j}.
- $w$ (summation index), bound on [Retained permutation cancellation](retained-permutations.md): The index of the sum defining the transform of R_beta z.
- $w'$ (new summation index), bound on [Retained permutation cancellation](retained-permutations.md): The summation index after the substitution w' = beta w.
- $\nu$ (setup degree), bound on [Retained permutation cancellation](retained-permutations.md): A fixed exponent such that setup work per line is O(p^nu).
- $F_q^+$ (opposite transform), bound on [Retained permutation cancellation](retained-permutations.md): The discrete Fourier transform of length q with the sign of the exponent reversed.
- $z$ (transformed vector), bound on [Retained permutation cancellation](retained-permutations.md): A vector of q complex entries.
- $A$ (axis input contraction), bound on [Retained permutation cancellation](retained-permutations.md): The linear contraction applied to the input of one axis in the resampling identity.
- $B_0$ (axis output contraction), bound on [Retained permutation cancellation](retained-permutations.md): The linear contraction applied to the output of one axis in the resampling identity.
- $P_s$ (source permutation), bound on [Retained permutation cancellation](retained-permutations.md): The permutation (P_s u)_j = u_{tj} of a length-s vector.
- $P_t$ (target permutation), bound on [Retained permutation cancellation](retained-permutations.md): The permutation (P_t v)_k = v_{-sk} of a length-t vector.
- $u$ (first array), bound on [Retained permutation cancellation](retained-permutations.md): A complex array, not an integer here.
- $v$ (second array), bound on [Retained permutation cancellation](retained-permutations.md): A complex array, not an integer here.
- $a$ (round count), bound on [Retained frequency order](frequency-order.md): The number of rounds of the transform, a=log_2 t.
- $j$ (output index), bound on [Retained frequency order](frequency-order.md): The position of an output of the transform.
- $s$ (completed rounds), bound on [Retained frequency order](frequency-order.md): The number of rounds completed so far.
- $B_t$ (bit-reversal permutation), bound on [Retained frequency order](frequency-order.md): The permutation moving the entry at j to rev_a(j).
- $\mathcal H$ (parallel butterfly), bound on [Retained frequency order](frequency-order.md): The parallel butterfly applying H_0 on every participating axis in one round.
- $J_E$ (recordwise monomial), bound on [Retained frequency order](frequency-order.md): The recordwise operation multiplying each record by y^E.
- $h_p$ (grid spacing), bound on [Error tracking and exact recovery](precision-recovery.md): The grid spacing 2^{-p} of the fixed-point records.
- $L$ (log of padded length), bound on [Error tracking and exact recovery](precision-recovery.md): The base-2 logarithm of the padded length T.
- $a$ (error size), bound on [Error tracking and exact recovery](precision-recovery.md): The size of an error in grid spacings.
- $x$ (disk array), bound on [Error tracking and exact recovery](precision-recovery.md): An array in the unit disk to which a phase or chirp transform is applied.
- $u$ (scaled first digits), bound on [Error tracking and exact recovery](precision-recovery.md): The scaled digit array of the first input.
- $v$ (scaled second digits), bound on [Error tracking and exact recovery](precision-recovery.md): The scaled digit array of the second input.
- $\tau$ (interchange exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The exponent in the cost of a chunk interchange.
- $\sigma$ (growth exponent bound), bound on [Parameter and prime-length choice](parameter-choice.md): An exponent bounding the growth of recursive calls.
- $\beta$ (threshold exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The exponent setting the threshold d^beta below which active chunks are handled singly.
- $\lambda$ (overhead exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The per-node overhead exponent.
- $\lambda'$ (final cost exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The final exponent of the layer cost V d^lambda' on bit volume V.
- $V$ (bit volume), bound on [Parameter and prime-length choice](parameter-choice.md): The bit volume of the data on which the layer acts.
- $c$ (chunk-width exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The exponent of the address-chunk width; not the scaling integer of controlled shifts.
- $\epsilon$ (axis-count exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The exponent of the axis count.
- $C_1$ (guard-bit exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The exponent of the guard bits.
- $\delta$ (resampling slack), bound on [Parameter and prime-length choice](parameter-choice.md): The resampling-cost slack.
- $K$ (address-chunk width), bound on [Parameter and prime-length choice](parameter-choice.md): The width in bits of an address chunk, floor of d^c.
- $\eta$ (relative prime distance), bound on [Parameter and prime-length choice](parameter-choice.md): The smallest relative distance at which a prime s_i may lie below t_i.
- $q$ (interval integer), bound on [Parameter and prime-length choice](parameter-choice.md): An integer in the prime-interval lemma, not a radix or sequence length.
- $a_d$ (a_d constant), bound on [Parameter and prime-length choice](parameter-choice.md): Lower constant in the bound a_d p^epsilon <= d.
- $b_d$ (b_d constant), bound on [Parameter and prime-length choice](parameter-choice.md): Upper constant in the bound d <= b_d p^epsilon.
- $a_r$ (a_r constant), bound on [Parameter and prime-length choice](parameter-choice.md): Lower constant in the bound 2^(a_r p/d) <= r.
- $b_r$ (b_r constant), bound on [Parameter and prime-length choice](parameter-choice.md): Upper constant in the bound r <= 2^(b_r p/d).
- $C_\ell$ (C_ell constant), bound on [Parameter and prime-length choice](parameter-choice.md): Constant in the bound d ell <= C_ell p.
- $E$ (first space), bound on [Tensor products of subspaces](tensor-product-of-spaces.md): The first of the two finite-dimensional vector spaces being tensored.
- $G$ (second space), bound on [Tensor products of subspaces](tensor-product-of-spaces.md): The second of the two finite-dimensional vector spaces being tensored.
- $A$ (ambient space), bound on [Tensor products of subspaces](tensor-product-of-spaces.md): A finite-dimensional space with a nondegenerate form, containing the subspace P.
- $C$ (second ambient space), bound on [Tensor products of subspaces](tensor-product-of-spaces.md): A finite-dimensional space with a nondegenerate form, containing the subspace Q.
- $P$ (subspace of A), bound on [Tensor products of subspaces](tensor-product-of-spaces.md): A subspace of A, later taken nondegenerate.
- $Q$ (subspace of C), bound on [Tensor products of subspaces](tensor-product-of-spaces.md): A subspace of C.
- $B$ (orthogonal complement), bound on [Tensor products of subspaces](tensor-product-of-spaces.md): The orthogonal complement of P in A.
- $F$ (base space), bound on [Tensor products of subspaces](tensor-product-of-spaces.md): A space of dimension h with a nondegenerate form, whose triple power is the label space.
- $s$ (number of smaller calls), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The total number of smaller calls that the edges of the network cost.
- $W$ (wire count), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The number of wires of the network under consideration.
- $U$ (a label subspace), bound on [Nested subspace labels and rank deficit](subspace-labels.md): A subspace of the label space, such as the label of a vertex.
- $F$ (one-factor label space), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The space $\mathbb Q^h$ with the form $x\cdot y-\frac19(\sum_ix_i)(\sum_iy_i)$ for the bit network, or $\mathbb F_2^h$ with the dot product for the complex network.
- $x$ (vector of F), bound on [Nested subspace labels and rank deficit](subspace-labels.md): A vector of $F$, the first argument of the bilinear form.
- $y$ (vector of F), bound on [Nested subspace labels and rank deficit](subspace-labels.md): A vector of $F$, the second argument of the bilinear form.
- $t_S$ (triple indicator), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The indicator vector in $F$ of the triple $S$.
- $\mathcal F$ (ambient label space), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The space $F^{\otimes3}$, of dimension $m=h^3$, in which all labels lie.
- $X$ (X bank), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The bank of data wires $X_a$.
- $Y$ (Y bank), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The bank of data wires $Y_a$.
- $U_a$ (terminal line), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The line spanned by $t_{a_1}\otimes t_{a_2}\otimes t_{a_3}$, the source label of $X_a$.
- $L$ (total dimension loss), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The total number of dimensions lost on decreasing edges.
- $j$ (stage number), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The stage, 1, 2 or 3, whose invocations act on coordinate $a_j$.
- $A$ (exposed factor space), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The tensor product $F^{\otimes(j-1)}$ of the factors exposed before stage $j$.
- $P$ (earlier tensor line), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The line spanned by $t_{a_1}\otimes\cdots\otimes t_{a_{j-1}}$ inside $A$.
- $B$ (complement of P), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The orthogonal complement of $P$ inside $A$.
- $K$ (later tensor line), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The line spanned by $t_{a_{j+1}}\otimes\cdots\otimes t_{a_3}$, tensored onto every label of stage $j$.
- $A'$ (next exposed space), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The next stage's $A$, equal to $A\otimes F$.
- $P'$ (next earlier line), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The next stage's $P$, equal to $P\otimes\langle t_{a_j}\rangle$.
- $B'$ (next complement), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The next stage's $B$, the orthogonal complement of $P'$ in $A'$.
- $K'$ (next later line), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The next stage's $K$, with $K=\langle t_{a_{j+1}}\rangle\otimes K'$.
- $t_X$ (X-bank indicator), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The indicator of the X-bank triple of a gate or side wire in one invocation.
- $t_Y$ (Y-bank indicator), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The indicator of the Y-bank triple of a gate or side wire in one invocation.
- $L_{\rm b}$ (bit dimension loss), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The total dimension lost on decreasing edges of the bit network.
- $L_{\rm c}$ (complex dimension loss), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The total dimension lost on decreasing edges of the complex network.
- $\Pi_U$ (projection onto a label), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The rational projection onto the label $U$ along $U^\perp$, the matrix of a bit-network vertex labelled $U$.
- $V$ (larger label), bound on [Nested subspace labels and rank deficit](subspace-labels.md): A label containing the label $U$ at the other end of an edge.
- $s_{\rm b}$ (bit smaller calls), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The number of smaller calls, the total rational rank of edge matrix differences, in the bit network.
- $s_{\rm c}$ (complex smaller calls), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The number of smaller calls, the total number of phase kernels, in the complex network.
- $f$ (call parameter), bound on [Recursive power saving](rank-recurrence.md): The parameter of a recursive call: the number of digits per interchanged chunk, or the number of selected axes of a layer.
- $\mathcal C$ (time per unit volume), bound on [Recursive power saving](rank-recurrence.md): The running time of a call at a given parameter, divided by the volume of its stream.
- $j$ (recursion depth), bound on [Recursive power saving](rank-recurrence.md): The number of recursion levels below the top call, indexing the terms of the unrolled sum; here not the stage number of the subspace-labels page.
- $\eta$ (relative rank deficit), bound on [Recursive power saving](rank-recurrence.md): The relative deficit (Wm-s)/(Wm) by which the number of smaller calls falls short of Wm.
- $u$ (chunk width), bound on [Fast address-chunk interchange](address-interchange.md): The number of bits in each of the two address chunks.
- $p$ (address prefix), bound on [Fast address-chunk interchange](address-interchange.md): The prefix field of an address, before the first chunk.
- $h$ (first chunk), bound on [Fast address-chunk interchange](address-interchange.md): The first of the two address chunks being interchanged.
- $d$ (second chunk), bound on [Fast address-chunk interchange](address-interchange.md): The second of the two address chunks being interchanged.
- $g$ (gap), bound on [Fast address-chunk interchange](address-interchange.md): The address field between the two chunks.
- $z$ (suffix), bound on [Fast address-chunk interchange](address-interchange.md): The address field after the second chunk.
- $q$ (digit radix), bound on [Fast address-chunk interchange](address-interchange.md): The fixed prime radix of the stored digits.
- $\tau$ (saving exponent), bound on [Fast address-chunk interchange](address-interchange.md): The exponent below 1 in the interchange cost, equal to 1 - 2^{-50}.
- $e$ (digit count), bound on [Fast address-chunk interchange](address-interchange.md): The number of radix-q digits in each chunk.
- $k$ (recursion levels), bound on [Fast address-chunk interchange](address-interchange.md): The number of recursion levels, with e = m^k.
- $M$ (vertex matrix), bound on [Fast address-chunk interchange](address-interchange.md): The rational m by m matrix carried by a terminal or gate of the network.
- $A_i$ (edge matrix), bound on [Fast address-chunk interchange](address-interchange.md): The difference of the matrices at the two ends of edge i.
- $\rho$ (output role), bound on [Fast address-chunk interchange](address-interchange.md): The output role to which input wire w is routed.
- $w$ (wire index), bound on [Fast address-chunk interchange](address-interchange.md): The index of an input wire of the network.
- $\Phi_M$ (address shear), bound on [Fast address-chunk interchange](address-interchange.md): The array permutation moving the entry at address (H,D) to (H+MD,D).
- $f_w$ (wire input), bound on [Fast address-chunk interchange](address-interchange.md): The physical input array of wire w.
- $x$ (stream row number), bound on [Fast address-chunk interchange](address-interchange.md): The row number within a role stream.
- $j$ (recursion level index), bound on [Fast address-chunk interchange](address-interchange.md): An index of a recursion level in the unrolled sum.
- $k'$ (levels needed), bound on [Fast address-chunk interchange](address-interchange.md): The number of recursion levels needed for chunks of e digits.
- $\nu$ (set-aside digits), bound on [Fast address-chunk interchange](address-interchange.md): The number of top digits of each chunk set aside to form the row field.
- $\Lambda$ (row range), bound on [Fast address-chunk interchange](address-interchange.md): The range of the row field formed by the top digits of both chunks.
- $\Lambda'$ (padded row count), bound on [Fast address-chunk interchange](address-interchange.md): The row count after padding with zero rows to a multiple of W^{k'}.
- $a_j$ (piece count), bound on [Fast address-chunk interchange](address-interchange.md): The number of pieces of width m^j into which each remaining chunk is cut.
- $v$ (binary vector), bound on [Binary phase frames](phase-frames.md): A binary vector in F_2^m (not the number of triples).
- $E$ (edge residual), bound on [Binary phase frames](phase-frames.md): The edge residual of an edge: the orthogonal summand added going from U to V (not a tensor factor).
- $k$ (column count), bound on [Binary phase frames](phase-frames.md): The number of columns of data, so that an address is a k-tuple (not a depth).
- $u$ (binary vector), bound on [Binary phase frames](phase-frames.md): A binary vector in F_2^m (not an input sequence).
- $w$ (binary vector), bound on [Binary phase frames](phase-frames.md): A binary vector in F_2^m.
- $z$ (binary vector), bound on [Binary phase frames](phase-frames.md): A binary vector in F_2^m.
- $\operatorname{supp}$ (support), bound on [Binary phase frames](phase-frames.md): The set of coordinates where a binary vector is 1.
- $\operatorname{wt}$ (Hamming weight), bound on [Binary phase frames](phase-frames.md): The Hamming weight: the number of coordinates where a binary vector is 1.
- $P_U$ (projection), bound on [Binary phase frames](phase-frames.md): The projection onto a label U over F_2.
- $X_v$ (translation by v), bound on [Binary phase frames](phase-frames.md): The translation of functions of x by the binary vector v.
- $q_U$ (weight phase exponent), bound on [Binary phase frames](phase-frames.md): The Hamming weight of P_U x, modulo four.
- $\mathcal C_U$ (phase frame), bound on [Binary phase frames](phase-frames.md): The phase frame of the label U.
- $\mathcal B$ (orthonormal basis), bound on [Binary phase frames](phase-frames.md): An orthonormal basis of the edge residual E.
- $\varepsilon$ (edge phase sign), bound on [Binary phase frames](phase-frames.md): The sign, plus or minus one modulo four, of one basis vector's phase term, including the edge direction.
- $Z$ (sign matrix), bound on [Binary phase frames](phase-frames.md): The diagonal matrix diag(1,-1).
- $Z_{a,k}$ (sign operator), bound on [Binary phase frames](phase-frames.md): Z on the 27 coordinates of supp(u) in every column, the identity elsewhere.
- $c$ (control bit), bound on [Packed selected-bit addition](packed-bit-addition.md): A control bit, equal to 0 or 1, that gates each addition.
- $u$ (first integer), bound on [Packed selected-bit addition](packed-bit-addition.md): One of the two integers whose parities the eight additions act on.
- $w$ (second integer), bound on [Packed selected-bit addition](packed-bit-addition.md): The other integer, an arbitrary auxiliary value that is restored.
- $R$ (record bits), bound on [Packed selected-bit addition](packed-bit-addition.md): The number of bits in the record stored at each address.
- $L$ (chunk width), bound on [Packed selected-bit addition](packed-bit-addition.md): The number of bits in each of the chunks x, y, z, equal to fK.
- $K$ (segment spacing), bound on [Packed selected-bit addition](packed-bit-addition.md): The number of bits between consecutive selected positions, at least 6.
- $f$ (selected-bit count), bound on [Packed selected-bit addition](packed-bit-addition.md): The number of selected bits.
- $M$ (address count), bound on [Packed selected-bit addition](packed-bit-addition.md): The number of addresses.
- $V$ (array volume), bound on [Packed selected-bit addition](packed-bit-addition.md): The total number of bits M times R.
- $A_{\rm rect}$ (counter length), bound on [Packed selected-bit addition](packed-bit-addition.md): An upper bound on the bits of the counters, the ceiling of log2(2V).
- $\rho$ (offset), bound on [Packed selected-bit addition](packed-bit-addition.md): The offset of the first selected position within a segment spacing.
- $j_i$ (selected position), bound on [Packed selected-bit addition](packed-bit-addition.md): The i-th selected bit position, rho plus iK.
- $\mathcal B$ (exceptional set), bound on [Packed selected-bit addition](packed-bit-addition.md): The set of addresses at which some guard value falls outside the safe interval.
- $S_0$ (packed map), bound on [Packed selected-bit addition](packed-bit-addition.md): The composition of the eight packed cyclic shifts.
- $T_0$ (ideal map), bound on [Packed selected-bit addition](packed-bit-addition.md): The ideal permutation that performs the required XORs and fixes all other coordinates.
- $D$ (selected chunk count), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The number of selected address chunks.
- $e$ (selected axis count), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The number of selected axes in a group.
- $z$ (array), bound on [Simultaneous butterfly layer](simultaneous-layer.md): An array acted on by the diagonal operator.
- $\mathcal S_D$ (diagonal phase operator), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The diagonal operator multiplying the value at address x by i to the sum of the selected bits.
- $\Gamma$ (basis-change matrix), bound on [Simultaneous butterfly layer](simultaneous-layer.md): An invertible F_2 matrix whose first columns are the residual basis vectors.
- $\mathcal P_\Gamma$ (address permutation), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The address permutation moving the value at x to Gamma x.
- $\xi$ (residual basis index), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The index of the residual basis vectors.
- $\eta_\xi$ (edge sign), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The sign plus or minus one of the xi-th residual basis vector's exponent.
- $\mathbf 1_\xi$ (standard basis vector), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The xi-th standard basis vector.
- $q_0$ (individual chunk count), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The number of leading chunks given individual C kernels.
- $\chi$ (operation-chain bound), bound on [Simultaneous butterfly layer](simultaneous-layer.md): A bound on the arithmetic operations on a chain from an input to an intermediate coefficient.
- $E$ (invocation operation bound), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The bound on arithmetic operations in one invocation of the network.
- $\Psi$ (level growth factor), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The sum s plus E, the factor by which each internal level multiplies the chain bound.
- $\varphi$ (chain bound), bound on [Simultaneous butterfly layer](simultaneous-layer.md): Any bound on a chain's operation count that is at least one.
- $\vartheta$ (exponent), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The least positive exponent j with m to the j at least Psi.
- $C_0$ (guard constant), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The constant 128 m Psi squared in the reserved extra bits Delta.
- $D$ (transformed axis count), bound on [Tape layout for synthetic transforms](transform-layout.md): The number of transformed axes, d-1.
- $b$ (leftover low bits), bound on [Tape layout for synthetic transforms](transform-layout.md): The number of leftover low bits of an axis.
- $q$ (whole chunks), bound on [Tape layout for synthetic transforms](transform-layout.md): The number of whole K-bit chunks of an axis.
- $B$ (bit reversal), bound on [Tape layout for synthetic transforms](transform-layout.md): The bit-reversal permutation applied along every axis.
- $L$ (layout permutation), bound on [Tape layout for synthetic transforms](transform-layout.md): The record permutation defined by the prefix moves and chunk exchanges.
- $z$ (round input), bound on [Tape layout for synthetic transforms](transform-layout.md): The array entering a round of the transform.
- $\tau$ (interchange exponent), bound on [Tape layout for synthetic transforms](transform-layout.md): The fixed exponent below 1 in the chunk interchange cost.
- $\lambda'$ (layer exponent), bound on [Tape layout for synthetic transforms](transform-layout.md): The fixed exponent below 1 in the simultaneous layer cost.
- $P$ (pointwise product), bound on [Convolution from the retained transform layout](ring-convolution.md): The pointwise product P(u,v)=uv/r of two arrays over the ring.
- $L$ (layout permutation), bound on [Convolution from the retained transform layout](ring-convolution.md): The permutation of records defined by the tape layout of the transforms.
- $B$ (bit-reversal order), bound on [Convolution from the retained transform layout](ring-convolution.md): The bit-reversal order applied along every axis.
- $\eta$ (truncation error bound), bound on [Convolution from the retained transform layout](ring-convolution.md): The bound sqrt2 times 2^{-p} on the change made by truncation to p fractional bits.
- $b$ (digit width), bound on [The multiplication algorithm](multiplication-algorithm.md): The number of bits in one radix digit.
- $a_j$ (radix digit), bound on [The multiplication algorithm](multiplication-algorithm.md): The j-th radix-2^b digit of an input.
- $F_{\boldsymbol s}$ (source transform), bound on [The multiplication algorithm](multiplication-algorithm.md): The discrete Fourier transform on the prime axes s_i, normalized by 1/S.
- $F_{\boldsymbol s}^+$ (opposite source transform), bound on [The multiplication algorithm](multiplication-algorithm.md): The source transform with the opposite sign in the exponent.
- $\widetilde a$ (computed chirp), bound on [The multiplication algorithm](multiplication-algorithm.md): The grid approximation of the chirp a.
- $x_0$ (first-phase operand), bound on [The multiplication algorithm](multiplication-algorithm.md): The data operand after the first phase of the computed chirp transform.
- $y_0$ (chirp convolution), bound on [The multiplication algorithm](multiplication-algorithm.md): The computed convolution of the approximate chirp with the data operand.
- $\widetilde{\mathcal M}_{\mathbb C}$ (computed convolution), bound on [The multiplication algorithm](multiplication-algorithm.md): The computed normalized complex cyclic convolution.
- $R$ (source permutation), bound on [The multiplication algorithm](multiplication-algorithm.md): The retained permutation of coordinates from resampling.
- $\widetilde{\mathscr F}^{+}$ (computed opposite transform), bound on [The multiplication algorithm](multiplication-algorithm.md): The computed source transform with the opposite exponent sign.
- $z$ (product array), bound on [The multiplication algorithm](multiplication-algorithm.md): The array given to the opposite transform: the truncated pointwise product of the two computed source transforms.
- $u$ (source array), bound on [The multiplication algorithm](multiplication-algorithm.md): The first source array of grid values.
- $v$ (source array), bound on [The multiplication algorithm](multiplication-algorithm.md): The second source array of grid values.
- $w$ (scaled exact array), bound on [The multiplication algorithm](multiplication-algorithm.md): The exact array (u*v)/S.
- $\widetilde w$ (computed scaled array), bound on [The multiplication algorithm](multiplication-algorithm.md): The computed approximation of w after multiplying by S.
- $V$ (volume), bound on [Cost accounting and the exponent κ](cost-accounting.md): The number of stored bits of the T coefficients of p bits, equal to Tp and Theta(n); not the larger label of the subspace-label pages.
- $g_i$ (margin), bound on [Cost accounting and the exponent κ](cost-accounting.md): The distance below one of the exponent of p in the i-th dominant normalized cost, so the cost is p^{1-g_i}.
- $A$ (visit exponent), bound on [Cost accounting and the exponent κ](cost-accounting.md): A fixed exponent such that the recursions make at most p^A visits; not the shear matrix or a space of earlier pages.
- $C$ (setup exponent), bound on [Cost accounting and the exponent κ](cost-accounting.md): A fixed exponent such that descriptor setup takes at most p^C steps per visit; not the two-point kernel or selection map of earlier pages.
- $V_{\rm call}$ (call volume), bound on [Cost accounting and the exponent κ](cost-accounting.md): The volume of one packed change of basis.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Cost accounting and the exponent κ](cost-accounting.md): Dividing each cost by V = Tp, the dominant terms are powers of p below one with minimum margin 2^{-181} = 2κ, giving total time O(n(lg n)^{1−κ}).
  Shown as: Power-saving integer multiplication *<predicate>* Cost accounting and the exponent κ
- [The multiplication algorithm](multiplication-algorithm.md): Digits, then the CRT map, two forward transforms with resampling and chirps, a pointwise product, the opposite transform, rescaling, rounding and carry propagation yield the exact 2n-bit product.
  Shown as: Power-saving integer multiplication *<predicate>* The multiplication algorithm
- [Schönhage–Strassen optimality conjecture](conjecture.md): The 1971 proposal that n log n is the optimal order of growth for multiplying n-bit integers on a multitape Turing machine.
  Shown as: Power-saving integer multiplication *<predicate>* Schönhage–Strassen optimality conjecture

## Other pages you may link to

- [Polynomial ring modulo y^r + 1](ring-y.md)
- [Fixed finite-tape machine model](machine-model.md)
- [Fixed-point Gaussian dyadic records](fixed-point.md)
- [Linear exchange network with restored scratch wires](exchange-network.md)
- [Frames on wire arrays](array-frames.md)
- [Cyclic convolution](convolution.md)
- [Multiplication as radix-digit convolution](radix-digit-reduction.md)
- [Phase twist](phase-twist.md)
- [Discrete Fourier transform](dft.md)
- [Butterflies and the fast transform](butterfly.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Elementary stream operations](stream-ops.md)
- [Bluestein chirp identity](chirp.md)
- [Established O(n log n) multiplier](hvdh-multiplier.md)
- [Signed packing](signed-packing.md)
- [Controlled shifts and rational scalings](controlled-shifts.md)
- [Matrix shear by triangular factorization](matrix-shear.md)
- [Two-point kernel C](phase-kernel.md)
- [Contractions and bilinear contractions](contraction-maps.md)
- [Multidimensional transforms](multidim-transform.md)
- [Chinese-remainder address map](crt-map.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Retained permutation cancellation](retained-permutations.md)
- [Retained frequency order](frequency-order.md)
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

## Evidence from the sources, with the paragraph around each quote

- "There is one deterministic Turing machine $A$, with a fixed finite" (paper)

  > \begin{theorem}\label{thm:main} There is one deterministic Turing machine $A$, with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, that computes this exact product for every $n\ge1$ and every pair of $n$-bit inputs. Its worst-case running time satisfies \[ T_A(n)=O\!\left(n(\lg n)^{1-\kappa}\right), \qquad \kappa=2^{-182}. \] \end{theorem}

- "disproves the $n\log n$ optimality conjecture" (paper)

  > \documentclass[11pt]{article} \usepackage[T1]{fontenc} \usepackage{lmodern,microtype} \usepackage{amsmath,amssymb,amsthm,mathrsfs,mathtools,booktabs,array,longtable} \usepackage[margin=1in]{geometry} \usepackage{tikz} \usetikzlibrary{positioning,arrows.meta} \usepackage[hyphens]{url} \usepackage{hyperref} \hypersetup{colorlinks=true,linkcolor=blue!45!black,citecolor=blue!45!black,urlcolor=blue!45!black,pdftitle={Integer multiplication below n log n},pdfauthor={OpenAI}} \pdfinfoomitdate=1 \pdftrailerid{} \pdfsuppressptexinfo=15 \newtheorem{theorem}{Theorem} \newtheorem{lemma}[theorem]{Lemma} \newtheorem{proposition}[theorem]{Proposition} \newtheorem{corollary}[theorem]{Corollary} \theoremstyle{definition} \newtheorem{definition}[theorem]{Definition} \newtheorem{remark}[theorem]{Remark} \newcommand{\norm}[1]{\lVert#1\rVert_\infty} \title{Integer multiplication below \texorpdfstring{$n\log n$}{n log n}} \author{OpenAI} \date{September 23, 2026} \begin{document} \maketitle \begin{abstract} We give a deterministic algorithm that multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ worst-case time, with $\kappa=2^{-182}$, on one fixed finite-alphabet Turing machine with a fixed finite number of one-dimensional tapes. The algorithm is exact for every input length and disproves the $n\log n$ optimality conjecture of Sch\"onhage and Strassen in this model. \end{abstract} \tableofcontents \clearpage \section{Introduction}


## Sources (read from disk as needed)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- A simulated reader (reader) trying to answer "Why does kappa equal 2^-182 and not some larger constant? Which part of the cost accounting fixes it, and why is the margin taken to be twice kappa?" got stuck at "Remaining factors are fixed powers of $\log p$, which are below $p^{\kappa}$ for large $p$, so the normalized total is $O(p^{1-\kappa})$": Same gap as on the cost page: the page says 'the rest is absorbed' and then asserts that the remaining factors are fixed powers of log p, without saying where they come from. I followed the arithmetic (p^(1-2 kappa) times p^kappa is p^(1-kappa)) but could not check that the factors are of this form. (stuck at the step level)
- A simulated reader (reader) trying to answer "Summarise in a few sentences what the main theorem says about multiplying two n-bit integers, in which machine model it holds, which earlier conjecture it refutes, and the overall plan the proof follows to get there." got stuck at "Beating that needs cheaper address movement and cheaper butterfly arithmetic": The page says the log factor can only be beaten by cheaper address movement and cheaper butterfly arithmetic. I could see that n log n comes from scanning n bits at each of log n layers, but not why these two are the only levers, or why cheaper address movement removes the log factor. I accepted the claim without seeing the link. (the reader followed the steps but not why they lead where they do: say what this step is for)
- A simulated reader (reader) trying to answer "Why can the log n factor in n log n only be beaten here by making address movement and butterfly arithmetic cheaper, rather than by some other tweak of a standard FFT-style multiplier? What accounting of a standard transform on a tape machine leads to this?" got stuck at "Beating that needs cheaper address movement and cheaper butterfly arithmetic": The page asserts that only cheaper address movement and cheaper butterfly arithmetic can beat the bound. No page I opened argues that other changes, such as fewer layers or another radix, cannot also cut the cost per layer. I could not tell whether this is a claim or a consequence. (stuck at the statement level)
- A simulated reader (reader) trying to answer "Why does kappa equal 2^-182 and not some larger constant? Which part of the cost accounting fixes it, and why is the margin taken to be twice kappa?" got stuck at "$\kappa=2^{-182}$, the exponent saved from the power of $\lg n$": The value of kappa is given with no reason for it. Its origin (half of the smallest margin) is only found on the Cost accounting and the exponent κ page. (stuck at the statement level)
- A simulated reader (reader) trying to answer "Why does kappa equal 2^-182 and not some larger constant? Which part of the cost accounting fixes it, and why is the margin taken to be twice kappa?" got stuck at "the interchange of address chunks and the [Simultaneous butterfly layer](tiz)": The name Simultaneous butterfly layer is a term I could not decode. I did not open its page. It is the layer primitive with margin g_3 = 2^-129, which is not the minimum, so it does not change the answer. (stuck at the symbol level)
- A simulated reader (reader) trying to answer "Summarise in a few sentences what the main theorem says about multiplying two n-bit integers, in which machine model it holds, which earlier conjecture it refutes, and the overall plan the proof follows to get there." got stuck at "Scanning $\Theta(n)$ stored bits at each of $\Theta(\log n)$ [Butterflies and the fast transform](bog) already costs $\Theta(n\log n)$. Beating that needs cheaper address movement and cheaper butterfly arithmetic": I could see that a log-n-layer transform costs n log n, so beating it means cheaper moves and butterflies. The page does not say why cheaper moves and butterflies are enough; I only saw the mechanism on the later tape-primitive pages. (the reader followed the steps but not why they lead where they do: say what this step is for)

## Previous version (revise it)

It has 436 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 545 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

Power-saving integer multiplication is the main result: for $n$, the number of bits in each input, and $\kappa=2^{-182}$, the exponent saved from the power of $\lg n$, a fixed Turing machine multiplies two $n$-bit integers exactly in time $O(n(\lg n)^{1-\kappa})$, which is $o(n\log n)$, so it refutes the [Schönhage–Strassen optimality conjecture](conjecture.md) in this model.

The machine is one deterministic Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, and is correct for every $n\ge1$ <cite data-source="paper">There is one deterministic Turing machine $A$, with a fixed finite</cite>. The saving is positive, however small: $(\lg n)^{1-\kappa}=\lg n/(\lg n)^{\kappa}$ and $(\lg n)^{\kappa}\to\infty$.

## Why the usual route stalls

Scanning $\Theta(n)$ stored bits at each of $\Theta(\log n)$ transform levels already costs $\Theta(n\log n)$. Beating that needs cheaper address movement and cheaper butterfly arithmetic <cite data-source="paper">We therefore need savings in both movement and arithmetic.</cite>

## How the saving is built

1. Two tape primitives, the interchange of address chunks and the simultaneous butterfly layer, are built from fixed finite linear networks. Each costs the data volume times a power below one of its width, by [Recursive power saving](rank-recurrence.md).
2. These speed up the synthetic transforms over $\mathbb C[y]/(y^r+1)$ ([Tape layout for synthetic transforms](transform-layout.md)) and the ring convolution built on them ([Convolution from the retained transform layout](ring-convolution.md)).
3. Gaussian resampling and Bluestein chirps turn the prime-length transforms into these power-of-two transforms, with permutations cancelled rather than sorted ([Retained permutation cancellation](retained-permutations.md)).
4. The exact $2n$-bit product is assembled by [The multiplication algorithm](multiplication-algorithm.md) from radix digits, two forward transforms, a pointwise product, the opposite transform, rescaling, rounding and carries, with total error below $1/2$.

## Totaling the cost

[Cost accounting and the exponent κ](cost-accounting.md) totals the running time as follows, dividing every cost by $V=Tp=\Theta(n)$, the number of stored bits, where $T$ counts coefficients and $p$, of order $\lg n$, is the precision in bits of each. The axis count is $d=\Theta(p^{\epsilon})$ and the chunk width $K=\lfloor d^{c}\rfloor$, with fixed exponents $\epsilon$ and $c$ from [Parameter and prime-length choice](parameter-choice.md); here $c$ is not the machine constant, the scaling integer, the control bit or the unit of earlier pages. The seven dominant normalized costs are powers of $p$:
$$p^{\epsilon(1+c)},\quad p^{1-\epsilon c(1-\tau)},\quad p^{1-\epsilon(1-\lambda')},\quad p^{\tau+\epsilon(2-\tau)},\quad p^{3/4+\delta+3\epsilon/2},\quad p^{\epsilon+\delta},\quad p^{1-\epsilon}.$$
They come from prefix moves and single butterfly rounds ($dK$), chunk exchanges ($pK^{\tau-1}$), simultaneous butterfly rounds ($\ell d^{\lambda'}$, with $\ell$ the address bits of a long axis), Chinese-remainder and axis layouts, Gaussian line maps, chirps and twists, and packed ring products ($\log(rp)$). The rest is absorbed.

The margin $g_i$ of the $i$-th term is one minus its exponent. The fixed parameters are $\tau=1-2^{-50}$, $\lambda'=1-2^{-54}$, $c=2^{-56}$, $\delta=1/16$ and $\epsilon=2^{-75}$ <cite data-source="paper">\epsilon=2^{-75},\qquad \kappa=2^{-182}.</cite>. The smallest margin belongs to chunk exchanges:
$$g_2=\epsilon c(1-\tau)=2^{-75}\cdot2^{-56}\cdot2^{-50}=2^{-181}=2\kappa,$$
and the other margins are larger <cite data-source="paper">Thus $\min_i g_i=2^{-181}=2\kappa$.</cite>

So every dominant term is at most $p^{1-2\kappa}$. Remaining factors are fixed powers of $\log p$, which are below $p^{\kappa}$ for large $p$, so the normalized total is $O(p^{1-\kappa})$ and the time is $O(Vp^{1-\kappa})=O(n(\lg n)^{1-\kappa})$.

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

Write the body to `exegenius/tasks/0386-write-main-result.answer.md` and the JSON to `exegenius/tasks/0386-write-main-result.answer.json`, then run `exegenius submit 0386-write-main-result` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0386-write-main-result`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
