# exegenius task 0163-write-controlled-shifts

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

Concept: Controlled shifts and rational scalings
Gloss: Updating a target address field by an offset computed from earlier control fields, or multiplying it by a unit, in time linear in the array volume.

## Where the argument relies on this page

- Bit variant: two disjoint address chunks of $u$ bits can be interchanged on a fixed number of tapes in $O(Vu^\tau)$ time, $\tau=1-2^{-50}$, although the intermediate steps form XOR combinations of data. (on [Fast address-chunk interchange](address-interchange.md))
- For a rational $m\times m$ matrix $A$ of rank $a$ and fields over $\mathbb Z/q^b\mathbb Z$, the shear $(H,D)\mapsto(H+AD,D)$ can be performed with exactly $a$ interchanges of pairs of $b$-digit fields and $O(V)$ further work. (on [Matrix shear by triangular factorization](matrix-shear.md))
- Selected bits of two chunks can be XORed (with a third chunk as restored scratch) by eight cyclic shifts of whole chunk ranges plus a repair of an explicitly bounded exceptional set of addresses, in time $O(V(L^\tau+1)+MA_{\rm rect}^3+\delta_{\rm bad}MA_{\rm rect}(R+A_{\rm rect}))$. (on [Packed selected-bit addition](packed-bit-addition.md))
- The Chinese-remainder map $\Phi:\mathbb C[x]/(x^S-1)\to\mathbb C[x_1,\dots,x_d]/(x_i^{s_i}-1)$, $x\mapsto\prod_ix_i^{\mu_i}$, is an isomorphism preserving cyclic convolution, and it (with its inverse and padding) is implemented by triangular controlled shifts in $O(Tp\,d^2(1+\ell^\tau))$ time. (on [Chinese-remainder address map](crt-map.md))

## Symbols already bound on earlier pages

The symbols in the names of the concepts the reader knows are listed with those concepts above.

