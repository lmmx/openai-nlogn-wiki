# exegenius task 0228-audit-prime-source-lengths

Project directory: `/mnt/openai-nlogn` (paths below are relative to it)

Audit one page of an explanatory wiki on behalf of a specific reader. Use only this task file: do not read the sources, other pages or any other file.

The reader knows exactly the concepts listed as known, together with what the reader profile states. Everything else that you know, the reader does not know: treat it as unknown to them, however elementary it seems to you. You are simulating that reader's lack of knowledge, so use your own knowledge only to recognise what the reader is missing.

Symbols: account for every symbol in the page's mathematics, each once, saying where the reader learns what it denotes:
- `here`: the page says what it denotes; quote the sentence that says it. A use in an example ("take $r = 4$") or a range ("a power of two $r$") does not say what $r$ denotes or counts. If the page uses the symbol before that sentence, submit records that the meaning comes too late.
- `page`: an earlier page binds it, as listed under "Symbols bound on earlier pages".
- `concept`: the name of a known concept contains it and binds it, as listed under that concept. A symbol in a known concept's name that is listed with no meaning is not known.
- `background`: standard notation the reader profile covers; say what covers it.
- `unbound`: nothing tells the reader what it denotes.
Submit checks that each symbol is in the page's mathematics, that each quote is on the page and contains the symbol, and that the named page or concept binds it.

Terms and steps: a term or step is followable if the reader knows it, the page explains it, or the page links it to another wiki page. Report every term or step on the page that the reader cannot follow:
- term: a named concept the reader does not know, which the page neither explains nor links.
- step: an inference, calculation or claim the reader cannot check from what the page gives.

Copy each quote from the page exactly, character for character, and keep it short: submit rejects quotes it cannot find on the page. Do not report anything the reader can follow. Answer with an empty list of gaps if the reader can follow the whole page.

## Reader profile

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

## Known concepts

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes (also: multitape Turing machine)
- Fixed-tape machine model (also: fixed finite-tape model)
- Exact integer multiplication
- The n log n optimality conjecture (also: Schönhage–Strassen conjecture)
- Established O(n log n) multiplier (also: Harvey–van der Hoeven multiplier)
- Radix-digit convolution
- Discrete Fourier transform (also: normalized Fourier transform, transform)
- Cyclic convolution
- Gaussian resampling (also: Harvey–van der Hoeven resampling, Gaussian weights)
- Chinese-remainder map (also: Agarwal–Cooley map, coefficient layout, generator)
- Bluestein's chirp identity (also: chirp identity)
- Synthetic polynomial transforms (also: Nussbaumer polynomial transforms, polynomial transforms, Nussbaumer and Quandalle)
- Polynomial ring modulo y^r + 1 (also: negacyclic polynomial ring)
  - $y$ (polynomial variable): The indeterminate of the polynomial ring, whose powers act as roots of unity.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Phase twist
