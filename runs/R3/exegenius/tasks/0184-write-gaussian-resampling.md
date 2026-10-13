# exegenius task 0184-write-gaussian-resampling

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
- Polynomial ring modulo $y^r+1$
  - $y$ (ring variable): The polynomial variable whose powers act as roots of unity.
  - $r$ (ring degree): The power of two giving the number of coefficients in each polynomial.
- Synthetic polynomial transforms (also: fast transform and transform axes)
- Address fields and array layout on tapes (also: fields, address rearrangements and signed shifts)
- Finite linear network with roles and frames (also: scalar network, source and sink nodes of a route)
- Address shear and lower-triangular factorization
- Restoring auxiliary scratch values (also: scratch (auxiliary) roles)
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

Concept: Gaussian resampling
Gloss: Harvey–van der Hoeven reduction expressing each Fourier transform of prime-length axes through a multidimensional transform with power-of-two axis lengths.
Also called: Gaussian (weighting function)

## This page in the argument

The step: Gaussian resampling expresses each source Fourier transform through a power-of-two tensor transform.

It serves these steps, from the main result down:

- An $n$-bit integer product is computed by a fixed-tape machine in $O(n(\lg n)^{1-\kappa})$ time, $\kappa=2^{-182}$.; how: reduce multiplication to ring convolution and speed up its address moves and butterfly layers (on [Integer multiplication in O(n(lg n)^{1-κ}) time](main-theorem.md))

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

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Discrete Fourier transform and butterflies](dft-fft.md): Evaluation of a coefficient list at roots of unity, computed in log-many levels of two-point butterfly operations; turns convolution into pointwise product.
  Shown as: Gaussian resampling *<predicate>* Discrete Fourier transform and butterflies
- [Chinese-remainder map to prime cyclic axes](crt-address-map.md): Places the coefficient list on a product of distinct prime cyclic axes by a map preserving convolution, implemented via triangular controlled shifts and axis moves.
  Shown as: Gaussian resampling *<predicate>* Chinese-remainder map to prime cyclic axes

## Pages that build on this one

- Convolution with retained transform order and cancelled permutations: Two forward synthetic transforms keep the same frequency order through the pointwise product, and the opposite transform consumes it, so retained permutations cancel without separate sorts.

## Other pages you may link to

