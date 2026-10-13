# exegenius task 0076-write-main-theorem

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
- Discrete Fourier transform and butterflies
- The n log n optimality conjecture
- Schönhage–Strassen to Harvey–van der Hoeven multiplication
- Reduction of integer product to digit convolution
- Chinese-remainder map to prime cyclic axes
- Gaussian resampling
- Bluestein's chirp identity
- Polynomial ring modulo $y^r+1$
  - $y$ (ring variable): The polynomial variable whose powers act as roots of unity.
  - $r$ (ring degree): The power of two giving the number of coefficients in each polynomial.
- Synthetic polynomial transforms
- Signed coefficient packing (Kronecker substitution)
- Last-coordinate phase twist
- Convolution with retained transform order and cancelled permutations
- Address fields and array layout on tapes (also: fields, address rearrangements and signed shifts)
- Finite linear network with roles and frames (also: scalar network)
- Three-element subset intersection construction
- Recursive power saving from s<Wm
- Address shear and lower-triangular factorization
- Restoring auxiliary scratch values
- Fast interchange of address fields (also: address interchange and numerical layer, interchange)
- Fast simultaneous butterfly layers
- Fixed-point precision and exact recovery
- Binary representation and bit operations (also: bits, XOR, bitwise operations, base 2)
- Modular arithmetic (also: congruence, residues mod m, remainder arithmetic)
- Prime numbers and coprimality (also: primes, relatively prime, gcd, distinct primes)
- Logarithms and floor/ceiling (also: lg, log base 2, floor, ceiling, iterated logarithm)
- Vectors, matrices and inverses (also: linear algebra, matrix multiplication, invertible matrix, dot product, orthogonality, linear map)
- Schoolbook and Karatsuba multiplication (also: grade-school multiplication, long multiplication, Karatsuba)
- Divide-and-conquer recurrences (also: master theorem, recurrence relations, recursion tree)
- Limits, series and convergence (also: geometric series, summation, converging sum, epsilon bounds)
- Cartesian product and tuples (also: product of sets, index tuples, mixed radix, multi-index)
- Permutations (also: bijection, rearrangement, reordering, inverse permutation)
- Roots of unity (also: nth roots of unity, primitive root of unity, e^{2 pi i/n})
- Rings and basic algebraic structures (also: ring, commutative ring, group, quotient ring, residue ring)
- Fixed-point and rounding arithmetic (also: rounding error, truncation, fixed-point numbers, absolute error)

## This page

Concept: Integer multiplication in O(n(lg n)^{1-κ}) time
Gloss: Deterministic fixed-tape Turing machine multiplying n-bit integers in O(n(lg n)^{1-κ}), κ=2^{-182}, by reducing to ring convolution with fast address interchanges and simultaneous butterfly layers, disproving the n log n conjecture in this model.
Heading: Integer multiplication in $O(n(\lg n)^{1-\kappa})$ time

The symbols in this page's heading denote (say so on the page):

- $n$ (input length): The number of bits in each integer being multiplied.
- $\kappa$ (saving exponent): The fixed constant 2^{-182} giving the power saving in the logarithmic factor.

## This page in the argument

The step: An $n$-bit integer product is computed by a fixed-tape machine in $O(n(\lg n)^{1-\kappa})$ time, $\kappa=2^{-182}$.
How: reduce multiplication to ring convolution and speed up its address moves and butterfly layers
Why: The n log n cost comes from moving data and applying butterflies at every transform level, so faster versions of exactly these operations lower the whole bound. (the sources leave this for the reader to work out: spell it out)
Striking feature: The logarithmic factor drops by a fixed power $\kappa$, strictly below the conjectured $n\log n$. (explain why it holds, from the method)

Its sub-steps, in order:

