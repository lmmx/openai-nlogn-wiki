# exegenius task 0187-write-signed-packing

Project directory: `/mnt/openai-nlogn` (paths below are relative to it)

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

For these sources: The reader has finished an undergraduate computer science degree: asymptotic analysis, discrete mathematics (modular arithmetic, primes, binary representation, induction), introductory linear algebra (vectors, matrices, inverses, dot products), and the calculus the degree requires (limits, convergence of sequences and series, basic integrals). They know basic Turing machines with several tapes and standard algorithm analysis, including recurrences and schoolbook multiplication. They have not studied the FFT-based multiplication literature, abstract algebra beyond basics, or tape-level data-movement algorithms.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers (also: Gaussian integer)
- Multitape Turing machine
- Fixed-tape machine model and stream operations (also: fixed-tape machine)
- Convolution
- Discrete Fourier transform and butterflies (also: transform (the DFT/FFT the layout is for), twiddle factor, bit-reversed input, forward transform of length S)
- The n log n optimality conjecture
- Schönhage–Strassen to Harvey–van der Hoeven multiplication
- Reduction of integer product to digit convolution
- Chinese-remainder map to prime cyclic axes
- Gaussian resampling (also: Gaussian (weighting function))
- Bluestein's chirp identity
- Polynomial ring modulo $y^r+1$
  - $y$ (ring variable): The polynomial variable whose powers act as roots of unity.
  - $r$ (ring degree): The power of two giving the number of coefficients in each polynomial.
- Synthetic polynomial transforms (also: fast transform and transform axes)
- Last-coordinate phase twist
- Address fields and array layout on tapes (also: fields, address rearrangements and signed shifts)
- Finite linear network with roles and frames (also: scalar network, source and sink nodes of a route)
- Address shear and lower-triangular factorization
- Restoring auxiliary scratch values (also: scratch (auxiliary) roles)
- Fixed-point precision and exact recovery (also: source scale 2^gamma)
- Binary representation and bit operations (also: bits, XOR, bitwise operations, base 2)
- Modular arithmetic (also: congruence, residues mod m, remainder arithmetic)
- Prime numbers and coprimality (also: primes, relatively prime, gcd, distinct primes)
- Logarithms and floor/ceiling (also: lg, log base 2, floor, ceiling, iterated logarithm)
- Vectors, matrices and inverses (also: linear algebra, matrix multiplication, invertible matrix, dot product, orthogonality, linear map, norm)
- Schoolbook and Karatsuba multiplication (also: grade-school multiplication, long multiplication, Karatsuba)
- Divide-and-conquer recurrences (also: master theorem, recurrence relations, recursion tree)
- Limits, series and convergence (also: geometric series, summation, converging sum, epsilon bounds)
- Cartesian product and tuples (also: product of sets, index tuples, mixed radix, multi-index)
- Permutations (also: bijection, rearrangement, reordering, inverse permutation)
- Roots of unity (also: nth roots of unity, primitive root of unity, e^{2 pi i/n})
- Rings and basic algebraic structures (also: ring, commutative ring, group, quotient ring, residue ring)
- Fixed-point and rounding arithmetic (also: rounding error, truncation, fixed-point numbers, absolute error)

## This page

Concept: Signed coefficient packing (Kronecker substitution)
Gloss: Packs polynomial coefficients into one integer so polynomial products are done by an ordinary n log n integer multiplier.

## This page in the argument

The step: Polynomial products use signed packing and the ordinary $O(n\log n)$ multiplier as a subroutine.

It serves these steps, from the main result down:

- An $n$-bit integer product is computed by a fixed-tape machine in $O(n(\lg n)^{1-\kappa})$ time, $\kappa=2^{-182}$.; how: reduce multiplication to ring convolution and speed up its address moves and butterfly layers (on [Integer multiplication in O(n(lg n)^{1-κ}) time](main-theorem.md))
- Convolution over $\mathbb C[y]/(y^r+1)$ on the remaining axes is computed by synthetic transforms and packed polynomial products.; how: use two forward transforms, a pointwise product and the opposite transform, with retained frequency order (on [Convolution with retained transform order and cancelled permutations](ring-convolution-retained-order.md))