- [The n log n optimality conjecture](nlogn-conjecture.md)
- [Convolution](convolution.md)
- [Reduction of integer product to digit convolution](radix-digit-reduction.md)
- [Polynomial ring modulo $y^r+1$](poly-ring-y-r.md)
- [Fixed-tape machine model and stream operations](fixed-tape-model.md)
- [Address fields and array layout on tapes](address-fields.md)
- [Schönhage–Strassen to Harvey–van der Hoeven multiplication](ss-hh-background.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Finite linear network with roles and frames](linear-network-roles.md)
- [Restoring auxiliary scratch values](scratch-restoration.md)
- [Address shear and lower-triangular factorization](address-shear-factorization.md)
- [Bluestein's chirp identity](bluestein-chirp.md)
- [Last-coordinate phase twist](phase-twist-convolution.md)
- [Fixed-point precision and exact recovery](fixed-point-precision.md)
- [Signed coefficient packing (Kronecker substitution)](signed-packing.md)
- [Convolution with retained transform order and cancelled permutations](ring-convolution-retained-order.md)
- [Tensor product of vector spaces](tensor-product-of-vector-spaces.md)
- [Three-element subset intersection construction](subset-intersection-construction.md)
- [Recursive power saving from s<Wm](recursive-power-saving.md)
- [Fast interchange of address fields](fast-address-interchange.md)
- [Fast simultaneous butterfly layers](fast-butterfly-layers.md)
- [Integer multiplication in O(n(lg n)^{1-κ}) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "it replaces the Fourier transforms needed for" (paper)

  > Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients. Our starting point is the Gaussian-resampling reduction of Harvey and van der Hoeven \cite{HarveyHoeven2021}: it replaces the Fourier transforms needed for this convolution by multidimensional transforms whose axis lengths are powers of two. After a further conversion to convolution, one coordinate is stored as the coefficient list of a polynomial modulo $y^r+1$, with $r$ a power of two. Powers of $y$ then serve as roots of unity in the remaining axes, and multiplication by such a root is a signed shift of the coefficient list. These are the synthetic polynomial transforms of Nussbaumer and Quandalle and Nussbaumer~\cite{NussbaumerQuandalle1978,Nussbaumer1980}.


## Sources (read from disk as needed)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The quotation does not support the claim it is attached to (unsupported): "Gaussian resampling is the reduction of Harvey and van der Hoeven that replaces each prime-length Fourier transform needed for a convolution" cites "by multidimensional transforms whose axis lengths are powers of two": The quotation only mentions transforms with power-of-two axis lengths; it says nothing about Gaussian resampling, Harvey and van der Hoeven, or replacing prime-length transforms. Say only what the source supports, or cite the passage that supports the claim.

## Previous version (revise it)

It has 427 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 533 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

Gaussian resampling is the reduction of Harvey and van der Hoeven that replaces each prime-length Fourier transform needed for a convolution <cite data-source="paper">by multidimensional transforms whose axis lengths are powers of two</cite>. A standard FFT of length $2m$ splits into two transforms of length $m$. A prime-length transform has no such split.

Let $p$ be the length of a prime axis, the number of entries in a list on that axis, and let $Q$ be a power of two, the number of entries in the list that replaces it, chosen slightly above $p$. Let $F_p$ and $F_Q$ be the normalized discrete Fourier transforms, $(F_p f)_k=\frac1p\sum_{j=0}^{p-1}f_j e^{-2\pi i jk/p}$ and likewise $F_Q$. Let $\pi_p$ and $\pi_Q$ be the coordinate reorderings used in the paper's identity. A contraction is a linear map that does not increase the largest modulus of an entry. Each normalized transform is a contraction <cite data-source="paper">since each output averages inputs multiplied by complex numbers of modulus one</cite>.

For an integer $\alpha$ with $2\le\alpha<\sqrt p$, the identity is
$$\pi_pF_p=2^{2\alpha^2}\,K\,\pi_QF_Q\,U,$$
where $U$ maps lists of length $p$ to lists of length $Q$, $K$ maps back, and $\alpha$ is the width parameter of the Gaussian weights below.

Both $U$ and $K$ are built from two Gaussian-weighted sums $\mathsf S$ and $\mathsf T$, each mapping lists of length $p$ to lists of length $Q$:
$$(\mathsf S f)_k=\frac1\alpha\sum_{j\in\mathbb Z}e^{-\pi\alpha^{-2}(j-pk/Q)^2}f_j,\qquad(\mathsf T f)_k=\sum_{j\in\mathbb Z}e^{-\pi\alpha^{2}(Qj/p-k)^2}f_j,$$
where entries $f_j$ are read modulo $p$, and $j$ and $k$ are entry indices. Each weight is a Gaussian centred on a point of the other grid. Harvey and van der Hoeven prove the Gaussian identity
$$\mathsf T\pi_pF_p=\pi_QF_Q\mathsf S$$
(their Theorem 4.2). It holds because the Fourier transform maps a Gaussian to a Gaussian.

$\mathsf T$ alone is not invertible, so we compensate. Put $\theta=Q/p-1$, which is assumed to satisfy $\theta>p/\alpha^4$. Let $z_j$ be the integer nearest $Qj/p$ and $\beta_j=Qj/p-z_j$. Let $R$ read the entries $z_j$ from a list of length $Q$, let $\Lambda$ multiply entry $j$ by $e^{\pi\alpha^2\beta_j^2}$, and set $\Phi=R\,\mathsf T\,\Lambda$, a map from length $p$ to length $p$. Entry $j$ of $\Phi f$ contains $f_j$ exactly, since $\Lambda$ cancels the Gaussian weight at $z_j$. The paper's Lemma 4.6 gives $\|\Phi-I\|<2^{-\alpha^2\theta}$. Since $\alpha^2\theta>p/\alpha^2>1$, we have $\|\Phi-I\|<1/2$, so $\Phi$ is invertible by the Neumann series $\Phi^{-1}=\sum_{\nu\ge0}(I-\Phi)^\nu$.

Since $R\mathsf T=\Phi\Lambda^{-1}$, the map $\Lambda\Phi^{-1}R$ is a left inverse of $\mathsf T$. Applying it to the Gaussian identity gives $\Lambda\Phi^{-1}R\,\pi_QF_Q\mathsf S=\pi_pF_p$. Set $U=\frac12\mathsf S$ and $K=2^{1-2\alpha^2}\Lambda\Phi^{-1}R$. Then $2^{2\alpha^2}K\pi_QF_QU=\pi_pF_p$, which is the identity.

The paper's Proposition 4.7(i) bounds $\|U\|<3/4$, $\|\tfrac12\Phi^{-1}\|<7/8$ and $\|2^{2-2\alpha^2}\Lambda\|<1$. Since $\|R\|=1$, $U$ and $K$ are contractions. Contractions keep composed approximation errors from growing.

To evaluate $F_p$ on a list $f$, apply $U$, then $\pi_QF_Q$, then $K$, multiply by $2^{2\alpha^2}$, and undo $\pi_p$.

Gaussian resampling acts on the axes placed by the [Chinese-remainder map to prime cyclic axes](crt-address-map.md). Gaussian resampling thus computes its transforms by the butterfly layers of [Discrete Fourier transform and butterflies](dft-fft.md), since a transform of length $Q$ has $\lg Q$ layers, each linear in the array size. The speedups of [Fast simultaneous butterfly layers](fast-butterfly-layers.md) and [Fast interchange of address fields](fast-address-interchange.md) therefore apply to these transforms.

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

Write the body to `exegenius/tasks/0184-write-gaussian-resampling.answer.md` and the JSON to `exegenius/tasks/0184-write-gaussian-resampling.answer.json`, then run `exegenius submit 0184-write-gaussian-resampling` in the project directory. If submit rejects the answer, fix the answer and submit again.
