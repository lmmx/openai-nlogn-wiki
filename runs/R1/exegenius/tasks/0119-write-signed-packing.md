# exegenius task 0119-write-signed-packing

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

- The reader cannot follow this step: "The packing lemma assumes $r<2^p$ with $p\ge 2$ (cited)" (The page never says that r < 2^p holds for the polynomials it packs, yet the bound |h_k| < 2^{3p} that it derives depends on it. The cited lemma's hypothesis is not shown to apply here.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step. It is inside reasoning added for an earlier step. If it is part of how this page's own step of the argument works (see "This page in the argument"), develop it here; if it concerns a result that step uses, say what the result states and cite it.
- The reader cannot follow this step: "has real and imaginary components $a,b\in\mathbb Z[y]$, whose coefficients are at most $2^p$ in absolute value (cited)" (The page does not say why a complex fixed-point record scaled by 2^{-p} has integer components with coefficients bounded by 2^p, and the cited source is not named. The page also defines p as a quantity different from the earlier working precision, so the reader cannot tie this bound to the fixed-point precision concept.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step. It is inside reasoning added for an earlier step. If it is part of how this page's own step of the argument works (see "This page in the argument"), develop it here; if it concerns a result that step uses, say what the result states and cite it.

## Previous version (revise it)

It has 358 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 447 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

Signed coefficient packing (Kronecker substitution) encodes a polynomial with integer coefficients of either sign as one integer, so that a polynomial product becomes an integer product, which an ordinary $O(n\log n)$ multiplier computes.

Let $p$ be a precision exponent, a quantity different from the working precision of earlier pages, such that every coefficient of the input polynomials has absolute value at most $2^p$, and let $B=2^{4p}$ be the block base. For $u=\sum_{j=0}^{r-1}u_j y^j$ in $\mathbb Z[y]$ with $|u_j|\le 2^p$, the packed integer is
$$u(B)=\sum_{j=0}^{r-1}u_jB^j.$$
Here $j$ and $t$ are coefficient positions, and $r$ is the number of coefficients. The sum may be negative. Reused letters are defined at first use.

On tapes, a carry $\gamma_j$ and a block digit $d_j$ satisfy $\gamma_0=0$, $0\le d_j<B$, $d_j\equiv u_j+\gamma_j \pmod B$, and $\gamma_{j+1}=(u_j+\gamma_j-d_j)/B$. Each $\gamma_j$ stays in $\{-1,0\}$, since $u_j+\gamma_j$ lies in $(-B,B)$. Telescoping gives $u(B)=\sum_j d_jB^j+\gamma_rB^r$. So the blocks are nonnegative digits, and the sign is the final carry $\gamma_r$, a sign extension above the top block. Each block is $4p$ bits wide <cite data-source="paper">Every block has $4p$ bits</cite>.

Evaluation respects products: for a second input polynomial $v=\sum_{t=0}^{r-1}v_t y^t$ with $|v_t|\le 2^p$, $u(B)\,v(B)=(uv)(B)$ exactly, where $uv$ is the ordinary product in $\mathbb Z[y]$. Signed coefficient packing computes its integer products by the [Schönhage–Strassen to Harvey–van der Hoeven multiplication](ss-hh-background.md), an ordinary subroutine call that costs $O(n\log n)$.

Recovering the coefficients. Write $h=uv$ for that product, and $h_k$ for its coefficient of $y^k$, with $k$ running over $0,\dots,2r-2$. Each $h_k$ sums at most $r$ products $u_jv_t$, so $|h_k|\le r2^{2p}$. The packing lemma assumes $r<2^p$ with $p\ge 2$ <cite data-source="paper">Let $r=2^\ell<2^p$ with integers $\ell\geq1$ and $p\geq2$</cite>, so $|h_k|<2^{3p}\le B/2$. Since every $h_kB^k$ with $k\ge1$ is a multiple of $B$, $h(B)\equiv h_0 \pmod B$. As $|h_0|<B/2$, $h_0$ is the unique integer in $[-B/2,B/2)$ congruent to $h(B)$ modulo $B$. Subtracting it and dividing by $B$ leaves the same form for $h_1,h_2,\dots$.

Example with $B=12$. For $u=2-y$ and $v=1+3y$, $u(12)=-10$ and $v(12)=37$, so the packed product is $-370$. Since $-370\equiv 2 \pmod{12}$ and $2\in[-6,6)$, $h_0=2$ and $(-370-2)/12=-31$. Then $-31\equiv 5$, so $h_1=5$ and $h_2=-3$, giving $uv=2+5y-3y^2$.

Gaussian products. A polynomial record is a polynomial of degree less than $r$ with complex fixed-point coefficients, stored on a tape. A record $f=2^{-p}(a+\sqrt{-1}\,b)$ has real and imaginary components $a,b\in\mathbb Z[y]$, whose coefficients are at most $2^p$ in absolute value <cite data-source="paper">The truncated numerators have magnitude at most $2^p$</cite>. The second record $g=2^{-p}(c+\sqrt{-1}\,e)$ has components $c,e\in\mathbb Z[y]$, and the product is
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

Write the body to `exegenius/tasks/0119-write-signed-packing.answer.md` and the JSON to `exegenius/tasks/0119-write-signed-packing.answer.json`, then run `exegenius submit 0119-write-signed-packing` in the project directory. If submit rejects the answer, fix the answer and submit again.