- Splitting the inputs into radix digits reduces the integer product to a convolution of short integer coefficients. (on [Reduction of integer product to digit convolution](radix-digit-reduction.md))
- Two fixed-tape procedures, an address interchange and a simultaneous butterfly layer, cost $O(Vu^\tau)$ and $O(Vd^{\lambda'})$ for fixed exponents below 1, where $V$ is the stored bit volume.
- The radix-digit coefficient list is placed on a product of distinct prime cyclic axes by a convolution-preserving Chinese-remainder map. (on [Chinese-remainder map to prime cyclic axes](crt-address-map.md))
- Gaussian resampling expresses each source Fourier transform through a power-of-two tensor transform. (on [Gaussian resampling](gaussian-resampling.md))
- Bluestein's chirp identity converts the middle transform into normalized cyclic convolution. (on [Bluestein's chirp identity](bluestein-chirp.md))
- A phase twist turns the last cyclic coordinate into a polynomial modulo $y^r+1$, whose negative wrap gives the original cyclic wrap after untwisting. (on [Last-coordinate phase twist](phase-twist-convolution.md))
- Convolution over $\mathbb C[y]/(y^r+1)$ on the remaining axes is computed by synthetic transforms and packed polynomial products. (on [Convolution with retained transform order and cancelled permutations](ring-convolution-retained-order.md))
- Known rescalings and rounding recover the coefficients since the error is below $1/2$, and carry propagation gives the exact product. (on [Fixed-point precision and exact recovery](fixed-point-precision.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S1). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S1**: Two fixed-tape procedures, an address interchange and a simultaneous butterfly layer, cost $O(Vu^\tau)$ and $O(Vd^{\lambda'})$ for fixed exponents below 1, where $V$ is the stored bit volume.
How: build both procedures from one finite linear network and a recursion that saves a power

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S2 (on [Reduction of integer product to digit convolution](radix-digit-reduction.md)): Splitting the inputs into radix digits reduces the integer product to a convolution of short integer coefficients.
- S3 (on [Chinese-remainder map to prime cyclic axes](crt-address-map.md)): The radix-digit coefficient list is placed on a product of distinct prime cyclic axes by a convolution-preserving Chinese-remainder map.
- S4 (on [Gaussian resampling](gaussian-resampling.md)): Gaussian resampling expresses each source Fourier transform through a power-of-two tensor transform.
- S5 (on [Bluestein's chirp identity](bluestein-chirp.md)): Bluestein's chirp identity converts the middle transform into normalized cyclic convolution.
- S6 (on [Last-coordinate phase twist](phase-twist-convolution.md)): A phase twist turns the last cyclic coordinate into a polynomial modulo $y^r+1$, whose negative wrap gives the original cyclic wrap after untwisting.
- S7 (on [Convolution with retained transform order and cancelled permutations](ring-convolution-retained-order.md)): Convolution over $\mathbb C[y]/(y^r+1)$ on the remaining axes is computed by synthetic transforms and packed polynomial products.
- S8 (on [Fixed-point precision and exact recovery](fixed-point-precision.md)): Known rescalings and rounding recover the coefficients since the error is below $1/2$, and carry propagation gives the exact product.
- S1.1 (on [Finite linear network with roles and frames](linear-network-roles.md)): Each procedure comes from a fixed linear network that exchanges two banks of values with prescribed signs and restores every auxiliary value; rows are distributed among $W$ roles and frames cancel along routes.
- S1.2 (on [Fast interchange of address fields](fast-address-interchange.md)): Two disjoint contiguous $u$-bit address fields can be interchanged in $O(Vu^\tau)$ for a fixed $\tau<1$, although the intermediate steps are XOR combinations.
- S1.3 (on [Fast simultaneous butterfly layers](fast-butterfly-layers.md)): A simultaneous layer of $H_0(u,v)=((u+v)/2,(u-v)/2)$ on selected address bits of polynomial-valued arrays costs $O(Vd^{\lambda'})$ with $\lambda'<1$, with a single truncation at the end.
- S1.4 (on [Three-element subset intersection construction](subset-intersection-construction.md)): The network is built from three-element subsets with gather, scatter and cancelling auxiliary wires, so that the total number $s$ of smaller calls satisfies $s<Wm$.
- S1.5 (on [Recursive power saving from s<Wm](recursive-power-saving.md)): A recursive call at parameter $mf$ uses $s$ calls at parameter $f$ on streams of volume $V/W$, so the volume-normalized cost grows as a power, giving a fixed power saving.

## Symbols already bound on earlier pages

The symbols in the names of the concepts the reader knows are listed with those concepts above.

- $n$ (input length), bound on [The n log n optimality conjecture](nlogn-conjecture.md): The number of bits in each of the two integers being multiplied.
- $n$ (list length), bound on [Convolution](convolution.md): The number of entries in each input and output coefficient list.
- $a$ (input list a), bound on [Convolution](convolution.md): The first input coefficient list, with entries $a_0,\dots,a_{n-1}$.
- $b$ (input list b), bound on [Convolution](convolution.md): The second input coefficient list, with entries $b_0,\dots,b_{n-1}$.
- $c$ (output list), bound on [Convolution](convolution.md): The cyclic convolution of $a$ and $b$, a list of $n$ entries.
- $i$ (index i), bound on [Convolution](convolution.md): An index into the entries of the input list $a$.
- $j$ (index j), bound on [Convolution](convolution.md): An index into the entries of the input list $b$.
- $k$ (output index), bound on [Convolution](convolution.md): An index into the entries of the output list $c$.
- $y$ (indeterminate), bound on [Convolution](convolution.md): A symbol with no value, used as the variable of the polynomials whose coefficients are the lists.
- $n$ (input bit length), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The bit length of each input, the number of bits in each of the two integers.
- $b$ (digit width), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The number of bits in each radix digit.
- $q$ (digit count), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The number of radix digits of each input.
- $x$ (first input), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The first $n$-bit input integer.
- $y$ (second input), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The second $n$-bit input integer.
- $x_j$ (digit of x), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The $j$th radix-$2^b$ digit of $x$.
- $y_j$ (digit of y), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The $j$th radix-$2^b$ digit of $y$.
- $c_k$ (product coefficient), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The $k$th coefficient of the digit convolution of $x$ and $y$.
- $h_k$ (carry), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The carry into position $k$ during carry propagation.
- $d_k$ (output digit), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The radix-$2^b$ digit of the product at position $k$.
- $y$ (ring variable), bound on [Polynomial ring modulo $y^r+1$](poly-ring-y-r.md): The polynomial variable whose powers act as roots of unity.
- $r$ (ring degree), bound on [Polynomial ring modulo $y^r+1$](poly-ring-y-r.md): The number of complex coefficients in each element of the ring, a power of two.
- $p$ (working precision), bound on [Fixed-point precision and exact recovery](fixed-point-precision.md): The number of fractional bits in each fixed-point numerator, so values are stored over the denominator $2^p$.
- $S$ (cyclic convolution length), bound on [Fixed-point precision and exact recovery](fixed-point-precision.md): The number of coefficients in the cyclic convolution whose transforms are computed.
- $c_j$ (product coefficient), bound on [Fixed-point precision and exact recovery](fixed-point-precision.md): The exact integer coefficient of the product at index $j$.
- $b$ (digit width), bound on [Fixed-point precision and exact recovery](fixed-point-precision.md): The number of bits in each radix digit, equal to the ceiling of the base-2 logarithm of the input length $n$.
- $d_j$ (output digit), bound on [Fixed-point precision and exact recovery](fixed-point-precision.md): The radix-$2^b$ digit of the product at position $j$.
- $k_j$ (carry), bound on [Fixed-point precision and exact recovery](fixed-point-precision.md): The carry from the processed coefficients into position $j$.
- $u$ (address field width), bound on [Address fields and array layout on tapes](address-fields.md): The number of bits in one address field, a count of bits.
- $V$ (stored bit volume), bound on [Address fields and array layout on tapes](address-fields.md): The total number of bits the array holds, a count of stored bits.
- $n$ (input size), bound on [Address fields and array layout on tapes](address-fields.md): The size of the input, so that the array holds $\Theta(n)$ bits.
- $n$ (list length), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The number of coefficients in the list $a$, a power of two.
- $a$ (coefficient list), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The list of $n$ complex coefficients $a_0,\dots,a_{n-1}$ being transformed.
- $\omega$ (root of unity), bound on [Discrete Fourier transform and butterflies](dft-fft.md): A primitive $n$-th root of unity, with $\omega^n=1$ and $\omega^m\neq 1$ for $0<m<n$.
- $A$ (transform of a), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The list of $n$ values $A_0,\dots,A_{n-1}$ obtained by evaluating $a$ at the powers of $\omega$.
- $n$ (integer length), bound on [Schönhage–Strassen to Harvey–van der Hoeven multiplication](ss-hh-background.md): The number of bits in each integer being multiplied.
- $W$ (role count), bound on [Finite linear network with roles and frames](linear-network-roles.md): The number of roles of the network, which counts the fixed places its wires occupy.
- $V$ (padded bit volume), bound on [Finite linear network with roles and frames](linear-network-roles.md): The number of bits stored in the array after padding, which counts the node volume the network handles.
- $D_v$ (frame), bound on [Finite linear network with roles and frames](linear-network-roles.md): The invertible linear operator assigned to a source, gate or sink $v$, acting on arrays indexed by the common address set.
- $\varepsilon_w$ (route sign), bound on [Finite linear network with roles and frames](linear-network-roles.md): The prescribed scalar sign carried by the route from input role $w$ through the network.
- $\rho$ (role permutation), bound on [Finite linear network with roles and frames](linear-network-roles.md): The permutation of roles that the scalar network applies, sending input role $w$ to output role $\rho(w)$.
- $a$ (initial auxiliary value), bound on [Restoring auxiliary scratch values](scratch-restoration.md): The initial content of an auxiliary register, which may be any value.
- $m$ (fields per vector), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): The number of address fields in each of the vectors $H$ and $D$.
- $H$ (first address vector), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): The vector $(H_1,\ldots,H_m)$ of $m$ address fields.
- $D$ (second address vector), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): The vector $(D_1,\ldots,D_m)$ of $m$ address fields.
- $b$ (digits per field), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): The number of radix-$q$ digits in one address field.
- $q$ (radix), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): A fixed odd prime, the radix of each digit.
- $A$ (shear matrix), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): A rational $m\times m$ matrix defining the shear $(H,D)\mapsto(H+AD,D)$.
- $a$ (rank), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): The rank of $A$ over $\mathbb Q$, the number of linearly independent rows of $A$.
- $E_1$ (left triangular factor), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): An invertible lower-triangular rational matrix in the factorization of $A$.
- $E_2$ (right triangular factor), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): An invertible lower-triangular rational matrix in the factorization of $A$.
- $\Pi$ (partial permutation factor), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): A partial permutation matrix with $a$ ones, at most one in each row and column, in the factorization of $A$.
- $V$ (stored volume), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): The stored bit volume, the number of bits held in the array.
- $s$ (smaller call count), bound on [Three-element subset intersection construction](subset-intersection-construction.md): The total number of smaller calls, found by summing over the network's edges the rank of the difference between the matrices at the edge's two ends.
- $W$ (wire count), bound on [Three-element subset intersection construction](subset-intersection-construction.md): The number of wires of the network.
- $m$ (subspace dimension), bound on [Three-element subset intersection construction](subset-intersection-construction.md): The dimension of the fixed space that the subspaces lie in.
- $f$ (call parameter), bound on [Recursive power saving from s<Wm](recursive-power-saving.md): The parameter of a call; it counts field digits for address interchange and selected axes for a numerical layer.
- $V$ (stored bit volume), bound on [Recursive power saving from s<Wm](recursive-power-saving.md): The number of stored bits in the array a call works on.
- $m$ (parameter multiplier), bound on [Recursive power saving from s<Wm](recursive-power-saving.md): The factor by which a recursive call multiplies the parameter.
- $s$ (subcall count), bound on [Recursive power saving from s<Wm](recursive-power-saving.md): The number of subcalls a recursive call makes.
- $W$ (volume divisor), bound on [Recursive power saving from s<Wm](recursive-power-saving.md): The divisor by which each subcall reduces the stream volume from $V$ to $V/W$.
- $T$ (normalized cost), bound on [Recursive power saving from s<Wm](recursive-power-saving.md): The cost of a call at parameter $f$ divided by the volume $V$ it works on.
- $u$ (field width), bound on [Fast interchange of address fields](fast-address-interchange.md): The number of bits in each of the two address fields being interchanged.
- $V$ (stored bit volume), bound on [Fast interchange of address fields](fast-address-interchange.md): The number of bits stored in the array.
- $\tau$ (cost exponent), bound on [Fast interchange of address fields](fast-address-interchange.md): A fixed exponent below 1 in the cost bound $O(Vu^\tau)$.
- $H$ (first field), bound on [Fast interchange of address fields](fast-address-interchange.md): The first of the two address fields, viewed as a vector of entries over a common residue ring.
- $D$ (second field), bound on [Fast interchange of address fields](fast-address-interchange.md): The second of the two address fields, viewed as a vector of entries over a common residue ring.
- $D$ (selected chunk count), bound on [Fast simultaneous butterfly layers](fast-butterfly-layers.md): The number of address chunks in which the same bit position is selected; a count.
- $d$ (chunk bound), bound on [Fast simultaneous butterfly layers](fast-butterfly-layers.md): An upper bound on the number of selected chunks $D$; a count.
- $K$ (chunk width), bound on [Fast simultaneous butterfly layers](fast-butterfly-layers.md): The number of bits in each address chunk; a count.
- $V$ (stored bit volume), bound on [Fast simultaneous butterfly layers](fast-butterfly-layers.md): The number of stored bits in the array; a count.
- $\lambda'$ (cost exponent), bound on [Fast simultaneous butterfly layers](fast-butterfly-layers.md): A fixed exponent below 1 in the layer's cost $O(Vd^{\lambda'})$.
- $H_0$ (butterfly), bound on [Fast simultaneous butterfly layers](fast-butterfly-layers.md): The map $H_0(u,v)=((u+v)/2,(u-v)/2)$ applied to each selected bit.
- $X$ (bit-flip matrix), bound on [Fast simultaneous butterfly layers](fast-butterfly-layers.md): The two-by-two matrix that swaps the two basis vectors of one bit.
- $\mathsf S$ (phase matrix), bound on [Fast simultaneous butterfly layers](fast-butterfly-layers.md): The diagonal matrix $\operatorname{diag}(1,i)$ of phases.
- $C$ (two-point kernel), bound on [Fast simultaneous butterfly layers](fast-butterfly-layers.md): The two-by-two kernel $\tfrac12((1+i)I+(1-i)X)$ from which each butterfly is built.
- $N$ (coefficient count), bound on [Chinese-remainder map to prime cyclic axes](crt-address-map.md): The number of coefficients in the list, which equals the product of the distinct primes $p_1 \cdots p_k$.
- $p_1$ (axis prime), bound on [Chinese-remainder map to prime cyclic axes](crt-address-map.md): One of the distinct primes $p_1, \dots, p_k$ whose product is $N$; each $p_j$ is the length of its cyclic axis.
- $i$ (coefficient index), bound on [Chinese-remainder map to prime cyclic axes](crt-address-map.md): The position of a coefficient in the list, taken in $\{0, \dots, N-1\}$.
- $p$ (axis length), bound on [Gaussian resampling](gaussian-resampling.md): The number of points on one prime cyclic axis, which is a prime number.
- $n$ (transform length), bound on [Bluestein's chirp identity](bluestein-chirp.md): The number of points in the transform.
- $\omega$ (primitive root), bound on [Bluestein's chirp identity](bluestein-chirp.md): A primitive $n$th root of unity, whose powers give the transform's phases.
- $\zeta$ (half-order root), bound on [Bluestein's chirp identity](bluestein-chirp.md): A primitive $2n$th root of unity whose square is $\omega$.
- $x$ (input value), bound on [Bluestein's chirp identity](bluestein-chirp.md): The $k$th input value of the transform, for $k=0,\dots,n-1$.
- $X$ (output value), bound on [Bluestein's chirp identity](bluestein-chirp.md): The $j$th output value of the transform, for $j=0,\dots,n-1$.
- $j$ (output index), bound on [Bluestein's chirp identity](bluestein-chirp.md): The index of an output of the transform, running from $0$ to $n-1$.
- $k$ (input index), bound on [Bluestein's chirp identity](bluestein-chirp.md): The index of an input of the transform, running from $0$ to $n-1$.
- $a$ (premultiplied inputs), bound on [Bluestein's chirp identity](bluestein-chirp.md): The sequence $a_k=x_k\zeta^{k^2}$, indexed by $k$.
- $b$ (chirp sequence), bound on [Bluestein's chirp identity](bluestein-chirp.md): The sequence of chirp phases $b_m=\zeta^{-m^2}$, indexed by $m$.
- $m$ (chirp index), bound on [Bluestein's chirp identity](bluestein-chirp.md): The index of the chirp sequence $b$.
- $\zeta$ (twist root of unity), bound on [Last-coordinate phase twist](phase-twist-convolution.md): The complex number e^{\pi i/r}, whose r-th power is -1; the twist multiplies coefficient k by its k-th power.
- $k$ (coefficient index), bound on [Last-coordinate phase twist](phase-twist-convolution.md): The index of a coefficient on the last cyclic axis, with 0 <= k < r.
- $x$ (cyclic variable), bound on [Last-coordinate phase twist](phase-twist-convolution.md): The formal variable of the cyclic ring C[x]/(x^r-1), in which exponents wrap modulo r.
- $l$ (second coefficient index), bound on [Last-coordinate phase twist](phase-twist-convolution.md): The index of a coefficient of the second factor, with 0 <= l < r.
- $j$ (cyclic product index), bound on [Last-coordinate phase twist](phase-twist-convolution.md): The cyclic index of a product term, the residue of k+l modulo r, with 0 <= j < r.
- $h$ (wrap bit), bound on [Last-coordinate phase twist](phase-twist-convolution.md): The bit in {0,1} recording whether the exponent k+l wrapped past r.
- $p$ (precision exponent), bound on [Signed coefficient packing (Kronecker substitution)](signed-packing.md): The exponent bounding the absolute value of each input coefficient by $2^p$.
- $B$ (block base), bound on [Signed coefficient packing (Kronecker substitution)](signed-packing.md): The base $B=2^{4p}$ in which packed integers are written, one block per coefficient.
- $u$ (packed polynomial), bound on [Signed coefficient packing (Kronecker substitution)](signed-packing.md): A polynomial in $\mathbb Z[y]$ of degree below $r$ whose coefficients have absolute value at most $2^p$; its packed integer is $u(B)$.
- $u_j$ (coefficient of u), bound on [Signed coefficient packing (Kronecker substitution)](signed-packing.md): The $j$th coefficient of $u$, an integer of absolute value at most $2^p$.
- $h$ (ordinary product), bound on [Signed coefficient packing (Kronecker substitution)](signed-packing.md): The ordinary product $uv$ in $\mathbb Z[y]$, before reduction modulo $y^r+1$.
- $h_j$ (product coefficient), bound on [Signed coefficient packing (Kronecker substitution)](signed-packing.md): The $j$th coefficient of the ordinary product $h=uv$.
- $u$ (first input array), bound on [Convolution with retained transform order and cancelled permutations](ring-convolution-retained-order.md): One of the two input arrays whose convolution is computed.
- $v$ (second input array), bound on [Convolution with retained transform order and cancelled permutations](ring-convolution-retained-order.md): The other of the two input arrays whose convolution is computed.
- $\mathcal{D}$ (forward transform), bound on [Convolution with retained transform order and cancelled permutations](ring-convolution-retained-order.md): The forward transform applied to each input array.
- $\mathcal{D}^{+}$ (opposite transform), bound on [Convolution with retained transform order and cancelled permutations](ring-convolution-retained-order.md): The opposite transform, which inverts the forward transform up to a known scalar.
- $L$ (layout permutation), bound on [Convolution with retained transform order and cancelled permutations](ring-convolution-retained-order.md): The permutation of addresses that the forward transform applies to its output, which fixes the frequency order.
- $\odot$ (pointwise product), bound on [Convolution with retained transform order and cancelled permutations](ring-convolution-retained-order.md): The product that multiplies the ring elements stored at the same address.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Fast interchange of address fields](fast-address-interchange.md): Interchange two disjoint contiguous u-bit address fields in an array in O(V u^τ) for fixed τ<1, via XOR combinations that end as an exact permutation.
  Shown as: Integer multiplication in O(n(lg n)^{1-κ}) time *<predicate>* Fast interchange of address fields
- [Fast simultaneous butterfly layers](fast-butterfly-layers.md): Applies H0(u,v)=((u+v)/2,(u-v)/2) on selected address bits of polynomial-valued arrays with exact Gaussian dyadics in O(V d^λ') with λ'<1, one truncation at the end.
  Shown as: Integer multiplication in O(n(lg n)^{1-κ}) time *<predicate>* Fast simultaneous butterfly layers
- [Convolution with retained transform order and cancelled permutations](ring-convolution-retained-order.md): Two forward synthetic transforms keep the same frequency order through the pointwise product, and the opposite transform consumes it, so retained permutations cancel without separate sorts.
  Shown as: Integer multiplication in O(n(lg n)^{1-κ}) time *<predicate>* Convolution with retained transform order and cancelled permutations
- [Fixed-point precision and exact recovery](fixed-point-precision.md): Complex fixed-point coefficients; bounding error below 1/2 so rounding recovers exact integer coefficients and carry propagation yields the product.
  Shown as: Integer multiplication in O(n(lg n)^{1-κ}) time *<predicate>* Fixed-point precision and exact recovery
- [The n log n optimality conjecture](nlogn-conjecture.md): Schönhage–Strassen's proposal that n log n is the optimal order of cost for multiplying n-bit integers.
  Shown as: Integer multiplication in O(n(lg n)^{1-κ}) time *<predicate>* The n log n optimality conjecture
- [Chinese-remainder map to prime cyclic axes](crt-address-map.md): Places the coefficient list on a product of distinct prime cyclic axes by a map preserving convolution, implemented via triangular controlled shifts and axis moves.
  Shown as: Integer multiplication in O(n(lg n)^{1-κ}) time *<predicate>* Chinese-remainder map to prime cyclic axes

## Other pages you may link to

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
- [Three-element subset intersection construction](subset-intersection-construction.md)
- [Recursive power saving from s<Wm](recursive-power-saving.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein's chirp identity](bluestein-chirp.md)
- [Last-coordinate phase twist](phase-twist-convolution.md)
- [Signed coefficient packing (Kronecker substitution)](signed-packing.md)

## Evidence from the sources, with the paragraph around each quote

- "There is one deterministic Turing machine $A$, with a fixed finite" (paper)

  > \begin{theorem}\label{thm:main} There is one deterministic Turing machine $A$, with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, that computes this exact product for every $n\ge1$ and every pair of $n$-bit inputs. Its worst-case running time satisfies \[ T_A(n)=O\!\left(n(\lg n)^{1-\kappa}\right), \qquad \kappa=2^{-182}. \] \end{theorem}


## Sources (read from disk as needed)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The reader cannot follow this step: "so that $s<Wm$" (The page presents the strict inequality s<Wm as following from the definitions of W, s and m, but gives no reason why these networks satisfy it. The reader cannot check it from the page.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "so that $u=m^k$" (The page asserts that the field width at recursion level k equals m^k, but does not say how the recursion splits the fields. The reader cannot check this link.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "so $F_k\le (s/W)F_{k-1}+O(1)$" (The recurrence assumes the work a call does apart from its subcalls is O(1) per unit of volume. The page never states this cost, so the reader cannot check the recurrence.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "The butterfly layer follows the same recursion." (The page does not give the butterfly network's s, W or m, nor how the exponent lambda' arises, so the reader cannot check that the same recursion yields O(V d^{lambda'}).). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "The factor drops by $\kappa$ because $s<Wm$ is strict" (The page never shows how the bound O(V u^tau) with tau<1 turns into the logarithmic factor (lg n)^{1-kappa}, nor how the fixed constant kappa=2^{-182} relates to tau or to the number of levels. The reader cannot check the claimed saving.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.

## Previous version (revise it)

It has 346 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 432 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

Integer multiplication in $O(n(\lg n)^{1-\kappa})$ time, the main theorem of this wiki, is that a fixed deterministic machine multiplies $n$-bit integers within this bound, where $n$ is the number of bits in each input integer and $\kappa=2^{-182}$ is the fixed saving exponent in the logarithmic factor. It disproves the [n log n optimality conjecture](nlogn-conjecture.md).

One deterministic Turing machine computes the exact product for every $n\ge1$, <cite data-source="paper">with a fixed finite alphabet and a fixed finite number of one-dimensional tapes</cite>.

Radix-digit splitting [reduces the integer product to a convolution](radix-digit-reduction.md) of short coefficients. The machine places the coefficient list by the [Chinese-remainder map to prime cyclic axes](crt-address-map.md) onto prime cyclic axes. Gaussian resampling, Bluestein's chirp and a phase twist then give a convolution over $\mathbb C[y]/(y^r+1)$. The machine computes its convolution by [Convolution with retained transform order and cancelled permutations](ring-convolution-retained-order.md). It recovers its coefficients by [Fixed-point precision and exact recovery](fixed-point-precision.md).

The machine performs its address moves by [Fast interchange of address fields](fast-address-interchange.md). It performs its butterfly layers by [Fast simultaneous butterfly layers](fast-butterfly-layers.md).

Let $V$ be the stored bit volume, $u$ the width of each address field, $d$ the number of equal-width address chunks in which one bit position is selected, and $\tau,\lambda'<1$ fixed exponents. Two tape procedures cost $O(Vu^\tau)$ for an address interchange of two $u$-bit fields and $O(Vd^{\lambda'})$ for a simultaneous butterfly layer.

Both procedures come from fixed linear networks. Let $W$ be the number of roles of each network, $s$ the total number of its smaller calls and $m$ the dimension of the space whose subspaces label its gates, so that $s<Wm$. Let $k$ be the recursion level and $F_k$ the time divided by volume at level $k$, so that $u=m^k$. A call at level $k$ makes $s$ calls at level $k-1$, each on a stream of volume $V/W$, so $F_k\le (s/W)F_{k-1}+O(1)$ with $F_0=O(1)$. Since $s/W<m$, choose a rational $\tau\in(0,1)$ with $s/W<m^\tau$. Then the sum of $(s/W)^j$ over $j\le k$ is $O(m^{k\tau})$, so $F_k=O(u^\tau)$ and the interchange costs $O(Vu^\tau)$. The butterfly layer follows the same recursion.

The $n\log n$ cost comes from scanning all stored bits at each of the $\Theta(\log n)$ transform levels. Faster versions of these operations lower the whole bound. The factor drops by $\kappa$ because $s<Wm$ is strict: the cost per unit volume grows as $m^{k\tau}$ with $\tau<1$, not linearly in the levels.

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

Write the body to `exegenius/tasks/0076-write-main-theorem.answer.md` and the JSON to `exegenius/tasks/0076-write-main-theorem.answer.json`, then run `exegenius submit 0076-write-main-theorem` in the project directory. If submit rejects the answer, fix the answer and submit again.