- Signed coefficient packing (also: Kronecker substitution)
- Subspace labels
- Linear networks and frames (also: roles, frames)
- Subset-intersection network (also: three-element subset network, subset-intersection network and complex phase network)
- Address-field interchange (also: power-width interchange, tape procedure for interchanging address chunks)
- Address shear
- Rank-saving recursion (also: recursive saving)
- Gaussian dyadics
- Complex phase network (also: phase-frame identity, complex variant)
- Simultaneous butterfly layer
- Packed selected-bit addition
- Guard-width bound
- Transform layout
- Transform identity with retained permutations (also: target permutation)
- Address field (also: address chunk, chunk, target chunk)
- Transform axis (also: axis, remaining axes)
- Linear algebra basics (also: linear algebra: invertible linear operator, matrix, inverse, matrix, linear map)
- Bilinear map (also: bilinear product)
- Bilinear form (also: bilinear space, orthogonality, bilinear form and orthogonality, bilinear space and bilinear form)
- Binary field (also: finite field F2, F_2, finite field F_2)
- Binary change of basis
- Bit procedure
- Butterfly
- Congruence (also: congruence modulo B, modulo)
- Centered residue
- Linear contraction (also: contraction)
- Cyclic shift (also: controlled cyclic shift)
- Convolution
- Coprime (also: gcd, pairwise coprime, coprime (gcd))
- Running time cost (also: cost)
- Cost table
- Stable radix sort
- Destination rank
- Endpoint operator
- Gate and terminal of a network
- Gaussian integer
- Grid numerator (also: grid numerators)
- Ground set
- Indicator vector
- Modular inverse (also: invertible modulo q)
- Cyclic coordinate (also: last cyclic coordinate)
- Limit inferior
- Line spanned by a vector
- Little-o notation
- Mixed-radix digits (also: mixed-radix digit)
- Multidimensional transform (also: multidimensional transforms with power-of-two axes)
- Array norm (also: norm of an array)
- Normalized cyclic convolution
- Normalization scales (also: normalizations and known scales)
- Numerical layer
- Opposite transform (also: opposite-sign transform)
- Padded transform box
- Payload
- Phase factor (also: phase factors and scalar corrections)
- Polynomial ring
- Matrix rank (also: rational rank)
- Ring homomorphism and isomorphism (also: ring homomorphism and ring isomorphism)
- Schoolbook multiplication
- Scratch storage (also: scratch values, scratch chunk, scratch wires)
- Tensor product (also: tensor power)
- Transform round
- Truncation
- Union bound
- Exclusive or (also: XOR)

## Symbols bound on earlier pages

