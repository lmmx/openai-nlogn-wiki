# exegenius task 0206-write-recursive-power-saving

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
- Signed coefficient packing (Kronecker substitution)
- Last-coordinate phase twist
- Convolution with retained transform order and cancelled permutations
- Address fields and array layout on tapes (also: fields, address rearrangements and signed shifts)
- Finite linear network with roles and frames (also: scalar network, source and sink nodes of a route)
- Three-element subset intersection construction
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
- Tensor product of vector spaces (also: tensor power)

## This page

Concept: Recursive power saving from s<Wm
Gloss: Recursive call at parameter mf uses s calls at parameter f on streams of volume V/W; since s/W<m the volume-normalized cost grows as a power, giving a fixed power saving.

## This page in the argument

The step: A recursive call at parameter $mf$ uses $s$ calls at parameter $f$ on streams of volume $V/W$, so the volume-normalized cost grows as a power, giving a fixed power saving.

It serves these steps, from the main result down:

- An $n$-bit integer product is computed by a fixed-tape machine in $O(n(\lg n)^{1-\kappa})$ time, $\kappa=2^{-182}$.; how: reduce multiplication to ring convolution and speed up its address moves and butterfly layers (on [Integer multiplication in O(n(lg n)^{1-κ}) time](main-theorem.md))
- Two fixed-tape procedures, an address interchange and a simultaneous butterfly layer, cost $O(Vu^\tau)$ and $O(Vd^{\lambda'})$ for fixed exponents below 1, where $V$ is the stored bit volume.; how: build both procedures from one finite linear network and a recursion that saves a power

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
- $x$ (first integer), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The first of the two integers being multiplied.
- $y$ (second integer), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The second of the two integers being multiplied.
- $b$ (digit width), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The number of bits in each radix digit.
- $q$ (digit count), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The number of radix digits of each input.
- $x_j$ (radix digit of x), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The $j$th radix digit of $x$, a value below $2^b$.
- $y_j$ (radix digit of y), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The $j$th radix digit of $y$, a value below $2^b$.
- $h_k$ (carry), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The carry into position $k$ in the radix-$2^b$ carry propagation, with $h_0=0$.
- $d_k$ (output digit), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The radix-$2^b$ digit at position $k$ of the product.
- $y$ (ring variable), bound on [Polynomial ring modulo $y^r+1$](poly-ring-y-r.md): The polynomial variable of the ring, whose powers act as roots of unity.
- $r$ (ring degree), bound on [Polynomial ring modulo $y^r+1$](poly-ring-y-r.md): The number of complex coefficients in each element of the ring, a power of two.
- $j$ (rule exponent), bound on [Polynomial ring modulo $y^r+1$](poly-ring-y-r.md): The exponent left after removing $y^r$ from $y^{r+j}$, with $0\le j<r$.
- $s$ (reduced exponent), bound on [Polynomial ring modulo $y^r+1$](poly-ring-y-r.md): The exponent of the power $y^s$ that equals a given power of $y$, with $0\le s<2r$.
- $m$ (tape position), bound on [Address fields and array layout on tapes](address-fields.md): The position of an item in tape order, so the item sits in the m-th cell.
- $u$ (field width), bound on [Address fields and array layout on tapes](address-fields.md): The number of bits in one address field.
- $V$ (stored bit volume), bound on [Address fields and array layout on tapes](address-fields.md): The total number of bits the array holds.
- $\omega$ (primitive root of unity), bound on [Discrete Fourier transform and butterflies](dft-fft.md): A primitive $n$-th root of unity, whose powers are the points at which the list is evaluated.
- $m$ (frequency index), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The position of an entry in a transform's output list, ranging over $0\le m<n$.
- $A$ (transform of a), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The transform of $a$, the list whose entries are $A_m$ for $0\le m<n$.
- $u$ (first butterfly input), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The first input of a butterfly.
- $v$ (second butterfly input), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The second input of a butterfly, multiplied by the twiddle factor.
- $s$ (butterfly exponent), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The exponent of the twiddle factor $\omega^s$ of a butterfly.
- $E$ (even-part transform), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The transform, with root $\omega^2$, of the even-indexed entries of $a$.
- $O$ (odd-part transform), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The transform, with root $\omega^2$, of the odd-indexed entries of $a$.
- $h$ (block size), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The number of entries in a block.
- $t$ (block offset), bound on [Discrete Fourier transform and butterflies](dft-fft.md): An offset within a block, ranging over $0\le t<h/2$.
- $B$ (transform of b), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The transform of the list $b$, with entries $B_m$.
- $C$ (transform of c), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The transform of the convolution list $c$, with entries $C_m$.
- $l$ (index into b), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The index into $b$ paired with $i$ at output $k$, namely $(k-i)\bmod n$.
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
- $\theta$ (scratch starting value), bound on [Restoring auxiliary scratch values](scratch-restoration.md): The starting value of a scratch wire, which may be any value.
- $\gamma$ (written update value), bound on [Restoring auxiliary scratch values](scratch-restoration.md): A value computed from the data and added to the scratch wire, then subtracted again on undo.
- $q$ (digit radix), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): A fixed odd prime, the radix of the digits of each field.
- $b$ (digits per field), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): The number of radix-q digits in each field.
- $R$ (fields per vector), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): The number of fields in each of the vectors H and D.
- $H$ (field vector H), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): The vector $(H_1,\ldots,H_R)$ of R address fields that a shear updates.
- $D$ (field vector D), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): The vector $(D_1,\ldots,D_R)$ of R address fields that a shear reads and leaves unchanged.
- $M$ (shear matrix), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): A rational R-by-R matrix whose shear $(H,D)\mapsto(H+MD,D)$ is performed.
- $\mu$ (numerator of an entry), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): The integer numerator of a rational entry of M.
- $\xi$ (denominator of an entry), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): The integer denominator of a rational entry of M, which q must not divide.
- $\Pi$ (partial permutation matrix), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): A 0-1 matrix with at most one 1 in each row and column, whose ones give the interchanges.
- $F_1$ (left lower-triangular factor), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): The invertible lower-triangular rational matrix on the left of the factorization $M=F_1\Pi F_2$.
- $F_2$ (right lower-triangular factor), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): The invertible lower-triangular rational matrix on the right of the factorization $M=F_1\Pi F_2$.
- $\sigma$ (row of a one), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): The row of a 1 in Pi, which names the field H_sigma that the update changes.
- $\tau$ (column of a one), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): The column of a 1 in Pi, which names the field D_tau that the update reads.
- $\eta$ (content of H_sigma), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): The value held by the field H_sigma before one update.
- $\zeta$ (content of D_tau), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): The value held by the field D_tau before one update.
- $W_{\rm b}$ (bit network wires), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): The number of wires of the bit network.
- $N$ (negative source projections), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): The number of negative source projections of the bit network.
- $L_{\rm b}$ (lost dimension), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): The total dimension lost over the decreasing edges of the bit network.
- $s_{\rm b}$ (network interchange total), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): The total number of interchanges the bit network needs, the sum of the ranks of its edge matrices.
- $N$ (list length), bound on [Chinese-remainder map to prime cyclic axes](crt-address-map.md): The number of coefficients in the list, which equals the product of the T distinct primes.
- $T$ (prime count), bound on [Chinese-remainder map to prime cyclic axes](crt-address-map.md): The number of distinct primes whose product is N, and so the number of axes.
- $P_\nu$ (ν-th prime), bound on [Chinese-remainder map to prime cyclic axes](crt-address-map.md): The ν-th of the distinct primes, which is also the length of the ν-th axis.
- $\nu$ (axis index), bound on [Chinese-remainder map to prime cyclic axes](crt-address-map.md): The index of one prime and of its axis, running from 1 to T.
- $e$ (list index), bound on [Chinese-remainder map to prime cyclic axes](crt-address-map.md): An index of an entry of the list, an integer from 0 to N-1.
- $P$ (prime axis length), bound on [Gaussian resampling](gaussian-resampling.md): The number of entries in a list on a prime axis.
- $Q$ (replacing length), bound on [Gaussian resampling](gaussian-resampling.md): The power of two giving the number of entries in the list that replaces a prime-length list.
- $F$ (normalized transform), bound on [Gaussian resampling](gaussian-resampling.md): The normalized discrete Fourier transform of length P, and likewise F_Q of length Q.
- $\pi$ (entry reorderings), bound on [Gaussian resampling](gaussian-resampling.md): The coordinate reorderings pi_P and pi_Q used in the identity.
- $\sigma$ (Gaussian width), bound on [Gaussian resampling](gaussian-resampling.md): The width parameter of the Gaussian weights, an integer with 2 at most sigma below the square root of P.
- $U$ (input map), bound on [Gaussian resampling](gaussian-resampling.md): The map from lists of length P to lists of length Q, equal to one half of S.
- $K$ (output map), bound on [Gaussian resampling](gaussian-resampling.md): The map from lists of length Q back to lists of length P.
- $\mathsf S$ (Gaussian sum S), bound on [Gaussian resampling](gaussian-resampling.md): The Gaussian-weighted sum whose weights are centred on points of the source grid.
- $\mathsf T$ (Gaussian sum T), bound on [Gaussian resampling](gaussian-resampling.md): The Gaussian-weighted sum whose weights are centred on points of the target grid.
- $\theta$ (excess ratio), bound on [Gaussian resampling](gaussian-resampling.md): The number Q/P minus one, the relative excess of the replacing length.
- $\zeta$ (nearest integer), bound on [Gaussian resampling](gaussian-resampling.md): The integer nearest Qj/P for each entry index j.
- $\delta$ (signed offset), bound on [Gaussian resampling](gaussian-resampling.md): The offset of Qj/P from its nearest integer zeta_j.
- $R$ (reading map), bound on [Gaussian resampling](gaussian-resampling.md): The map that reads the entries zeta_j from a list of length Q.
- $\Lambda$ (weight diagonal), bound on [Gaussian resampling](gaussian-resampling.md): The diagonal map multiplying entry j by e^{pi sigma^2 delta_j^2}.
- $\Phi$ (compensated map), bound on [Gaussian resampling](gaussian-resampling.md): The map R T Lambda from length P to length P, invertible by a Neumann series.
- $\zeta$ (primitive 2n-th root), bound on [Bluestein's chirp identity](bluestein-chirp.md): A primitive 2n-th root of unity whose square is omega.
- $j$ (output index), bound on [Bluestein's chirp identity](bluestein-chirp.md): The index of an output of the transform, ranging over 0 to n-1.
- $k$ (input index), bound on [Bluestein's chirp identity](bluestein-chirp.md): The index of an entry of the input list a, ranging over 0 to n-1.
- $e$ (chirp index), bound on [Bluestein's chirp identity](bluestein-chirp.md): The integer at which the chirp is evaluated.
- $g$ (chirped input list), bound on [Bluestein's chirp identity](bluestein-chirp.md): The list whose entry at index k is a_k times zeta to the power k squared.
- $z$ (chirp list), bound on [Bluestein's chirp identity](bluestein-chirp.md): The chirp list, whose entry at integer index e is zeta to the power minus e squared.
- $l$ (chirp list index), bound on [Bluestein's chirp identity](bluestein-chirp.md): The index into the chirp list z, ranging over 0 to n-1.
- $w$ (twisted convolution), bound on [Bluestein's chirp identity](bluestein-chirp.md): The cyclic convolution of the twisted lists, at output index j.
- $c$ (wrap count), bound on [Bluestein's chirp identity](bluestein-chirp.md): The number of wraps, 0 or 1, in the relation k+l=j+cn.
- $\sigma$ (last-axis exponent), bound on [Last-coordinate phase twist](phase-twist-convolution.md): An exponent of $x$ on the last cyclic axis, ranging over $0\le\sigma<r$.
- $\tau$ (second last-axis exponent), bound on [Last-coordinate phase twist](phase-twist-convolution.md): A second exponent of $x$ on the last cyclic axis, ranging over $0\le\tau<r$.
- $\xi_\sigma$ (last-axis coefficient), bound on [Last-coordinate phase twist](phase-twist-convolution.md): The coefficient of $x^\sigma$ in a polynomial on the last axis, indexed by the exponent $\sigma$.
- $x$ (cyclic variable), bound on [Last-coordinate phase twist](phase-twist-convolution.md): The variable of the cyclic ring $\mathbb C[x]/(x^r-1)$ on the last axis, whose exponents wrap modulo $r$.
- $\lambda$ (twist root), bound on [Last-coordinate phase twist](phase-twist-convolution.md): A complex number with $\lambda^r=-1$, whose powers rescale the coefficients under the twist.
- $\mu$ (cyclic product index), bound on [Last-coordinate phase twist](phase-twist-convolution.md): The exponent of the cyclic product, with $0\le\mu<r$, obtained by reducing $\sigma+\tau$ modulo $r$.
- $\eta$ (wrap flag), bound on [Last-coordinate phase twist](phase-twist-convolution.md): The flag, 0 or 1, recording whether the sum $\sigma+\tau$ wrapped past $r$.
- $X$ (first entry), bound on [Last-coordinate phase twist](phase-twist-convolution.md): An entry on the remaining axes, an element of $\mathbb C[y]/(y^r+1)$ with untwisted coefficients $X_\sigma$.
- $Y$ (second entry), bound on [Last-coordinate phase twist](phase-twist-convolution.md): A second entry on the remaining axes, an element of $\mathbb C[y]/(y^r+1)$ with untwisted coefficients $Y_\tau$.
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
- $\Theta$ (block base), bound on [Signed coefficient packing (Kronecker substitution)](signed-packing.md): The base $2^{4p}$ in which the coefficients of a packed polynomial are placed.
- $o$ (first coefficient position), bound on [Signed coefficient packing (Kronecker substitution)](signed-packing.md): The index of a coefficient of $J$, ranging over $0\le o<r$.
- $\tau$ (second coefficient position), bound on [Signed coefficient packing (Kronecker substitution)](signed-packing.md): The index of a coefficient of $\Delta$, ranging over $0\le\tau<r$.
- $J$ (first packed polynomial), bound on [Signed coefficient packing (Kronecker substitution)](signed-packing.md): A polynomial in $\mathbb Z[y]$ whose coefficients $J_o$ are integers of absolute value at most $2^p$.
- $\Delta$ (second packed polynomial), bound on [Signed coefficient packing (Kronecker substitution)](signed-packing.md): A polynomial in $\mathbb Z[y]$ whose coefficients $\Delta_\tau$ are integers of absolute value at most $2^p$.
- $\Upsilon$ (product polynomial), bound on [Signed coefficient packing (Kronecker substitution)](signed-packing.md): The ordinary product $J\Delta$ in $\mathbb Z[y]$, whose coefficients $\Upsilon_\eta$ are recovered from one packed integer product.
- $\eta$ (product coefficient position), bound on [Signed coefficient packing (Kronecker substitution)](signed-packing.md): The index of a coefficient of $\Upsilon$, ranging over $0\le\eta\le 2r-2$.
- $\Xi$ (first record), bound on [Signed coefficient packing (Kronecker substitution)](signed-packing.md): A record, a polynomial of degree less than $r$ with complex fixed-point coefficients, whose real and imaginary numerators are $a_r$ and $b_i$.
- $a_r$ (real numerator), bound on [Signed coefficient packing (Kronecker substitution)](signed-packing.md): The polynomial in $\mathbb Z[y]$ holding the numerators of the real part of the first record.
- $b_i$ (imaginary numerator), bound on [Signed coefficient packing (Kronecker substitution)](signed-packing.md): The polynomial in $\mathbb Z[y]$ holding the numerators of the imaginary part of the first record.
- $\Gamma$ (second record), bound on [Signed coefficient packing (Kronecker substitution)](signed-packing.md): The second record, $2^{-p}(c_r+\sqrt{-1}\,c_i)$, multiplied with the first record.
- $c_r$ (second real numerator), bound on [Signed coefficient packing (Kronecker substitution)](signed-packing.md): The polynomial in $\mathbb Z[y]$ holding the numerators of the real part of the second record.
- $c_i$ (second imaginary numerator), bound on [Signed coefficient packing (Kronecker substitution)](signed-packing.md): The polynomial in $\mathbb Z[y]$ holding the numerators of the imaginary part of the second record.
- $\phi$ (first input array), bound on [Convolution with retained transform order and cancelled permutations](ring-convolution-retained-order.md): The first of the two input arrays of the convolution, indexed by $i$ on each axis.
- $\psi$ (second input array), bound on [Convolution with retained transform order and cancelled permutations](ring-convolution-retained-order.md): The second of the two input arrays of the convolution, indexed by $j$ on each axis.
- $\ast$ (ring convolution), bound on [Convolution with retained transform order and cancelled permutations](ring-convolution-retained-order.md): The cyclic convolution of two arrays on one axis, with products taken in the ring.
- $\mathcal{D}$ (forward transform), bound on [Convolution with retained transform order and cancelled permutations](ring-convolution-retained-order.md): The transform sending an array to its entries $(\mathcal D\phi)_m$, indexed by frequency $m$.
- $\mathcal{D}^{+}$ (opposite transform), bound on [Convolution with retained transform order and cancelled permutations](ring-convolution-retained-order.md): The transform that inverts the forward transform up to the scalar $M$.
- $M$ (normalization scalar), bound on [Convolution with retained transform order and cancelled permutations](ring-convolution-retained-order.md): The known scalar fixed by the normalization of the transforms.
- $\odot$ (entrywise product), bound on [Convolution with retained transform order and cancelled permutations](ring-convolution-retained-order.md): The product of ring elements at the same address, applied entry by entry.
- $\sigma$ (layout permutation), bound on [Convolution with retained transform order and cancelled permutations](ring-convolution-retained-order.md): The permutation of addresses fixed by the layout, which moves the entry for frequency $m$ to address $\sigma(m)$.
- $F$ (vector space), bound on [Tensor product of vector spaces](tensor-product-of-vector-spaces.md): The vector space whose tensor powers are formed, here Q^h in the bit network.
- $\nu$ (field dimension), bound on [Tensor product of vector spaces](tensor-product-of-vector-spaces.md): The number of vectors in a basis of F, which counts the coordinates of each factor.
- $K$ (number of factors), bound on [Tensor product of vector spaces](tensor-product-of-vector-spaces.md): The number of factors in the tensor power F^{\otimes K}, a count of how many vectors each pure tensor has.
- $\xi$ (factor vector), bound on [Tensor product of vector spaces](tensor-product-of-vector-spaces.md): A vector of F, one tensor factor of a pure tensor.
- $\lambda$ (scalar), bound on [Tensor product of vector spaces](tensor-product-of-vector-spaces.md): A scalar of the field over which F is a vector space.
- $\phi$ (basis vector), bound on [Tensor product of vector spaces](tensor-product-of-vector-spaces.md): A basis vector of F, indexed by position in the basis.
- $\mu$ (basis position), bound on [Tensor product of vector spaces](tensor-product-of-vector-spaces.md): The position of a basis vector in the basis of F, running from 1 to nu, one for each factor of a basis product.
- $t_T$ (triple indicator), bound on [Tensor product of vector spaces](tensor-product-of-vector-spaces.md): The vector of F that has entry 1 on the three elements of the triple T and 0 elsewhere.
- $T$ (triple), bound on [Three-element subset intersection construction](subset-intersection-construction.md): A three-element subset of the ground set $[h]$.
- $S$ (neighbor triple), bound on [Three-element subset intersection construction](subset-intersection-construction.md): A triple, paired with $T$ as a neighbor when $|T\cap S|=1$.
- $\mathcal T$ (triple set), bound on [Three-element subset intersection construction](subset-intersection-construction.md): The set of all three-element subsets of $[h]$.
- $g$ (triple value), bound on [Three-element subset intersection construction](subset-intersection-construction.md): The value carried by a triple $T$, written $g_T$.
- $C_e$ (central wire), bound on [Three-element subset intersection construction](subset-intersection-construction.md): The central wire of element $e$, which carries the sum of the $g_T$ over triples $T$ containing $e$.
- $A_{ST}$ (auxiliary wire), bound on [Three-element subset intersection construction](subset-intersection-construction.md): The auxiliary wire for a neighbor pair $S,T$, which carries a copy of $g_T$.
- $\mathcal F$ (label space), bound on [Three-element subset intersection construction](subset-intersection-construction.md): The space $(\mathbb Q^h)^{\otimes 3}$ in which labels live.
- $D$ (label space dimension), bound on [Three-element subset intersection construction](subset-intersection-construction.md): The dimension of the label space $\mathcal F$, which is $h^3$.
- $U$ (label), bound on [Three-element subset intersection construction](subset-intersection-construction.md): A nondegenerate subspace of the label space, attached to a gate, sink or source.
- $\iota$ (source index), bound on [Three-element subset intersection construction](subset-intersection-construction.md): A triple of triples $(T_1,T_2,T_3)$, indexing a source and its label $U_\iota$.
- $P_U$ (label projection), bound on [Three-element subset intersection construction](subset-intersection-construction.md): The projection onto the label $U$ along its orthogonal complement $U^\perp$.
- $s$ (total rank), bound on [Three-element subset intersection construction](subset-intersection-construction.md): The total rank of the edge matrices over all edges, which counts the smaller calls.
- $N$ (index count), bound on [Three-element subset intersection construction](subset-intersection-construction.md): The number of indices $\iota$, equal to $\binom h3^3$.
- $L$ (lost dimension), bound on [Three-element subset intersection construction](subset-intersection-construction.md): The total dimension lost on decreasing edges of the network.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Three-element subset intersection construction](subset-intersection-construction.md): Gather/scatter with auxiliary wires cancelling unwanted coefficients, using indicator-vector orthogonality to assign subspaces; gives s<Wm smaller calls.
  Shown as: Recursive power saving from s<Wm *<predicate>* Three-element subset intersection construction

## Pages that build on this one

- Fast interchange of address fields: Interchange two disjoint contiguous u-bit address fields in an array in O(V u^τ) for fixed τ<1, via XOR combinations that end as an exact permutation.
- Fast simultaneous butterfly layers: Applies H0(u,v)=((u+v)/2,(u-v)/2) on selected address bits of polynomial-valued arrays with exact Gaussian dyadics in O(V d^λ') with λ'<1, one truncation at the end.

## Other pages you may link to

- [The n log n optimality conjecture](nlogn-conjecture.md)
- [Convolution](convolution.md)
- [Reduction of integer product to digit convolution](radix-digit-reduction.md)
- [Polynomial ring modulo $y^r+1$](poly-ring-y-r.md)
- [Fixed-tape machine model and stream operations](fixed-tape-model.md)
- [Address fields and array layout on tapes](address-fields.md)
- [Discrete Fourier transform and butterflies](dft-fft.md)
- [Schönhage–Strassen to Harvey–van der Hoeven multiplication](ss-hh-background.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Finite linear network with roles and frames](linear-network-roles.md)
- [Restoring auxiliary scratch values](scratch-restoration.md)
- [Address shear and lower-triangular factorization](address-shear-factorization.md)
- [Chinese-remainder map to prime cyclic axes](crt-address-map.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein's chirp identity](bluestein-chirp.md)
- [Last-coordinate phase twist](phase-twist-convolution.md)
- [Fixed-point precision and exact recovery](fixed-point-precision.md)
- [Signed coefficient packing (Kronecker substitution)](signed-packing.md)
- [Convolution with retained transform order and cancelled permutations](ring-convolution-retained-order.md)
- [Tensor product of vector spaces](tensor-product-of-vector-spaces.md)
- [Fast interchange of address fields](fast-address-interchange.md)
- [Fast simultaneous butterfly layers](fast-butterfly-layers.md)
- [Integer multiplication in O(n(lg n)^{1-κ}) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "This strict inequality" (paper)

  > A recursive call at parameter $mf$ therefore uses $s$ calls at parameter $f$, each on a stream of volume $V/W$. The parameter counts field digits for address interchange and selected axes for a numerical layer. After dividing cost by volume, multiplying the parameter by $m$ increases the recursive contribution by $s/W<m$. This strict inequality is the source of the power saving. The later tape and arithmetic estimates preserve it, including the work of changing numerical address coordinates. Those changes are implemented by whole-chunk moves and controlled shifts, followed by a deterministic correction of the explicitly identified exceptional addresses.

- "is the source of the power saving." (paper)

  > A recursive call at parameter $mf$ therefore uses $s$ calls at parameter $f$, each on a stream of volume $V/W$. The parameter counts field digits for address interchange and selected axes for a numerical layer. After dividing cost by volume, multiplying the parameter by $m$ increases the recursive contribution by $s/W<m$. This strict inequality is the source of the power saving. The later tape and arithmetic estimates preserve it, including the work of changing numerical address coordinates. Those changes are implemented by whole-chunk moves and controlled shifts, followed by a deterministic correction of the explicitly identified exceptional addresses.


## Sources (read from disk as needed)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- $\lambda$ means power exponent here, but scalar on [Tensor product of vector spaces](tensor-product-of-vector-spaces.md), which this page builds on: Use another letter for the power exponent instead of lambda, since lambda is a scalar on the tensor-product page.
- $m$ means growth factor here, but tape position on [Address fields and array layout on tapes](address-fields.md), which this page builds on: Use another letter for the growth factor instead of m, since m is the tape position on the address-fields page.
- $K$ means chunk bit count here, but number of factors on [Tensor product of vector spaces](tensor-product-of-vector-spaces.md), which this page builds on: Use another letter for the chunk bit count instead of K, since K is the number of factors on the tensor-product page.
- $\beta$ means threshold exponent here, but edge head on [Finite linear network with roles and frames](linear-network-roles.md), which this page builds on: Use another letter for the threshold exponent instead of beta, since beta is an edge head on the linear-network page.
- $\nu$ means recursion level here, but field dimension on [Tensor product of vector spaces](tensor-product-of-vector-spaces.md), which this page builds on: Use another letter for the recursion level instead of nu, since nu is the field dimension on the tensor-product page.
- $\nu$ means recursion level here, but network node on [Finite linear network with roles and frames](linear-network-roles.md), which this page builds on: Use another letter for the recursion level instead of nu, since nu is a network node on the linear-network page.

## Previous version (revise it)

It has 412 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 515 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

Recursive power saving is the argument that a recursion's cost per bit can grow as a fixed power of its parameter, with exponent $\lambda<1$ (this letter changes meaning here: on the tensor-product page $\lambda$ is a scalar), which the main theorem needs.

Let $f$ be the parameter of a call (this letter changes meaning here: on the linear-network page $f$ is the logical array): the number of field digits for an address interchange (exchanging two disjoint address fields of $u$ bits), or the number of selected axes for a numerical layer (a butterfly layer on chosen axes of a polynomial-valued array). Here $m$ is the factor by which the parameter grows; this letter changes meaning from the subspace dimension of the prerequisite and from the tape position on the address-fields page. A recursive call at parameter $mf$ makes $s$ subcalls at parameter $f$, each on a stream of volume $V/W$. The recursion is built on the [Three-element subset intersection construction](subset-intersection-construction.md), which gives $s<Wm$ smaller calls.

Let $\Phi(f)$ be the cost of a call divided by the volume $V$ it works on. The subcalls contribute $\frac{s}{W}\Phi(f)$. Let $C$ be a constant such that the call's own outside work is at most $C(mf)^\lambda$, so

$$\Phi(mf)\le\frac{s}{W}\Phi(f)+C(mf)^\lambda.$$

The outside work is a fixed number of address-field row additions. An address interchange of $u$-bit fields costs $O(Vu^\tau)$, where $\tau<1$ is fixed. <cite data-source="paper">Its cost is $O(Vu^\tau)$ for a fixed $\tau<1$.</cite> Here $K$ is the bit count of one axis chunk (this letter changes meaning here: on the tensor-product page $K$ is the number of factors), $d$ is the paper's axis-count parameter (this letter changes meaning from the DFT page), and $\eta>0$ is fixed, with $K\le d^\eta$. A row addition on fields of $u=fK$ bits costs $O(V(u^\tau+1))$. Since $\beta=\tfrac12$ (this letter changes meaning here: on the linear-network page $\beta$ is an edge head) and $f\ge d^\beta$ at an internal node, $d\le f^{1/\beta}$, so the outside work divided by $V$ is $O((fK)^\tau+1)\le O(f^{\tau(1+\eta/\beta)}+1)$, which is $O(f^\lambda)$ when $\lambda>\tau(1+\eta/\beta)$.

Let $\nu$ count the levels of unrolling (this letter changes meaning here: on the linear-network page $\nu$ is a network node, and on the tensor-product page a field dimension), which stop once $f/m^\nu<d^\beta$. Each leaf is handled by one kernel per chunk, at cost $O(f/m^\nu)$. After $\nu$ levels the weight is $(s/W)^\nu$, so the internal costs sum to

$$C f^\lambda\sum_{\nu\ge0}\Big(\frac{s/W}{m^\lambda}\Big)^\nu.$$

The saving exists because $s/W<m$. <cite data-source="paper">This strict inequality is the source of the power saving.</cite> Taking $\lambda$ with $\log_m(s/W)<\lambda<1$ makes the ratio below 1, so the internal sum is at most a constant times $f^\lambda$.

The leaves at depth $\nu$ have $u=f/m^\nu<d^\beta$ chunks and total weight $(s/W)^\nu$, so they cost $O((s/W)^\nu u)$. Choose $\sigma$ with $\max\{0,\log_m(s/W)\}\le\sigma<\lambda$. Then $(s/W)^\nu\le m^{\nu\sigma}=(f/u)^\sigma$, and the leaves cost $O(f^\sigma d^{\beta(1-\sigma)})\le O(f^\lambda)$.

For example, with $m=2$, $s=3$, $W=2$, we have $s/W=\tfrac32$ and $\log_2(3/2)\approx0.585$. For $\lambda=0.8$ the ratio is $\tfrac{3/2}{2^{0.8}}\approx0.86$.

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

Write the body to `exegenius/tasks/0206-write-recursive-power-saving.answer.md` and the JSON to `exegenius/tasks/0206-write-recursive-power-saving.answer.json`, then run `exegenius submit 0206-write-recursive-power-saving` in the project directory. If submit rejects the answer, fix the answer and submit again.
