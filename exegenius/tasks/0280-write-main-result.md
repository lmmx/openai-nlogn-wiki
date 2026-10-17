# exegenius task 0280-write-main-result

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
- $c$ (machine constant), bound on [Schönhage–Strassen optimality conjecture](conjecture.md): A positive constant, depending on the machine, in the lower bound c n log n.
- $\kappa$ (power saving), bound on [Schönhage–Strassen optimality conjecture](conjecture.md): A fixed positive constant by which the exponent of the logarithm is lowered.
- $p$ (fractional bits), bound on [Fixed-point Gaussian dyadic records](fixed-point.md): The number of fractional bits of the grid on which stored values lie.
- $k$ (depth), bound on [Fixed-point Gaussian dyadic records](fixed-point.md): The number of operations in sequence since the layer began that produced a value.
- $\Delta$ (reserved extra bits), bound on [Fixed-point Gaussian dyadic records](fixed-point.md): The number of extra bits reserved, at least the maximal depth reached in the layer.
- $Q_p$ (truncation), bound on [Fixed-point Gaussian dyadic records](fixed-point.md): The truncation that drops the bits below 2^{-p} in each real and imaginary part, returning a record to the p-bit grid.
- $h$ (ground-set size), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The size of the ground set [h] whose three-element subsets index the data.
- $\mathcal T$ (triple set), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The set of three-element subsets of [h].
- $v$ (number of triples), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of three-element subsets of [h].
- $X$ (bank X), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The first data bank, with entries X_a.
- $Y$ (bank Y), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The second data bank, with entries Y_a.
- $a$ (bank index), bound on [Linear exchange network with restored scratch wires](exchange-network.md): A triple of three-element subsets of [h] indexing the bank entries (not a shift exponent here).
- $N$ (bank size), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of entries in each data bank.
- $m$ (label dimension), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The dimension of the label space used on later pages.
- $S$ (slice index), bound on [Linear exchange network with restored scratch wires](exchange-network.md): A three-element subset of [h]: the varying coordinate of a within a slice.
- $x_S$ (source value), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The entry of the source bank at slice index S.
- $y_S$ (target value), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The entry of the target bank at slice index S.
- $C_i$ (central wire), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The central wire for the element i of [h].
- $S'$ (other triple), bound on [Linear exchange network with restored scratch wires](exchange-network.md): Another three-element subset in the same slice.
- $A_{SS'}$ (side wire), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The scratch wire for the ordered neighbour pair (S,S').
- $\sigma$ (initial side values), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The initial values of the side wires.
- $\gamma$ (initial central values), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The initial values of the central wires.
- $\mathcal V$ (copy map), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The linear map copying source values onto side wires.
- $\mathcal G$ (gather map), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The linear map gathering source values onto central wires.
- $\mathcal J$ (injection map), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The linear map injecting side wires into the target.
- $\mathcal R$ (scatter map), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The linear map scattering central wires into the target.
- $I$ (number of invocations), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of invocations in the three stages.
- $z_{\rm b}$ (bit neighbour count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of neighbours of a fixed triple in the bit construction.
- $z_{\rm c}$ (complex neighbour count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of neighbours of a fixed triple in the complex construction.
- $c_{\rm b}$ (bit central wires), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of central wires per invocation in the bit network.
- $c_{\rm c}$ (complex central wires), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of central wires per invocation in the complex network.
- $W_{\rm b}$ (bit wire count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The total number of wires in the bit network.
- $W_{\rm c}$ (complex wire count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The total number of wires in the complex network.
- $R$ (scalar ring), bound on [Frames on wire arrays](array-frames.md): The ring of scalars carried by the wires.
- $\Omega$ (address set), bound on [Frames on wire arrays](array-frames.md): A finite set of addresses indexing every array.
- $D_v$ (frame), bound on [Frames on wire arrays](array-frames.md): The invertible R-linear operator on R^Omega assigned to a source, gate or sink v.
- $t$ (gate input count), bound on [Frames on wire arrays](array-frames.md): The number of input arrays of a gate.
- $q$ (sequence length), bound on [Cyclic convolution](convolution.md): The number of entries in each of the two sequences being convolved.
- $d$ (axis count), bound on [Cyclic convolution](convolution.md): The number of axes of an array, counting the d-1 cyclic axes plus the coefficient axis.
- $t_i$ (axis length), bound on [Cyclic convolution](convolution.md): The length of cyclic axis i.
- $M$ (address count), bound on [Cyclic convolution](convolution.md): The number of cyclic addresses of an array, the product of the axis lengths.
- $T$ (coefficient count), bound on [Cyclic convolution](convolution.md): The total number of complex coefficients in an array.
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
- $V$ (array volume), bound on [Elementary stream operations](stream-ops.md): The number of radix-q digits an array stores.
- $q$ (radix), bound on [Elementary stream operations](stream-ops.md): The number of values one digit can take.
- $P$ (prefix values), bound on [Elementary stream operations](stream-ops.md): The number of prefix values indexing the first axis of the array.
- $R$ (row count), bound on [Elementary stream operations](stream-ops.md): The number of rows in the array of item 4.
- $B$ (entries per row), bound on [Elementary stream operations](stream-ops.md): The number of entries in each row.
- $W$ (stream count), bound on [Elementary stream operations](stream-ops.md): The fixed number of streams the rows are dealt into.
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
- $q$ (prime modulus base), bound on [Controlled shifts and rational scalings](controlled-shifts.md): A fixed prime; on this page it is not a sequence length.
- $b$ (field digit count), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The number of base-$q$ digits of a field.
- $Q$ (field value count), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The number of values a field can take, q^b.
- $a$ (offset), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The offset in [Q] added to the target field, prepared from the control values.
- $B$ (suffix bit count), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The number of bits following the target field.
- $c$ (scaling integer), bound on [Controlled shifts and rational scalings](controlled-shifts.md): A fixed positive integer prime to q by which the target field is multiplied; not the machine constant.
- $j$ (wrap count), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The integer part of cy/Q, counting how often cy wraps past Q.
- $y'$ (new position), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The position cy-jQ to which the block at position y is sent.
- $c'$ (unit denominator), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The positive integer prime to q in the denominator of a rational unit c/c'.
- $m$ (fields per group), bound on [Matrix shear by triangular factorization](matrix-shear.md): The number of fields in each of the groups H and D.
- $a$ (rank of A), bound on [Matrix shear by triangular factorization](matrix-shear.md): The rank of the rational matrix A.
- $A$ (shear matrix), bound on [Matrix shear by triangular factorization](matrix-shear.md): A rational m by m matrix, taken from a fixed finite set, that the shear applies.
- $H$ (target group), bound on [Matrix shear by triangular factorization](matrix-shear.md): The first group of m fields, which receives AD.
- $D$ (source group), bound on [Matrix shear by triangular factorization](matrix-shear.md): The second group of m fields, which is left unchanged by the shear.
- $a$ (kernel coefficient a), bound on [Two-point kernel C](phase-kernel.md): The complex constant (1+i)/2, the coefficient of the identity in C.
- $b$ (kernel coefficient b), bound on [Two-point kernel C](phase-kernel.md): The complex constant (1-i)/2, the coefficient of the bit flip in C.
- $I$ (identity matrix), bound on [Two-point kernel C](phase-kernel.md): The 2 by 2 identity matrix.
- $X$ (bit flip), bound on [Two-point kernel C](phase-kernel.md): The 2 by 2 matrix swapping the two entries of a pair.
- $C$ (two-point kernel), bound on [Two-point kernel C](phase-kernel.md): The 2 by 2 matrix aI+bX.
- $\mathsf S$ (phase matrix), bound on [Two-point kernel C](phase-kernel.md): The diagonal matrix diag(1,i) multiplying the second entry of a pair by i.
- $H$ (normalized Hadamard matrix), bound on [Two-point kernel C](phase-kernel.md): The matrix sqrt(2) H_0, symmetric with H squared equal to the identity.
- $H_0$ (two-point butterfly), bound on [Two-point kernel C](phase-kernel.md): The matrix (1/2)[[1,1],[1,-1]] of the averaging and differencing step on a pair.
- $L$ (linear map), bound on [Contractions and bilinear contractions](contraction-maps.md): A linear map whose norm bound is being defined.
- $\mathcal M$ (bilinear map), bound on [Contractions and bilinear contractions](contraction-maps.md): A map linear in each of its two operands.
- $f$ (first operand), bound on [Contractions and bilinear contractions](contraction-maps.md): The first operand of the bilinear map.
- $g$ (second operand), bound on [Contractions and bilinear contractions](contraction-maps.md): The second operand of the bilinear map.
- $u'$ (computed input), bound on [Contractions and bilinear contractions](contraction-maps.md): A computed approximation replacing the exact input u.
- $f'$ (perturbed first operand), bound on [Contractions and bilinear contractions](contraction-maps.md): A perturbed replacement for the operand f.
- $g'$ (perturbed second operand), bound on [Contractions and bilinear contractions](contraction-maps.md): A perturbed replacement for the operand g.
- $F_q$ (normalized transform), bound on [Contractions and bilinear contractions](contraction-maps.md): The normalized discrete Fourier transform on sequences of q entries.
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
- $S$ (convolution length), bound on [Chinese-remainder address map](crt-map.md): The length of the cyclic convolution, the product of the s_i.
- $d$ (number of axes), bound on [Chinese-remainder address map](crt-map.md): The number of axes of the target ring.
- $i$ (axis index), bound on [Chinese-remainder address map](crt-map.md): The index of an axis, from 1 to d.
- $s_i$ (axis source length), bound on [Chinese-remainder address map](crt-map.md): The length of axis i, pairwise coprime with the others; unrelated to the s_i of the chirp page.
- $P_i$ (prefix product), bound on [Chinese-remainder address map](crt-map.md): The product of the lengths s_j of the axes before axis i.
- $\mu_i$ (coordinate exponent), bound on [Chinese-remainder address map](crt-map.md): The inverse of P_i modulo s_i.
- $x_i$ (axis variable), bound on [Chinese-remainder address map](crt-map.md): The polynomial variable of axis i, with x_i^{s_i}=1.
- $\Phi$ (Chinese-remainder map), bound on [Chinese-remainder address map](crt-map.md): The ring isomorphism sending x to the product of x_i^{mu_i}.
- $a_j$ (mixed-radix digit), bound on [Chinese-remainder address map](crt-map.md): The j-th digit of k in mixed radix, 0 <= a_j < s_j.
- $b_i$ (axis coordinate), bound on [Chinese-remainder address map](crt-map.md): The axis-i coordinate of Phi(x^k).
- $t_i$ (padded axis length), bound on [Chinese-remainder address map](crt-map.md): The padded length of axis i, either r/2 or r.
- $\ell$ (address bits), bound on [Chinese-remainder address map](crt-map.md): The base-2 logarithm of the record length r, the number of address bits of a full-width axis.
- $V$ (stream volume), bound on [Chinese-remainder address map](crt-map.md): The volume of the stream being moved, Tp bits.
- $\tau$ (chunk-swap exponent), bound on [Chinese-remainder address map](crt-map.md): A fixed exponent below 1 in the cost of a chunk interchange.
- $T$ (padded record count), bound on [Chinese-remainder address map](crt-map.md): The number of padded records, the product of the t_i.
- $k$ (coefficient index), bound on [Chinese-remainder address map](crt-map.md): The index of a coefficient of the length-S sequence.
- $s$ (source length), bound on [Gaussian resampling](gaussian-resampling.md): The length of the Fourier transform to be replaced.
- $\alpha$ (Gaussian width parameter), bound on [Gaussian resampling](gaussian-resampling.md): An integer, with 2 <= alpha < sqrt p, that is the width parameter of the Gaussian weights.
- $\theta$ (relative gap), bound on [Gaussian resampling](gaussian-resampling.md): The relative gap t/s - 1 between the two lengths.
- $C$ (coordinate selection), bound on [Gaussian resampling](gaussian-resampling.md): The map from C^t to C^s that selects coordinate q_j into position j.
- $\delta$ (exponent slack), bound on [Gaussian resampling](gaussian-resampling.md): A fixed constant 0 < delta < 1/8 that is the slack in the exponents of the time bounds.
- $k$ (output coordinate index), bound on [Gaussian resampling](gaussian-resampling.md): A coordinate index of a vector in C^t, taken modulo t.
- $t$ (target length), bound on [Gaussian resampling](gaussian-resampling.md): The larger length, a power of two in the application, of the transform used instead of the length-s one.
- $\widetilde E$ (approximate E), bound on [Gaussian resampling](gaussian-resampling.md): The numerical approximation of E = N - I computed on D_p records.
- $\boldsymbol s$ (source length tuple), bound on [Retained permutation cancellation](retained-permutations.md): The tuple of the prime axis lengths $s_i$.
- $\boldsymbol t$ (padded length tuple), bound on [Retained permutation cancellation](retained-permutations.md): The tuple of the power-of-two axis lengths $t_i$.
- $F_q^+$ (positive-sign transform), bound on [Retained permutation cancellation](retained-permutations.md): The transform of a vector of q entries with the exponent's sign reversed and the same factor 1/q as F_q, so that F_q^+F_q=I/q.
- $z$ (vector), bound on [Retained permutation cancellation](retained-permutations.md): A vector of q complex entries being transformed.
- $c$ (unit), bound on [Retained permutation cancellation](retained-permutations.md): An integer that is a unit modulo q, used to permute coordinates by z_{cj}.
- $h$ (summation index), bound on [Retained permutation cancellation](retained-permutations.md): The index of summation in the Fourier sum, substituted by ck.
- $g$ (setup degree), bound on [Retained permutation cancellation](retained-permutations.md): A fixed exponent such that setup work per line is O(p^g).
- $t_{\max}$ (largest padded length), bound on [Retained permutation cancellation](retained-permutations.md): The largest axis length, $2^\ell$, each $t_i$ being $t_{\max}/2$ or $t_{\max}$.
- $u$ (first array), bound on [Retained permutation cancellation](retained-permutations.md): A complex array (not an integer) in the resampling and convolution identities of this page.
- $v$ (second array), bound on [Retained permutation cancellation](retained-permutations.md): A complex array (not an integer) in the resampling and convolution identities of this page.
- $a$ (round count), bound on [Retained frequency order](frequency-order.md): The number of rounds of the transform, a=log_2 t.
- $j$ (output index), bound on [Retained frequency order](frequency-order.md): The position of an output of the transform.
- $s$ (completed rounds), bound on [Retained frequency order](frequency-order.md): The number of rounds completed so far.
- $B_t$ (bit-reversal permutation), bound on [Retained frequency order](frequency-order.md): The permutation moving the entry at j to rev_a(j).
- $\mathcal H$ (parallel butterfly), bound on [Retained frequency order](frequency-order.md): The parallel butterfly applying H_0 on every participating axis in one round.
- $J_E$ (recordwise monomial), bound on [Retained frequency order](frequency-order.md): The recordwise operation multiplying each record by y^E.
- $h_p$ (grid spacing), bound on [Error tracking and exact recovery](precision-recovery.md): The spacing $2^{-p}$ of the fractional-bit grid, the unit in which errors are measured.
- $L$ (log of padded length), bound on [Error tracking and exact recovery](precision-recovery.md): The base-2 logarithm of the padded length $T$.
- $E_s$ (source error), bound on [Error tracking and exact recovery](precision-recovery.md): The factor $9\cdot2^\gamma TL$ such that a computed source transform has error under $E_sh_p$.
- $u$ (scaled digit array), bound on [Error tracking and exact recovery](precision-recovery.md): The array of scaled radix digits of the first input, each stored as its value times $2^{-b-2}$ (not the integer).
- $v$ (scaled digit array), bound on [Error tracking and exact recovery](precision-recovery.md): The array of scaled radix digits of the second input (not the integer).
- $Q_0$ (carry base), bound on [Error tracking and exact recovery](precision-recovery.md): The radix $2^b$ of the digits during carry propagation.
- $j$ (coefficient index), bound on [Error tracking and exact recovery](precision-recovery.md): The index of the product coefficient being processed during carry propagation.
- $k_j$ (carry), bound on [Error tracking and exact recovery](precision-recovery.md): The carry into position $j$ from the lower coefficients.
- $d_j$ (output digit), bound on [Error tracking and exact recovery](precision-recovery.md): The $j$-th radix-$2^b$ digit of the product.
- $\boldsymbol t$ (axis lengths), bound on [Error tracking and exact recovery](precision-recovery.md): The tuple of padded axis lengths of the array.
- $\tau$ (chunk-interchange exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The exponent in the cost of a chunk interchange.
- $\sigma$ (recursion growth exponent), bound on [Parameter and prime-length choice](parameter-choice.md): An exponent bounding the growth of the number of recursive calls.
- $\beta$ (active-chunk threshold exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The exponent in the threshold d^beta below which active chunks are handled singly.
- $\lambda$ (overhead exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The per-node overhead exponent.
- $\lambda'$ (final cost exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The final exponent of the cost V d^lambda' on bit volume V.
- $V$ (bit volume), bound on [Parameter and prime-length choice](parameter-choice.md): The number of bits of the logical array the layer acts on.
- $c$ (chunk-width exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The exponent of the address-chunk width (a new meaning of c).
- $\epsilon$ (axis-count exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The exponent of the axis count.
- $C_1$ (guard-bit exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The exponent of the guard bits.
- $\delta$ (resampling slack), bound on [Parameter and prime-length choice](parameter-choice.md): The slack in the exponent of the resampling cost.
- $K$ (chunk width), bound on [Parameter and prime-length choice](parameter-choice.md): The width in bits of an address chunk.
- $\eta$ (prime window offset), bound on [Parameter and prime-length choice](parameter-choice.md): The smallest relative distance at which a prime s_i may lie below t_i.
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
- $T$ (a triple), bound on [Nested subspace labels and rank deficit](subspace-labels.md): A three-element subset of $[h]$ (not the padded size used on other pages).
- $t_T$ (triple indicator), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The indicator vector in $F$ of the triple $T$.
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
- $m$ (label dimension), bound on [Recursive power saving](rank-recurrence.md): The dimension of the label space, 10^6, which is also the number of slots a chunk is split into, so a parameter grows by the factor m per recursion level.
- $s$ (number of smaller calls), bound on [Recursive power saving](rank-recurrence.md): The number of calls at parameter f that one call at parameter mf makes, equal to the total rank of the frame changes over the network's edges.
- $f$ (call parameter), bound on [Recursive power saving](rank-recurrence.md): The size parameter of a call: the number of digits in each interchanged chunk, or the number of selected axes of a layer.
- $F$ (time per unit volume), bound on [Recursive power saving](rank-recurrence.md): The running time of a call at a given parameter divided by the volume of its stream.
- $j$ (recursion depth), bound on [Recursive power saving](rank-recurrence.md): The number of recursion levels between the top call and a given call.
- $\eta$ (relative deficit), bound on [Recursive power saving](rank-recurrence.md): The relative rank deficit (Wm - s)/(Wm) of a network, the fraction by which the number of smaller calls falls short of Wm.
- $u$ (chunk width), bound on [Fast address-chunk interchange](address-interchange.md): The number of bits in each of the two interchanged address chunks.
- $V$ (array volume), bound on [Fast address-chunk interchange](address-interchange.md): The number of bits stored in the array.
- $\tau$ (saving exponent), bound on [Fast address-chunk interchange](address-interchange.md): The fixed exponent below 1 in the cost, equal to 1 - 2^{-50}.
- $p$ (prefix), bound on [Fast address-chunk interchange](address-interchange.md): The part of an address before the first chunk.
- $h$ (first chunk), bound on [Fast address-chunk interchange](address-interchange.md): The first of the two address chunks being interchanged.
- $g$ (gap), bound on [Fast address-chunk interchange](address-interchange.md): The part of an address between the two chunks.
- $d$ (second chunk), bound on [Fast address-chunk interchange](address-interchange.md): The second of the two address chunks being interchanged.
- $z$ (suffix), bound on [Fast address-chunk interchange](address-interchange.md): The part of an address after the second chunk.
- $q$ (digit radix), bound on [Fast address-chunk interchange](address-interchange.md): The fixed prime that is the radix of the digits.
- $e$ (chunk digit count), bound on [Fast address-chunk interchange](address-interchange.md): The number of radix-q digits in a chunk.
- $k$ (recursion levels), bound on [Fast address-chunk interchange](address-interchange.md): The number of recursion levels, with e = m^k.
- $M$ (vertex matrix), bound on [Fast address-chunk interchange](address-interchange.md): The rational m by m matrix carried by a terminal or gate of the network.
- $A_i$ (edge matrix), bound on [Fast address-chunk interchange](address-interchange.md): The difference of the matrices at the head and tail of edge i.
- $i$ (edge index), bound on [Fast address-chunk interchange](address-interchange.md): The index of an edge of the network.
- $w$ (wire index), bound on [Fast address-chunk interchange](address-interchange.md): The index of an input wire of the network.
- $\rho$ (role map), bound on [Fast address-chunk interchange](address-interchange.md): The map sending input wire w to its output role.
- $I_m$ (identity), bound on [Fast address-chunk interchange](address-interchange.md): The m by m identity matrix.
- $\Phi_M$ (address shear), bound on [Fast address-chunk interchange](address-interchange.md): The array permutation moving the entry at address (H,D) to (H+MD,D).
- $f_w$ (wire input), bound on [Fast address-chunk interchange](address-interchange.md): The physical input array of wire w.
- $x$ (stream row), bound on [Fast address-chunk interchange](address-interchange.md): The row number within a role stream.
- $j$ (recursion level), bound on [Fast address-chunk interchange](address-interchange.md): The index of a recursion level in the unrolled recurrence.
- $k'$ (level count), bound on [Fast address-chunk interchange](address-interchange.md): The least integer with m^{k'} at least e, used for arbitrary widths.
- $\nu$ (high digit count), bound on [Fast address-chunk interchange](address-interchange.md): The number of top digits of each chunk set aside to form the row field.
- $\Lambda$ (row range), bound on [Fast address-chunk interchange](address-interchange.md): The number of values of the row field formed by the high parts of both chunks.
- $\Lambda'$ (padded row range), bound on [Fast address-chunk interchange](address-interchange.md): The row count after padding with zero rows to a multiple of W^{k'}.
- $a_j$ (piece count), bound on [Fast address-chunk interchange](address-interchange.md): The number of pieces of width m^j into which each remaining chunk is cut.
- $v$ (binary vector), bound on [Binary phase frames](phase-frames.md): A vector of F_2^m; in the main argument a basis vector of an edge residual. Here v does not mean the triple count.
- $q_U$ (phase exponent), bound on [Binary phase frames](phase-frames.md): The weight modulo four of the projection of an address x onto the label U.
- $\mathcal C_U$ (phase frame), bound on [Binary phase frames](phase-frames.md): The operator on arrays attached to the label U.
- $X_v$ (translation), bound on [Binary phase frames](phase-frames.md): The operator shifting an array by the vector v: (X_v f)(x)=f(x+v).
- $\mathcal B$ (residual basis), bound on [Binary phase frames](phase-frames.md): An orthonormal basis of the edge residual E.
- $E$ (edge residual), bound on [Binary phase frames](phase-frames.md): The subspace added to U to reach V, orthogonal to U; here E is not the first space of a tensor product.
- $\varepsilon$ (phase sign), bound on [Binary phase frames](phase-frames.md): The coefficient +1 or -1 modulo four of a basis vector's phase, including the edge direction.
- $Z$ (sign matrix), bound on [Binary phase frames](phase-frames.md): The diagonal matrix diag(1,-1).
- $Z_{a,k}$ (sign correction), bound on [Binary phase frames](phase-frames.md): The tensor product of Z on the 27 coordinates of supp(u) in every column and the identity elsewhere.
- $k$ (column count), bound on [Binary phase frames](phase-frames.md): The number of columns of an address; here k changes meaning from the fixed-point page.
- $c$ (control bit), bound on [Packed selected-bit addition](packed-bit-addition.md): A bit, 0 or 1, that gates the eight additions.
- $u$ (first integer), bound on [Packed selected-bit addition](packed-bit-addition.md): The integer updated by lines 1, 3, 6 and 8 of the eight additions.
- $w$ (second integer), bound on [Packed selected-bit addition](packed-bit-addition.md): The integer updated by lines 2, 4, 5 and 7, restored at the end.
- $R$ (record bits), bound on [Packed selected-bit addition](packed-bit-addition.md): The number of bits in the record at each address.
- $L$ (chunk bits), bound on [Packed selected-bit addition](packed-bit-addition.md): The number of bits in each of the chunks x, y, z, equal to fK.
- $K$ (segment spacing), bound on [Packed selected-bit addition](packed-bit-addition.md): The spacing between selected positions, at least 6, which is the length of each segment.
- $f$ (selected bit count), bound on [Packed selected-bit addition](packed-bit-addition.md): The number of selected bits per chunk.
- $M$ (address count), bound on [Packed selected-bit addition](packed-bit-addition.md): The number of addresses.
- $A_{\rm rect}$ (counter length), bound on [Packed selected-bit addition](packed-bit-addition.md): An upper bound on the number of bits of every counter, the ceiling of log2(2V).
- $\rho$ (selected-bit offset), bound on [Packed selected-bit addition](packed-bit-addition.md): The offset of the lowest selected position, 0 <= rho < K.
- $j_i$ (selected position), bound on [Packed selected-bit addition](packed-bit-addition.md): The i-th selected bit position in a chunk.
- $g$ (guard value), bound on [Packed selected-bit addition](packed-bit-addition.md): The guard value of a segment, any g_i or h_i: its high K-1 bits.
- $g_i$ (y guard), bound on [Packed selected-bit addition](packed-bit-addition.md): The guard value of the i-th segment of y, with u_i = 2 g_i + a_i.
- $h_i$ (z guard), bound on [Packed selected-bit addition](packed-bit-addition.md): The guard value of the i-th segment of z, with w_i = 2 h_i + b_i.
- $a_i$ (y segment bit), bound on [Packed selected-bit addition](packed-bit-addition.md): The lowest bit of the i-th segment of y.
- $b_i$ (z segment bit), bound on [Packed selected-bit addition](packed-bit-addition.md): The lowest bit of the i-th segment of z.
- $u_i$ (y segment), bound on [Packed selected-bit addition](packed-bit-addition.md): The value of the i-th K-bit segment of y.
- $w_i$ (z segment), bound on [Packed selected-bit addition](packed-bit-addition.md): The value of the i-th K-bit segment of z.
- $c_i$ (segment control), bound on [Packed selected-bit addition](packed-bit-addition.md): The selected bit of x at j_i that controls the i-th pair of segments.
- $S_0$ (packed map), bound on [Packed selected-bit addition](packed-bit-addition.md): The composition of the eight packed cyclic shifts.
- $T_0$ (ideal map), bound on [Packed selected-bit addition](packed-bit-addition.md): The permutation of addresses that performs the required XORs at j_0 to j_{f-2}.
- $\mathcal B$ (exceptional addresses), bound on [Packed selected-bit addition](packed-bit-addition.md): The set of addresses where some guard of y or z lies outside [10, 2^{K-1}-11].
- $\delta_{\rm bad}$ (bad fraction), bound on [Packed selected-bit addition](packed-bit-addition.md): The bound min{1, 80(f-1)2^{-K}} on the fraction of exceptional addresses.
- $q$ (address), bound on [Packed selected-bit addition](packed-bit-addition.md): An address of a record after S_0; q' is its destination T_0 S_0^{-1}(q).
- $D$ (selected chunk count), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The number of address chunks, at most d, on which the layer acts.
- $\mathcal S_D$ (phase diagonal), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The diagonal operator multiplying the value at address x by i to the sum of the D selected bits.
- $z$ (array), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The array of records that the operators act on.
- $e$ (group axis count), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The number of selected axes in a group, e = mf.
- $h$ (slot index), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The index of a slot and of the residual basis vector placed in it.
- $v_h$ (residual vector), bound on [Simultaneous butterfly layer](simultaneous-layer.md): A residual basis vector of an edge, in F_2^m.
- $\eta_h$ (direction sign), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The sign +1 or -1 giving the exponent of the kernel for v_h.
- $C_v$ (translation kernel), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The kernel aI + bX_v acting along the direction v.
- $X_v$ (column shift), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The operator shifting a column by v.
- $G$ (basis-change matrix), bound on [Simultaneous butterfly layer](simultaneous-layer.md): An invertible F_2 matrix whose first columns are the residual vectors.
- $\mathcal P_G$ (address permutation), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The permutation of addresses sending x to Gx.
- $e_h$ (standard basis vector), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The h-th standard basis vector of F_2^m.
- $q_0$ (individual chunk count), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The number of leading chunks handled by individual C kernels.
- $A$ (chain length bound), bound on [Simultaneous butterfly layer](simultaneous-layer.md): A(e) bounds the number of arithmetic operations along a chain from an input to an intermediate coefficient.
- $E$ (per-invocation bound), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The bound 64(W+m+1)^3 on the operations added by one invocation of the network.
- $B$ (level factor), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The number s+E by which each recursion level multiplies the chain bound.
- $\varphi$ (bound), bound on [Simultaneous butterfly layer](simultaneous-layer.md): A bound at least 1 on a chain length.
- $\nu$ (exponent of m), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The least j at least 1 with m^j at least B.
- $C_0$ (guard constant), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The constant 128 m B^2 in the number of reserved extra bits.
- $\ell$ (depth), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The depth of a value, the number of operations in sequence that produced it.
- $D$ (transformed axes), bound on [Tape layout for synthetic transforms](transform-layout.md): The number of transformed axes, d-1.
- $K$ (chunk width), bound on [Tape layout for synthetic transforms](transform-layout.md): The number of bits in an address chunk.
- $\tau$ (interchange exponent), bound on [Tape layout for synthetic transforms](transform-layout.md): The fixed exponent below 1 in the cost of the chunk interchange.
- $\lambda'$ (layer exponent), bound on [Tape layout for synthetic transforms](transform-layout.md): The fixed exponent below 1 in the cost of the simultaneous layer.
- $\ell$ (long-axis address bits), bound on [Tape layout for synthetic transforms](transform-layout.md): The base-2 logarithm of r, the number of address bits of a long axis.
- $\boldsymbol t$ (axis lengths), bound on [Tape layout for synthetic transforms](transform-layout.md): The tuple (t_1,...,t_D) of the axis lengths.
- $F_{\boldsymbol t}^-$ (forward synthetic transform), bound on [Tape layout for synthetic transforms](transform-layout.md): The forward synthetic transform along all D axes, axis i having length t_i.
- $F_{\boldsymbol t}^+$ (opposite transform), bound on [Tape layout for synthetic transforms](transform-layout.md): The opposite of the forward synthetic transform along all D axes.
- $B$ (bit reversal), bound on [Tape layout for synthetic transforms](transform-layout.md): The bit-reversal permutation applied along every axis.
- $b$ (leftover low bits), bound on [Tape layout for synthetic transforms](transform-layout.md): The number of low address bits of an axis left over after whole K-bit chunks.
- $q$ (whole chunks), bound on [Tape layout for synthetic transforms](transform-layout.md): The number of whole K-bit chunks per axis.
- $L$ (layout permutation), bound on [Tape layout for synthetic transforms](transform-layout.md): The record permutation made by the prefix moves and chunk exchanges.
- $z$ (round input), bound on [Tape layout for synthetic transforms](transform-layout.md): The array entering a round.
- $M$ (number of records), bound on [Convolution from the retained transform layout](ring-convolution.md): The number of polynomial records, one per cyclic address of the remaining axes.
- $T$ (number of coefficients), bound on [Convolution from the retained transform layout](ring-convolution.md): The number of complex coefficients in an array, T = rM.
- $F^-$ (forward transform), bound on [Convolution from the retained transform layout](ring-convolution.md): The forward synthetic transform.
- $F^+$ (opposite transform), bound on [Convolution from the retained transform layout](ring-convolution.md): The opposite synthetic transform.
- $P$ (pointwise product), bound on [Convolution from the retained transform layout](ring-convolution.md): The pointwise product of records, P(u,v) = uv/r.
- $L$ (layout permutation), bound on [Convolution from the retained transform layout](ring-convolution.md): The permutation of records produced by the tape layout.
- $B$ (bit-reversal order), bound on [Convolution from the retained transform layout](ring-convolution.md): The bit-reversal order in which forward outputs are written.
- $\mathcal T_+$ (opposite map), bound on [Convolution from the retained transform layout](ring-convolution.md): The exact counterpart F^+ B^{-1} L^{-1} of the opposite procedure.
- $\ell$ (log of record length), bound on [Convolution from the retained transform layout](ring-convolution.md): The base-2 logarithm of the record length r.
- $\delta$ (transform error), bound on [Convolution from the retained transform layout](ring-convolution.md): The error bound sqrt2 * l * 2^{-p} of each forward or opposite procedure.
- $\eta$ (truncation error), bound on [Convolution from the retained transform layout](ring-convolution.md): The error bound sqrt2 * 2^{-p} for one truncation.
- $K$ (layout chunk width), bound on [Convolution from the retained transform layout](ring-convolution.md): The width of the address chunks used by the tape layout.
- $b$ (digit width), bound on [The multiplication algorithm](multiplication-algorithm.md): The number of bits in one radix digit, the ceiling of log2 n.
- $t_i$ (padded axis length), bound on [The multiplication algorithm](multiplication-algorithm.md): The power-of-two length of axis i; their product is T.
- $F_{\boldsymbol s}$ (prime-axis transform), bound on [The multiplication algorithm](multiplication-algorithm.md): The discrete Fourier transform on the axes s_i, normalized by 1/S.
- $F_{\boldsymbol t}$ (padded-axis transform), bound on [The multiplication algorithm](multiplication-algorithm.md): The discrete Fourier transform on the axes t_i, normalized by 1/T.
- $\mathcal M_{\mathbb C}$ (normalized convolution), bound on [The multiplication algorithm](multiplication-algorithm.md): The normalized cyclic convolution f*g/T.
- $a_{\boldsymbol j}$ (chirp), bound on [The multiplication algorithm](multiplication-algorithm.md): The chirp array, a quadratic phase in the index.
- $\widetilde a$ (computed chirp), bound on [The multiplication algorithm](multiplication-algorithm.md): The stored approximation of the chirp a.
- $x_0$ (data operand), bound on [The multiplication algorithm](multiplication-algorithm.md): The data operand after the first chirp phase.
- $y_0$ (computed convolution), bound on [The multiplication algorithm](multiplication-algorithm.md): The computed convolution of the chirp with the data operand.
- $\widetilde{\mathcal M}_{\mathbb C}$ (computed convolution map), bound on [The multiplication algorithm](multiplication-algorithm.md): The computed approximate version of the normalized cyclic convolution.
- $\widetilde{\mathscr C}$ (computed chirp transform), bound on [The multiplication algorithm](multiplication-algorithm.md): The computed chirp transform.
- $\widetilde{\mathscr F}$ (computed source transform), bound on [The multiplication algorithm](multiplication-algorithm.md): The computed source transform: resample, chirp transform, resample, scale.
- $\mathcal A$ (input resampling map), bound on [The multiplication algorithm](multiplication-algorithm.md): The Gaussian resampling map applied first in the source transform.
- $\mathcal B_0$ (output resampling map), bound on [The multiplication algorithm](multiplication-algorithm.md): The resampling map applied after the chirp transform.
- $\gamma$ (resampling scale exponent), bound on [The multiplication algorithm](multiplication-algorithm.md): The exponent of the exact scale 2^gamma applied at the end of the source transform.
- $\mathscr F$ (exact source transform), bound on [The multiplication algorithm](multiplication-algorithm.md): The exact counterpart of the computed source transform.
- $R$ (retained permutation), bound on [The multiplication algorithm](multiplication-algorithm.md): The retained coordinate permutation of the source axes.
- $z$ (pointwise product array), bound on [The multiplication algorithm](multiplication-algorithm.md): An array to which the opposite-sign source transform is applied.
- $\widetilde{\mathscr F}^{+}$ (opposite-sign source transform), bound on [The multiplication algorithm](multiplication-algorithm.md): The computed source transform with the opposite sign, conjugating input and output.
- $\widetilde w$ (scaled computed array), bound on [The multiplication algorithm](multiplication-algorithm.md): The computed array after the first scaling by S.
- $w$ (scaled exact array), bound on [The multiplication algorithm](multiplication-algorithm.md): The exact array (u*v)/S that the computed array approximates.
- $u$ (first source array), bound on [The multiplication algorithm](multiplication-algorithm.md): In this page, the first source array obtained by applying Phi to the digits, not the integer.
- $V$ (volume), bound on [Cost accounting and the exponent κ](cost-accounting.md): The number of stored bits of the T coefficients of p bits, V=Tp.
- $g_i$ (margin), bound on [Cost accounting and the exponent κ](cost-accounting.md): The margin below one of the i-th dominant power of p, so the power is p^{1-g_i}.
- $A$ (visit exponent), bound on [Cost accounting and the exponent κ](cost-accounting.md): A fixed exponent such that the recursions make at most p^A visits in total.
- $C$ (setup exponent), bound on [Cost accounting and the exponent κ](cost-accounting.md): A fixed exponent such that descriptor setup per visit is at most p^C steps.
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

- The quotation does not support the claim it is attached to (unsupported): "$g_3=2^{-129}$, $g_7=2^{-75}$" cites "Thus $\min_i g_i=2^{-181}=2\kappa$.": The quotation only states the minimum margin 2^{-181}=2kappa; it gives no values for g_3 or g_7. Say only what the source supports, or cite the passage that supports the claim.
- $c$ means chunk-width exponent here, but machine constant on [Schönhage–Strassen optimality conjecture](conjecture.md), which this page builds on: The page already says c is not the machine constant; keep that remark or rename.
- $c$ means chunk-width exponent here, but scaling integer on [Controlled shifts and rational scalings](controlled-shifts.md), which this page builds on: The page already says c is not the machine constant; keep that remark or rename.
- $c$ means chunk-width exponent here, but control bit on [Packed selected-bit addition](packed-bit-addition.md), which this page builds on: Say that c is not the other meaning of c, or use another letter.
- $c$ means chunk-width exponent here, but unit on [Retained permutation cancellation](retained-permutations.md), which this page builds on: The page already says c is not the machine constant; keep that remark or rename.

## Previous version (revise it)

It has 425 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 531 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

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

[Cost accounting and the exponent κ](cost-accounting.md) totals the running time as follows, dividing every cost by $V=Tp=\Theta(n)$, the number of stored bits, where $T$ counts coefficients and $p$, of order $\lg n$, is the precision in bits of each. The axis count is $d=\Theta(p^{\epsilon})$ and the chunk width $K=\lfloor d^{c}\rfloor$, with fixed exponents $\epsilon$ and $c$ from [Parameter and prime-length choice](parameter-choice.md); here $c$ is not the machine constant. The seven dominant normalized costs are powers of $p$:
$$p^{\epsilon(1+c)},\quad p^{1-\epsilon c(1-\tau)},\quad p^{1-\epsilon(1-\lambda')},\quad p^{\tau+\epsilon(2-\tau)},\quad p^{3/4+\delta+3\epsilon/2},\quad p^{\epsilon+\delta},\quad p^{1-\epsilon}.$$
They come from prefix moves and single butterfly rounds ($dK$), chunk exchanges ($pK^{\tau-1}$), simultaneous butterfly rounds ($\ell d^{\lambda'}$, with $\ell$ the address bits of a long axis), Chinese-remainder and axis layouts, Gaussian line maps, chirps and twists, and packed ring products ($\log(rp)$). The rest is absorbed.

The margin $g_i$ of the $i$-th term is one minus its exponent. The fixed parameters are $\tau=1-2^{-50}$, $\lambda'=1-2^{-54}$, $c=2^{-56}$, $\delta=1/16$ and $\epsilon=2^{-75}$ <cite data-source="paper">\epsilon=2^{-75},\qquad \kappa=2^{-182}.</cite>. The smallest margin belongs to chunk exchanges:
$$g_2=\epsilon c(1-\tau)=2^{-75}\cdot2^{-56}\cdot2^{-50}=2^{-181}=2\kappa,$$
and the others are larger, e.g. $g_3=2^{-129}$, $g_7=2^{-75}$ <cite data-source="paper">Thus $\min_i g_i=2^{-181}=2\kappa$.</cite>

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

Write the body to `exegenius/tasks/0280-write-main-result.answer.md` and the JSON to `exegenius/tasks/0280-write-main-result.answer.json`, then run `exegenius submit 0280-write-main-result` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0280-write-main-result`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