- $n$ (sequence length), bound on `convolution`: The number of entries in each input sequence.
- $i$ (input position in a), bound on `convolution`: The position of an entry of a in a product a_i b_j.
- $t_i$ (axis length), bound on `transform-axis`: The length of axis $i$: the number of values that coordinate of an address takes.
- $u$ (field width), bound on `address-field`: The number of address bits in each of the two fields being interchanged, a count.
- $x$ (vector), bound on `linear-algebra-basics`: A vector in a vector space over $F$.
- $y$ (vector), bound on `linear-algebra-basics`: A second vector in a vector space over $F$.
- $T$ (linear map), bound on `linear-algebra-basics`: A linear map between vector spaces over $F$.
- $S$ (candidate inverse), bound on `linear-algebra-basics`: A linear map that is a two-sided inverse of the operator $T$ when $T$ is invertible.
- $t$ (gate input count), bound on `linear-network-frames`: The number of input arrays a gate takes.
- $w$ (input wire), bound on `linear-network-frames`: An input wire of the network.
- $r$ (output role), bound on `linear-network-frames`: An output role of the network.
- $w$ (input role), bound on `endpoint-operator`: An input role of the network, whose route starts at its source vertex.
- $x$ (sequence), bound on `limit-inferior`: A sequence of real numbers $x_1, x_2, x_3, \dots$ whose $k$-th term is $x_k$.
- $y$ (tail infimum), bound on `limit-inferior`: The smallest term of the sequence at or after position $m$, written $y_m$.
- $n$ (input length), bound on `limit-inferior`: The number of bits in each input, which is the index of the running-time function.
- $n$ (input bit length), bound on `fixed-tape-model`: The number of bits in each of the two input integers.
- $x$ (first input), bound on `exact-integer-multiplication`: The first input, a binary string of length n.
- $y$ (second input), bound on `exact-integer-multiplication`: The second input, a binary string of length n.
- $p$ (working precision), bound on `cost-table`: The precision parameter $p = 6b$, which sets the coefficient width up to a constant factor.
- $T$ (padded box size), bound on `cost-table`: The power of two that sets the number of cells in the padded box.
- $d$ (axis count), bound on `cost-table`: The number of axes of the padded box.
- $r$ (longest axis length), bound on `cost-table`: The number of cells along the longest axis of the padded box.
- $i$ (position index), bound on `cyclic-shift`: A position in the block, numbered from 0 to L-1.
- $u$ (field width), bound on `address-interchange`: The number of bits in each field.
- $s$ (child call count), bound on `address-interchange`: The number of calls that one call makes on smaller fields.
- $T$ (triple), bound on `indicator-vector`: A three-element subset of the ground set $[h]$.
- $i$ (imaginary unit), bound on `gaussian-integer`: The number whose square is $-1$.
- $p$ (fractional precision), bound on `truncation`: The number of fractional binary places kept, so the grid spacing is $2^{-p}$.
- $w$ (key width), bound on `stable-radix-sort`: The number of bits in each key.
- $i$ (bit index), bound on `stable-radix-sort`: The position of a key bit, counting from 0 at the least significant end; pass $i$ sorts by bit $k_i$.
- $\beta$ (imaginary part), bound on `phase-factor`: The imaginary part of the complex number z.
- $l$ (second denominator power), bound on `gaussian-dyadics`: The number of factors of two in the denominator of the second element $b/2^l$.
- $u$ (input vector), bound on `discrete-fourier-transform`: A vector of q complex numbers, the input of the transform.
- $i$ (digit position), bound on `radix-digit-convolution`: The position of a digit in an input, running from 0 to m-1.
- $t$ (product coefficient position), bound on `radix-digit-convolution`: The position of a coefficient of the product polynomial, running from 0 to 2m-2.
- $s$ (axis index), bound on `multidimensional-transform`: The index of an axis, running from 1 to D.
- $Y$ (output array), bound on `multidimensional-transform`: The output array, the transformed array.
- $r$ (record length), bound on `synthetic-transforms`: The number of complex coefficients in a record, a power of two at least 2.
- $y$ (polynomial variable), bound on `synthetic-transforms`: The formal variable of the polynomial ring $R_r$.
- $s$ (shift amount), bound on `synthetic-transforms`: The number of places a shift moves each coefficient of a record, with $0 \le s < 2r$.
- $t$ (transform length), bound on `synthetic-transforms`: The number of entries in the transform, a power of two dividing $2r$.
- $s$ (source length), bound on `gaussian-resampling`: The number of entries in the source vector, which is the length of the transform being replaced.
- $t$ (resampled length), bound on `gaussian-resampling`: The number of entries in the resampled vector, a power of two greater than s.
- $\theta$ (relative gap), bound on `gaussian-resampling`: The relative gap t/s - 1 between the two lengths.
- $p$ (precision parameter), bound on `gaussian-resampling`: An integer precision parameter of the resampling identity.
- $S$ (first Gaussian map), bound on `gaussian-resampling`: A Gaussian-weighted map from length-s vectors to length-t vectors, used in the proof.
- $T$ (second Gaussian map), bound on `gaussian-resampling`: A second Gaussian-weighted map from length-s vectors to length-t vectors, used in the proof.
- $\xi$ (first input value), bound on `butterfly`: The first of the two values that the butterfly takes as input.
- $\eta$ (second input value), bound on `butterfly`: The second of the two values that the butterfly takes as input.
- $w$ (array entry), bound on `array-norm`: A single entry of the array X, which is a complex number.
- $w$ (input vector), bound on `linear-contraction`: A vector in the input space of a linear map, with m complex coordinates.
- $\eta$ (error vector), bound on `linear-contraction`: The difference between a computed input and the exact input w.
- $d$ (integer), bound on `congruence-modulo`: An integer, one of the two integers compared by congruence.
- $e$ (integer), bound on `congruence-modulo`: An integer, the other of the two integers compared by congruence.
- $w$ (class member), bound on `congruence-modulo`: An integer in the residue class of d modulo m.
- $p$ (coefficient bit bound), bound on `signed-packing`: The number of bits in the magnitude bound on each coefficient, so that $|f_j| \le 2^p$.
- $w$ (formal variable), bound on `cyclic-convolution`: A formal variable in which a sequence is written as a polynomial, never evaluated.
- $d$ (number of cyclic coordinates), bound on `cyclic-coordinate`: The number of cyclic coordinates of an array, a positive integer.
- $\beta$ (bilinear map), bound on `bilinear-map`: A map sending each pair of vectors, one from V and one from W, to a vector in U.
- $w$ (second argument), bound on `bilinear-map`: A vector of W, the second argument of the bilinear map.
- $\xi$ (vector), bound on `bilinear-form`: A vector of $X$.
- $\eta$ (vector), bound on `bilinear-form`: A vector of $X$.
- $x$ (address), bound on `subspace-labels`: An address, a binary point at which array entries are indexed; the letter changes meaning here.
- $T$ (triple), bound on `subspace-labels`: A three-element subset of the ground set.
- $S$ (triple), bound on `subspace-labels`: A second three-element subset, used for inner products.
- $Y$ (bank Y), bound on `subset-intersection-network`: The second of the two banks of scalars, indexed by triples of triples.
- $\beta$ (bank index), bound on `subset-intersection-network`: A triple of triples that indexes one entry of a bank.
- $\xi$ (source vector), bound on `subset-intersection-network`: The vector of source-bank entries on one line, indexed by triples.
- $\eta$ (target vector), bound on `subset-intersection-network`: The vector of target-bank entries on one line, indexed by triples.
- $i$ (imaginary unit), bound on `complex-phase-network`: The imaginary unit, with $i^2 = -1$.
- $x$ (address), bound on `complex-phase-network`: A binary vector in $\mathbb{F}_2^m$ at which the arrays are evaluated.
- $\sigma$ (binary vector), bound on `complex-phase-network`: A binary vector used in the weight identity.
- $d$ (axis bound), bound on `numerical-layer`: An upper bound on the number D of selected axes in one layer, a count of axes.
- $s$ (smaller-call count), bound on `rank-saving-recursion`: The total number of smaller calls that one call makes.
- $i$ (axis index), bound on `transform-round`: The index of a participating axis, running over the D participating axes.
- $\eta$ (twiddle exponent), bound on `transform-round`: The exponent of y at an address, an integer taken modulo 2r.
- $d$ (axis count), bound on `padded-transform-box`: The number of axes of the transform, the count of coordinate directions along which the data is laid out.
- $\sigma$ (digit scale), bound on `normalization-scales`: The power of two 2^{-b-2} by which each radix-2^b digit is multiplied when it is stored.
- $p$ (fractional bit count), bound on `guard-width-bound`: The number of fractional bits each input coefficient carries, so the inputs lie on $2^{-p}\mathbb{Z}[i]$.
- $d$ (axis bound), bound on `guard-width-bound`: A positive integer bound $d \ge D$ on the number of selected axes.
- $\eta$ (per-level operation count), bound on `guard-width-bound`: The fixed count $64(W+m+1)^3$ of operations that a level adds beyond its $s$ child calls.
- $\beta$ (depth growth bound), bound on `guard-width-bound`: The fixed count $s+\eta$ bounding how much the depth bound grows at each recursive level.
- $\beta$ (first integer), bound on `coprime`: One of the two integers whose greatest common divisor is taken, not both zero.
- $\beta$ (integer to invert), bound on `modular-inverse`: The integer whose inverse modulo $M$ is sought.
- $S$ (product of the lengths), bound on `modular-inverse`: The product $M_1 M_2 \cdots$ of all the lengths, the order of the cyclic group.
- $\xi$ (cyclic generator), bound on `modular-inverse`: A generator of a cyclic group of order $S$, which the map sends to $\prod_i \xi_i^{\mu_i}$.
- $d$ (current value of D), bound on `address-shear`: The value of the single field $D$ when $m = 1$.
- $i$ (row index), bound on `address-shear`: The row of a one in $\Pi$, which names an $H$ field.
- $\sigma$ (segment index), bound on `packed-bit-addition`: The index of a segment within a chunk, running from 0 to nu minus 1.
- $\beta$ (control bit), bound on `packed-bit-addition`: The bit that decides whether a controlled update is applied.
- $\xi$ (target segment value), bound on `packed-bit-addition`: The value of a segment of the target chunk during the eight updates.
- $\eta$ (scratch segment value), bound on `packed-bit-addition`: The value of the corresponding segment of the scratch chunk during the eight updates.
- $w$ (second vector), bound on `transform-identity`: A second complex vector of length q, paired with u in the permutation and product formulas.
- $S$ (Gaussian map S), bound on `transform-identity`: A Gaussian-weighted map from length-s vectors to length-t vectors, used in the source's resampling identity.
- $T$ (Gaussian map T), bound on `transform-identity`: A second Gaussian-weighted map from length-s vectors to length-t vectors, used in the source's resampling identity.
- $w$ (scaled input), bound on `bluestein-chirp-identity`: The input vector u with each entry divided by the corresponding chirp entry.
- $l$ (second record position), bound on `phase-twist`: The position of the coefficient taken from the second record in a product.
- $\xi$ (ring element), bound on `ring-homomorphism`: An arbitrary element of the source ring $Q$.
- $\eta$ (ring element), bound on `ring-homomorphism`: A second arbitrary element of the source ring $Q$.
- $w$ (indeterminate), bound on `ring-homomorphism`: The variable of the example ring $Q=\mathbb{C}[w]/(w^2-1)$, whose square is $1$.
- $\beta$ (number of places), bound on `mixed-radix-digits`: The number of places in the system, a positive integer.
- $e$ (coefficient index), bound on `chinese-remainder-map`: An ordinary coefficient index, an integer with $0\le e<\Lambda$.