## Symbols already bound on earlier pages

The symbols in the names of the concepts the reader knows are listed with those concepts above.

- $n$ (integer length), bound on [The n log n optimality conjecture](nlogn-conjecture.md): The number of bits in each of the two integers being multiplied.
- $A$ (fixed-tape machine), bound on [The n log n optimality conjecture](nlogn-conjecture.md): The paper's deterministic Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes.
- $T_A$ (running time of A), bound on [The n log n optimality conjecture](nlogn-conjecture.md): The worst-case running time of machine A on pairs of n-bit inputs.
- $\kappa$ (logarithm exponent gap), bound on [The n log n optimality conjecture](nlogn-conjecture.md): A fixed positive constant, equal to 2^{-182}.
- $n$ (list length), bound on [Convolution](convolution.md): The number of entries in each input and output coefficient list.
- $a$ (input list a), bound on [Convolution](convolution.md): The first input coefficient list, with entries $a_0,\dots,a_{n-1}$.
- $b$ (input list b), bound on [Convolution](convolution.md): The second input coefficient list, with entries $b_0,\dots,b_{n-1}$.
- $c$ (output list), bound on [Convolution](convolution.md): The cyclic convolution of $a$ and $b$, a list of $n$ entries.
- $i$ (index i), bound on [Convolution](convolution.md): An index into the entries of the input list $a$.
- $j$ (index j), bound on [Convolution](convolution.md): An index into the entries of the input list $b$.
- $k$ (output index), bound on [Convolution](convolution.md): An index into the entries of the output list $c$.
- $y$ (indeterminate), bound on [Convolution](convolution.md): A symbol with no value, used as the variable of the polynomials whose coefficients are the lists.
- $x$ (first input integer), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The first of the two integers being multiplied, written with n bits.
- $y$ (second input integer), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The second of the two integers being multiplied, written with n bits.
- $b$ (digit width), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The number of bits in each radix digit.
- $q$ (digit count), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The number of radix digits of each input, q = ceil(n/b).
- $x_j$ (radix digit of x), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The j-th radix digit of x, a value in the range 0 to 2^b minus 1.
- $y_j$ (radix digit of y), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The j-th radix digit of y, a value in the range 0 to 2^b minus 1.
- $h_k$ (carry), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The carry into radix position k during carry propagation.
- $d_k$ (output digit), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The radix-2^b output digit at position k of the product.
- $y$ (ring variable), bound on [Polynomial ring modulo $y^r+1$](poly-ring-y-r.md): The polynomial variable whose powers act as roots of unity.
- $r$ (ring degree), bound on [Polynomial ring modulo $y^r+1$](poly-ring-y-r.md): The number of complex coefficients in each element of the ring, a power of two.
- $j$ (reduction offset), bound on [Polynomial ring modulo $y^r+1$](poly-ring-y-r.md): The exponent left after removing $y^r$ from a power $y^{r+j}$, ranging over $0\le j<r$.
- $s$ (root exponent), bound on [Polynomial ring modulo $y^r+1$](poly-ring-y-r.md): The exponent of a power of $y$ used as a root, reduced to $0\le s<2r$.
- $m$ (tape position), bound on [Address fields and array layout on tapes](address-fields.md): The position of an item in tape order, which is also the item's address written in binary.
- $u$ (field width), bound on [Address fields and array layout on tapes](address-fields.md): The number of bits in one address field.
- $V$ (stored bit volume), bound on [Address fields and array layout on tapes](address-fields.md): The total number of bits the array holds.
- $\omega$ (primitive root of unity), bound on [Discrete Fourier transform and butterflies](dft-fft.md): A primitive $n$-th root of unity, with $\omega^n=1$ and no smaller power equal to 1.
- $A$ (transform of a), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The list of $n$ values $A_m$, the transform of the input list $a$; this letter does not denote the fixed machine.
- $m$ (frequency index), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The index of a transform value $A_m$, ranging over $0\le m<n$; this letter does not denote a cell position.
- $u$ (butterfly input u), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The first input of a butterfly; this letter does not denote the field width.
- $v$ (butterfly input v), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The second input of a butterfly.
- $s$ (butterfly exponent), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The exponent of the power $\omega^s$ that multiplies the second input of a butterfly.
- $E$ (even-index transform), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The transform with root $\omega^2$ of the even-indexed entries of $a$.
- $O$ (odd-index transform), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The transform with root $\omega^2$ of the odd-indexed entries of $a$.
- $h$ (block size), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The number of entries in a block, a power of two from 2 to $n$.
- $t$ (block offset), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The position of an entry within the first half of a block.
- $B$ (transform of b), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The transform of the input list $b$.
- $C$ (transform of c), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The transform of the convolution list $c$.
- $l$ (paired index), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The index into $b$ paired with the index $i$ at output $k$, namely $(k-i)\bmod n$.
- $S$ (padded length), bound on [Schönhage–Strassen to Harvey–van der Hoeven multiplication](ss-hh-background.md): The number of entries in each zero-padded list, a power of two at least $2q-1$.
- $L$ (transform axis length), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The number of entries along the transform axis, a power of two dividing $2r$.
- $z$ (input list), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The list of ring elements that the transform acts on, with entries $z_0,\dots,z_{L-1}$.
- $Z$ (transformed list), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The list of $L$ ring elements that the transform produces from the input list $z$.
- $p$ (input index), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The index of an entry of the input list $z$, running from $0$ to $L-1$.
- $g$ (output index), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The index of an entry of the transformed list $Z$, running from $0$ to $L-1$.
- $e$ (power exponent), bound on [Synthetic polynomial transforms](synthetic-transforms.md): An integer with $0\le e<2r$, the exponent of the power $y^e$ that multiplies a coefficient list.
- $W$ (number of roles), bound on [Finite linear network with roles and frames](linear-network-roles.md): The number of roles, the wires' fixed places in the network, over which rows are distributed.
- $\rho$ (role permutation), bound on [Finite linear network with roles and frames](linear-network-roles.md): The permutation of roles that the scalar network applies, sending input role w to output role rho(w).
- $w$ (input role), bound on [Finite linear network with roles and frames](linear-network-roles.md): An input role of the scalar network, whose value is moved to output role rho(w).
- $\varepsilon_w$ (route sign), bound on [Finite linear network with roles and frames](linear-network-roles.md): The sign, +1 or -1, carried by the route from input role w to output role rho(w).
- $\nu$ (network node), bound on [Finite linear network with roles and frames](linear-network-roles.md): A source, gate or sink of the network, which carries one frame.
- $D_\nu$ (frame), bound on [Finite linear network with roles and frames](linear-network-roles.md): The invertible linear operator carried by node nu, acting on arrays indexed by the common address set.
- $\alpha$ (edge tail), bound on [Finite linear network with roles and frames](linear-network-roles.md): The node at which an edge starts.
- $\beta$ (edge head), bound on [Finite linear network with roles and frames](linear-network-roles.md): The node at which an edge ends.
- $f$ (logical array), bound on [Finite linear network with roles and frames](linear-network-roles.md): The logical array that a node stores in the form D_nu f.
- $G$ (pointwise gate), bound on [Finite linear network with roles and frames](linear-network-roles.md): A pointwise linear gate, which combines its input arrays at each address with fixed scalar coefficients.
- $p$ (gate input count), bound on [Finite linear network with roles and frames](linear-network-roles.md): The number of input arrays of a gate, counting the arrays it combines.
- $\ell$ (row index), bound on [Finite linear network with roles and frames](linear-network-roles.md): The index of a row at a fixed prefix, which selects the role that receives the row.
- $I$ (identity operator), bound on [Finite linear network with roles and frames](linear-network-roles.md): The identity operator, which leaves every array unchanged.
- $\alpha$ (starting scratch value), bound on [Restoring auxiliary scratch values](scratch-restoration.md): The value a scratch wire holds before the procedure runs, which may be any value.
- $\gamma$ (written value), bound on [Restoring auxiliary scratch values](scratch-restoration.md): The value added to a scratch wire, computed from data and not from the wire's starting value.
- $m$ (field count), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): The number of address fields in each vector.
- $H$ (first field vector), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): The vector of m address fields $(H_1,\ldots,H_m)$ that the shear updates.
- $D$ (second field vector), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): The vector of m address fields $(D_1,\ldots,D_m)$ that the shear reads.
- $q$ (radix), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): The fixed odd prime that is the radix of the digits of each field.
- $b$ (digit count per field), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): The number of radix-q digits in each field.
- $u$ (numerator), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): The integer numerator of a rational entry u/v.
- $v$ (denominator), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): The integer denominator of a rational entry u/v, not divisible by q.
- $M$ (rational shear matrix), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): A rational m-by-m matrix whose shear is (H,D) mapped to (H+MD,D).
- $\Pi$ (partial permutation), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): A 0-1 matrix with at most one 1 in each row and column, having rank many ones.
- $E_1$ (left lower-triangular factor), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): An invertible lower-triangular rational matrix in the factorization M = E_1 Pi E_2.
- $E_2$ (right lower-triangular factor), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): An invertible lower-triangular rational matrix in the factorization M = E_1 Pi E_2.
- $s$ (row of a one), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): The row index of a 1 in Pi.
- $g$ (column of a one), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): The column index of a 1 in Pi.
- $h$ (first field content), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): The content of the field H_s in a pair (h,d).
- $d$ (second field content), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): The content of the field D_g in a pair (h,d).
- $W_{\rm b}$ (wire count), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): The number of wires of the bit network.
- $N$ (source dimension), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): The total source dimension of the bit network.
- $L_{\rm b}$ (lost dimension), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): The total dimension lost on decreasing edges of the bit network.
- $s_{\rm b}$ (interchange count), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): The number of interchanges of the bit network, the sum of its edge ranks.
- $N$ (list length), bound on [Chinese-remainder map to prime cyclic axes](crt-address-map.md): The number of coefficients in the list, which equals the product of the T distinct primes.
- $T$ (prime count), bound on [Chinese-remainder map to prime cyclic axes](crt-address-map.md): The number of distinct primes whose product is N, and so the number of axes.
- $P_\nu$ (ν-th prime), bound on [Chinese-remainder map to prime cyclic axes](crt-address-map.md): The ν-th of the distinct primes, which is also the length of the ν-th axis.
- $\nu$ (axis index), bound on [Chinese-remainder map to prime cyclic axes](crt-address-map.md): The index of one prime and of its axis, running from 1 to T.
- $e$ (list index), bound on [Chinese-remainder map to prime cyclic axes](crt-address-map.md): An index of an entry of the list, an integer from 0 to N-1.
- $p$ (prime axis length), bound on [Gaussian resampling](gaussian-resampling.md): The number of entries in a list on a prime axis.
- $Q$ (replacing power-of-two length), bound on [Gaussian resampling](gaussian-resampling.md): The number of entries in the power-of-two list that replaces a list of length p, chosen slightly above p.
- $F_p$ (length-p transform), bound on [Gaussian resampling](gaussian-resampling.md): The normalized discrete Fourier transform of a list of length p.
- $F_Q$ (length-Q transform), bound on [Gaussian resampling](gaussian-resampling.md): The normalized discrete Fourier transform of a list of length Q.
- $\pi_p$ (reordering of length p), bound on [Gaussian resampling](gaussian-resampling.md): The fixed coordinate reordering of lists of length p used in the paper's identity.
- $\pi_Q$ (reordering of length Q), bound on [Gaussian resampling](gaussian-resampling.md): The fixed coordinate reordering of lists of length Q used in the paper's identity.
- $\alpha$ (Gaussian width parameter), bound on [Gaussian resampling](gaussian-resampling.md): The integer width parameter of the Gaussian weights, satisfying 2 <= alpha < sqrt(p).
- $U$ (forward resampling map), bound on [Gaussian resampling](gaussian-resampling.md): The contraction from lists of length p to lists of length Q, equal to half the map S.
- $K$ (backward resampling map), bound on [Gaussian resampling](gaussian-resampling.md): The contraction from lists of length Q back to lists of length p, which undoes the resampling.
- $\mathsf S$ (Gaussian sum S), bound on [Gaussian resampling](gaussian-resampling.md): The Gaussian-weighted sum from lists of length p to lists of length Q, with weights centred at p k/Q.
- $\mathsf T$ (Gaussian sum T), bound on [Gaussian resampling](gaussian-resampling.md): The Gaussian-weighted sum from lists of length p to lists of length Q, with weights centred at Q j/p.
- $\theta$ (relative margin), bound on [Gaussian resampling](gaussian-resampling.md): The relative excess Q/p - 1 of the power-of-two length over the prime length.
- $z_j$ (nearest grid index), bound on [Gaussian resampling](gaussian-resampling.md): The integer nearest to Q j/p, the grid point of the power-of-two list paired with entry j.
- $\beta_j$ (grid offset), bound on [Gaussian resampling](gaussian-resampling.md): The signed distance from Q j/p to its nearest integer z_j.
- $R$ (selection map), bound on [Gaussian resampling](gaussian-resampling.md): The map that reads the entries z_j from a list of length Q.
- $\Lambda$ (diagonal compensation), bound on [Gaussian resampling](gaussian-resampling.md): The diagonal map that multiplies entry j by e^{pi alpha^2 beta_j^2}.
- $\Phi$ (compensated map), bound on [Gaussian resampling](gaussian-resampling.md): The compensated map from lists of length p to lists of length p, close to the identity and hence invertible.
- $\zeta$ (chirp root of unity), bound on [Bluestein's chirp identity](bluestein-chirp.md): A primitive 2n-th root of unity whose square is omega, from which the chirp phases are built.
- $g$ (scaled input list), bound on [Bluestein's chirp identity](bluestein-chirp.md): The list whose k-th entry is a_k times the chirp phase zeta to the power k squared.
- $z$ (chirp), bound on [Bluestein's chirp identity](bluestein-chirp.md): The chirp zeta to the power minus t squared, read at an integer index t.
- $v$ (twisted convolution), bound on [Bluestein's chirp identity](bluestein-chirp.md): The cyclic convolution of the twisted lists, whose entry at output j is v_j.
- $j$ (output index), bound on [Bluestein's chirp identity](bluestein-chirp.md): The index of an output of the transform, running from 0 to n-1.
- $k$ (input index), bound on [Bluestein's chirp identity](bluestein-chirp.md): The index of an input a_k of the transform, running from 0 to n-1.
- $l$ (paired index), bound on [Bluestein's chirp identity](bluestein-chirp.md): The index of the chirp z_l paired with k in the twisted sum, running from 0 to n-1.
- $t$ (chirp index), bound on [Bluestein's chirp identity](bluestein-chirp.md): The integer at which the chirp z_t is read.
- $h$ (wrap count), bound on [Bluestein's chirp identity](bluestein-chirp.md): The number of multiples of n by which k+l exceeds j, either 0 or 1.
- $k$ (last-axis exponent), bound on [Last-coordinate phase twist](phase-twist-convolution.md): An exponent on the last axis, with $0\le k<r$, indexing one coefficient.
- $l$ (second last-axis exponent), bound on [Last-coordinate phase twist](phase-twist-convolution.md): A second exponent on the last axis, with $0\le l<r$, paired with $k$ in a product.
- $z$ (cyclic variable), bound on [Last-coordinate phase twist](phase-twist-convolution.md): The variable of the cyclic ring $\mathbb C[z]/(z^r-1)$, whose exponents wrap modulo $r$.
- $\zeta$ (twist root), bound on [Last-coordinate phase twist](phase-twist-convolution.md): The root of unity $e^{\pi \mathrm i/r}$, whose $r$-th power is $-1$, used to rescale coefficients.
- $j$ (cyclic product index), bound on [Last-coordinate phase twist](phase-twist-convolution.md): The exponent $j$, with $0\le j<r$, of the cyclic product $z^j$.
- $h$ (wrap flag), bound on [Last-coordinate phase twist](phase-twist-convolution.md): The flag $h\in\{0,1\}$ recording whether the exponent $k+l$ wrapped past $r$.
- $\alpha$ (first entry coefficient), bound on [Last-coordinate phase twist](phase-twist-convolution.md): The untwisted coefficient $\alpha_k$ of the first entry at index $k$.
- $\beta$ (second entry coefficient), bound on [Last-coordinate phase twist](phase-twist-convolution.md): The untwisted coefficient $\beta_l$ of the second entry at index $l$.
- $v$ (remaining-axis index), bound on [Last-coordinate phase twist](phase-twist-convolution.md): An index tuple with one coordinate per remaining cyclic axis, each wrapping modulo its length.
- $R$ (entry ring), bound on [Last-coordinate phase twist](phase-twist-convolution.md): The ring $\mathbb C[y]/(y^r+1)$ in which each entry on the remaining axes lives.
- $X$ (integer numerator), bound on [Fixed-point precision and exact recovery](fixed-point-precision.md): An integer numerator storing a complex coefficient; it represents the value X/2^p.
- $p$ (working precision), bound on [Fixed-point precision and exact recovery](fixed-point-precision.md): The number of bits of precision, the power of two 2^p in each numerator's denominator.
- $T$ (power-of-two length), bound on [Fixed-point precision and exact recovery](fixed-point-precision.md): The power of two in [4n/b, 8n/b), the number of points in the power-of-two grid.
- $S$ (cyclic convolution length), bound on [Fixed-point precision and exact recovery](fixed-point-precision.md): The length of the cyclic convolution, the number of entries in each transformed list, with T/2 < S < T.
- $L$ (log of T), bound on [Fixed-point precision and exact recovery](fixed-point-precision.md): The base-2 logarithm of T, which bounds the number of levels in the error constants.
- $\xi$ (scaled digit list x), bound on [Fixed-point precision and exact recovery](fixed-point-precision.md): The digit list of x divided by 2^{b+2}, with entries in [0,1/4).
- $\psi$ (scaled digit list y), bound on [Fixed-point precision and exact recovery](fixed-point-precision.md): The digit list of y divided by 2^{b+2}, with entries in [0,1/4).
- $\Phi$ (forward transform), bound on [Fixed-point precision and exact recovery](fixed-point-precision.md): The forward transform of length S, whose entries are the normalized sums (1/S) times the sum of xi_k omega^{mk}.
- $\Phi^{+}$ (opposite transform), bound on [Fixed-point precision and exact recovery](fixed-point-precision.md): The opposite transform, the forward transform with omega^{-mk} in place of omega^{mk}.
- $E_s$ (transform error constant), bound on [Fixed-point precision and exact recovery](fixed-point-precision.md): The error constant: each computed transform, after the source scale, has error below E_s times 2^{-p}.
- $\gamma$ (source scale exponent), bound on [Fixed-point precision and exact recovery](fixed-point-precision.md): The exponent of the source scale 2^gamma applied to each computed transform.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Schönhage–Strassen to Harvey–van der Hoeven multiplication](ss-hh-background.md): Chain of multitape algorithms from O(n log n log log n) to the unconditional O(n log n) bound, using transforms over rings with cheap roots of unity.
  Shown as: Signed coefficient packing (Kronecker substitution) *<predicate>* Schönhage–Strassen to Harvey–van der Hoeven multiplication

## Pages that build on this one

- Convolution with retained transform order and cancelled permutations: Two forward synthetic transforms keep the same frequency order through the pointwise product, and the opposite transform consumes it, so retained permutations cancel without separate sorts.

## Other pages you may link to

- [The n log n optimality conjecture](nlogn-conjecture.md)
- [Convolution](convolution.md)
- [Reduction of integer product to digit convolution](radix-digit-reduction.md)
- [Polynomial ring modulo $y^r+1$](poly-ring-y-r.md)
- [Fixed-tape machine model and stream operations](fixed-tape-model.md)
- [Address fields and array layout on tapes](address-fields.md)
- [Discrete Fourier transform and butterflies](dft-fft.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Finite linear network with roles and frames](linear-network-roles.md)
- [Restoring auxiliary scratch values](scratch-restoration.md)
- [Address shear and lower-triangular factorization](address-shear-factorization.md)
- [Chinese-remainder map to prime cyclic axes](crt-address-map.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein's chirp identity](bluestein-chirp.md)
- [Last-coordinate phase twist](phase-twist-convolution.md)
- [Fixed-point precision and exact recovery](fixed-point-precision.md)
- [Convolution with retained transform order and cancelled permutations](ring-convolution-retained-order.md)
- [Tensor product of vector spaces](tensor-product-of-vector-spaces.md)
- [Three-element subset intersection construction](subset-intersection-construction.md)
- [Recursive power saving from s<Wm](recursive-power-saving.md)
- [Fast interchange of address fields](fast-address-interchange.md)
- [Fast simultaneous butterfly layers](fast-butterfly-layers.md)
- [Integer multiplication in O(n(lg n)^{1-κ}) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "Signed coefficient" (paper)

  > More specifically, the proof adapts Harvey and van der Hoeven's Gaussian-resampling identity, contraction bounds, and short-convolution procedures~\cite[Theorem~4.2, Proposition~4.7 and Lemmas~4.8--4.12]{HarveyHoeven2021}. Their framework already permits arbitrary dimension. Here the source and target permutations remain in the transform identity, while the faster tape procedures perform the required axis movements. Bluestein's conversion to convolution~\cite{Bluestein1970} and the synthetic-root convolution algorithm are retained; the latter follows the polynomial-transform construction in~\cite[Section~2.4 and Section~3]{HarveyHoeven2021}. Signed coefficient packing is a form of Kronecker substitution, with the fixed-tape version of~\cite[Lemma~2.5]{HarveyHoeven2021} as a direct antecedent. Calls to the established $O(n\log n)$ multiplier are ordinary subroutine calls; they do not invoke the improved theorem recursively.


## Sources (read from disk as needed)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- $B$ means block base here, but transform of b on [Discrete Fourier transform and butterflies](dft-fft.md), which this page builds on: Rename the block base on signed-packing (for example L); B is the transform of the input list b on dft-fft, which this page builds on.
- $u$ means packed polynomial here, but butterfly input u on [Discrete Fourier transform and butterflies](dft-fft.md), which this page builds on: Rename the packed polynomial on signed-packing (for example x); u is the first butterfly input on dft-fft, which this page builds on.
- $u$ means packed polynomial here, but field width on [Address fields and array layout on tapes](address-fields.md), which this page builds on: Rename the packed polynomial on signed-packing (for example p); u is the field width on address-fields, which this page builds on.
- $v$ means second packed polynomial here, but butterfly input v on [Discrete Fourier transform and butterflies](dft-fft.md), which this page builds on: Rename the second packed polynomial on signed-packing (for example q); v is the second butterfly input on dft-fft, which this page builds on.
- $h$ means product polynomial here, but block size on [Discrete Fourier transform and butterflies](dft-fft.md), which this page builds on: Rename the product polynomial on signed-packing (for example w); h is the block size on dft-fft, which this page builds on.
- $j$ means coefficient position here, but index j on [Convolution](convolution.md), which this page builds on: Rename the coefficient position on signed-packing (for example s); j indexes the entries of the second input list b on convolution, which this page builds on.
- $t$ means second coefficient position here, but block offset on [Discrete Fourier transform and butterflies](dft-fft.md), which this page builds on: Rename the second coefficient position on signed-packing (for example o); t is the block offset on dft-fft, which this page builds on.
- $a$ means real part a here, but input list a on [Convolution](convolution.md), which this page builds on: Rename the real part a on signed-packing (for example a_r); a is the first input list on convolution, which this page builds on.
- $b$ means imaginary part b here, but input list b on [Convolution](convolution.md), which this page builds on: Rename the imaginary part b on signed-packing (for example b_i); b is the second input list on convolution, which this page builds on.
- $c$ means real part c here, but output list on [Convolution](convolution.md), which this page builds on: Rename the real part c on signed-packing (for example c_r); c is the output list on convolution, which this page builds on.

## Previous version (revise it)

It has 378 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 472 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

Signed coefficient packing (Kronecker substitution) encodes a polynomial with integer coefficients of either sign as one integer, so that a polynomial product becomes an integer product, which an ordinary $O(n\log n)$ multiplier computes.

Let $p$ be the working precision of the fixed-point page, so each coefficient of an input polynomial is an integer of absolute value at most $2^p$. Let $B=2^{4p}$ be the block base. Let $u=\sum_{j=0}^{r-1}u_j y^j$ denote a polynomial in $\mathbb Z[y]$ with $|u_j|\le 2^p$; its packed integer is
$$u(B)=\sum_{j=0}^{r-1}u_jB^j.$$
Here $j$ and $t$ are coefficient positions; the sum may be negative.

On tapes, a carry $\gamma_j$ and a block digit $d_j$ satisfy $\gamma_0=0$, $0\le d_j<B$, $d_j\equiv u_j+\gamma_j \pmod B$, and $\gamma_{j+1}=(u_j+\gamma_j-d_j)/B$. Each $\gamma_j$ stays in $\{-1,0\}$, since $u_j+\gamma_j$ lies in $(-B,B)$. Telescoping gives $u(B)=\sum_j d_jB^j+\gamma_rB^r$. So the blocks are nonnegative digits, and the sign is the final carry $\gamma_r$. Each block is $4p$ bits wide <cite data-source="paper">Every block has $4p$ bits</cite>.

Evaluation respects products: let $v=\sum_{t=0}^{r-1}v_t y^t$ denote a second input polynomial with $|v_t|\le 2^p$. Then $u(B)\,v(B)=(uv)(B)$ exactly, where $uv$ is the ordinary product in $\mathbb Z[y]$. Signed coefficient packing computes its integer products by the [Schönhage–Strassen to Harvey–van der Hoeven multiplication](ss-hh-background.md), an ordinary subroutine call that costs $O(n\log n)$.

Recovering the coefficients. Write $h=uv$, and $h_k$ for its coefficient of $y^k$, with $k$ running over $0,\dots,2r-2$. Each $h_k$ sums at most $r$ products $u_jv_t$, so $|h_k|\le r2^{2p}$. Recovery needs $|h_k|<B/2$, which holds because $r<2^p$: the ring degree is at most the padded length, $r\le T$ <cite data-source="paper">t_i\leq r\leq T</cite>, and $T<2^p$ for sufficiently large inputs by the choice of $p$ on the fixed-point page. Hence $|h_k|\le r2^{2p}<2^{3p}<B/2$. Since every $h_kB^k$ with $k\ge1$ is a multiple of $B$, $h(B)\equiv h_0 \pmod B$. As $|h_0|<B/2$, $h_0$ is the unique integer in $[-B/2,B/2)$ congruent to $h(B)$ modulo $B$. Subtracting it and dividing by $B$ leaves the same form for $h_1,h_2,\dots$.

Example with $B=12$. For $u=2-y$ and $v=1+3y$, $u(12)=-10$ and $v(12)=37$, so the packed product is $-370$. Recovery gives $h_0=2$, $h_1=5$, $h_2=-3$, so $uv=2+5y-3y^2$.

Gaussian products. A record is a polynomial of degree less than $r$ with complex fixed-point coefficients. A record $f=2^{-p}(a+\sqrt{-1}\,b)$ has real and imaginary components $a,b\in\mathbb Z[y]$. Records have norm at most one, so their parts lie in $[-1,1]$ <cite data-source="paper">A disk array has norm at most one.</cite>. Truncation puts each part on the grid $2^{-p}\mathbb Z$, so $2^p$ times each part is an integer, and its coefficients are at most $2^p$ in absolute value <cite data-source="paper">The truncated numerators have magnitude at most $2^p$</cite>. The second record $g=2^{-p}(c+\sqrt{-1}\,e)$ has components $c,e\in\mathbb Z[y]$, and the product is
$$(a+\sqrt{-1}\,b)(c+\sqrt{-1}\,e)=(ac-be)+\sqrt{-1}\,(ae+bc).$$
The four ordinary products $ac$, $be$, $ae$, $bc$ are each one packed product. Each is unpacked to exact coefficients before subtraction or addition, so the bound $|h_k|<B/2$ holds for each product, not for the sums.

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

Write the body to `exegenius/tasks/0187-write-signed-packing.answer.md` and the JSON to `exegenius/tasks/0187-write-signed-packing.answer.json`, then run `exegenius submit 0187-write-signed-packing` in the project directory. If submit rejects the answer, fix the answer and submit again.
