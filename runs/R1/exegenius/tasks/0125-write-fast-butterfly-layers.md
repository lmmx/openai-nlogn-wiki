# exegenius task 0125-write-fast-butterfly-layers

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
- Recursive power saving from s<Wm
- Address shear and lower-triangular factorization
- Restoring auxiliary scratch values (also: scratch (auxiliary) roles)
- Fast interchange of address fields (also: address interchange and numerical layer, interchange, address interchange)
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

Concept: Fast simultaneous butterfly layers
Gloss: Applies H0(u,v)=((u+v)/2,(u-v)/2) on selected address bits of polynomial-valued arrays with exact Gaussian dyadics in O(V d^λ') with λ'<1, one truncation at the end.

## This page in the argument

The step: A simultaneous layer of $H_0(u,v)=((u+v)/2,(u-v)/2)$ on selected address bits of polynomial-valued arrays costs $O(Vd^{\lambda'})$ with $\lambda'<1$, with a single truncation at the end.

It serves these steps, from the main result down:

- An $n$-bit integer product is computed by a fixed-tape machine in $O(n(\lg n)^{1-\kappa})$ time, $\kappa=2^{-182}$.; how: reduce multiplication to ring convolution and speed up its address moves and butterfly layers (on [Integer multiplication in O(n(lg n)^{1-κ}) time](main-theorem.md))
- Two fixed-tape procedures, an address interchange and a simultaneous butterfly layer, cost $O(Vu^\tau)$ and $O(Vd^{\lambda'})$ for fixed exponents below 1, where $V$ is the stored bit volume.; how: build both procedures from one finite linear network and a recursion that saves a power

## Symbols already bound on earlier pages

The symbols in the names of the concepts the reader knows are listed with those concepts above.

- $n$ (input bit length), bound on [The n log n optimality conjecture](nlogn-conjecture.md): The number of bits in each of the two integers being multiplied.
- $A$ (fixed machine), bound on [The n log n optimality conjecture](nlogn-conjecture.md): The paper's deterministic Turing machine that multiplies integers.
- $T_A$ (running time of A), bound on [The n log n optimality conjecture](nlogn-conjecture.md): The worst-case running time of the machine A on pairs of n-bit inputs.
- $\kappa$ (savings exponent), bound on [The n log n optimality conjecture](nlogn-conjecture.md): The fixed positive constant 2^{-182} that gives the exponent of the logarithm in the bound.
- $n$ (list length), bound on [Convolution](convolution.md): The number of entries in each input and output coefficient list.
- $a$ (input list a), bound on [Convolution](convolution.md): The first input coefficient list, with entries $a_0,\dots,a_{n-1}$.
- $b$ (input list b), bound on [Convolution](convolution.md): The second input coefficient list, with entries $b_0,\dots,b_{n-1}$.
- $c$ (output list), bound on [Convolution](convolution.md): The cyclic convolution of $a$ and $b$, a list of $n$ entries.
- $i$ (index i), bound on [Convolution](convolution.md): An index into the entries of the input list $a$.
- $j$ (index j), bound on [Convolution](convolution.md): An index into the entries of the input list $b$.
- $k$ (output index), bound on [Convolution](convolution.md): An index into the entries of the output list $c$.
- $y$ (indeterminate), bound on [Convolution](convolution.md): A symbol with no value, used as the variable of the polynomials whose coefficients are the lists.
- $x$ (first input), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The first of the two integers being multiplied.
- $y$ (second input), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The second of the two integers being multiplied.
- $b$ (digit width), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The number of bits in each radix digit.
- $q$ (digit count), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The number of radix digits of each input, $\lceil n/b\rceil$.
- $x_j$ (radix digit of x), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The $j$th radix digit of $x$, an integer with $0\le x_j<2^b$.
- $y_j$ (radix digit of y), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The $j$th radix digit of $y$, an integer with $0\le y_j<2^b$.
- $c_k$ (digit coefficient), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The $k$th coefficient of the digit convolution, the sum of $x_i\,y_j$ over all $i+j=k$.
- $h_k$ (carry), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The carry into position $k$ during carry propagation, a nonnegative integer.
- $d_k$ (output digit), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The radix-$2^b$ digit of the product at position $k$, with $0\le d_k<2^b$.
- $y$ (ring variable), bound on [Polynomial ring modulo $y^r+1$](poly-ring-y-r.md): The polynomial variable whose powers act as roots of unity.
- $r$ (ring degree), bound on [Polynomial ring modulo $y^r+1$](poly-ring-y-r.md): The number of complex coefficients in each element, a power of two.
- $j$ (rule index), bound on [Polynomial ring modulo $y^r+1$](poly-ring-y-r.md): The index of the coefficient that the wrap rule $y^{r+j}=-y^j$ reduces to, ranging over $0\le j<r$.
- $k$ (shift exponent), bound on [Polynomial ring modulo $y^r+1$](poly-ring-y-r.md): The exponent of the power $y^k$ that acts as a signed shift, with $0\le k<r$.
- $L$ (axis length), bound on [Polynomial ring modulo $y^r+1$](poly-ring-y-r.md): The number of entries along one of the remaining transform axes, a divisor of $2r$.
- $m$ (cell position), bound on [Address fields and array layout on tapes](address-fields.md): The position of an item in the array, which is also its address written in binary.
- $u$ (field width), bound on [Address fields and array layout on tapes](address-fields.md): The number of bits in one address field.
- $V$ (stored bit volume), bound on [Address fields and array layout on tapes](address-fields.md): The number of bits the array holds in total.
- $\omega$ (root of unity), bound on [Discrete Fourier transform and butterflies](dft-fft.md): A primitive $n$-th root of unity, with $\omega^n=1$ and $\omega^m\ne1$ for $0<m<n$.
- $m$ (frequency index), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The frequency index of an entry of a transform, $0\le m<n$; it is also the exponent in $\omega^m$.
- $A$ (transform of a), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The transform of $a$: the list of $n$ entries $A_m$ defined by the sum.
- $u$ (butterfly input), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The first input of a butterfly.
- $v$ (butterfly input), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The second input of a butterfly.
- $s$ (butterfly exponent), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The exponent of the power $\omega^s$ that a butterfly applies to its second input.
- $E$ (even-index transform), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The transform, with root $\omega^2$, of the even-indexed entries of $a$.
- $O$ (odd-index transform), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The transform, with root $\omega^2$, of the odd-indexed entries of $a$.
- $h$ (block length), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The number of entries in a block at a level.
- $t$ (block offset), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The offset of an entry within a block.
- $B$ (transform of b), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The transform of $b$.
- $C$ (transform of c), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The transform of the cyclic convolution $c$.
- $l$ (paired index), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The index into $b$ paired with $i$ at output $k$, $l=(k-i)\bmod n$.
- $d$ (index difference), bound on [Discrete Fourier transform and butterflies](dft-fft.md): An integer, the difference of two output indices in the inverse sum.
- $t$ (transform length), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The number of entries in the transformed list, a power of two dividing 2r.
- $z$ (input list), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The list of t ring elements being transformed.
- $Z$ (transformed list), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The list of t entries produced by the transform.
- $g$ (output index), bound on [Synthetic polynomial transforms](synthetic-transforms.md): A position in the transformed list, running from 0 to t-1.
- $s$ (input index), bound on [Synthetic polynomial transforms](synthetic-transforms.md): A position in the input list, running from 0 to t-1.
- $m$ (primitivity exponent), bound on [Synthetic polynomial transforms](synthetic-transforms.md): An exponent used to test that the root has order exactly t.
- $W$ (role count), bound on [Finite linear network with roles and frames](linear-network-roles.md): The number of roles of the network, the fixed places a wire can occupy.
- $\ell$ (row index), bound on [Finite linear network with roles and frames](linear-network-roles.md): The index of a row among the rows at a fixed prefix.
- $V$ (stored bit volume), bound on [Finite linear network with roles and frames](linear-network-roles.md): The number of bits stored in the padded array.
- $v$ (node), bound on [Finite linear network with roles and frames](linear-network-roles.md): A source, gate or sink of the network.
- $D_v$ (frame), bound on [Finite linear network with roles and frames](linear-network-roles.md): The invertible linear operator on arrays carried by node $v$.
- $u$ (edge tail node), bound on [Finite linear network with roles and frames](linear-network-roles.md): The node at the start of an edge, a node rather than the address field width.
- $g$ (logical array), bound on [Finite linear network with roles and frames](linear-network-roles.md): The array the network computes on before the frame is applied.
- $G$ (pointwise gate), bound on [Finite linear network with roles and frames](linear-network-roles.md): The pointwise linear gate operation that combines input arrays at each address.
- $t$ (gate input count), bound on [Finite linear network with roles and frames](linear-network-roles.md): The number of input arrays of a gate.
- $\rho$ (role permutation), bound on [Finite linear network with roles and frames](linear-network-roles.md): The permutation of roles that the scalar network applies.
- $w$ (input role), bound on [Finite linear network with roles and frames](linear-network-roles.md): An input role of the scalar network, whose route ends at output role rho(w).
- $\varepsilon_w$ (route sign), bound on [Finite linear network with roles and frames](linear-network-roles.md): The sign on the route from input role w.
- $\mathrm{sink}$ (sink of a route), bound on [Finite linear network with roles and frames](linear-network-roles.md): The function giving the sink node at the output end of a route.
- $\mathrm{source}$ (source of a route), bound on [Finite linear network with roles and frames](linear-network-roles.md): The function giving the source node at the input end of a route.
- $I$ (identity operator), bound on [Finite linear network with roles and frames](linear-network-roles.md): The identity operator, which leaves every array unchanged.
- $\alpha$ (initial register value), bound on [Restoring auxiliary scratch values](scratch-restoration.md): The initial value of an auxiliary register, which may be any value.
- $\gamma$ (computed scratch result), bound on [Restoring auxiliary scratch values](scratch-restoration.md): The value left in the register by the intended computation of stage 2, which depends only on the data.
- $m$ (field count), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): The number of fields in each of the vectors $H$ and $D$.
- $H$ (first field vector), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): A vector of $m$ address fields, $H_1,\ldots,H_m$.
- $D$ (second field vector), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): A vector of $m$ address fields, $D_1,\ldots,D_m$.
- $q$ (digit radix), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): A fixed odd prime, the radix of the digits of each field; this letter changes meaning from the earlier pages.
- $b$ (digits per field), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): The number of radix-$q$ digits in one field, a count of digits; this letter changes meaning from the earlier pages.
- $M$ (rational matrix), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): A rational $m\times m$ matrix whose shear $(H,D)\mapsto(H+MD,D)$ is taken.
- $\Pi$ (partial permutation), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): The partial permutation matrix in the factorization of $M$, with at most one 1 in each row and column.
- $E_1$ (left factor), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): The invertible lower-triangular rational matrix on the left of the factorization of $M$.
- $E_2$ (right factor), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): The invertible lower-triangular rational matrix on the right of the factorization of $M$.
- $s$ (row index), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): The row index of an entry of $\Pi$.
- $g$ (column index), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): The column index of an entry of $\Pi$.
- $N$ (list length), bound on [Chinese-remainder map to prime cyclic axes](crt-address-map.md): The number of coefficients in the list, which equals the product of the $t$ distinct primes.
- $t$ (prime count), bound on [Chinese-remainder map to prime cyclic axes](crt-address-map.md): The number of distinct primes whose product is $N$, which is also the number of axes.
- $P_\ell$ (prime axis length), bound on [Chinese-remainder map to prime cyclic axes](crt-address-map.md): The $\ell$-th of the distinct primes, which is the length of the $\ell$-th cyclic axis.
- $\ell$ (axis index), bound on [Chinese-remainder map to prime cyclic axes](crt-address-map.md): The position of an axis among the $t$ axes, running from 1 to $t$.
- $\mathbb{Z}_{P_\ell}$ (residue axis), bound on [Chinese-remainder map to prime cyclic axes](crt-address-map.md): The set of residues modulo $P_\ell$, which is the $\ell$-th cyclic axis.
- $t$ (power-of-two length), bound on [Gaussian resampling](gaussian-resampling.md): The number of points in the power-of-two transform, chosen slightly above each prime length $p_j$.
- $L$ (list length), bound on [Gaussian resampling](gaussian-resampling.md): The number of entries in a list to which a transform or reordering applies.
- $F$ (discrete Fourier transform), bound on [Gaussian resampling](gaussian-resampling.md): The discrete Fourier transform of a list of length $L$, which evaluates the list at the $L$-th roots of unity.
- $P$ (coordinate reordering), bound on [Gaussian resampling](gaussian-resampling.md): A fixed reordering of the $L$ coordinates of a list of length $L$.
- $G$ (up-map to power-of-two grid), bound on [Gaussian resampling](gaussian-resampling.md): A linear contraction that maps lists of length $p_j$ to lists of length $t$.
- $J$ (down-map to prime grid), bound on [Gaussian resampling](gaussian-resampling.md): A linear contraction that maps lists of length $t$ back to lists of length $p_j$.
- $e$ (scale exponent), bound on [Gaussian resampling](gaussian-resampling.md): A fixed integer exponent giving the power-of-two factor $2^{e}$ in the identity.
- $\zeta$ (chirp root of unity), bound on [Bluestein's chirp identity](bluestein-chirp.md): A primitive $2n$th root of unity whose square is $\omega$, the base of the chirp phases.
- $g$ (premultiplied input), bound on [Bluestein's chirp identity](bluestein-chirp.md): The $k$th input $a_k$ multiplied by the chirp phase $\zeta^{k^2}$.
- $z$ (chirp), bound on [Bluestein's chirp identity](bluestein-chirp.md): The chirp sequence $\zeta^{-t^2}$, indexed by every integer $t$.
- $t$ (chirp index), bound on [Bluestein's chirp identity](bluestein-chirp.md): An integer index of the chirp $z_t$.
- $j$ (output index), bound on [Bluestein's chirp identity](bluestein-chirp.md): The index of an output $A_j$, ranging over the outputs.
- $k$ (input index), bound on [Bluestein's chirp identity](bluestein-chirp.md): The index of an input $a_k$, ranging over the inputs.
- $l$ (twisted chirp index), bound on [Bluestein's chirp identity](bluestein-chirp.md): The index of a twisted chirp $\zeta^l z_l$ in the cyclic sum.
- $v$ (twisted cyclic sum), bound on [Bluestein's chirp identity](bluestein-chirp.md): The cyclic convolution of the twisted lists $\zeta^k g_k$ and $\zeta^l z_l$ at index $j$.
- $z$ (cyclic variable), bound on [Last-coordinate phase twist](phase-twist-convolution.md): The formal variable of the cyclic ring $\mathbb C[z]/(z^r-1)$, whose exponents wrap modulo $r$.
- $\zeta$ (twist constant), bound on [Last-coordinate phase twist](phase-twist-convolution.md): The complex number $e^{\pi \mathrm i/r}$, whose $r$th power is $-1$, used to scale the twist.
- $k$ (last-axis index), bound on [Last-coordinate phase twist](phase-twist-convolution.md): An index of a coefficient on the last axis, with $0\le k<r$.
- $l$ (second last-axis index), bound on [Last-coordinate phase twist](phase-twist-convolution.md): A second index of a last-axis coefficient, paired with $k$ in a product.
- $j$ (cyclic product index), bound on [Last-coordinate phase twist](phase-twist-convolution.md): The cyclic index of a product coefficient, with $0\le j<r$.
- $h$ (wrap bit), bound on [Last-coordinate phase twist](phase-twist-convolution.md): The bit recording whether the exponent $k+l$ wrapped past $r$, so $h\in\{0,1\}$; not the radix carry $h_k$.
- $R$ (twisted ring), bound on [Last-coordinate phase twist](phase-twist-convolution.md): The polynomial ring $\mathbb C[y]/(y^r+1)$, in which the entries on the remaining axes lie.
- $v$ (remaining-axis index), bound on [Last-coordinate phase twist](phase-twist-convolution.md): A tuple with one coordinate per remaining cyclic axis, each wrapping modulo its length.
- $\alpha$ (first entry coefficients), bound on [Last-coordinate phase twist](phase-twist-convolution.md): The coefficients $\alpha_k$ of the first entry of a product, indexed by last-axis position $k$.
- $\beta$ (second entry coefficients), bound on [Last-coordinate phase twist](phase-twist-convolution.md): The coefficients $\beta_l$ of the second entry of a product, indexed by last-axis position $l$.
- $p$ (working precision), bound on [Fixed-point precision and exact recovery](fixed-point-precision.md): The number of fractional bits in each numerator, $p=6b$ in the source.
- $T$ (padded length), bound on [Fixed-point precision and exact recovery](fixed-point-precision.md): A power of two giving the padded length of the box of digit positions, with $4n/b\le T<8n/b$.
- $S$ (convolution length), bound on [Fixed-point precision and exact recovery](fixed-point-precision.md): The length of the cyclic convolution, the number of coefficients $c_j$ it produces.
- $L$ (log of padded length), bound on [Fixed-point precision and exact recovery](fixed-point-precision.md): The base-2 logarithm of $T$.
- $\gamma$ (source scale exponent), bound on [Fixed-point precision and exact recovery](fixed-point-precision.md): The exponent of the source scale $2^{\gamma}$ in the error bound, with $\gamma\le b/4$ for large $b$.
- $u$ (scaled digit list u), bound on [Fixed-point precision and exact recovery](fixed-point-precision.md): The digit list of the first input, each entry divided by $2^{b+2}$.
- $v$ (scaled digit list v), bound on [Fixed-point precision and exact recovery](fixed-point-precision.md): The digit list of the second input, each entry divided by $2^{b+2}$.
- $\mathcal F$ (forward transform), bound on [Fixed-point precision and exact recovery](fixed-point-precision.md): The forward transform of length $S$ applied to digit lists.
- $\mathcal F^{+}$ (opposite transform), bound on [Fixed-point precision and exact recovery](fixed-point-precision.md): The opposite transform, the conjugate-direction counterpart of $\mathcal F$.
- $p$ (precision exponent), bound on [Signed coefficient packing (Kronecker substitution)](signed-packing.md): The exponent bounding every input coefficient by $2^p$ in absolute value.
- $B$ (block base), bound on [Signed coefficient packing (Kronecker substitution)](signed-packing.md): The base $2^{4p}$ in which the coefficients of a packed integer are written, one block per coefficient.
- $u$ (packed polynomial), bound on [Signed coefficient packing (Kronecker substitution)](signed-packing.md): The input polynomial in $\mathbb Z[y]$ whose coefficients are packed into one integer.
- $v$ (second polynomial), bound on [Signed coefficient packing (Kronecker substitution)](signed-packing.md): The second input polynomial in $\mathbb Z[y]$, multiplied with $u$ through their packed integers.
- $j$ (coefficient position), bound on [Signed coefficient packing (Kronecker substitution)](signed-packing.md): The position of a coefficient of $u$, running over $0,\dots,r-1$.
- $t$ (coefficient position of v), bound on [Signed coefficient packing (Kronecker substitution)](signed-packing.md): The position of a coefficient of $v$, running over $0,\dots,r-1$.
- $h$ (ordinary product), bound on [Signed coefficient packing (Kronecker substitution)](signed-packing.md): The ordinary product $uv$ in $\mathbb Z[y]$, whose coefficients are recovered from one packed integer.
- $k$ (product coefficient index), bound on [Signed coefficient packing (Kronecker substitution)](signed-packing.md): The index of a coefficient of the ordinary product $h$, so that $h_k$ is the coefficient of $y^k$.
- $d$ (block digit), bound on [Signed coefficient packing (Kronecker substitution)](signed-packing.md): The nonnegative digit below $B$ stored in block $j$ of the packed integer.
- $\gamma$ (carry), bound on [Signed coefficient packing (Kronecker substitution)](signed-packing.md): The carry into block $j$ when the coefficients of $u$ are written in blocks, starting from $\gamma_0=0$.
- $a$ (real component of record), bound on [Signed coefficient packing (Kronecker substitution)](signed-packing.md): The real component of the numerator of the first record, a polynomial in $\mathbb Z[y]$.
- $b$ (imaginary component of record), bound on [Signed coefficient packing (Kronecker substitution)](signed-packing.md): The imaginary component of the numerator of the first record, a polynomial in $\mathbb Z[y]$.
- $c$ (second record real part), bound on [Signed coefficient packing (Kronecker substitution)](signed-packing.md): The real component of the numerator of the second record, a polynomial in $\mathbb Z[y]$.
- $e$ (second record imaginary part), bound on [Signed coefficient packing (Kronecker substitution)](signed-packing.md): The imaginary component of the numerator of the second record, a polynomial in $\mathbb Z[y]$.
- $f$ (input array f), bound on [Convolution with retained transform order and cancelled permutations](ring-convolution-retained-order.md): One of the two input arrays over the ring whose convolution is computed.
- $g$ (input array g), bound on [Convolution with retained transform order and cancelled permutations](ring-convolution-retained-order.md): The second of the two input arrays over the ring whose convolution is computed.
- $\mathcal{D}$ (forward transform), bound on [Convolution with retained transform order and cancelled permutations](ring-convolution-retained-order.md): The synthetic forward transform applied to each input array.
- $\mathcal{D}^{+}$ (opposite transform), bound on [Convolution with retained transform order and cancelled permutations](ring-convolution-retained-order.md): The transform that inverts the forward transform up to the scalar $M$.
- $M$ (known scalar), bound on [Convolution with retained transform order and cancelled permutations](ring-convolution-retained-order.md): A fixed constant, set by the normalization of the transforms, by which the forward and opposite transforms differ from inverses.
- $L$ (frequency-order permutation), bound on [Convolution with retained transform order and cancelled permutations](ring-convolution-retained-order.md): The permutation of addresses that the forward transform applies to its output, which fixes the frequency order.
- $k$ (frequency position), bound on [Convolution with retained transform order and cancelled permutations](ring-convolution-retained-order.md): The position of a frequency entry in the transform's output order.
- $h$ (ground set size), bound on [Three-element subset intersection construction](subset-intersection-construction.md): The number of elements of the ground set $[h]$, here 100.
- $\mathcal T$ (triple set), bound on [Three-element subset intersection construction](subset-intersection-construction.md): The set of three-element subsets of the ground set $[h]$.
- $t_T$ (indicator vector), bound on [Three-element subset intersection construction](subset-intersection-construction.md): The indicator vector of the triple $T$, with entry 1 at each element of $T$ and 0 elsewhere.
- $g_T$ (triple value), bound on [Three-element subset intersection construction](subset-intersection-construction.md): The value carried by the triple $T$ as a source of the network.
- $\alpha$ (data index), bound on [Three-element subset intersection construction](subset-intersection-construction.md): An ordered triple $(T_1,T_2,T_3)$ of triples, indexing one data entry of the network.
- $U_\alpha$ (index label), bound on [Three-element subset intersection construction](subset-intersection-construction.md): The line in the label space spanned by the tensor product of the indicator vectors of the triples in $\alpha$.
- $\mathcal F$ (label space), bound on [Three-element subset intersection construction](subset-intersection-construction.md): The ambient space $(\mathbb Q^h)^{\otimes 3}$ in which all labels are subspaces.
- $m$ (label dimension), bound on [Three-element subset intersection construction](subset-intersection-construction.md): The dimension of the label space $\mathcal F$, which is $h^3$.
- $J$ (all-one matrix), bound on [Three-element subset intersection construction](subset-intersection-construction.md): The $h\times h$ matrix with every entry equal to 1.
- $P_U$ (label projection), bound on [Three-element subset intersection construction](subset-intersection-construction.md): The projection onto the subspace $U$ along its orthogonal complement $U^\perp$, assigned to a gate or sink with label $U$.
- $s$ (smaller call count), bound on [Three-element subset intersection construction](subset-intersection-construction.md): The number of smaller calls, the sum over all edges of the rank of the difference of the matrices at its two ends.
- $N$ (data index count), bound on [Three-element subset intersection construction](subset-intersection-construction.md): The number of data indices $\alpha$, which is also the total dimension of the source labels.
- $L$ (lost label dimension), bound on [Three-element subset intersection construction](subset-intersection-construction.md): The total dimension lost by the label along the decreasing edges of the network.
- $f$ (call parameter), bound on [Recursive power saving from s<Wm](recursive-power-saving.md): The parameter of a call, counting field digits for address interchange or selected axes for a numerical layer.
- $m$ (parameter factor), bound on [Recursive power saving from s<Wm](recursive-power-saving.md): The factor by which a call's parameter is multiplied in the recursive call.
- $T$ (normalized cost), bound on [Recursive power saving from s<Wm](recursive-power-saving.md): The cost of a call at parameter f divided by the volume it works on.
- $C$ (overhead constant), bound on [Recursive power saving from s<Wm](recursive-power-saving.md): The constant bounding the normalized outside work at a node.
- $\lambda$ (outside-work exponent), bound on [Recursive power saving from s<Wm](recursive-power-saving.md): The exponent, below 1, bounding the normalized outside work at a node of parameter mf.
- $\tau$ (cost exponent), bound on [Fast interchange of address fields](fast-address-interchange.md): A fixed exponent below 1 in the cost $O(Vu^\tau)$ of the procedure.
- $\mathbb F_2$ (two-element field), bound on [Fast interchange of address fields](fast-address-interchange.md): The field with elements 0 and 1, in which addition and subtraction are both XOR.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Recursive power saving from s<Wm](recursive-power-saving.md): Recursive call at parameter mf uses s calls at parameter f on streams of volume V/W; since s/W<m the volume-normalized cost grows as a power, giving a fixed power saving.
  Shown as: Fast simultaneous butterfly layers *<predicate>* Recursive power saving from s<Wm
- [Fast interchange of address fields](fast-address-interchange.md): Interchange two disjoint contiguous u-bit address fields in an array in O(V u^τ) for fixed τ<1, via XOR combinations that end as an exact permutation.
  Shown as: Fast simultaneous butterfly layers *<predicate>* Fast interchange of address fields
- [Synthetic polynomial transforms](synthetic-transforms.md): Nussbaumer-style transforms over the polynomial ring where root multiplications are signed shifts, leaving address rearrangements, shifts and butterflies.
  Shown as: Fast simultaneous butterfly layers *<predicate>* Synthetic polynomial transforms
- [Fixed-point precision and exact recovery](fixed-point-precision.md): Complex fixed-point coefficients; bounding error below 1/2 so rounding recovers exact integer coefficients and carry propagation yields the product.
  Shown as: Fast simultaneous butterfly layers *<predicate>* Fixed-point precision and exact recovery

## Pages that build on this one

- Integer multiplication in O(n(lg n)^{1-κ}) time: Deterministic fixed-tape Turing machine multiplying n-bit integers in O(n(lg n)^{1-κ}), κ=2^{-182}, by reducing to ring convolution with fast address interchanges and simultaneous butterfly layers, disproving the n log n conjecture in this model.

## Other pages you may link to

- [The n log n optimality conjecture](nlogn-conjecture.md)
- [Convolution](convolution.md)
- [Reduction of integer product to digit convolution](radix-digit-reduction.md)
- [Polynomial ring modulo $y^r+1$](poly-ring-y-r.md)
- [Fixed-tape machine model and stream operations](fixed-tape-model.md)
- [Address fields and array layout on tapes](address-fields.md)
- [Discrete Fourier transform and butterflies](dft-fft.md)
- [Schönhage–Strassen to Harvey–van der Hoeven multiplication](ss-hh-background.md)
- [Finite linear network with roles and frames](linear-network-roles.md)
- [Restoring auxiliary scratch values](scratch-restoration.md)
- [Address shear and lower-triangular factorization](address-shear-factorization.md)
- [Chinese-remainder map to prime cyclic axes](crt-address-map.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein's chirp identity](bluestein-chirp.md)
- [Last-coordinate phase twist](phase-twist-convolution.md)
- [Signed coefficient packing (Kronecker substitution)](signed-packing.md)
- [Convolution with retained transform order and cancelled permutations](ring-convolution-retained-order.md)
- [Tensor product of vector spaces](tensor-product-of-vector-spaces.md)
- [Three-element subset intersection construction](subset-intersection-construction.md)
- [Integer multiplication in O(n(lg n)^{1-κ}) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "The second procedure applies" (paper)

  > The second procedure applies \[ H_0(u,v)=\bigl((u+v)/2,(u-v)/2\bigr) \] simultaneously on selected coordinate bits of the numerical arrays. Each record is a polynomial with complex fixed-point coefficients, and $H_0$ acts coefficientwise. On the layouts used in the multiplication algorithm, one selects the same bit position in each of at most $d$ equal-width address chunks, and the cost is $O(Vd^{\lambda'})$ for a fixed $\lambda'<1$. Intermediate values are exact Gaussian dyadics, whose real and imaginary parts have power-of-two denominators. A single truncation follows the completed contractive layer. Section~\ref{sec:tape-interchange} proves the address bound, and Section~\ref{sec:fast-butterfly-layers} gives the numerical layout, precision hypotheses, and layer bound.


## Sources (read from disk as needed)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The reader cannot follow this step: "The network satisfies $s/W<m^{\sigma}$" (This is the central complexity property of the layer and is cited, but the page does not say which network it is or why the bound applies to the network used here.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step. It is inside reasoning added for an earlier step. If it is part of how this page's own step of the argument works (see "This page in the argument"), develop it here; if it concerns a result that step uses, say what the result states and cite it.
- The reader cannot follow this step: "A network of these changes turns $C^{\otimes mf}$ into $s$ child calls" (The page asserts that the network of interchanges turns C^{tensor mf} into s calls of C^{tensor f} on slots without explaining the construction or why it works.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step. It is inside reasoning added for an earlier step. If it is part of how this page's own step of the argument works (see "This page in the argument"), develop it here; if it concerns a result that step uses, say what the result states and cite it.
- The reader cannot follow this step: "Splitting the rows among the network's $W$ wires gives each child $1/W$ of the volume." (The page does not say how the rows are split or why each child receives exactly 1/W of the volume.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step. It is inside reasoning added for an earlier step. If it is part of how this page's own step of the argument works (see "This page in the argument"), develop it here; if it concerns a result that step uses, say what the result states and cite it.
- The reader cannot follow this step: "$T(mf)\le (s/W)\,T(f)+O(1)$" (The O(1) term (the network's outside work) is not explained, so the inequality cannot be checked from the page.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step. It is inside reasoning added for an earlier step. If it is part of how this page's own step of the argument works (see "This page in the argument"), develop it here; if it concerns a result that step uses, say what the result states and cite it.
- The reader cannot follow this step: "Applying the identity to each selected bit gives" (The identity that the tensor power of a product factors into the product of tensor powers is not stated or justified on the page.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step. It is inside reasoning added for an earlier step. If it is part of how this page's own step of the argument works (see "This page in the argument"), develop it here; if it concerns a result that step uses, say what the result states and cite it.
- The reader cannot follow this step: "taking $\lambda'$ above $\sigma+\tfrac12(1-\sigma)$" (The page links to the recursive power saving page but does not say what that result states or how the threshold sigma + (1-sigma)/2 arises for this layer.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step. It is inside reasoning added for an earlier step. If it is part of how this page's own step of the argument works (see "This page in the argument"), develop it here; if it concerns a result that step uses, say what the result states and cite it.
- The reader cannot follow this step: "Because $C$ is unitary, a coefficient can exceed modulus 1 mid-computation" (The page does not explain why unitarity lets intermediate coefficients exceed modulus 1.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step. It is inside reasoning added for an earlier step. If it is part of how this page's own step of the argument works (see "This page in the argument"), develop it here; if it concerns a result that step uses, say what the result states and cite it.
- The reader cannot follow this step: "so the procedure carries $O(p)$ extra fractional bits" (The number of extra bits needed is not derived from the growth of intermediate values, so the O(p) claim cannot be checked.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step. It is inside reasoning added for an earlier step. If it is part of how this page's own step of the argument works (see "This page in the argument"), develop it here; if it concerns a result that step uses, say what the result states and cite it.
- The reader cannot follow this step: "This truncation keeps error within the bound of" (The cited claim does not say what the error bound is or why truncation satisfies it at this point.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step. It is inside reasoning added for an earlier step. If it is part of how this page's own step of the argument works (see "This page in the argument"), develop it here; if it concerns a result that step uses, say what the result states and cite it.
- Explain "unitary" in a sentence where it is first used.

## Previous version (revise it)

It has 413 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 516 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

Fast simultaneous butterfly layers is a fixed-tape procedure that applies $H_0(u,v)=((u+v)/2,(u-v)/2)$ to one bit position in several address chunks at once, where $u$ and $v$ are the two records at addresses that differ only in the selected bit and $H_0$ combines them coefficientwise. Applied one at a time, the butterflies would cost one whole-array pass each. The layer performs the butterfly rounds of [Synthetic polynomial transforms](synthetic-transforms.md).

## The layer

Let $D$ be the number of selected address chunks, and let $d$ be an upper bound on $D$, so $D\le d$. Each chunk has $K$ bits, and the selected bit has one common offset. The width of a coefficient is its number of stored bits, $O(p)$ per real or imaginary component. The layer leaves the other address bits unchanged and costs $O(Vd^{\lambda'})$ for a fixed exponent $\lambda'<1$.

## Method

Let $X$ be the bit-flip matrix. Here $i$ is the imaginary unit, so the letter changes meaning here. Let $\Phi=\operatorname{diag}(1,i)$ be the diagonal phase matrix. Let $C=\tfrac12\bigl((1+i)I+(1-i)X\bigr)$ be the two-point kernel. Direct multiplication gives

$$H_0=\tfrac{1-i}{2}\,\Phi C\Phi.$$

So each butterfly is the kernel $C$ between two phases. Multiplying by a power of $i$ only swaps and negates real and imaginary parts, at cost linear in the coefficient width. The tensor product of matrices, written $\otimes$, replaces each entry of the first matrix by that entry times the second matrix, so $C^{\otimes D}$ is a $2^D\times 2^D$ matrix on the $D$ selected bits. Applying the identity to each selected bit gives

$$H_0^{\otimes D}=\left(\tfrac{1-i}{2}\right)^{D}\Phi^{\otimes D}\,C^{\otimes D}\,\Phi^{\otimes D},$$

so the cost lies in computing $C^{\otimes D}$.

The layer computes $C^{\otimes D}$ recursively. A group of $mf$ selected bits is split into $m$ slots of $f$ bits, and the layer moves whole chunks by [Fast interchange of address fields](fast-address-interchange.md) to realize its binary basis changes. A network of these changes turns $C^{\otimes mf}$ into $s$ child calls, each computing $C^{\otimes f}$ on one slot. Splitting the rows among the network's $W$ wires gives each child $1/W$ of the volume. Writing $T(f)$ for normalized cost at parameter $f$, $T(mf)\le (s/W)\,T(f)+O(1)$. The network satisfies $s/W<m^{\sigma}$ for a fixed exponent $\sigma=1-2^{-50}$. <cite data-source="paper">For both recurrences we may use the fixed rational exponent</cite>. Unrolling over the $\log_m d$ levels, $T(d)$ grows no faster than $d^{\sigma}$. The layer gets its exponent $\lambda'<1$ from [Recursive power saving from s<Wm](recursive-power-saving.md), taking $\lambda'$ above $\sigma+\tfrac12(1-\sigma)$.

## Exactness

A Gaussian dyadic is a complex number whose real and imaginary parts have power-of-two denominators. Each entry of $C$ is $\tfrac{1\pm i}{2}$, so each selected bit adds one binary digit to the denominators. <cite data-source="paper">Intermediate values are exact Gaussian dyadics</cite>. Because $C$ is unitary, a coefficient can exceed modulus 1 mid-computation, so the procedure carries $O(p)$ extra fractional bits. The final values stay in the unit disk, because one butterfly maps moduli at most 1 to $(|u|+|v|)/2\le 1$.

<cite data-source="paper">A single truncation follows the completed contractive layer.</cite> This truncation keeps error within the bound of [Fixed-point precision and exact recovery](fixed-point-precision.md).

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

Write the body to `exegenius/tasks/0125-write-fast-butterfly-layers.answer.md` and the JSON to `exegenius/tasks/0125-write-fast-butterfly-layers.answer.json`, then run `exegenius submit 0125-write-fast-butterfly-layers` in the project directory. If submit rejects the answer, fix the answer and submit again.