## Pages in the wiki

- [Convolution](convolution.md)
- [Transform axis](transform-axis.md)
- [Address field](address-field.md)
- [Exclusive or](xor.md)
- [Linear algebra basics](linear-algebra-basics.md)
- [Linear networks and frames](linear-network-frames.md)
- [Endpoint operator](endpoint-operator.md)
- [Limit inferior](limit-inferior.md)
- [Fixed-tape machine model](fixed-tape-model.md)
- [Running time cost](running-time-cost.md)
- [Exact integer multiplication](exact-integer-multiplication.md)
- [The n log n optimality conjecture](n-log-n-conjecture.md)
- [Cost table](cost-table.md)
- [Established O(n log n) multiplier](established-multiplier.md)
- [Cyclic shift](cyclic-shift.md)
- [Ground set](ground-set.md)
- [Gate and terminal of a network](network-gate-terminal.md)
- [Scratch storage](scratch-storage.md)
- [Address-field interchange](address-interchange.md)
- [Bit procedure](bit-procedure.md)
- [Binary field](binary-field.md)
- [Indicator vector](indicator-vector.md)
- [Line spanned by a vector](line-spanned-by-vector.md)
- [Gaussian integer](gaussian-integer.md)
- [Tensor product](tensor-product.md)
- [Matrix rank](matrix-rank.md)
- [Truncation](truncation.md)
- [Payload](payload.md)
- [Union bound](union-bound.md)
- [Schoolbook multiplication](schoolbook-multiplication.md)
- [Stable radix sort](stable-radix-sort.md)
- [Destination rank](destination-rank.md)
- [Binary change of basis](binary-change-of-basis.md)
- [Phase factor](phase-factor.md)
- [Gaussian dyadics](gaussian-dyadics.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Radix-digit convolution](radix-digit-convolution.md)
- [Multidimensional transform](multidimensional-transform.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md)
- [Butterfly](butterfly.md)
- [Opposite transform](opposite-transform.md)
- [Polynomial ring](polynomial-ring.md)
- [Array norm](array-norm.md)
- [Grid numerator](grid-numerator.md)
- [Linear contraction](linear-contraction.md)
- [Congruence](congruence-modulo.md)
- [Signed coefficient packing](signed-packing.md)
- [Centered residue](centered-residue.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Cyclic coordinate](cyclic-coordinate.md)
- [Bilinear map](bilinear-map.md)
- [Bilinear form](bilinear-form.md)
- [Subspace labels](subspace-labels.md)
- [Subset-intersection network](subset-intersection-network.md)
- [Complex phase network](complex-phase-network.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Transform layout](transform-layout.md)
- [Numerical layer](numerical-layer.md)
- [Rank-saving recursion](rank-saving-recursion.md)
- [Transform round](transform-round.md)
- [Padded transform box](padded-transform-box.md)
- [Normalized cyclic convolution](normalized-cyclic-convolution.md)
- [Normalization scales](normalization-scales.md)
- [Little-o notation](little-o-notation.md)
- [Guard-width bound](guard-width-bound.md)
- [Coprime](coprime.md)
- [Modular inverse](modular-inverse.md)
- [Address shear](address-shear.md)
- [Packed selected-bit addition](packed-bit-addition.md)
- [Transform identity with retained permutations](transform-identity.md)
- [Bluestein's chirp identity](bluestein-chirp-identity.md)
- [Phase twist](phase-twist.md)
- [Ring homomorphism and isomorphism](ring-homomorphism.md)
- [Mixed-radix digits](mixed-radix-digits.md)
- [Chinese-remainder map](chinese-remainder-map.md)
- [Prime source lengths](prime-source-lengths.md)
- [Carry propagation](carry-propagation.md)
- [Convolution over the polynomial ring](polynomial-ring-convolution.md)
- [Exact coefficient recovery](recovery-and-error.md)
- [Integer multiplication below n log n](main-theorem.md)

## Page to audit (`prime-source-lengths`)

````markdown
# Prime source lengths

Prime source lengths are distinct odd primes $s_1,\dots,s_d$, where $s_i$ is the prime source length of axis $i$ and $d$ is the number of axes of a multidimensional transform, each prime chosen close to the power of two to which its axis is padded. Their product fills a fixed fraction of the padded box, which is what lets the [integer multiplication below n log n](main-theorem.md) algorithm keep every term of its cost table within the bound of the theorem.

An axis is one coordinate direction of a multidimensional array, and a multidimensional transform acts along every axis. Padding an axis to length $t$ means extending it with unused positions up to $t$ entries. Let $d$ be the number of axes. Let $\beta=\lceil\log_2 n\rceil$ be the number of bits needed to write $n$. Let $t_i$ be the padded length of axis $i$, a power of two, and let $T=t_1t_2\cdots t_d$ be the size of the padded box. The source takes, so $4n/\beta\le T<8n/\beta$.

Let $u$ be the smallest power of two with $u^d\ge T$. The source calls this length $r$, but $r$ is the record length on earlier pages, so here it is $u$. Let $w$ be the number of axes whose padded length is $u/2$; the other axes have length $u$. The source's rule is to choose. The lengths then multiply to $u^d/2^w$, which must equal $T$, so $w=d\log_2 u-\log_2 T$. Minimality of $u$ gives $(u/2)^d<T\le u^d$, so $0\le w<d$ and such a choice exists. The bound on $T$ alone does not fix the lengths; the construction does.

The counting tool is a prime-interval bound.. Here $\eta$ is a slack fraction, $\xi$ is a real scale, and $\sigma$ is a prime. For $0<\eta<1/4$ and $\xi>e^{2/\eta}$, the interval $(1-2\eta)\xi<\sigma\le(1-\eta)\xi$ contains at least $\eta\xi/(2\ln\xi)$ primes $\sigma$, where $\ln$ is the natural logarithm.

Take $\eta=1/(4d)$, so $2/\eta=8d$ and the lower bound is $\xi/(8d\ln\xi)$. Apply it with $\xi=u/2$ and $\xi=u$. Each needs $\xi>e^{8d}$, that is $\ln\xi>8d$, and a count above $d$, that is $\xi>8d^2\ln\xi$. Both persist for larger $\xi$, so it suffices to check $\xi=u/2$. The source's parameters give $\ln(u/2)/d\to\infty$. With $Y=\ln(u/2)$, for large $n$ we have $Y>8d$ and $d<Y$, so $u/2=e^Y>8Y^3\ge 8d^2Y$.

Both intervals lie above $2$, so their primes are odd. They are disjoint, since $(1-\eta)u/2<(1-2\eta)u$ when $3\eta<1$. Each holds more than $d$ primes, so the axes of length $u/2$ take distinct primes from the first and the others from the second. Let $s_i$ be the prime source length of axis $i$, a distinct odd prime, chosen so that
$$(1-2\eta)\,t_i<s_i\le(1-\eta)\,t_i .$$

Here $\gcd$ is the greatest common divisor. The lengths $s_1,\dots,s_d$ are distinct primes, so they satisfy the pairwise form of [Coprime](coprime.md). The distinct primes supply pairwise coprime lengths to the [Chinese-remainder map](chinese-remainder-map.md), which relabels coefficient positions by [Mixed-radix digits](mixed-radix-digits.md).

Let $S=s_1s_2\cdots s_d$, the total number of positions. Since $2\eta=\frac{1}{2d}$, each $s_i>(1-\frac{1}{2d})t_i$, and multiplying these bounds with $\prod_i t_i=T$ gives $S>(1-\frac{1}{2d})^dT$. The source derives the next step from $(1-\frac{1}{2d})^d>\frac12$ for $d\ge2$. Bernoulli's inequality $(1+x)^d\ge1+dx$ is strict for $x\ne0$ and $d\ge2$, and with $x=-\frac{1}{2d}$ the right side is $\frac12$. Since $s_i<t_i$ for each $i$, $S<T$, so. The lengths set the place values of the [Mixed-radix digits](mixed-radix-digits.md) of the $S$ positions, so digit $i$ runs from $0$ to $s_i-1$.

Let $\theta_i=t_i/s_i-1$ be the relative gap of axis $i$. From $s_i\le(1-\eta)t_i$ we get $t_i/s_i\ge1/(1-\eta)$, so $\theta_i\ge\eta/(1-\eta)>\eta$. Each ratio $t_i/s_i$ must leave enough separation for [Gaussian resampling](gaussian-resampling.md). The source checks this gap against its parameter choices; this page establishes only $\theta_i>\eta=1/(4d)$.

The machine finds these primes, testing each candidate by trial division (dividing by the integers up to its square root). Scanning $O(u)$ candidates with $O(\sqrt u)$ divisors each costs $O(d\,u^{3/2}\,\mathrm{poly}(\beta))$. Since $\log_2 u<1+(\beta+3)/d$, the logarithm of this cost is $O(\log\beta)+O(\beta/d)=o(\beta)$, because $d$ grows with $\beta$. As $2^\beta$ is about $n$, the search takes $n^{o(1)}=o(n)$ time, as the source states:

Worked example. Take $d=2$, so $\eta=1/8$, and $T=128$. Then $u=16$, since $8^2<128\le 16^2$, and $w=1$, so $t_1=16$ and $t_2=8$. The interval $(12,14]$ contains only $13$, and $(6,7]$ contains only $7$, so $s_1=13$, $s_2=7$, $S=91$, and $64<91<128$. The gap $\theta_1=16/13-1\approx0.23$ exceeds $\eta/(1-\eta)=1/7$. The lemma needs $\xi>e^{2/\eta}=e^{16}\approx 8.9\times10^6$, far above the scales $8$ and $16$, so the example picks the primes by hand.
````

## Answer

The answer is one JSON object following this schema:

```json
{
  "$defs": {
    "Anchor": {
      "description": "Where the reader learns what a symbol denotes.",
      "oneOf": [
        {
          "additionalProperties": false,
          "description": "This page says what the symbol denotes. A use in an example (\"take $r = 4$\") does not.",
          "properties": {
            "kind": {
              "const": "here",
              "type": "string"
            },
            "quote": {
              "description": "The sentence that says it, copied exactly from the page.",
              "type": "string"
            }
          },
          "required": [
            "kind",
            "quote"
          ],
          "type": "object"
        },
        {
          "additionalProperties": false,
          "description": "An earlier page binds it: one listed under \"Symbols bound on earlier pages\".",
          "properties": {
            "kind": {
              "const": "page",
              "type": "string"
            },
            "page": {
              "description": "Id of that page.",
              "type": "string"
            }
          },
          "required": [
            "kind",
            "page"
          ],
          "type": "object"
        },
        {
          "additionalProperties": false,
          "description": "The name of a known concept contains it and binds it, as listed under the known\nconcepts.",
          "properties": {
            "concept": {
              "description": "Id of that concept.",
              "type": "string"
            },
            "kind": {
              "const": "concept",
              "type": "string"
            }
          },
          "required": [
            "kind",
            "concept"
          ],
          "type": "object"
        },
        {
          "additionalProperties": false,
          "description": "Standard notation the reader profile covers, such as $n$ for an input size.",
          "properties": {
            "kind": {
              "const": "background",
              "type": "string"
            },
            "note": {
              "description": "What in the reader profile covers it.",
              "type": "string"
            }
          },
          "required": [
            "kind",
            "note"
          ],
          "type": "object"
        },
        {
          "additionalProperties": false,
          "description": "Nothing tells the reader what it denotes.",
          "properties": {
            "kind": {
              "const": "unbound",
              "type": "string"
            },
            "note": {
              "description": "What the reader cannot tell.",
              "type": "string"
            },
            "quote": {
              "description": "Where it is first used, copied exactly from the page.",
              "type": "string"
            }
          },
          "required": [
            "kind",
            "quote",
            "note"
          ],
          "type": "object"
        }
      ]
    },
    "Gap": {
      "additionalProperties": false,
      "properties": {
        "kind": {
          "$ref": "#/$defs/GapKind"
        },
        "note": {
          "description": "Why this reader cannot follow it.",
          "type": "string"
        },
        "quote": {
          "description": "The passage on the page where the gap occurs, copied exactly (a phrase or one sentence).",
          "type": "string"
        },
        "term": {
          "description": "The term, or a short label for the step.",
          "type": "string"
        }
      },
      "required": [
        "term",
        "quote",
        "kind",
        "note"
      ],
      "type": "object"
    },
    "GapKind": {
      "oneOf": [
        {
          "const": "term",
          "description": "A named concept the reader does not know, which the page neither explains nor links.",
          "type": "string"
        },
        {
          "const": "step",
          "description": "An inference, calculation or claim the reader cannot check from what the page gives.",
          "type": "string"
        }
      ]
    },
    "SymbolUse": {
      "additionalProperties": false,
      "properties": {
        "anchor": {
          "$ref": "#/$defs/Anchor"
        },
        "symbol": {
          "description": "The symbol in LaTeX, as it appears in the page's mathematics, without dollar signs.",
          "type": "string"
        }
      },
      "required": [
        "symbol",
        "anchor"
      ],
      "type": "object"
    }
  },
  "additionalProperties": false,
  "properties": {
    "gaps": {
      "description": "Every term or step the reader cannot follow; empty if the reader can follow them all.",
      "items": {
        "$ref": "#/$defs/Gap"
      },
      "type": "array"
    },
    "symbols": {
      "description": "Every symbol in the page's mathematics, each once, with where the reader learns what\nit denotes. Empty only if the page has no mathematics.",
      "items": {
        "$ref": "#/$defs/SymbolUse"
      },
      "type": "array"
    }
  },
  "required": [
    "symbols",
    "gaps"
  ],
  "title": "AuditAnswer",
  "type": "object"
}
```

Write the answer to `exegenius/tasks/0228-audit-prime-source-lengths.answer.json`, then run `exegenius submit 0228-audit-prime-source-lengths` in the project directory. If submit rejects the answer, fix the answer and submit again.