- $y$ (ring variable), bound on [Polynomial ring modulo y^r + 1](ring-y.md): The indeterminate of the polynomials; it satisfies y^r = -1 in the ring.
- $r$ (record length), bound on [Polynomial ring modulo y^r + 1](ring-y.md): The number of complex coefficients in a polynomial of the ring, always a power of two.
- $j$ (excess degree), bound on [Polynomial ring modulo y^r + 1](ring-y.md): The number of places a term's degree exceeds r-1.
- $a$ (shift exponent), bound on [Polynomial ring modulo y^r + 1](ring-y.md): An integer exponent of y by which an element is multiplied.
- $n$ (bit length), bound on [Schönhage–Strassen optimality conjecture](conjecture.md): The number of bits in each of the two integers being multiplied.
- $c$ (machine constant), bound on [Schönhage–Strassen optimality conjecture](conjecture.md): A positive constant, depending on the machine, in the lower bound c n log n.
- $\kappa$ (power saving), bound on [Schönhage–Strassen optimality conjecture](conjecture.md): A fixed positive constant by which the exponent of the logarithm is lowered.
- $p$ (fractional bits), bound on [Fixed-point Gaussian dyadic records](fixed-point.md): The number of fractional bits of the grid on which stored values lie.
- $k$ (depth), bound on [Fixed-point Gaussian dyadic records](fixed-point.md): The number of operations in sequence since the layer began that produced a value.
- $\Delta$ (reserved extra bits), bound on [Fixed-point Gaussian dyadic records](fixed-point.md): The number of extra bits reserved, at least the maximal depth reached in the layer.
- $Q_p$ (truncation), bound on [Fixed-point Gaussian dyadic records](fixed-point.md): The truncation that drops the bits below 2^{-p} in each real and imaginary part, returning a record to the p-bit grid.
- $h$ (ground-set size), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The size of the ground set [h] whose three-element subsets index the values.
- $v$ (triple count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of three-element subsets of [h].
- $\mathcal T$ (triple set), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The set of three-element subsets of [h].
- $N$ (bank size), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The size of each data bank.
- $m$ (label dimension), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The dimension of the label space used later.
- $S$ (triple), bound on [Linear exchange network with restored scratch wires](exchange-network.md): A three-element subset of [h], indexing a value in a bank.
- $x$ (source vector), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The vector of all values x_S.
- $y$ (target vector), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The vector of all values y_S.
- $S'$ (other triple), bound on [Linear exchange network with restored scratch wires](exchange-network.md): A second triple, the index of a source value x_{S'}.
- $a$ (bank index), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The index of a value in a data bank, a triple of triples.
- $\sigma$ (side scratch vector), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The initial values of the side scratch wires.
- $\gamma$ (central scratch vector), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The initial values of the central scratch wires.
- $I$ (invocation count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of invocations.
- $z_{\rm b}$ (bit neighbours), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of neighbours of a fixed triple in the bit construction.
- $z_{\rm c}$ (complex neighbours), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of neighbours of a fixed triple in the complex construction.
- $c_{\rm b}$ (bit central wires), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of central wires per invocation in the bit network.
- $c_{\rm c}$ (complex central wires), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of central wires per invocation in the complex network.
- $W_{\rm b}$ (bit wire count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of wires of the bit network.
- $W_{\rm c}$ (complex wire count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of wires of the complex network.
- $R$ (scalar ring), bound on [Frames on wire arrays](array-frames.md): The ring of scalars carried by the wires.
- $\Omega$ (address set), bound on [Frames on wire arrays](array-frames.md): A finite set of addresses indexing every array.
- $D_v$ (frame), bound on [Frames on wire arrays](array-frames.md): The invertible R-linear operator on R^Omega assigned to a source, gate or sink v.
- $t$ (gate input count), bound on [Frames on wire arrays](array-frames.md): The number of input arrays of a gate.
- $q$ (sequence length), bound on [Cyclic convolution](convolution.md): The number of entries in each sequence being convolved.
- $d$ (axis count), bound on [Cyclic convolution](convolution.md): One more than the number of cyclic axes of an array.
- $t_i$ (axis length), bound on [Cyclic convolution](convolution.md): The length of cyclic axis i.
- $M$ (cyclic address count), bound on [Cyclic convolution](convolution.md): The number of addresses on the cyclic axes of an array.
- $T$ (total coefficient count), bound on [Cyclic convolution](convolution.md): The total number of complex coefficients in an array.
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
- $\boldsymbol j$ (output index), bound on [Bluestein chirp identity](chirp.md): The index tuple (j_1,...,j_d) of an entry of the data and of the output position.
- $s_i$ (source length), bound on [Bluestein chirp identity](chirp.md): An integer coprime to t_i attached to axis i, the multiplier of the frequency read.
- $\boldsymbol f$ (frequency), bound on [Bluestein chirp identity](chirp.md): The frequency tuple (f_1,...,f_d) labelling an output entry of the transform.
- $Q$ (target permutation), bound on [Bluestein chirp identity](chirp.md): The permutation of the output so that position j holds the entry of frequency (-s_i j_i)_i.
- $a$ (chirp), bound on [Bluestein chirp identity](chirp.md): The array of phases a_j = exp(-pi i sum s_i j_i^2/t_i), quadratic in the index.
- $\mathcal R_r$ (negacyclic ring), bound on [Retained frequency order](frequency-order.md): The ring of polynomials in y with r complex coefficients, modulo y^r+1.
- $a$ (number of rounds), bound on [Retained frequency order](frequency-order.md): The number of rounds, log base 2 of the transform length t.
- $F_t^-$ (forward synthetic transform), bound on [Retained frequency order](frequency-order.md): The forward length-t synthetic transform on t ring elements.
- $H_0$ (two-point butterfly), bound on [Retained frequency order](frequency-order.md): The 2x2 butterfly matrix (1/2)[[1,1],[1,-1]].
- $B_t$ (bit-reversal record permutation), bound on [Retained frequency order](frequency-order.md): The permutation moving the entry at j to rev_a(j).
- $\operatorname{rev}_a$ (bit reversal), bound on [Retained frequency order](frequency-order.md): The map reversing the a binary digits of j.
- $s$ (completed rounds), bound on [Retained frequency order](frequency-order.md): The number of rounds completed so far.
- $i$ (axis index), bound on [Retained frequency order](frequency-order.md): Index of an axis of the array.
- $u_i$ (current axis length), bound on [Retained frequency order](frequency-order.md): The current length of axis i.
- $b_i$ (new bit), bound on [Retained frequency order](frequency-order.md): The bit newly written by the latest round on axis i.
- $k_i$ (twiddle index), bound on [Retained frequency order](frequency-order.md): The number formed by the bits in axis i's unprocessed slots below the paired slot, with 0<=k_i<u_i/2.
- $\mathcal H$ (parallel butterfly), bound on [Retained frequency order](frequency-order.md): The operation applying H_0 on every participating axis at once.
- $J_E$ (recordwise monomial), bound on [Retained frequency order](frequency-order.md): The operation multiplying the record at each address by y^E.
- $E$ (combined exponent), bound on [Retained frequency order](frequency-order.md): The exponent of y by which the record at an address is multiplied, determined by that address.
- $j_0$ (odd part), bound on [Retained frequency order](frequency-order.md): The odd part of j, so j=2^v j_0.
- $v$ (two-adic exponent), bound on [Retained frequency order](frequency-order.md): The exponent of 2 in j, with 0<=v<a.
- $N$ (factor bit length), bound on [Established O(n log n) multiplier](hvdh-multiplier.md): The number of bits in each of the two integers of one product given to the established multiplier (not the bank size).
- $p$ (fractional bits), bound on [Signed packing](signed-packing.md): The number of fractional bits of each coefficient component.
- $\mathcal R_r$ (ring), bound on [Signed packing](signed-packing.md): The ring of polynomials of degree below r modulo y^r+1.
- $f$ (first polynomial), bound on [Signed packing](signed-packing.md): A polynomial of the ring with coefficients 2^{-p} times Gaussian integers.
- $a$ (integer polynomial), bound on [Signed packing](signed-packing.md): Integer-coefficient polynomial, real part numerator of f (similarly b, c, e).
- $B_0$ (packing base), bound on [Signed packing](signed-packing.md): The base 2^{4p} at which polynomials are evaluated.
- $A_u$ (signed evaluation integer), bound on [Signed packing](signed-packing.md): The integer u(B_0) for u among a, b, c, e.
- $u_j$ (coefficient of u), bound on [Signed packing](signed-packing.md): The coefficient of y^j in u.
- $\gamma_j$ (packing carry), bound on [Signed packing](signed-packing.md): The carry into block j when forming A_u, in {-1,0}.
- $d_j$ (packed block), bound on [Signed packing](signed-packing.md): The j-th block of 4p bits of the encoding of A_u, in [0,B_0).
- $h_j$ (product coefficient), bound on [Signed packing](signed-packing.md): The coefficient of y^j in an ordinary integer-polynomial product such as h=ac.
- $Z$ (product integer), bound on [Signed packing](signed-packing.md): One of the four product integers, equal to the sum of h_j B_0^j for its ordinary product h.
- $q_j$ (block of Z), bound on [Signed packing](signed-packing.md): The j-th block of Z in sign-extended two's complement, in [0,B_0).
- $\varepsilon$ (sign extension), bound on [Signed packing](signed-packing.md): The sign-extension digit of Z, in {-1,0}.
- $\rho_j$ (extraction carry), bound on [Signed packing](signed-packing.md): The carry into block j during extraction, in {0,1}.
- $\widehat h_j$ (extracted coefficient), bound on [Signed packing](signed-packing.md): The centered residue of q_j+rho_j modulo B_0, equal to h_j.
- $H_j$ (numerator coefficient), bound on [Signed packing](signed-packing.md): The Gaussian integer coefficient of y^j after reduction modulo y^r+1.
- $j_1$ (first-factor index), bound on [Signed packing](signed-packing.md): The index of a coefficient of the first factor.
- $j_2$ (second-factor index), bound on [Signed packing](signed-packing.md): The index of a coefficient of the second factor.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Elementary stream operations](stream-ops.md): Linear-time scans on arrays stored in lexicographic order: swapping two digits, moving a digit, splitting into streams, applying a pointwise map and merging back.
  Shown as: Controlled shifts and rational scalings *<predicate>* Elementary stream operations

## Pages that build on this one

- Matrix shear by triangular factorization: Factoring a rational matrix as A = E₁ΠE₂ with lower triangular E₁, E₂ and partial permutation Π lets the shear (H,D)→(H+AD,D) be done with exactly rank(A) field interchanges.
- Chinese-remainder address map: An isomorphism that places a cyclic convolution of length S = s₁⋯s_d on pairwise coprime prime axes, implemented as triangular controlled shifts.
- Packed selected-bit addition: XORing selected bits between two address chunks (with a third chunk as restored scratch) using cyclic shifts of whole chunk ranges plus a repair of explicitly bounded exceptional addresses.

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
- [Butterflies and the fast transform](butterfly.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Bluestein chirp identity](chirp.md)
- [Retained frequency order](frequency-order.md)
- [Established O(n log n) multiplier](hvdh-multiplier.md)
- [Signed packing](signed-packing.md)
- [Matrix shear by triangular factorization](matrix-shear.md)
- [Two-point kernel C](phase-kernel.md)
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

- "Controlled shifts and fixed rational scalings" (paper)

  > \begin{lemma}[Controlled shifts and fixed rational scalings] \label{lem:ordered-affine-streams} Fix a prime $q$, a fixed number of control fields, and finitely many rational coefficients whose denominators are prime to $q$. Whenever a coefficient is used as a unit, also require its numerator to be prime to $q$. Put $Q=q^b$, $b\ge1$. Suppose a target field $y\in[Q]$ follows its control fields, each control used in an offset having $O(b)$ digits. An update \[ y\longmapsto y+a(\text{controls})\pmod Q \] costs $O(V)$ if the offset can be prepared in $b^{O(1)}$ time from the fixed number of control values. In particular, this holds for a fixed rational linear combination of them, specialized modulo $Q$. Multiplication of $y$ by any of the specified rational units, and its inverse, also costs $O(V)$. Arbitrarily long intervening spectator fields and suffix records are permitted. \end{lemma}

- "Suppose a target field $y\in[Q]$ follows its control fields" (paper)

  > \begin{lemma}[Controlled shifts and fixed rational scalings] \label{lem:ordered-affine-streams} Fix a prime $q$, a fixed number of control fields, and finitely many rational coefficients whose denominators are prime to $q$. Whenever a coefficient is used as a unit, also require its numerator to be prime to $q$. Put $Q=q^b$, $b\ge1$. Suppose a target field $y\in[Q]$ follows its control fields, each control used in an offset having $O(b)$ digits. An update \[ y\longmapsto y+a(\text{controls})\pmod Q \] costs $O(V)$ if the offset can be prepared in $b^{O(1)}$ time from the fixed number of control values. In particular, this holds for a fixed rational linear combination of them, specialized modulo $Q$. Multiplication of $y$ by any of the specified rational units, and its inverse, also costs $O(V)$. Arbitrarily long intervening spectator fields and suffix records are permitted. \end{lemma}


## Sources (read from disk as needed)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The reader cannot follow this step: "Exchanging split and merge multiplies by $c^{-1}$ (cited)" (The page never says what the exchanged split and merge are for the inverse map, or why the swap gives multiplication by c^{-1}. The scaling construction splits by j and merges by a residue condition mod c, so the reader cannot tell what the swap means (split by residue class, merge by j). This stands in for how the inverse scaling works, and the later claim that the inverse of a unit costs O(V) depends on it. Paper line 604 says only that reversing the roles of split and merge implements multiplication by c^{-1}.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.

## Previous version (revise it)

It has 421 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 526 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

A controlled shift adds to one field of each record an offset computed from earlier fields, and a rational scaling multiplies that field by a fixed unit; both run in time linear in the array volume.

Fix a prime $q$ (on this page $q$ is a prime, not a sequence length), and let $b\ge1$ be the number of base-$q$ digits of a field. Put $Q=q^b$, the number of values a field can take, and let $V$ be the array volume, the number of stored data bits. The target field has value $y\in[Q]=\{0,\dots,Q-1\}$ and follows a fixed number of control fields. The update is
$$y\longmapsto y+a \pmod Q,$$
where $a\in[Q]$ is the offset, prepared from the control values. It costs $O(V)$ if each control used in the offset has $O(b)$ digits and the offset can be prepared in $b^{O(1)}$ time from the fixed number of control values <cite data-source="paper">costs $O(V)$ if the offset can be prepared in $b^{O(1)}$ time from the fixed number of control values</cite>. A fixed rational linear combination of the controls, with denominators prime to $q$ and reduced modulo $Q$, qualifies. Spectator fields of any length may lie between or after.

**Why a shift is linear.** Because the target follows its controls, fixing everything before the target fixes $a$. If $B$ bits follow the target, the target and its suffix form $Q$ consecutive blocks of $B$ bits. Adding $a$ modulo $Q$ rotates these blocks. Split them at $Q-a$, append the two pieces to two tapes, then merge by reading the second piece before the first. Each update is carried out by splitting into streams and merging back, as in [Elementary stream operations](stream-ops.md). Reading the $O(b)$-digit controls and computing $a$ takes $b^{O(1)}=O(Q)$ time per prefix, absorbed by the $QB\ge Q$ bits of the blocks; longer controls would break this.

**Scaling.** Let $c$ be a fixed positive integer prime to $q$. The map $y\mapsto cy \pmod Q$ consists of $c$ increasing pieces, indexed by $j=\lfloor cy/Q\rfloor$. Split the blocks into $c$ streams by $j$, then produce output coordinates $y'=0,\dots,Q-1$ in order, taking each block from the stream $j$ with $y'+jQ\equiv 0\pmod c$, where $y=(y'+jQ)/c$. This $j$ is unique since $\gcd(Q,c)=1$. Exchanging split and merge multiplies by $c^{-1}$ <cite data-source="paper">Reversing the roles of this split and merge implements multiplication by $c^{-1}$ modulo $Q$.</cite>

**Negation and units.** Negation sends block $y$ to block $Q-y$: it leaves block $0$ fixed and reverses the other $Q-1$ blocks <cite data-source="paper">Negation leaves the block at zero fixed and reverses the order of the other $Q-1$ blocks.</cite> Push them onto a temporary tape and pop them, which also reverses the bits inside each block, then reverse each popped block again on a second tape before writing it.

A rational unit is a signed ratio $c/c'$ of positive integers $c,c'$ both prime to $q$. Multiply by $c$, multiply by the inverse of $c'$, and negate if the sign is negative: a fixed number of $O(V)$ passes, so the unit and its inverse cost $O(V)$.

**Example.** Take $q=2$, $b=2$, so $Q=4$, and $a=1$. Blocks $0,1,2,3$ split at $3$ into $(0,1,2)$ and $(3)$; reading $(3)$ first gives $3,0,1,2$.

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

Write the body to `exegenius/tasks/0163-write-controlled-shifts.answer.md` and the JSON to `exegenius/tasks/0163-write-controlled-shifts.answer.json`, then run `exegenius submit 0163-write-controlled-shifts` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0163-write-controlled-shifts`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
