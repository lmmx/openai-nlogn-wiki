# exegenius task 0191-write-main-theorem

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
- Fast simultaneous butterfly layers
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
- $B$ (block base), bound on [Signed coefficient packing (Kronecker substitution)](signed-packing.md): The base $B=2^{4p}$ in which each coefficient of a packed integer is a block.
- $u$ (packed polynomial), bound on [Signed coefficient packing (Kronecker substitution)](signed-packing.md): A polynomial in $\mathbb Z[y]$ with coefficients of absolute value at most $2^p$, whose packed integer is $u(B)$.
- $v$ (second packed polynomial), bound on [Signed coefficient packing (Kronecker substitution)](signed-packing.md): The second input polynomial in $\mathbb Z[y]$, with coefficients $v_t$ of absolute value at most $2^p$.
- $h$ (product polynomial), bound on [Signed coefficient packing (Kronecker substitution)](signed-packing.md): The ordinary product $h=uv$ in $\mathbb Z[y]$ whose coefficients are recovered from the packed product.
- $k$ (product coefficient index), bound on [Signed coefficient packing (Kronecker substitution)](signed-packing.md): The exponent $k$ of a coefficient $h_k$ of the product polynomial, running over $0,\dots,2r-2$.
- $j$ (coefficient position), bound on [Signed coefficient packing (Kronecker substitution)](signed-packing.md): The position of a coefficient $u_j$ of a packed polynomial, which is also its block exponent.
- $t$ (second coefficient position), bound on [Signed coefficient packing (Kronecker substitution)](signed-packing.md): The position of a coefficient $v_t$ of the second input polynomial.
- $\gamma$ (carry), bound on [Signed coefficient packing (Kronecker substitution)](signed-packing.md): The carry $\gamma_j$ into block $j$ when packing, which is $0$ at $j=0$ and lies in $\{-1,0\}$.
- $d$ (block digit), bound on [Signed coefficient packing (Kronecker substitution)](signed-packing.md): The digit $d_j$ stored in block $j$ of a packed integer, with $0\le d_j<B$.
- $a$ (real part a), bound on [Signed coefficient packing (Kronecker substitution)](signed-packing.md): The real component $a\in\mathbb Z[y]$ of a record, whose coefficients are $2^p$ times the real parts of the record's coefficients.
- $b$ (imaginary part b), bound on [Signed coefficient packing (Kronecker substitution)](signed-packing.md): The imaginary component $b\in\mathbb Z[y]$ of a record, whose coefficients are $2^p$ times the imaginary parts of the record's coefficients.
- $f$ (first record), bound on [Signed coefficient packing (Kronecker substitution)](signed-packing.md): The first polynomial record, a polynomial of degree less than $r$ with complex fixed-point coefficients.
- $c$ (real part c), bound on [Signed coefficient packing (Kronecker substitution)](signed-packing.md): The real component $c\in\mathbb Z[y]$ of the second record $g$.
- $e$ (imaginary part e), bound on [Signed coefficient packing (Kronecker substitution)](signed-packing.md): The imaginary component $e\in\mathbb Z[y]$ of the second record $g$.
- $g$ (second record), bound on [Signed coefficient packing (Kronecker substitution)](signed-packing.md): The second polynomial record, multiplied with $f$ in the Gaussian product.
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
- $h$ (ground set size), bound on [Three-element subset intersection construction](subset-intersection-construction.md): The number of elements of the ground set $[h]$, here $100$.
- $\mathcal T$ (triples), bound on [Three-element subset intersection construction](subset-intersection-construction.md): The set of three-element subsets of $[h]$.
- $T$ (triple), bound on [Three-element subset intersection construction](subset-intersection-construction.md): A three-element subset of $[h]$, one of the elements of $\mathcal T$.
- $t_T$ (indicator vector of T), bound on [Three-element subset intersection construction](subset-intersection-construction.md): The indicator vector of the triple $T$.
- $g_T$ (triple value), bound on [Three-element subset intersection construction](subset-intersection-construction.md): The value carried by the triple $T$.
- $S$ (target triple), bound on [Three-element subset intersection construction](subset-intersection-construction.md): A second triple, used as the target or a neighbor of $T$.
- $e$ (element), bound on [Three-element subset intersection construction](subset-intersection-construction.md): An element of the ground set $[h]$.
- $C_e$ (central wire), bound on [Three-element subset intersection construction](subset-intersection-construction.md): The central wire of element $e$, which carries the sum of $g_T$ over the triples $T\ni e$.
- $A_{ST}$ (auxiliary wire), bound on [Three-element subset intersection construction](subset-intersection-construction.md): The auxiliary wire for the neighbor pair $(S,T)$, carrying a copy of $g_T$.
- $J$ (all-one matrix), bound on [Three-element subset intersection construction](subset-intersection-construction.md): The all-one matrix.
- $\mathcal F$ (label space), bound on [Three-element subset intersection construction](subset-intersection-construction.md): The tensor cube of $\mathbb Q^h$, the space containing every label.
- $m$ (label space dimension), bound on [Three-element subset intersection construction](subset-intersection-construction.md): The dimension of $\mathcal F$, which counts the coordinates of a label space.
- $\alpha$ (index), bound on [Three-element subset intersection construction](subset-intersection-construction.md): An ordered triple of triples $(T_1,T_2,T_3)$.
- $U$ (label), bound on [Three-element subset intersection construction](subset-intersection-construction.md): A label, a nondegenerate subspace of $\mathcal F$; $U_\alpha$ is the label of index $\alpha$.
- $P_U$ (label projection), bound on [Three-element subset intersection construction](subset-intersection-construction.md): The projection onto $U$ along $U^\perp$.
- $s$ (smaller-call count), bound on [Three-element subset intersection construction](subset-intersection-construction.md): The number of smaller calls, the total rank over all edges.
- $N$ (index count), bound on [Three-element subset intersection construction](subset-intersection-construction.md): The number of indices $\alpha$, which is $\binom h3^3$.
- $L$ (decreasing loss), bound on [Three-element subset intersection construction](subset-intersection-construction.md): The total dimension lost on decreasing edges.
- $f$ (call parameter), bound on [Recursive power saving from s<Wm](recursive-power-saving.md): The parameter of a call, counting field digits for an address interchange or selected axes for a numerical layer.
- $m$ (growth factor), bound on [Recursive power saving from s<Wm](recursive-power-saving.md): The factor by which the parameter grows in one recursive call.
- $\Phi$ (normalized cost), bound on [Recursive power saving from s<Wm](recursive-power-saving.md): The cost of a call at parameter f divided by the volume V it works on.
- $C$ (outside-work constant), bound on [Recursive power saving from s<Wm](recursive-power-saving.md): A constant bounding the outside work at a node of parameter mf.
- $\lambda$ (power exponent), bound on [Recursive power saving from s<Wm](recursive-power-saving.md): The fixed exponent below 1 of the power that bounds the cost per stored bit.
- $\tau$ (interchange exponent), bound on [Recursive power saving from s<Wm](recursive-power-saving.md): The fixed exponent below 1 in the cost O(V u^tau) of an address interchange.
- $K$ (chunk bit count), bound on [Recursive power saving from s<Wm](recursive-power-saving.md): The number of address bits in one axis chunk.
- $d$ (axis-count parameter), bound on [Recursive power saving from s<Wm](recursive-power-saving.md): The paper's parameter giving the number of axes, which sets the chunk width and the threshold d^beta.
- $\eta$ (chunk width exponent), bound on [Recursive power saving from s<Wm](recursive-power-saving.md): The fixed positive exponent in the bound K at most d^eta on the chunk width.
- $\beta$ (threshold exponent), bound on [Recursive power saving from s<Wm](recursive-power-saving.md): The fixed exponent 1/2 giving the threshold d^beta below which the recursion stops.
- $\nu$ (recursion depth), bound on [Recursive power saving from s<Wm](recursive-power-saving.md): The number of levels the recursion has been unrolled.
- $\sigma$ (leaf exponent), bound on [Recursive power saving from s<Wm](recursive-power-saving.md): A fixed exponent with max{0, log_m(s/W)} at most sigma below lambda, used to bound the leaf costs.
- $\tau$ (cost exponent), bound on [Fast interchange of address fields](fast-address-interchange.md): A fixed exponent below 1 in the interchange cost $O(Vu^\tau)$, chosen so that $s/W<m^\tau$.
- $k$ (recursion level), bound on [Fast interchange of address fields](fast-address-interchange.md): The number of times the field width has been multiplied by $m$, so a level-$k$ field has $m^k$ bits.
- $Q_k$ (level cost), bound on [Fast interchange of address fields](fast-address-interchange.md): A uniform upper bound on the time per unit of logical volume for interchanging fields at recursion level $k$.
- $D$ (selected chunk count), bound on [Fast simultaneous butterfly layers](fast-butterfly-layers.md): The number of selected address chunks.
- $d$ (chunk-count bound), bound on [Fast simultaneous butterfly layers](fast-butterfly-layers.md): An upper bound on D, the number of selected address chunks.
- $K$ (chunk width), bound on [Fast simultaneous butterfly layers](fast-butterfly-layers.md): The number of consecutive address bits in each chunk.
- $X$ (bit-flip matrix), bound on [Fast simultaneous butterfly layers](fast-butterfly-layers.md): The 2 by 2 matrix that swaps the two basis values.
- $\Phi$ (phase matrix), bound on [Fast simultaneous butterfly layers](fast-butterfly-layers.md): The diagonal matrix diag(1, i) of phases.
- $i$ (imaginary unit), bound on [Fast simultaneous butterfly layers](fast-butterfly-layers.md): The imaginary unit, with i squared equal to -1.
- $C$ (two-point kernel), bound on [Fast simultaneous butterfly layers](fast-butterfly-layers.md): The 2 by 2 kernel that each butterfly applies to its pair of values.
- $H_0$ (butterfly map), bound on [Fast simultaneous butterfly layers](fast-butterfly-layers.md): The map H_0(u,v) = ((u+v)/2, (u-v)/2) applied coefficientwise to a pair of records.
- $\sigma$ (recursion exponent), bound on [Fast simultaneous butterfly layers](fast-butterfly-layers.md): The fixed exponent 1 minus 2^{-50}, below 1, with s/W < m^sigma.
- $\lambda'$ (layer exponent), bound on [Fast simultaneous butterfly layers](fast-butterfly-layers.md): The fixed exponent below 1 in the layer's cost O(V d^{lambda'}).

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
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein's chirp identity](bluestein-chirp.md)
- [Last-coordinate phase twist](phase-twist-convolution.md)
- [Signed coefficient packing (Kronecker substitution)](signed-packing.md)
- [Tensor product of vector spaces](tensor-product-of-vector-spaces.md)
- [Three-element subset intersection construction](subset-intersection-construction.md)
- [Recursive power saving from s<Wm](recursive-power-saving.md)

## Evidence from the sources, with the paragraph around each quote

- "There is one deterministic Turing machine $A$, with a fixed finite" (paper)

  > \begin{theorem}\label{thm:main} There is one deterministic Turing machine $A$, with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, that computes this exact product for every $n\ge1$ and every pair of $n$-bit inputs. Its worst-case running time satisfies \[ T_A(n)=O\!\left(n(\lg n)^{1-\kappa}\right), \qquad \kappa=2^{-182}. \] \end{theorem}


## Sources (read from disk as needed)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The quotation does not support the claim it is attached to (unsupported): "The smallest margin is $2^{-181}$" cites "Direct substitution gives": 'Direct substitution gives' is a lead-in with no value; it does not state the smallest margin or any value of 2^{-181}. Say only what the source supports, or cite the passage that supports the claim.
- The quotation does not support the claim it is attached to (unsupported): "For the bit network, $s$ equals $Wm$ minus $N$, the number of negative source projections, plus twice the lost label dimension $L$" cites "The sum of the rational ranks of all edge differences is": The quotation only says the sum of rational ranks of edge differences is (cut off); it does not state the formula s = Wm - N + 2L or the condition s < Wm needs N > 2L. Say only what the source supports, or cite the passage that supports the claim.
- $e$ means chunk digit count here, but list index on [Chinese-remainder map to prime cyclic axes](crt-address-map.md), which this page builds on: Rename the chunk digit count on main-theorem (for example ell); e is the list index on crt-address-map, which this page builds on.
- $e$ means chunk digit count here, but imaginary part e on [Signed coefficient packing (Kronecker substitution)](signed-packing.md), which this page builds on: Rename the chunk digit count on main-theorem (for example ell); e is the imaginary part on signed-packing, which this page builds on.
- $e$ means chunk digit count here, but power exponent on [Synthetic polynomial transforms](synthetic-transforms.md), which this page builds on: Rename the chunk digit count on main-theorem (for example ell); e is the power exponent on synthetic-transforms, which this page builds on.
- $e$ means chunk digit count here, but element on [Three-element subset intersection construction](subset-intersection-construction.md), which this page builds on: Rename the chunk digit count on main-theorem (for example ell); e is an element of the ground set on subset-intersection-construction, which this page builds on.
- $t$ means recursion level here, but block offset on [Discrete Fourier transform and butterflies](dft-fft.md), which this page builds on: Rename the recursion level on main-theorem (for example s); t is the block offset on dft-fft, which this page builds on.
- $t$ means recursion level here, but chirp index on [Bluestein's chirp identity](bluestein-chirp.md), which this page builds on: Rename the recursion level on main-theorem (for example s); t is the chirp index on bluestein-chirp, which this page builds on.
- $t$ means recursion level here, but second coefficient position on [Signed coefficient packing (Kronecker substitution)](signed-packing.md), which this page builds on: Rename the recursion level on main-theorem (for example s); t is the second coefficient position on signed-packing, which this page builds on.
- $F$ means time per volume here, but vector space on [Tensor product of vector spaces](tensor-product-of-vector-spaces.md), which this page builds on: Rename the time per volume on main-theorem (for example G); F is the vector space on tensor-product-of-vector-spaces, which this page builds on.
- $\rho$ means recursion ratio here, but role permutation on [Finite linear network with roles and frames](linear-network-roles.md), which this page builds on: Rename the recursion ratio on main-theorem (for example varrho); rho is the role permutation on linear-network-roles, which this page builds on.

## Previous version (revise it)

It has 512 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 640 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

The main theorem is that one fixed deterministic Turing machine multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time, where $n$ is the number of bits in each input and $\kappa=2^{-182}$ is a fixed saving exponent. It disproves the [n log n optimality conjecture](nlogn-conjecture.md) for this model.

The machine uses a fixed finite alphabet and a fixed number of one-dimensional tapes, and computes the exact product for every $n\ge1$ <cite data-source="paper">There is one deterministic Turing machine $A$, with a fixed finite</cite>.

[Reduction of integer product to digit convolution](radix-digit-reduction.md) turns the product into a convolution of short coefficients. The machine places its coefficient list by the [Chinese-remainder map to prime cyclic axes](crt-address-map.md). The machine computes its convolution by [Convolution with retained transform order and cancelled permutations](ring-convolution-retained-order.md). The machine recovers its coefficients by [Fixed-point precision and exact recovery](fixed-point-precision.md).

The machine performs its address moves by [Fast interchange of address fields](fast-address-interchange.md). It performs its butterfly layers by [Fast simultaneous butterfly layers](fast-butterfly-layers.md). These cost $O(Vu^\tau)$ and $O(Vd^{\lambda'})$, where $V$ is the stored bit volume, $u$ the field width, $d$ the number of selected chunks, and $\tau,\lambda'<1$ fixed exponents. Here $u$ and $d$ are powers of $\lg n$ with exponents below one.

The $n\log n$ cost scans all $V$ stored bits at each of the $\Theta(\log n)$ transform levels, so cheaper moves and layers lower the whole bound.

The logarithmic factor drops by the fixed power $\kappa$ because $\kappa$ is set by the smallest margin in the sources' cost table. Each row of that table is a power $p$ with exponent one minus a margin, where $p=6\lceil\lg n\rceil$. The smallest margin is $2^{-181}$ <cite data-source="paper">Direct substitution gives</cite>, which is $2\kappa$, so the largest power is $p^{1-2\kappa}$. A fixed power of $\log p$ is at most $p^{\kappa}$ for large $p$, so $p^{1-2\kappa}$ times it is $O(p^{1-\kappa})=O((\lg n)^{1-\kappa})$.

Both procedures come from one fixed linear network with $W$ roles and $s$ child calls. For the bit network, $s$ equals $Wm$ minus $N$, the number of negative source projections, plus twice the lost label dimension $L$ <cite data-source="paper">The sum of the rational ranks of all edge differences is</cite>, so $s<Wm$ needs $N>2L$. A negative source projection is a source operator $-P_U$, where $P_U$ projects onto a label subspace along its orthogonal complement.

Let $e=m^t$ be the number of radix-$q$ digits in a chunk at recursion level $t$, where $m$ is the number of fields per chunk and $q$ is a fixed prime. Let $F(e)$ be the time divided by $V$ at that level. Here $e$, $t$ and $F$ change meaning. Each chunk is cut into $m$ fields of $e/m$ digits. A call makes $s$ child calls on streams of volume $V/W$, and its own splitting, gates and reassembly cost $O(1)$ per unit volume <cite data-source="paper">merging, gates, and triangular operations have total cost $O(V)$ because</cite>. Hence $F(e)\le (s/W)F(e/m)+O(e^\tau+1)$ with $F(1)=O(1)$, since the children cost $s(V/W)F(e/m)$ and dividing by $V$ gives $s/W$.

Put $\rho=(s/W)/m^\tau$, not the role permutation of earlier pages. Since $s/W<m$, some rational $\tau<1$ gives $\rho<1$; this is where $s<Wm$ is used. Dividing by $m^{t\tau}$ gives $m^{-t\tau}F(m^t)\le\rho\,m^{-(t-1)\tau}F(m^{t-1})+O(1)$, since $e^\tau+1\le 2e^\tau$. Unrolling gives a geometric sum with ratio $\rho<1$, so $F(m^t)=O(m^{t\tau})$. A field of $e$ radix-$q$ digits has $\Theta(e)$ bits, because $q$ is fixed, so $e$ is proportional to $u$ and the interchange costs $O(Vu^\tau)$. The butterfly layer uses a second fixed network, also with $s<Wm$, and runs the same recursion on the $d$ selected chunks, so it costs $O(Vd^{\lambda'})$ once $\lambda'$ exceeds two exponents.

Nodes with at least $\sqrt d$ active chunks have node overhead of $O(e^\lambda)$ per unit volume, with $e\le d$ and $\lambda=1-2^{-52}$. Smaller nodes, the small-level leaves, cost $O(d^{\sigma+(1-\sigma)/2})$ with $\sigma=1-2^{-50}$. So $\lambda'$ must exceed $\lambda$ and $\sigma+(1-\sigma)/2$, and $\lambda'=1-2^{-54}$ does.

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

Write the body to `exegenius/tasks/0191-write-main-theorem.answer.md` and the JSON to `exegenius/tasks/0191-write-main-theorem.answer.json`, then run `exegenius submit 0191-write-main-theorem` in the project directory. If submit rejects the answer, fix the answer and submit again.
