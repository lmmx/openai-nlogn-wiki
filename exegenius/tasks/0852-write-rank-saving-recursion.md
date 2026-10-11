# exegenius task 0852-write-rank-saving-recursion

Project directory: `/mnt/openai-nlogn` (paths below are relative to it)

Write one page of an explanatory wiki. The wiki explains a target result from source documents to a specific reader, one concept per page, in reading order.

- Open with one or two sentences that say what the concept is and what it is for on the way to the target (the step of the argument it presents, and the pages that build on it, are listed below), so a reader arriving from a link knows at once why the page matters.
- If the page presents a step of the argument, explain how its method shows its claim. Give the reader every motivation the task marks as not stated by the sources: the sources will not.
- Explain the page's concept so that this reader can follow it using only what they already understand (listed below), what this page itself explains, and the linked prerequisite pages.
- Define any other technical term on this page, where it is first used.
- Say what each symbol denotes where you introduce it: what it stands for, and for a size or count, what it counts ("$r$, the number of complex coefficients in a record", not "a power of two $r$"). A use in an example ("take $r = 4$") does not say what $r$ denotes. Symbols listed as already bound can be used without restating them: the page shows the reader their meanings. Using one of those letters with another meaning confuses readers: pick another letter, or say on the page that the letter changes meaning here.
- Link each prerequisite page the first time you rely on it, using the exact markdown link given. You may also link the other pages listed. Submit rejects links to anything else in the wiki; external URLs are allowed.
- For each prerequisite page, say in a sentence what this page uses it for, and give that sentence as a relation: the prerequisite's id, a predicate, and the sentence copied exactly. The page shows the relation as "<this page's concept> *<predicate>* <prerequisite>", so pick a predicate that makes that a true sentence, with this page's concept as subject and the prerequisite as object: "is reduced to", "computes its transforms by", "is based on", "follows from", "bounds the cost of". If the sentence says "the transforms are reduced by X", the predicate is "reduces its transforms by", not "are reduced to". Build the predicate from the sentence's own words (other forms of a word count: "reduces" for "reduced"); the sentence must link or name the prerequisite. Pick the predicate that says what the prerequisite does for this page: "uses" says little.
- Stay accurate to the sources: read the parts you need (search for the evidence quotes). State only what the sources support or what is standard background; do not invent results, constants or attributions.
- Back each specific claim taken from a source (a result, a constant, a construction step) with the source text it rests on, right after the claim: `<cite data-source="id">text copied word for word from that source</cite>`. Readers see these as "(see p. 5)"-style references, hidden until they ask for them. Submit rejects text not found in the named source. Do not cite common background.
- Be concrete and specific. Give a small worked example where it makes the idea clearer. No filler, no rhetorical flourishes, no announcing what the page will do.
- Write mathematics in LaTeX: $...$ inline, $$...$$ on its own lines for display.
- Do not write a title heading, a prerequisites list or a sources section: those are added automatically. Use ## subheadings only if the page is long.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes (also: multitape Turing machine)
- Fixed-tape machine model (also: fixed finite-tape model)
- Exact integer multiplication (also: exact multiplication, Binary product)
- The n log n optimality conjecture (also: Schönhage–Strassen conjecture, the conjecture)
- Established O(n log n) multiplier (also: Harvey–van der Hoeven multiplier, der Hoeven)
- Radix-digit convolution (also: radix-digit coefficients)
- Discrete Fourier transform (also: normalized Fourier transform, transform, Fourier transform, normalized form, frequency order)
- Cyclic convolution
- Gaussian resampling (also: Harvey–van der Hoeven resampling, Gaussian weights, Gaussian line map, Gaussian corrections, target)
- Chinese-remainder map (also: Agarwal–Cooley map, coefficient layout, generator)
- Bluestein's chirp identity (also: chirp identity)
- Synthetic polynomial transforms (also: Nussbaumer polynomial transforms, polynomial transforms, Nussbaumer and Quandalle, the paper's representation)
- Polynomial ring modulo y^r + 1 (also: negacyclic polynomial ring, quotient ring)
  - $y$ (polynomial variable): The indeterminate of the polynomial ring, whose powers act as roots of unity.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Phase twist
- Signed coefficient packing (also: Kronecker substitution, packed polynomial product)
- Convolution over the polynomial ring
- Subspace labels (also: binary label, label, neighbors)
- Linear networks and frames (also: roles, frames, network of wires and gates, network, vertex, edge, source and sink vertices, Edge change, network, frame of a gate, role, data banks X_τ and Y_τ)
- Subset-intersection network (also: three-element subset network, subset-intersection network and complex phase network, side and central wires, gather and scatter, scalar network, decreasing edge)
- Address-field interchange (also: power-width interchange, tape procedure for interchanging address chunks, address-field interchange procedure, field interchanges, tape step, chunk interchange)
- Address shear (also: shear of address pairs, Matrix shear, shear)
- Gaussian dyadics
- Complex phase network (also: phase-frame identity, complex variant, orthogonal residual of an edge)
- Simultaneous butterfly layer (also: selected bits, two-point operator on selected bits, butterfly layer)
- Guard-width bound (also: segment)
- Transform layout (also: transform layout and packed selected-bit addition, axis layouts)
- Prime source lengths (also: pairwise coprime source lengths)
- Transform identity with retained permutations (also: target permutation, coordinate permutations, retained order)
- Carry propagation (also: carry scan)
- Exact coefficient recovery (also: construction constant of the source)
- Address field (also: address chunk, chunk, target chunk, selected address bits)
- Transform axis (also: axis, remaining axes, reduction axis, participating axis)
- Linear algebra basics (also: linear algebra: invertible linear operator, matrix, inverse, matrix, linear map, usual axioms, basis)
- Bilinear map (also: bilinear product, bilinear contraction)
- Bilinear form (also: bilinear space, orthogonality, bilinear form and orthogonality, bilinear space and bilinear form, orthogonal, nondegenerate space)
- Binary field (also: finite field F2, F_2, finite field F_2, copy step, exclusive or and AND)
- Binary change of basis (also: residual basis of directions)
- Bit procedure (also: fields of the bit procedure)
- Butterfly (also: two-point butterfly map, two-point map, Butterfly operation)
- Congruence (also: congruence modulo B, modulo, modulo arithmetic, residue, modulo (mod 4), residue class)
- Centered residue
- Linear contraction (also: contraction)
- Cyclic shift (also: controlled cyclic shift, signed shifts)
- Convolution
- Coprime (also: gcd, pairwise coprime, coprime (gcd))
- Running time cost (also: cost, linear-cost update, bit-complexity bound, linear tape time)
- Cost table (also: chirp and twist)
- Stable radix sort (also: label-and-sort operations)
- Destination rank (also: prefix-slot move, move, extracted records, rectangular routine, hole, destination key, destination map, rank counter)
- Endpoint operator (also: role array)
- Gate and terminal of a network (also: gate applied pointwise, pointwise linear gate, sink)
- Gaussian integer
- Grid numerator (also: grid numerators)
- Ground set (also: finite set, sets)
- Indicator vector
- Modular inverse (also: invertible modulo q, unit modulo M_i, invertible modulo n)
- Two-point kernel (also: kernel)
- Cyclic coordinate (also: last cyclic coordinate, cyclic axes, cyclic axes of the proof)
- Limit inferior
- Line spanned by a vector
- Little-o notation (also: limit as lambda tends to infinity)
- Middle transform (also: QFt, the paper's transform and middle transform)
- Mixed-radix digits (also: mixed-radix digit, digit)
- Multidimensional transform (also: multidimensional transforms with power-of-two axes)
- Array norm (also: norm of an array, coefficient bound, norm of a vector)
- Normalized cyclic convolution
- Normalization scales (also: normalizations and known scales)
- Numerical layer (also: butterfly layers, layer)
- Opposite transform (also: opposite-sign transform)
- Padded transform box (also: update line and rectangle, padded address set, padded box, working grid)
- Payload (also: record)
- Phase factor (also: phase factors and scalar corrections, phase frames)
- Polynomial ring (also: polynomial suffix)
- Matrix rank (also: rational rank, rank of a shear, Row reduction and pivots)
- Ring homomorphism and isomorphism (also: ring homomorphism and ring isomorphism)
- Schoolbook multiplication (also: the paper's construction)
- Scratch storage (also: scratch values, scratch chunk, scratch wires, forward schedule, linear-readout version)
- Tensor product (also: tensor power)
- Transform round (also: butterfly round, current recursive length, level the round processes, inverse child, transform levels, transform level, branch bit, highest unprocessed bit)
- Truncation
- Union bound
- Exclusive or (also: XOR)
- Address (also: binary addresses, least significant end)
- Array (also: disk array, disk-grid ring array)
- Logical array (also: logical array and stored array)
- Logarithm (also: logarithm lg)
- Base-2 logarithm (also: logarithm and ceiling)
- Ceiling function
- Bézout's identity (also: Bezout's identity)
- Big-Theta notation
- Bijection
- Permutation
- Bit network (also: the paper's bit network)
- Bit construction (also: bit case)
- Complex construction
- Chinese remainder theorem (also: CRT)
- Cyclic group (also: cyclic group of order S)
- Order of an element (also: multiplicative order)
- Diagonal scaling
- Eigenvalue
- Extended real numbers
- Frequency domain
- Incidence
- Independence of events
- Mathematical induction (also: induction)
- Integer
- Prime number (also: prime)
- Logical bit volume
- Ring
- Orthogonal complement
- Pointwise product
- Projection along a subspace
- Root of unity (also: roots of unity, primitive root of unity)
- Stream (also: fixed track, scan, role stream, stream position, aligned streams)
- Supremum
- Tape procedure (also: tape lemmas)
- Telescoping identity (also: signed dimension changes, source and sink dimensions)
- Schönhage–Strassen multiplication (also: Schönhage and Strassen, Schönhage–Strassen bound)
- Fixed-width digit blocks (also: B-adic blocks)
- Exceptional set (also: bad addresses)
- Big-Omega notation
- Bit-reversed index order
- Directed graph (also: directed graph (vertices))
- Closed disk in the complex plane (also: disk)
- Linear functional
- Dual space (also: dual space U^*)
- Floor function
- Forward transform (also: forward procedure)
- Gram matrix
- Schedule (also: inverse schedule)
- Iverson bracket
- Axis line (also: line)
- Near-linear time
- Negacyclic convolution
- Neumann series
- Probability (also: probability in general)
- Radix-two factorization
- Real numbers (also: Real number)
- Standard basis vector
- Symmetric matrix

## This page

Concept: Rank-saving recursion
Gloss: The recursion in which each call splits into s smaller calls on streams of 1/W of the volume, where s < W m, so that the cost grows by the strictly smaller factor s/W per level.
Also called: recursive saving, rank-saving argument

## This page in the argument

The step: The total number $s$ of smaller calls satisfies $s < Wm$, so each recursive level saves a strict power.
How: count the smaller calls against the wire count and the label dimension
Why: A recursion whose branching factor $s/W$ is strictly below $m$ shrinks the cost by a strict power at each level. (the sources leave this for the reader to work out: spell it out)

Its sub-steps, in order:

- The total number $s$ of smaller calls satisfies $s < Wm$.
- The strict inequality $s/W < m$ is the source of the power saving.

It serves these steps, from the main result down:

- Exact multiplication of two $n$-bit integers runs in $O(n(\lg n)^{1-\kappa})$ time on one deterministic fixed-tape machine, with $\kappa = 2^{-182}$.; how: reduce exact multiplication to radix-digit convolution, compute that convolution with fast tape transforms, and recover the exact product (on [Integer multiplication below n log n](main-theorem.md))

## Symbols already bound on earlier pages

The symbols in the names of the concepts the reader knows are listed with those concepts above.

- $b$ (base), bound on [Integer](integer.md): The base (radix) of a digit representation, an integer at least 2.
- $c$ (digit), bound on [Integer](integer.md): A digit of a digit list, an integer between 0 and the base minus one.
- $k$ (digit count), bound on [Integer](integer.md): The number of digits in a digit list.
- $j$ (digit position), bound on [Integer](integer.md): The position of a digit or bit, counted from the left starting at 1.
- $x$ (binary string), bound on [Integer](integer.md): A binary string of bits, read as an integer by the paper's rule.
- $m$ (bit count), bound on [Integer](integer.md): The number of bits in a binary string.
- $t$ (indeterminate), bound on [Integer](integer.md): A formal variable of polynomials, which is not a number.
- $b$ (base), bound on [Logarithm](logarithm.md): The fixed base of the logarithm, a number greater than 1.
- $y$ (argument), bound on [Logarithm](logarithm.md): The positive number whose logarithm is taken.
- $n$ (input integer), bound on [Logarithm](logarithm.md): The positive integer whose base-2 logarithm is taken.
- $\lg n$ (base-2 logarithm), bound on [Base-2 logarithm](base-two-logarithm.md): The base-2 logarithm of the positive integer $n$ under the paper's convention, which is at least 1.
- $\kappa$ (bound constant), bound on [Base-2 logarithm](base-two-logarithm.md): The fixed constant $2^{-182}$ in the paper's running-time bound.
- $z$ (complex number), bound on [Root of unity](root-of-unity.md): A complex number whose powers are taken; a root of unity is such a number.
- $m$ (order), bound on [Root of unity](root-of-unity.md): The least positive integer with $z^m = 1$, which is also the number of distinct powers of $z$.
- $y$ (polynomial variable), bound on [Root of unity](root-of-unity.md): The variable of the polynomial ring $\mathbb{C}[y]/(y^4+1)$, in which $y^4 = -1$; this replaces the logarithm page's meaning of $y$ on this page.
- $k$ (integer exponent), bound on [Root of unity](root-of-unity.md): An integer exponent of $y$ in the power $y^k$ that multiplies the coefficient list.
- $n$ (input length), bound on [Running time cost](running-time-cost.md): The number of cells that hold the input, which is the argument of the running time cost.
- $\kappa$ (exponent constant), bound on [Running time cost](running-time-cost.md): The fixed constant $2^{-182}$ in the exponent of the bound $O(n(\lg n)^{1-\kappa})$.
- $A$ (machine), bound on [Running time cost](running-time-cost.md): A machine whose running time cost is being measured.
- $T_A(n)$ (running time cost), bound on [Running time cost](running-time-cost.md): The largest number of steps machine $A$ takes on any input of length $n$.
- $M$ (example machine), bound on [Running time cost](running-time-cost.md): The example machine that reads cells from the first cell until it finds a $1$ or reaches the last cell.
- $x$ (first input), bound on [Exact integer multiplication](exact-integer-multiplication.md): The first binary input string, of length $n$.
- $y$ (second input), bound on [Exact integer multiplication](exact-integer-multiplication.md): The second binary input string, of length $n$.
- $n$ (input length), bound on [Exact integer multiplication](exact-integer-multiplication.md): The number of bits in each of the two inputs $x$ and $y$.
- $\mathrm{val}$ (value function), bound on [Exact integer multiplication](exact-integer-multiplication.md): $\mathrm{val}(x)$ is the nonnegative integer value of a binary string $x$, with the leftmost bit most significant.
- $k$ (padded length), bound on [Exact integer multiplication](exact-integer-multiplication.md): The number of bits in a padded binary string, that is, the length to which $\mathrm{bin}_k$ pads.
- $z$ (padded integer), bound on [Exact integer multiplication](exact-integer-multiplication.md): A nonnegative integer with $z < 2^k$ that is written in binary.
- $\mathrm{bin}_k$ (padded binary representation), bound on [Exact integer multiplication](exact-integer-multiplication.md): $\mathrm{bin}_k(z)$ is the binary representation of $z$ padded on the left with zeros to length $k$.
- $\#$ (separator), bound on [Exact integer multiplication](exact-integer-multiplication.md): A separator symbol placed between $x$ and $y$ in the input, marking where $x$ ends and $y$ begins.
- $a$ (first input sequence), bound on [Convolution](convolution.md): The first of the two input sequences, of length $n$.
- $b$ (second input sequence), bound on [Convolution](convolution.md): The second of the two input sequences, of length $n$.
- $n$ (entries per input), bound on [Convolution](convolution.md): The number of entries in each input sequence.
- $t$ (output position), bound on [Convolution](convolution.md): The position of an entry of the convolution output.
- $i$ (input position in a), bound on [Convolution](convolution.md): The position of an entry of $a$.
- $j$ (input position in b), bound on [Convolution](convolution.md): The position of an entry of $b$.
- $c$ (convolution), bound on [Convolution](convolution.md): The convolution of $a$ and $b$, a sequence of length $2n-1$.
- $V$ (stream volume), bound on [Payload](payload.md): The number of bits stored in the stream, which the time bound counts.
- $L$ (chunk width), bound on [Payload](payload.md): The width, in address bits, of an address chunk.
- $\tau$ (fixed exponent), bound on [Payload](payload.md): A fixed exponent strictly between 0 and 1 that sets the power of L in the time bound.
- $t$ (step index), bound on [Mathematical induction](mathematical-induction.md): The number of recursion levels passed, a nonnegative integer.
- $q$ (level ratio), bound on [Mathematical induction](mathematical-induction.md): The fixed positive real number by which one recursion level may multiply a bound.
- $g_t$ (level bound), bound on [Mathematical induction](mathematical-induction.md): A nonnegative bound on the cost after t levels, with g_0 = 1.
- $\lambda$ (evaluation point), bound on [Little-o notation](little-o-notation.md): The real point at which both functions are evaluated, taken to infinity.
- $\varphi$ (bounded function), bound on [Little-o notation](little-o-notation.md): The function being bounded, mapping the positive reals to the positive reals.
- $\psi$ (comparison function), bound on [Little-o notation](little-o-notation.md): The comparison function, positive for all large lambda, mapping the positive reals to the positive reals.
- $C$ (big-O constant), bound on [Little-o notation](little-o-notation.md): A constant such that the running time is at most C times n(lg n) to the power 1 minus kappa for all sufficiently large n.
- $c_A$ (lower-bound constant), bound on [Little-o notation](little-o-notation.md): A positive constant, depending on the machine A, in the optimality conjecture's lower bound on T_A(n).
- $N$ (entry count), bound on [Address](address.md): The number of entries in the array, counting each stored entry once; it counts the positions $0$ through $N-1$.
- $d$ (address length), bound on [Address](address.md): The number of bits in each address of the array, the length of every address string.
- $\alpha$ (address string), bound on [Address](address.md): A binary string of $d$ bits that labels one entry of the array.
- $p$ (precision), bound on [Truncation](truncation.md): The number of fractional binary places kept, which counts the binary digits after the point.
- $w$ (coefficient list), bound on [Truncation](truncation.md): A finite list of complex numbers, called coefficients.
- $Q_p$ (truncation operator), bound on [Truncation](truncation.md): The map that truncates each real and imaginary part of each coefficient toward zero onto the grid $2^{-p}\mathbb{Z}$.
- $\mathbb{Z}$ (integers), bound on [Truncation](truncation.md): The set of integers, whose multiples of $2^{-p}$ form the truncation grid.
- $\|\cdot\|_\infty$ (array norm), bound on [Truncation](truncation.md): The largest complex modulus of any coefficient in an array.
- $H$ (layer), bound on [Truncation](truncation.md): The map that replaces each pair of values $s$ and $r$ by $((s+r)/2,(s-r)/2)$, applied to every pair of entries whose addresses differ in one of several selected bits.
- $s$ (first pair value), bound on [Truncation](truncation.md): The first of the two values in a pair that a layer combines.
- $r$ (second pair value), bound on [Truncation](truncation.md): The second of the two values in a pair that a layer combines.
- $V$ (stored bit volume), bound on [Array](array.md): The number of stored data bits in an array, the volume in which cost bounds are stated.
- $X$ (array), bound on [Array norm](array-norm.md): A finite array of complex values, whose norm is taken.
- $u$ (entry), bound on [Array norm](array-norm.md): An entry of the array X, whose modulus is taken.
- $\|X\|$ (array norm), bound on [Array norm](array-norm.md): The largest modulus over all entries of X.
- $r$ (coefficient count), bound on [Array norm](array-norm.md): The number of coefficients in each representative of an element of the ring.
- $h$ (ring element), bound on [Array norm](array-norm.md): An element of the ring modulo y^r+1, written as a polynomial in y.
- $s$ (coefficient index), bound on [Array norm](array-norm.md): The index of a coefficient of a ring element, running from 0 to r-1.
- $s$ (real number), bound on [Ceiling function](ceiling-function.md): The real number that the ceiling rounds up to an integer.
- $j$ (integer), bound on [Ceiling function](ceiling-function.md): Any integer, which is its own ceiling.
- $f$ (bounded function), bound on [Big-Theta notation](big-theta-notation.md): The function from input sizes to nonnegative reals whose order is compared with that of $h$.
- $h$ (comparison function), bound on [Big-Theta notation](big-theta-notation.md): The function from input sizes to nonnegative reals against which $f$ is compared.
- $c_1$ (lower factor), bound on [Big-Theta notation](big-theta-notation.md): A positive real constant multiplying $h(n)$ in the lower inequality.
- $c_2$ (upper factor), bound on [Big-Theta notation](big-theta-notation.md): A positive real constant multiplying $h(n)$ in the upper inequality.
- $n_0$ (threshold), bound on [Big-Theta notation](big-theta-notation.md): The input size from which both inequalities hold.
- $V$ (stored bit volume), bound on [Big-Theta notation](big-theta-notation.md): The number of stored bits, which is of order $n$.
- $\mathbb{R}$ (real numbers), bound on [Extended real numbers](extended-reals.md): The set of real numbers.
- $\overline{\mathbb{R}}$ (extended real numbers), bound on [Extended real numbers](extended-reals.md): The set $\mathbb{R}\cup\{-\infty,+\infty\}$ of the reals with positive and negative infinity added.
- $\sigma$ (generic real number), bound on [Extended real numbers](extended-reals.md): A real number used as a generic value in the order, sums and limit conditions.
- $S$ (set of extended reals), bound on [Extended real numbers](extended-reals.md): Any set of extended real numbers, whose infimum and supremum are taken.
- $F$ (real elements), bound on [Extended real numbers](extended-reals.md): The set of real elements of $S$, used to find the supremum of $S$.
- $b$ (least real bound), bound on [Extended real numbers](extended-reals.md): The least real upper bound of $R$, which is the supremum of $S$ in that case.
- $\tau$ (sequence term), bound on [Extended real numbers](extended-reals.md): The term of a sequence at position $\delta$.
- $\delta$ (term position), bound on [Extended real numbers](extended-reals.md): The position of a term in a sequence, a positive integer.
- $L$ (candidate limit), bound on [Extended real numbers](extended-reals.md): A point of $\overline{\mathbb{R}}$ that a sequence may have as its limit.
- $\delta'$ (dummy position index), bound on [Extended real numbers](extended-reals.md): A dummy index ranging over the positions at or after $\delta$ in a tail.
- $\Sigma$ (real set), bound on [Supremum](supremum.md): A nonempty set of real numbers whose supremum is taken.
- $\chi$ (arbitrary element), bound on [Supremum](supremum.md): An arbitrary element of $\Sigma$, compared with a candidate upper bound.
- $\Omega$ (candidate bound), bound on [Supremum](supremum.md): A real number, tested as an upper bound of $\Sigma$.
- $s$ (positive integer index), bound on [Supremum](supremum.md): A positive integer index, the exponent in each element $1-2^{-s}$ of the example set.
- $\varepsilon$ (positive gap), bound on [Supremum](supremum.md): The positive number $1-\Omega$, the distance from $\Omega$ up to $1$.
- $L$ (linear map), bound on [Supremum](supremum.md): A linear map, meaning a map that preserves sums and scalar multiples, whose operator norm is taken.
- $u$ (input vector), bound on [Supremum](supremum.md): One input vector in the supremum defining the operator norm, a finite list of complex numbers.
- $o$ (last index), bound on [Telescoping identity](telescoping-identity.md): The index of the last term of the sequence, so that the sequence has o+1 terms.
- $k$ (term position), bound on [Telescoping identity](telescoping-identity.md): The position of a term in the sequence, running from 0 to o.
- $\iota_k$ (term at position k), bound on [Telescoping identity](telescoping-identity.md): The number at position k of the sequence.
- $x$ (list of numbers), bound on [Telescoping identity](telescoping-identity.md): A list of numbers indexed by position k, whose entry at position k is x_k.
- $s$ (first position), bound on [Telescoping identity](telescoping-identity.md): The first position of a sum over positions, the lower limit of the sum.
- $e$ (last position), bound on [Telescoping identity](telescoping-identity.md): The last position of a sum over positions, the upper limit of the sum.
- $\beta$ (place count), bound on [Mixed-radix digits](mixed-radix-digits.md): The number of places, a positive integer; the places are numbered 1 to beta.
- $j$ (place index), bound on [Mixed-radix digits](mixed-radix-digits.md): A place, numbered from 1 to beta.
- $\lambda_j$ (place length), bound on [Mixed-radix digits](mixed-radix-digits.md): The number of values the digit at place j can take.
- $\Lambda$ (digit string count), bound on [Mixed-radix digits](mixed-radix-digits.md): The product of the lengths: the number of distinct digit strings the system can write.
- $w_j$ (place value), bound on [Mixed-radix digits](mixed-radix-digits.md): The product of the lengths of the places below place j, with w_1 = 1.
- $\nu$ (integer being written), bound on [Mixed-radix digits](mixed-radix-digits.md): The integer whose mixed-radix expansion is taken, with 0 <= nu < Lambda.
- $e_j$ (digit), bound on [Mixed-radix digits](mixed-radix-digits.md): The digit of an expansion at place j, an integer from 0 to lambda_j - 1.
- $s$ (common length), bound on [Mixed-radix digits](mixed-radix-digits.md): The common length of every place, which is also the base; it counts the digit values.
- $i$ (lower place index), bound on [Mixed-radix digits](mixed-radix-digits.md): A place index that runs over the places below j in the sums of the proof.
- $e'_i$ (second digit), bound on [Mixed-radix digits](mixed-radix-digits.md): The digit at place i of the second expansion.
- $B$ (block base), bound on [Fixed-width digit blocks](fixed-width-digit-blocks.md): The base of the digits in a block, a fixed integer at least 2.
- $L$ (block length), bound on [Fixed-width digit blocks](fixed-width-digit-blocks.md): The number of digit places in each block, counting zeros.
- $\ell$ (place index), bound on [Fixed-width digit blocks](fixed-width-digit-blocks.md): The position of a digit in a block, running from 0 to L-1, with 0 the least significant place.
- $v$ (block value), bound on [Fixed-width digit blocks](fixed-width-digit-blocks.md): The integer stored in a block, from 0 up to B^L minus 1.
- $s_\ell$ (digit), bound on [Fixed-width digit blocks](fixed-width-digit-blocks.md): The digit of a block at place index ell, an integer from 0 to B minus 1 that multiplies B to the power ell.
- $F$ (generic formula), bound on [Exceptional set](exceptional-set.md): The rule that gives a value F(\alpha) for each address \alpha, and is correct outside the exceptional set.
- $E$ (exceptional set), bound on [Exceptional set](exceptional-set.md): The set of addresses at which the special rule gives a value different from the generic formula F.
- $\Omega$ (Big-Omega), bound on [Big-Omega notation](big-omega-notation.md): The notation $\Omega(h)$ for the set of functions bounded below by a positive constant times $h$ for all large inputs, so that $u(N)=\Omega(h(N))$ says $u$ lies in that set.
- $\alpha_s$ (address bit), bound on [Bit-reversed index order](bit-reversed-order.md): The bit of an address with weight $2^s$, which is 0 or 1.
- $\rho_d$ (bit-reversal map), bound on [Bit-reversed index order](bit-reversed-order.md): The map on $d$-bit addresses that reverses the order of their bits, whose value is the slot number of an address.
- $G$ (directed graph), bound on [Directed graph](directed-graph.md): The directed graph, written as the pair of its vertex set V and its edge set E.
- $V$ (vertex set), bound on [Directed graph](directed-graph.md): The set of vertices of the directed graph, the points that edges join.
- $E$ (edge set), bound on [Directed graph](directed-graph.md): The set of directed edges of the directed graph, each an ordered pair of vertices.
- $F$ (field), bound on [Linear algebra basics](linear-algebra-basics.md): The field of scalars over which the vector spaces are taken.
- $\mathbb{F}_2$ (two-element field), bound on [Linear algebra basics](linear-algebra-basics.md): The field of integers modulo 2.
- $\mathbb{Q}$ (rational numbers), bound on [Linear algebra basics](linear-algebra-basics.md): The field of rational numbers.
- $x$ (vector), bound on [Linear algebra basics](linear-algebra-basics.md): A vector in a vector space, changed from earlier pages.
- $y$ (vector), bound on [Linear algebra basics](linear-algebra-basics.md): A vector in a vector space, changed from earlier pages.
- $\gamma$ (scalar), bound on [Linear algebra basics](linear-algebra-basics.md): A scalar in F multiplying a vector.
- $\eta$ (scalar), bound on [Linear algebra basics](linear-algebra-basics.md): A scalar in F multiplying a vector.
- $m$ (coordinate count), bound on [Linear algebra basics](linear-algebra-basics.md): The number of coordinates in each vector of F^m.
- $j$ (coordinate index), bound on [Linear algebra basics](linear-algebra-basics.md): The index of a coordinate of a vector, running from 1 to m.
- $i$ (row index), bound on [Linear algebra basics](linear-algebra-basics.md): The index of a row of a matrix, running from 1 to m.
- $A$ (matrix), bound on [Linear algebra basics](linear-algebra-basics.md): An m by m matrix with entries in F.
- $B$ (candidate inverse), bound on [Linear algebra basics](linear-algebra-basics.md): A matrix that satisfies AB=BA=I.
- $l$ (column index), bound on [Linear algebra basics](linear-algebra-basics.md): The index of a column of a matrix product.
- $I$ (identity matrix), bound on [Linear algebra basics](linear-algebra-basics.md): The square matrix with ones on the diagonal and zeros elsewhere.
- $T$ (linear map), bound on [Linear algebra basics](linear-algebra-basics.md): A linear map between vector spaces over F.
- $S$ (inverse map), bound on [Linear algebra basics](linear-algebra-basics.md): A linear map that inverts an invertible operator T.
- $\mathrm{id}$ (identity map), bound on [Linear algebra basics](linear-algebra-basics.md): The map that sends every vector to itself.
- $u$ (vertex), bound on [Linear algebra basics](linear-algebra-basics.md): A vertex of the paper's directed graph.
- $v$ (vertex), bound on [Linear algebra basics](linear-algebra-basics.md): A vertex of the paper's directed graph.
- $D_v$ (frame), bound on [Linear algebra basics](linear-algebra-basics.md): The invertible linear operator on arrays carried by vertex v.
- $g$ (logical array), bound on [Linear algebra basics](linear-algebra-basics.md): The array the computation means.
- $H$ (address block), bound on [Linear algebra basics](linear-algebra-basics.md): The first bit block of an address.
- $K$ (address block), bound on [Linear algebra basics](linear-algebra-basics.md): The second bit block of an address.
- $M$ (shear matrix), bound on [Linear algebra basics](linear-algebra-basics.md): A matrix over F_2 that determines the shear.
- $\Phi_M$ (shear frame), bound on [Linear algebra basics](linear-algebra-basics.md): The frame that shears address pairs by M.
- $q$ (transform length), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The number of coordinates of each vector the transform acts on, a positive integer.
- $i$ (imaginary unit), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The imaginary unit, the complex number whose square is $-1$, used in this page in place of the convolution page's input position $i$.
- $\omega$ (primitive root of unity), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The complex number $e^{-2\pi i/q}$, a primitive $q$-th root of unity.
- $f$ (input vector), bound on [Discrete Fourier transform](discrete-fourier-transform.md): A vector of $q$ complex numbers, the input to the transform, with coordinates $f_0, \ldots, f_{q-1}$.
- $s$ (input index), bound on [Discrete Fourier transform](discrete-fourier-transform.md): An integer index running over $0, 1, \ldots, q-1$ that labels an input coordinate $f_s$.
- $\ell$ (output index), bound on [Discrete Fourier transform](discrete-fourier-transform.md): An integer index running over $0, 1, \ldots, q-1$ that labels an output coordinate $(F_q f)_\ell$.
- $F_q$ (Fourier transform), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The discrete Fourier transform of length $q$, the map sending $f$ to the vector $F_q f$ with the coordinates given above.
- $F_q^+$ (positive-sign transform), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The same map with the positive sign in the exponent, which replaces $\omega$ by $\omega^{-1}$.
- $\sigma$ (dummy index), bound on [Discrete Fourier transform](discrete-fourier-transform.md): A second index running over $0, 1, \ldots, q-1$, introduced so that the substituted sum does not reuse $s$.
- $\rho$ (exponent), bound on [Discrete Fourier transform](discrete-fourier-transform.md): An integer exponent of $\omega$; in the inner sum it is the difference $\sigma - \ell$, with $-q < \rho < q$.
- $\|f\|$ (vector norm), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The largest modulus of a coordinate of the vector $f$.
- $D$ (axis count), bound on [Transform axis](transform-axis.md): The number of axes of the array.
- $i$ (axis index), bound on [Transform axis](transform-axis.md): An index naming one axis, running from 1 to D.
- $x_i$ (axis coordinate), bound on [Transform axis](transform-axis.md): The coordinate of an address along axis i.
- $t_i$ (axis length), bound on [Transform axis](transform-axis.md): The length of axis i: the number of values its coordinate takes.
- $t_1$ (length of axis 1), bound on [Transform axis](transform-axis.md): The length of axis 1 in the example, which takes 2 values.
- $t_2$ (length of axis 2), bound on [Transform axis](transform-axis.md): The length of axis 2 in the example, which takes 4 values.
- $x_1$ (coordinate along axis 1), bound on [Transform axis](transform-axis.md): The coordinate of an address along axis 1, in the set {0,1} in the example.
- $x_2$ (coordinate along axis 2), bound on [Transform axis](transform-axis.md): The coordinate of an address along axis 2, in the set {0,1,2,3} in the example.
- $s$ (coefficient count), bound on [Transform axis](transform-axis.md): A power of two that is the number of coefficients of the stored polynomial, which is also the length of its axis.
- $a_k$ (coefficient), bound on [Transform axis](transform-axis.md): The coefficient of y^k in the stored polynomial.
- $R_r$ (polynomial ring), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The ring of polynomials in $y$ with complex coefficients in which $y^r$ is identified with $-1$.
- $\rho$ (coefficient position), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The position of a coefficient in a record, running from 0 to r-1.
- $\sigma$ (shift count), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The number of places a shift moves each coefficient.
- $\mu_\rho$ (wrap count), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The number of times a shift carries the coefficient at position $\rho$ past position $r-1$.
- $\omega_N$ (polynomial root of unity), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The primitive $N$-th root of unity $y^{2r/N}$ in the polynomial ring $R_r$.
- $f$ (input list), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The list of $N$ records that the transform takes as input.
- $Z$ (transformed list), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The list of $N$ entries that the transform produces from the input list.
- $j$ (entry index), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The index that numbers the entries of a list, running from $0$ to $N-1$.
- $\eta$ (half-size), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The number of positions in each half of a block at a level of the transform.
- $\gamma$ (block offset), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The position within a block at which a butterfly pair starts.
- $U$ (first butterfly entry), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The entry of a butterfly pair at position $\gamma$ of the block.
- $W$ (second butterfly entry), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The entry of a butterfly pair at position $\gamma+\eta$ of the block.
- $\theta$ (twiddle), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The power of $\omega_N$ by which a butterfly multiplies its second entry.
- $L$ (linear map), bound on [Linear contraction](linear-contraction.md): A linear map from vectors in C^m to vectors in C^{m'} whose contraction property is tested.
- $m'$ (output coordinate count), bound on [Linear contraction](linear-contraction.md): The number of coordinates in each output vector of L.
- $\|x\|$ (vector norm), bound on [Linear contraction](linear-contraction.md): The largest modulus among the coordinates of the vector x.
- $\|L\|$ (operator norm), bound on [Linear contraction](linear-contraction.md): The largest value of the norm of Lx over all vectors x with norm at most 1, so L is a contraction exactly when it is at most 1.
- $\eta$ (carried error), bound on [Linear contraction](linear-contraction.md): The error vector carried by the computed input, so that the computed input is x + η.
- $\rho$ (rounding error), bound on [Linear contraction](linear-contraction.md): The rounding error introduced at one step of a computation, added to that step's output.
- $\pi$ (bilinear map), bound on [Bilinear map](bilinear-map.md): The map sending each pair of arguments to a vector of the output space, linear in each argument.
- $U$ (first argument space), bound on [Bilinear map](bilinear-map.md): The vector space that the first argument of the bilinear map ranges over.
- $V$ (second argument space), bound on [Bilinear map](bilinear-map.md): The vector space that the second argument of the bilinear map ranges over.
- $W$ (output space), bound on [Bilinear map](bilinear-map.md): The vector space that the bilinear map returns its values in.
- $\xi$ (first argument), bound on [Bilinear map](bilinear-map.md): An arbitrary element of the first argument space $U$.
- $\zeta$ (second argument), bound on [Bilinear map](bilinear-map.md): An arbitrary element of the second argument space $V$.
- $\xi'$ (computed first argument), bound on [Bilinear map](bilinear-map.md): A computed approximation of the first argument $\xi$.
- $\zeta'$ (computed second argument), bound on [Bilinear map](bilinear-map.md): A computed approximation of the second argument $\zeta$.
- $P$ (exact product map), bound on [Bilinear map](bilinear-map.md): The exact map in the paper's error analysis: the pointwise product of two arrays of records, with products taken modulo $y^r+1$ and divided by $r$.
- $\gamma$ (first integer), bound on [Coprime](coprime.md): One of two integers, not both zero, whose gcd is taken.
- $\rho$ (second integer), bound on [Coprime](coprime.md): The other of two integers, not both zero, whose gcd is taken.
- $J$ (family size), bound on [Coprime](coprime.md): The number of integers in the family f_1 to f_J.
- $f_\sigma$ (family member), bound on [Coprime](coprime.md): The sigma-th integer of the family.
- $\sigma$ (member index), bound on [Coprime](coprime.md): An index running over 1 to J, numbering the family members.
- $Y$ (common multiple), bound on [Coprime](coprime.md): An integer that both gamma and rho divide, or that every member of the family divides.
- $\xi$ (Bezout coefficient), bound on [Coprime](coprime.md): An integer with $\gamma\xi+\rho\zeta=1$, the first of the two Bezout coefficients.
- $\zeta$ (Bezout coefficient), bound on [Coprime](coprime.md): An integer with $\gamma\xi+\rho\zeta=1$, the second of the two Bezout coefficients.
- $W$ (family product), bound on [Coprime](coprime.md): The product f_1 times f_2 up to f_J, which is the least positive integer divisible by every member.
- $\mathbb{Z}$ (integers), bound on [Coprime](coprime.md): The set of integers.
- $\mathbb{Z}/f$ (integers modulo f), bound on [Coprime](coprime.md): The integers with addition taken modulo f.
- $G$ (transform group), bound on [Coprime](coprime.md): The product group Z/f_1 times ... times Z/f_J, with tuples added entrywise.
- $\mathbf{1}$ (all-ones tuple), bound on [Coprime](coprime.md): The tuple (1, ..., 1) in G.
- $W_\sigma$ (prefix product), bound on [Coprime](coprime.md): The product f_1 times ... times f_(sigma-1), with W_1 = 1.
- $\mu_\sigma$ (inverse of prefix product), bound on [Coprime](coprime.md): An integer whose product with W_sigma is 1 modulo f_sigma.
- $\rho$ (Bézout coefficient of β), bound on [Bézout's identity](bezout-identity.md): The integer multiplying β in the combination βρ+γσ that equals gcd(β,γ).
- $\sigma$ (Bézout coefficient of γ), bound on [Bézout's identity](bezout-identity.md): The integer multiplying γ in the combination βρ+γσ that equals gcd(β,γ).
- $\rho'$ (trial coefficient of β), bound on [Bézout's identity](bezout-identity.md): A trial integer multiplying β, which need not yet be the Bézout coefficient.
- $\sigma'$ (trial coefficient of γ), bound on [Bézout's identity](bezout-identity.md): A trial integer multiplying γ, which need not yet be the Bézout coefficient.
- $\xi$ (least positive combination), bound on [Bézout's identity](bezout-identity.md): The least positive value of βρ'+γσ' over all integers ρ' and σ'.
- $f$ (quotient), bound on [Bézout's identity](bezout-identity.md): The integer quotient in the division of β by ξ.
- $\varepsilon$ (remainder), bound on [Bézout's identity](bezout-identity.md): The remainder in the division of β by ξ, which satisfies 0 ≤ ε < ξ.
- $t$ (family parameter), bound on [Bézout's identity](bezout-identity.md): An arbitrary integer labelling one pair of coefficients.
- $\rho$ (generator), bound on [Cyclic group](cyclic-group.md): An element of a group, the base of its powers; when its powers are all the elements, it is the generator.
- $W$ (cyclic group order), bound on [Cyclic group](cyclic-group.md): The number of elements of the cyclic group $C_W$, which counts its distinct powers of the generator.
- $C_W$ (cyclic group), bound on [Cyclic group](cyclic-group.md): The group with $W$ elements, each a power of the generator $\rho$.
- $\xi$ (exponent), bound on [Cyclic group](cyclic-group.md): An integer to which the generator is raised, giving the power $\rho^\xi$.
- $\sigma$ (order of an element), bound on [Cyclic group](cyclic-group.md): The least positive integer with $\rho^\sigma=1$, which is the order of $\rho$ as a group element.
- $\Gamma$ (target map), bound on [Cyclic group](cyclic-group.md): The map from polynomials in $\rho$ modulo $\rho^S-1$ to the target monomials, sending $\rho$ to $\prod_i Y_i^{\mu_i}$.
- $Y_i$ (axis variable), bound on [Cyclic group](cyclic-group.md): The variable of cyclic axis $i$, whose powers index the target monomials.
- $\zeta_i$ (monomial exponent), bound on [Cyclic group](cyclic-group.md): The exponent of $Y_i$ in a target monomial, an integer from $0$ to $s_i-1$.
- $G$ (group), bound on [Order of an element](order-of-element.md): The group in which the order of sigma is taken, a set with an associative operation, an identity, and inverses.
- $\sigma$ (element), bound on [Order of an element](order-of-element.md): An element of the group G whose powers are taken.
- $\rho$ (order), bound on [Order of an element](order-of-element.md): The least positive integer with sigma to the power rho equal to 1; it counts the distinct powers of sigma.
- $x$ (indeterminate), bound on [Order of an element](order-of-element.md): The indeterminate of the ring C[x] modulo x^S minus 1, whose image the map sends to a product of axis indeterminates.
- $x_i$ (axis indeterminate), bound on [Order of an element](order-of-element.md): The indeterminate of axis i, the variable of the i-th cyclic factor of the target ring.
- $\Phi$ (Chinese-remainder map), bound on [Order of an element](order-of-element.md): The map sending x to the product of the axis indeterminates raised to the powers mu_i.
- $\mathcal{I}$ (coordinate label set), bound on [Diagonal scaling](diagonal-scaling.md): The finite set of coordinate labels, one for each coordinate of the vectors.
- $\iota$ (coordinate label), bound on [Diagonal scaling](diagonal-scaling.md): A label in $\mathcal I$ that names one coordinate of the vectors.
- $\tau$ (scalar family), bound on [Diagonal scaling](diagonal-scaling.md): A family of scalars $\tau_\iota$ in $F$, one for each label, which defines a diagonal scaling.
- $\Delta_\tau$ (diagonal scaling), bound on [Diagonal scaling](diagonal-scaling.md): The map multiplying each coordinate $\iota$ of a vector by its scalar $\tau_\iota$.
- $w$ (selected bit count), bound on [Diagonal scaling](diagonal-scaling.md): The number of selected bits of an address, the count of bits that the layer acts on.
- $\sigma$ (second scalar family), bound on [Diagonal scaling](diagonal-scaling.md): A second family of scalars, one for each label, used to compose diagonal scalings.
- $\iota_0$ (zero label), bound on [Diagonal scaling](diagonal-scaling.md): A label in $\mathcal I$ whose scalar $\tau_{\iota_0}$ is zero.
- $f$ (sequence), bound on [Frequency domain](frequency-domain.md): A sequence $f=(f_0,\ldots,f_{q-1})$ of $q$ complex numbers, whose frequency domain is taken.
- $\zeta$ (frequency summation index), bound on [Frequency domain](frequency-domain.md): An index running over the frequencies $0,\ldots,q-1$, summed over in the inversion identity.
- $\ast$ (cyclic convolution), bound on [Frequency domain](frequency-domain.md): The cyclic convolution of two sequences of length $q$, whose entries are sums of products of entries with indices adding to a value modulo $q$.
- $\sigma$ (first input position), bound on [Frequency domain](frequency-domain.md): The position of an entry of the first input sequence $a$ in the convolution sum, running from $0$ to $q-1$.
- $\rho$ (second input position), bound on [Frequency domain](frequency-domain.md): The position of an entry of the second input sequence $b$ in the convolution sum, running from $0$ to $q-1$.
- $\xi$ (binary digit count), bound on [Frequency domain](frequency-domain.md): The number of binary digits of an index, so that the transform length is $q=2^{\xi}$; it counts digits.
- $\mathrm{rev}$ (bit-reversal map), bound on [Frequency domain](frequency-domain.md): The map sending an index $\ell$ to the index whose $\xi$ binary digits are those of $\ell$ in reverse order.
- $\Pi$ (record permutation), bound on [Frequency domain](frequency-domain.md): The permutation of storage slots that moves the entry of frequency $\ell$ to slot $\mathrm{rev}(\ell)$.
- $W$ (ambient space), bound on [Projection along a subspace](projection-along-subspace.md): The finite-dimensional vector space over $F$ on which every projection acts.
- $U$ (subspace), bound on [Projection along a subspace](projection-along-subspace.md): A subspace of $W$ onto which a vector is projected.
- $Y$ (complementary subspace), bound on [Projection along a subspace](projection-along-subspace.md): A subspace of $W$ meeting $U$ only in $0$ and with $U$ spanning $W$ together with it.
- $x_U$ (component in U), bound on [Projection along a subspace](projection-along-subspace.md): The part of a vector $x$ lying in $U$ in its split $x = x_U + x_Y$.
- $x_Y$ (component in Y), bound on [Projection along a subspace](projection-along-subspace.md): The part of a vector $x$ lying in $Y$ in its split $x = x_U + x_Y$.
- $\Theta$ (projection along Y), bound on [Projection along a subspace](projection-along-subspace.md): The map sending each vector $x$ to its component $x_U$ in $U$.
- $\langle\cdot,\cdot\rangle$ (bilinear form), bound on [Projection along a subspace](projection-along-subspace.md): The nondegenerate bilinear form on $W$ whose orthogonality defines the complements $U^\perp$.
- $U^\perp$ (orthogonal complement), bound on [Projection along a subspace](projection-along-subspace.md): The set of vectors orthogonal to every vector of $U$.
- $\Theta_U$ (label projection), bound on [Projection along a subspace](projection-along-subspace.md): The projection onto $U$ along $U^\perp$, which the paper writes $P_U$.
- $V$ (larger nested subspace), bound on [Projection along a subspace](projection-along-subspace.md): A nondegenerate subspace containing $U$, the larger of two nested labels.
- $\mathbb{C}$ (complex numbers), bound on [Closed disk in the complex plane](complex-disk.md): The set of complex numbers, the plane in which the disks lie.
- $\xi$ (disk center), bound on [Closed disk in the complex plane](complex-disk.md): The fixed center of the disk, a complex number.
- $\rho$ (disk radius), bound on [Closed disk in the complex plane](complex-disk.md): The fixed nonnegative real radius, the largest allowed distance from the center.
- $\zeta$ (generic point), bound on [Closed disk in the complex plane](complex-disk.md): A generic point of the plane, a complex number tested for membership in the disk.
- $\mathcal{D}$ (closed disk), bound on [Closed disk in the complex plane](complex-disk.md): The closed disk of center $\xi$ and radius $\rho$, the set of points within distance $\rho$ of $\xi$.
- $\mathbb{Z}[i]$ (Gaussian integers), bound on [Closed disk in the complex plane](complex-disk.md): The set of complex numbers whose real and imaginary parts are both integers.
- $\varepsilon$ (Gaussian integer), bound on [Closed disk in the complex plane](complex-disk.md): A generic element of the Gaussian integers, whose scaled value $2^{-p}\varepsilon$ is a point of the grid disk.
- $\mathcal{D}_p$ (grid disk), bound on [Closed disk in the complex plane](complex-disk.md): The points of the unit disk whose real and imaginary parts are multiples of $2^{-p}$, for precision $p$.
- $V$ (vector space), bound on [Linear functional](linear-functional.md): The vector space over F whose vectors a linear functional takes as input.
- $f$ (linear functional), bound on [Linear functional](linear-functional.md): The map from V to F under study, which sends each vector to one scalar and respects addition and scalar multiplication.
- $a_j$ (coefficient), bound on [Linear functional](linear-functional.md): The value that the functional f takes on the vector with 1 in coordinate j and 0 elsewhere.
- $U$ (vector space), bound on [Dual space](dual-space.md): A vector space over the field F, whose linear functionals form the dual space.
- $U^*$ (dual space), bound on [Dual space](dual-space.md): The vector space of all linear functionals on U.
- $f$ (linear functional), bound on [Dual space](dual-space.md): A generic element of the dual space U^*, which is a linear map from U to F.
- $\sigma$ (example functional), bound on [Dual space](dual-space.md): The linear functional on R^2 sending x to 3x_1 - x_2.
- $\rho$ (second example functional), bound on [Dual space](dual-space.md): The linear functional on R^2 sending x to x_1.
- $\xi$ (real argument), bound on [Floor function](floor-function.md): The real number whose floor is taken.
- $\lfloor\xi\rfloor$ (floor), bound on [Floor function](floor-function.md): The greatest integer not greater than the real number $\xi$.
- $U$ (source set), bound on [Bijection](bijection.md): The set of inputs of the map $f$, each of which $f$ sends to an element of $W$.
- $W$ (target set), bound on [Bijection](bijection.md): The set that the map $f$ sends its inputs into, the set of outputs.
- $f$ (map), bound on [Bijection](bijection.md): The map from the source set $U$ to the target set $W$ whose bijectivity is tested.
- $\sigma$ (source element), bound on [Bijection](bijection.md): An element of the source set $U$, the input of the map $f$.
- $\xi$ (target element), bound on [Bijection](bijection.md): An element of the target set $W$, the output that a bijection must hit exactly once.
- $\Gamma$ (padded address set), bound on [Bijection](bijection.md): A set of integer addresses on which a tape procedure acts, including its padding.
- $f_2$ (non-example map), bound on [Bijection](bijection.md): The map $\sigma\mapsto\lfloor\sigma/2\rfloor$ on $\{0,1,2,3\}$, which is not a bijection.
- $G$ (singled-out set), bound on [Bijection](bijection.md): A subset of the source set $U$ singled out by the argument, which is where two bijections may differ: the bad addresses.
- $S_0$ (composed bijection), bound on [Bijection](bijection.md): The bijection of the rectangle that the update lines of the interchange compose to.
- $T_0$ (ideal bijection), bound on [Bijection](bijection.md): The ideal bijection of the rectangle that performs the required XORs and fixes the other coordinates.
- $W$ (position set), bound on [Permutation](permutation.md): The finite set of positions on which a permutation acts.
- $\sigma$ (permutation), bound on [Permutation](permutation.md): The map from W to W that sends each position to its new position.
- $\xi$ (address), bound on [Permutation](permutation.md): The position of one entry of an array.
- $G$ (array), bound on [Permutation](permutation.md): An array whose entries are stored at addresses.
- $G'$ (moved array), bound on [Permutation](permutation.md): The array holding the entries of G at their new addresses under the permutation.
- $\alpha$ (first entry), bound on [Permutation](permutation.md): The entry of the sequence at position 1.
- $\beta$ (second entry), bound on [Permutation](permutation.md): The entry of the sequence at position 2.
- $\gamma$ (third entry), bound on [Permutation](permutation.md): The entry of the sequence at position 3.
- $\delta$ (fourth entry), bound on [Permutation](permutation.md): The entry of the sequence at position 4.
- $\rho$ (field width), bound on [Address field](address-field.md): The number of bits in each of the two fields being interchanged, a count of bit positions.
- $\ell$ (input wire), bound on [Linear networks and frames](linear-network-frames.md): An input wire of the network, whose supplied array and source vertex are named.
- $\theta_\ell$ (supplied array), bound on [Linear networks and frames](linear-network-frames.md): The physical array supplied on the input wire $\ell$.
- $\mathrm{source}(\ell)$ (source vertex), bound on [Linear networks and frames](linear-network-frames.md): The vertex where the input wire $\ell$ starts.
- $g_\ell$ (input logical array), bound on [Linear networks and frames](linear-network-frames.md): The logical array of the input wire $\ell$, the array it is meant to represent.
- $\rho$ (role permutation), bound on [Linear networks and frames](linear-network-frames.md): The permutation of roles that sends each input role to an output role.
- $\varepsilon_\ell$ (role sign), bound on [Linear networks and frames](linear-network-frames.md): The fixed sign that the output of the input role $\ell$ carries.
- $\sigma$ (output role), bound on [Linear networks and frames](linear-network-frames.md): An output role of the network.
- $\mathrm{sink}(\sigma)$ (sink vertex), bound on [Linear networks and frames](linear-network-frames.md): The sink vertex of the output role $\sigma$.
- $x_h$ (route vertex), bound on [Linear networks and frames](linear-network-frames.md): The vertex at position $h$ along a route.
- $L$ (route length), bound on [Linear networks and frames](linear-network-frames.md): The number of edges on a route, so that the route has $L+1$ vertices.
- $h$ (route position), bound on [Linear networks and frames](linear-network-frames.md): The position of a vertex along a route, running from $0$ to $L$.
- $G$ (pointwise gate), bound on [Linear networks and frames](linear-network-frames.md): A pointwise linear gate, which combines its inputs the same way at every address.
- $t$ (gate input count), bound on [Linear networks and frames](linear-network-frames.md): The number of input arrays that the gate $G$ takes.
- $L$ (route length), bound on [Logical array](logical-array.md): The number of edges on a route, so the route has $L+1$ vertices.
- $J$ (block length), bound on [Cyclic shift](cyclic-shift.md): The number of positions in the block that the shift rotates, a count of those positions.
- $\zeta$ (position), bound on [Cyclic shift](cyclic-shift.md): A position in the block, numbered from 0 to J-1.
- $\xi_\zeta$ (stored value), bound on [Cyclic shift](cyclic-shift.md): The value stored at position zeta of the block.
- $\sigma$ (offset), bound on [Cyclic shift](cyclic-shift.md): The amount of rotation, an integer taken modulo J.
- $V$ (stored bit volume), bound on [Cyclic shift](cyclic-shift.md): The number of stored bits in the array, a count of its data bits.
- $\xi$ (first input value), bound on [Butterfly](butterfly.md): The first of the two input values of the butterfly.
- $\zeta$ (second input value), bound on [Butterfly](butterfly.md): The second of the two input values of the butterfly.
- $H_0$ (butterfly map), bound on [Butterfly](butterfly.md): The two-point map sending a pair of values to its half-sum and half-difference.
- $\sigma$ (index bit), bound on [Butterfly](butterfly.md): The index of one bit of a position, counted from 0 at the least significant end, so a level acts on the pairs that differ in this bit.
- $b$ (digit width), bound on [Radix-digit convolution](radix-digit-convolution.md): The number of bits in each digit of an input.
- $J$ (digit count), bound on [Radix-digit convolution](radix-digit-convolution.md): The number of digits in each input, that is, the number of blocks of $b$ bits.
- $x_i$ (input digit), bound on [Radix-digit convolution](radix-digit-convolution.md): The digit of the first input $x$ at position $i$, a value from $0$ to $2^b-1$.
- $y_j$ (input digit of y), bound on [Radix-digit convolution](radix-digit-convolution.md): The digit of the second input $y$ at position $j$, defined as the digits of $x$ are.
- $\xi$ (formal variable), bound on [Radix-digit convolution](radix-digit-convolution.md): A symbol, not a number, that the digit polynomials are written in.
- $\hat{x}$ (digit polynomial of x), bound on [Radix-digit convolution](radix-digit-convolution.md): The polynomial in $\xi$ whose coefficients are the digits of $x$.
- $\hat{y}$ (digit polynomial of y), bound on [Radix-digit convolution](radix-digit-convolution.md): The polynomial in $\xi$ whose coefficients are the digits of $y$.
- $c_m$ (product coefficient), bound on [Radix-digit convolution](radix-digit-convolution.md): The coefficient of $\xi^m$ in the product of the two digit polynomials, which is entry $m$ of the convolution of the digit sequences.
- $h$ (ground set size), bound on [Ground set](ground-set.md): The number of elements of the ground set, the count of its elements.
- $\mathcal{T}$ (three-element subsets), bound on [Ground set](ground-set.md): The set of all three-element subsets of $[h]$.
- $g_1$ (first input array), bound on [Gate and terminal of a network](network-gate-terminal.md): The logical array on the first input wire of a two-wire gate.
- $g_2$ (second input array), bound on [Gate and terminal of a network](network-gate-terminal.md): The logical array on the second input wire of a two-wire gate.
- $g_1$ (input array), bound on [Incidence](incidence.md): The logical array on input wire 1 of the gate.
- $g_2$ (second input array), bound on [Incidence](incidence.md): The logical array on input wire 2 of the gate.
- $g_t$ (last input array), bound on [Incidence](incidence.md): The logical array on the last of the $t$ input wires of the gate.
- $D'$ (other frame), bound on [Incidence](incidence.md): An invertible operator on arrays that one incidence uses in place of the gate's frame $D_v$.
- $\Gamma$ (moving-back operator), bound on [Incidence](incidence.md): The single operator that would move the gate's result back to logical form.
- $P$ (matrix P), bound on [Tensor product](tensor-product.md): A matrix, the first factor of a tensor product.
- $p_{\xi\sigma}$ (entry of P), bound on [Tensor product](tensor-product.md): The entry of $P$ in row $\xi$ and column $\sigma$.
- $Q$ (matrix Q), bound on [Tensor product](tensor-product.md): A second matrix, the second factor of a tensor product.
- $q_{\upsilon\zeta}$ (entry of Q), bound on [Tensor product](tensor-product.md): The entry of $Q$ in row $\upsilon$ and column $\zeta$.
- $\xi$ (row index), bound on [Tensor product](tensor-product.md): A row index of $P$, and in an address the output bit string $\xi$.
- $\sigma$ (column index), bound on [Tensor product](tensor-product.md): A column index of $P$, and in an address the input bit string $\sigma$.
- $\upsilon$ (row index of Q), bound on [Tensor product](tensor-product.md): A row index of $Q$.
- $\zeta$ (column index of Q), bound on [Tensor product](tensor-product.md): A column index of $Q$.
- $J$ (factor count), bound on [Tensor product](tensor-product.md): The number of factors in a tensor power, which is also the number of coordinates it acts on.
- $\sigma_l$ (address bit), bound on [Tensor product](tensor-product.md): The bit of an input address $\sigma$ at coordinate $l$.
- $l$ (coordinate index), bound on [Tensor product](tensor-product.md): The index of a coordinate, running from $1$ to $J$.
- $\Psi$ (function on addresses), bound on [Tensor product](tensor-product.md): A complex-valued function on addresses of $J$ bits, which $P^{\otimes J}$ transforms.
- $P'$ (second matrix P'), bound on [Tensor product](tensor-product.md): A second matrix compatible with $P$ in the mixed-product rule.
- $Q'$ (second matrix Q'), bound on [Tensor product](tensor-product.md): A second matrix compatible with $Q$ in the mixed-product rule.
- $W$ (row index of P'), bound on [Tensor product](tensor-product.md): A row index of $P'$, summed over as a middle index of $P$ and $P'$.
- $Y$ (row index of Q'), bound on [Tensor product](tensor-product.md): A row index of $Q'$, summed over as a middle index of $Q$ and $Q'$.
- $P_{(l)}$ (single-coordinate operator), bound on [Tensor product](tensor-product.md): The operator that applies $P$ to coordinate $l$ and the identity to the other coordinates.
- $Q_0$ (radix), bound on [Carry propagation](carry-propagation.md): The number of values a digit can take, $2^b$, which is also the base for writing digits.
- $c_t$ (product coefficient), bound on [Carry propagation](carry-propagation.md): The integer coefficient of $z^t$ in the product of the two digit polynomials, at position $t$.
- $t$ (position index), bound on [Carry propagation](carry-propagation.md): The position of a coefficient or digit in the list, running over $0, 1, \dots$.
- $\sigma_t$ (output digit), bound on [Carry propagation](carry-propagation.md): The digit of the output at position $t$, an integer from $0$ to $Q_0-1$.
- $\gamma_t$ (carry), bound on [Carry propagation](carry-propagation.md): The amount carried into position $t$ from the lower positions.
- $B$ (modulus), bound on [Congruence](congruence-modulo.md): The positive integer modulus by which congruence is taken.
- $d$ (integer), bound on [Congruence](congruence-modulo.md): An integer compared with $e$ modulo $B$.
- $e$ (integer), bound on [Congruence](congruence-modulo.md): An integer compared with $d$ modulo $B$.
- $\mathbb{Z}$ (integers), bound on [Congruence](congruence-modulo.md): The set of all integers.
- $\xi$ (multiple of B), bound on [Congruence](congruence-modulo.md): The integer with $d-e=\xi B$, so $\xi B$ is the difference of two congruent integers.
- $\zeta$ (third integer), bound on [Congruence](congruence-modulo.md): An integer used in the transitivity argument, with $e \equiv \zeta$.
- $\sigma$ (class member), bound on [Congruence](congruence-modulo.md): An integer in the residue class of $d$.
- $\delta$ (remainder), bound on [Congruence](congruence-modulo.md): The unique integer in $\{0,\dots,B-1\}$ lying in a residue class.
- $d'$ (second integer), bound on [Congruence](congruence-modulo.md): An integer congruent to $d$ modulo $B$.
- $e'$ (second integer), bound on [Congruence](congruence-modulo.md): An integer congruent to $e$ modulo $B$.
- $\eta$ (second multiple), bound on [Congruence](congruence-modulo.md): The integer with $e'-e=\eta B$.
- $u_j$ (input coefficient), bound on [Congruence](congruence-modulo.md): The input coefficient at position $j$.
- $\gamma_j$ (carry), bound on [Congruence](congruence-modulo.md): The carry into position $j$.
- $d_j$ (output digit), bound on [Congruence](congruence-modulo.md): The output digit at position $j$.
- $\gamma_{j+1}$ (next carry), bound on [Congruence](congruence-modulo.md): The carry into position $j+1$.
- $\sigma$ (residue bit count), bound on [Schönhage–Strassen multiplication](schonhage-strassen.md): The number of bits in a residue, which sets the modulus $2^\sigma+1$.
- $\xi$ (shift count), bound on [Schönhage–Strassen multiplication](schonhage-strassen.md): The number of places a multiplication shifts, with $0\le\xi<\sigma$.
- $\zeta$ (residue), bound on [Schönhage–Strassen multiplication](schonhage-strassen.md): A residue, represented by the integer $\zeta$ with $0\le\zeta<2^\sigma$.
- $\zeta_i$ (bit of a residue), bound on [Schönhage–Strassen multiplication](schonhage-strassen.md): The bit of $\zeta$ at position $i$, either 0 or 1.
- $i$ (bit position), bound on [Schönhage–Strassen multiplication](schonhage-strassen.md): A bit position of a residue, an integer from 0 to $\sigma-1$.
- $R$ (ring), bound on [Ring](ring.md): A set with an addition and a multiplication that satisfy the axioms listed on this page.
- $\xi$ (ring element), bound on [Ring](ring.md): An element of the ring $R$, one of the arguments of its addition and multiplication.
- $\zeta$ (ring element), bound on [Ring](ring.md): An element of the ring $R$, one of the arguments of its addition and multiplication.
- $\vartheta$ (ring element), bound on [Ring](ring.md): An element of the ring $R$, one of the arguments of its addition and multiplication.
- $y$ (polynomial variable), bound on [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md): The indeterminate of the polynomial ring whose powers act as roots of unity.
- $r$ (record length), bound on [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md): The number of complex coefficients in a polynomial record, a power of two.
- $\sigma$ (exponent of y), bound on [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md): An integer exponent of $y$, the power being reduced or the order being tested.
- $\xi$ (quotient polynomial), bound on [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md): The polynomial whose product with $y^r+1$ is the difference of two representatives.
- $\zeta$ (root of unity), bound on [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md): An element of the ring whose positive integer power equals 1.
- $\chi$ (sequence), bound on [Limit inferior](limit-inferior.md): A sequence of real numbers; $\chi_k$ is its $k$-th term.
- $k$ (term position), bound on [Limit inferior](limit-inferior.md): A position in a sequence, the index of a term.
- $m$ (tail start), bound on [Limit inferior](limit-inferior.md): The position from which a tail of the sequence starts.
- $\tau_m$ (tail infimum), bound on [Limit inferior](limit-inferior.md): The infimum of the terms of the sequence from position $m$ on.
- $\varepsilon$ (tolerance), bound on [Limit inferior](limit-inferior.md): A positive real number against which the terms of the sequence are compared.
- $\rho_n$ (time ratio), bound on [Limit inferior](limit-inferior.md): The ratio of the running time $T_A(n)$ to $n\lg n$, for $n \ge 2$.
- $\delta_A$ (conjecture constant), bound on [Limit inferior](limit-inferior.md): The positive constant in the conjectured lower bound for machine $A$.
- $\Gamma_A$ (conjecture threshold), bound on [Limit inferior](limit-inferior.md): The input length from which the conjectured lower bound for machine $A$ holds.
- $\delta$ (arbitrary positive real), bound on [Limit inferior](limit-inferior.md): A real number greater than zero, arbitrary in the negation of the conjecture.
- $\Gamma$ (arbitrary threshold), bound on [Limit inferior](limit-inferior.md): A threshold on input length, arbitrary in the negation of the conjecture.
- $\log$ (base-2 logarithm), bound on [The n log n optimality conjecture](n-log-n-conjecture.md): The base-2 logarithm, the function the page writes as log.
- $N_A$ (eventual threshold), bound on [The n log n optimality conjecture](n-log-n-conjecture.md): The input length from which the lower bound for machine A is required to hold.
- $n_0$ (threshold input length), bound on [The n log n optimality conjecture](n-log-n-conjecture.md): A threshold on the input length, from which the negated statement asks for some input length with a small running time ratio.
- $\sigma$ (positive constant), bound on [Fixed-tape machine model](fixed-tape-model.md): A positive constant multiplying $n\log n$ in the lower bound $T_A(n) \geq \sigma\, n\log n$ for machine $A$.
- $n_0$ (threshold input length), bound on [Fixed-tape machine model](fixed-tape-model.md): The input length from which the lower bound on $T_A(n)$ holds for machine $A$.
- $\Omega$ (Big-Omega notation), bound on [Fixed-tape machine model](fixed-tape-model.md): The notation $\Omega(g)$ for the functions that are at least a positive constant times $g$ for all large inputs.
- $\mathbb{F}_2$ (binary field), bound on [Binary field](binary-field.md): The field with the two elements 0 and 1, in which addition is exclusive or and multiplication is AND.
- $\oplus$ (exclusive or), bound on [Binary field](binary-field.md): The addition of the binary field, which gives 1 exactly when its two bits differ.
- $\sigma$ (three-element subset), bound on [Binary field](binary-field.md): A three-element subset of the ground set, one of the two whose shared elements give a coefficient.
- $\sigma'$ (second three-element subset), bound on [Binary field](binary-field.md): A second three-element subset of the ground set, the output side of the coefficient.
- $\beta$ (integer to invert), bound on [Modular inverse](modular-inverse.md): The integer whose inverse modulo M is sought.
- $M$ (modulus), bound on [Modular inverse](modular-inverse.md): The fixed positive integer modulo which the inverse is taken.
- $\mu$ (modular inverse), bound on [Modular inverse](modular-inverse.md): An integer whose product with beta is congruent to 1 modulo M, the inverse of beta.
- $\sigma$ (integer quotient), bound on [Modular inverse](modular-inverse.md): The integer quotient of beta times mu minus 1 divided by M.
- $i$ (axis index), bound on [Modular inverse](modular-inverse.md): The index of an axis, an integer from 1 to d.
- $M_i$ (axis length), bound on [Modular inverse](modular-inverse.md): The length of axis i, the number of values its coordinate takes.
- $j$ (axis index in products), bound on [Modular inverse](modular-inverse.md): An axis index that runs over the axes before a given axis in a product.
- $P_i$ (prefix product), bound on [Modular inverse](modular-inverse.md): The product of the axis lengths before axis i, with P_1 equal to 1.
- $\xi$ (group generator), bound on [Modular inverse](modular-inverse.md): A generator of the cyclic group of order S.
- $\xi_i$ (axis generator), bound on [Modular inverse](modular-inverse.md): A generator of the cyclic group of order M_i for axis i.
- $\zeta$ (positive exponent), bound on [Modular inverse](modular-inverse.md): A positive integer exponent for which the power of the image is 1.
- $\sigma$ (selected bit values), bound on [Binary change of basis](binary-change-of-basis.md): The column $(\sigma_1,\dots,\sigma_m)$ of the values of the $m$ selected bits, each in $\mathbb F_2$.
- $P_M$ (address permutation), bound on [Binary change of basis](binary-change-of-basis.md): The permutation of addresses that moves the value at each address $\alpha$ to $M\alpha$, for a fixed invertible $M$.
- $v$ (direction vector), bound on [Binary change of basis](binary-change-of-basis.md): A vector of $\mathbb F_2^m$ in a residual basis; $v_j$ is its $j$-th member.
- $\rho$ (residual dimension), bound on [Binary change of basis](binary-change-of-basis.md): The number of vectors in a residual basis, which counts the dimension of the edge's residual.
- $\zeta_j$ (standard basis vector), bound on [Binary change of basis](binary-change-of-basis.md): The vector of $\mathbb F_2^m$ with a 1 in position $j$ and 0 elsewhere.
- $\sigma$ (triple), bound on [Bit network](bit-network.md): An element of $T$, a three-element subset of $[h]$.
- $W$ (source bank), bound on [Bit network](bit-network.md): The bank of source bits, holding one bit $W_\sigma$ for each triple $\sigma$.
- $Y$ (target bank), bound on [Bit network](bit-network.md): The bank of target bits, holding one bit $Y_\sigma$ for each triple $\sigma$.
- $\zeta_{\sigma\sigma'}$ (side wire), bound on [Bit network](bit-network.md): The scratch wire of the ordered neighbouring pair $(\sigma,\sigma')$.
- $J_\upsilon$ (central wire), bound on [Bit network](bit-network.md): The scratch wire attached to the element $\upsilon$ of $[h]$.
- $\upsilon$ (ground element), bound on [Bit network](bit-network.md): An element of the ground set $[h]$, indexing a central wire.
- $\zeta$ (phase factor), bound on [Phase factor](phase-factor.md): A complex number of modulus one, the factor multiplied into coefficients.
- $D$ (selected bit count), bound on [Phase factor](phase-factor.md): The number of selected address bits on which a butterfly layer acts.
- $x$ (address), bound on [Phase factor](phase-factor.md): An address whose selected bits are $x_1,\dots,x_D$, each 0 or 1.
- $S_D$ (diagonal phase operator), bound on [Phase factor](phase-factor.md): The operator multiplying the value at each address by the power of i given by its selected bits.
- $C$ (forward kernel), bound on [Phase factor](phase-factor.md): The 2 by 2 matrix with entries (1+i)/2 and (1-i)/2 that is the forward kernel.
- $Z$ (sign matrix), bound on [Phase factor](phase-factor.md): The diagonal matrix diag(1,-1) that flips the sign of the second basis coordinate.
- $\otimes$ (tensor product), bound on [Phase factor](phase-factor.md): The Kronecker product of matrices, whose D-fold power acts on D coordinates at once.
- $\mathcal{G}$ (Gaussian dyadics), bound on [Gaussian dyadics](gaussian-dyadics.md): The set of Gaussian dyadics.
- $\sigma$ (numerator), bound on [Gaussian dyadics](gaussian-dyadics.md): The Gaussian integer numerator of a Gaussian dyadic $\sigma/2^{\Gamma}$.
- $\Gamma$ (denominator exponent), bound on [Gaussian dyadics](gaussian-dyadics.md): The number of factors of two in the denominator of a Gaussian dyadic, a nonnegative integer.
- $\sigma'$ (second numerator), bound on [Gaussian dyadics](gaussian-dyadics.md): The Gaussian integer numerator of a second Gaussian dyadic $\sigma'/2^{\Gamma'}$.
- $\Gamma'$ (second exponent), bound on [Gaussian dyadics](gaussian-dyadics.md): The number of factors of two in the denominator of the second Gaussian dyadic.
- $\Upsilon$ (common exponent), bound on [Gaussian dyadics](gaussian-dyadics.md): The larger of the two exponents $\Gamma$ and $\Gamma'$, the number of factors of two in the common denominator of a sum.
- $\nu$ (address), bound on [Two-point kernel](two-point-kernel.md): An integer from 0 to 2^d-1 labeling one entry of an array, whose binary form has d bits.
- $e$ (bit position), bound on [Two-point kernel](two-point-kernel.md): An index from 0 to d-1 naming the bit along which a kernel acts, counted from the least significant bit.
- $\chi$ (array of values), bound on [Two-point kernel](two-point-kernel.md): An array of complex values with one entry for each address.
- $X$ (bit flip), bound on [Two-point kernel](two-point-kernel.md): The 2 by 2 matrix that interchanges the two entries of a pair.
- $\delta$ (identity coefficient), bound on [Two-point kernel](two-point-kernel.md): The complex coefficient of the identity matrix in a two-point kernel.
- $\kappa$ (bit-flip coefficient), bound on [Two-point kernel](two-point-kernel.md): The complex coefficient of the bit flip in a two-point kernel.
- $K$ (two-point kernel), bound on [Two-point kernel](two-point-kernel.md): The 2 by 2 matrix delta I plus kappa X, which is the two-point kernel.
- $K_e$ (kernel along bit e), bound on [Two-point kernel](two-point-kernel.md): The operator on arrays that applies the kernel to each pair of addresses differing in bit e.
- $f$ (modulus polynomial), bound on [Polynomial ring](polynomial-ring.md): The fixed monic polynomial with complex coefficients by which the ring is reduced.
- $m$ (coefficient count), bound on [Polynomial ring](polynomial-ring.md): The number of coefficients in each representative, which is the degree of f.
- $R$ (polynomial ring), bound on [Polynomial ring](polynomial-ring.md): The ring of classes of complex polynomials, where two polynomials are identified when their difference is a multiple of f.
- $g_1$ (first polynomial), bound on [Polynomial ring](polynomial-ring.md): A polynomial with complex coefficients, one of two that are compared modulo f.
- $g_2$ (second polynomial), bound on [Polynomial ring](polynomial-ring.md): A second polynomial with complex coefficients, compared with g_1 modulo f.
- $u$ (representative), bound on [Polynomial ring](polynomial-ring.md): The unique polynomial of degree less than m in a class, the representative of that class.
- $u_t$ (coefficient), bound on [Polynomial ring](polynomial-ring.md): The complex coefficient of y^t in the representative u.
- $t$ (coefficient index), bound on [Polynomial ring](polynomial-ring.md): The index of a coefficient of the representative, running from 0 to m-1.
- $e$ (exponent), bound on [Polynomial ring](polynomial-ring.md): The exponent of y in a term of a product, the power of y that reduction tests against m.
- $R_r$ (record ring), bound on [Polynomial ring](polynomial-ring.md): The paper's name for the polynomial ring modulo y^r+1, the ring C[y]/(y^r+1).
- $s$ (shift exponent), bound on [Polynomial ring](polynomial-ring.md): The integer exponent of the power of y that multiplies the representative, which the paper writes as a.
- $\sigma_1$ (real numerator), bound on [Grid numerator](grid-numerator.md): The integer multiplier of $2^{-p}$ in the real part of a grid value.
- $\sigma_2$ (imaginary numerator), bound on [Grid numerator](grid-numerator.md): The integer multiplier of $2^{-p}$ in the imaginary part of a grid value.
- $W$ (output coefficient), bound on [Grid numerator](grid-numerator.md): One output coefficient of the paper's polynomial multiplication, a sum of $r$ signed products of input coefficients.
- $\mathrm{trunc}_0$ (truncation toward zero), bound on [Grid numerator](grid-numerator.md): The map that sends a real number to the integer nearest to it on the side of 0.
- $J$ (word width), bound on [Grid numerator](grid-numerator.md): The number of bits in a signed word that stores one component numerator.
- $J$ (number of congruences), bound on [Chinese remainder theorem](chinese-remainder-theorem.md): The number of congruences in the system, a positive integer.
- $\sigma$ (congruence index), bound on [Chinese remainder theorem](chinese-remainder-theorem.md): An integer index numbering the congruences, running from 1 to J.
- $W_\sigma$ (modulus), bound on [Chinese remainder theorem](chinese-remainder-theorem.md): The modulus of the sigma-th congruence, a positive integer.
- $\varrho_\sigma$ (residue), bound on [Chinese remainder theorem](chinese-remainder-theorem.md): The residue of the sigma-th congruence, an integer.
- $Y$ (unknown integer), bound on [Chinese remainder theorem](chinese-remainder-theorem.md): The unknown integer whose congruences are being solved.
- $\Gamma$ (product of moduli), bound on [Chinese remainder theorem](chinese-remainder-theorem.md): The product of all the moduli, a positive integer.
- $Y'$ (second solution), bound on [Chinese remainder theorem](chinese-remainder-theorem.md): A second integer that is also a solution of the system.
- $D$ (difference of solutions), bound on [Chinese remainder theorem](chinese-remainder-theorem.md): The difference Y' minus Y of two solutions.
- $\sigma'$ (earlier congruence index), bound on [Chinese remainder theorem](chinese-remainder-theorem.md): An index of a modulus among the first sigma moduli.
- $\Delta$ (quotient integer), bound on [Chinese remainder theorem](chinese-remainder-theorem.md): The integer by which W_1 through W_sigma times Delta gives D.
- $\varpi_\sigma$ (inverse integer), bound on [Chinese remainder theorem](chinese-remainder-theorem.md): An integer that inverts Gamma/W_sigma modulo W_sigma.
- $\Xi_\sigma$ (Bezout cofactor), bound on [Chinese remainder theorem](chinese-remainder-theorem.md): The integer multiplying W_sigma in the Bezout identity for Gamma/W_sigma and W_sigma.
- $f$ (input sequence), bound on [Cyclic convolution](cyclic-convolution.md): The first input sequence, of length n, with entries indexed from 0 to n-1.
- $g$ (second input sequence), bound on [Cyclic convolution](cyclic-convolution.md): The second input sequence, of length n, with entries indexed from 0 to n-1.
- $k$ (output position), bound on [Cyclic convolution](cyclic-convolution.md): The position of an entry of the output $f \ast g$, running from 0 to n-1.
- $j$ (summand position), bound on [Cyclic convolution](cyclic-convolution.md): The position in $f$ of each summand of an output entry, so it indexes $f$ here.
- $w$ (formal variable), bound on [Cyclic convolution](cyclic-convolution.md): The formal variable in which the sequence $f$ is written as a polynomial.
- $d$ (axis count), bound on [Cyclic convolution](cyclic-convolution.md): The number of axes in the split, that is, the number of factors $n_1, \dots, n_d$ of the length n.
- $\kappa$ (axis index), bound on [Cyclic convolution](cyclic-convolution.md): The index of an axis, running from 1 to d.
- $n_\kappa$ (axis length), bound on [Cyclic convolution](cyclic-convolution.md): The length of axis $\kappa$, the number of values the coordinate along that axis takes.
- $\mu_\kappa$ (chosen multiplier), bound on [Cyclic convolution](cyclic-convolution.md): A positive integer, invertible modulo $n_\kappa$, that multiplies the index $k$ in the layout map.
- $\nu_\kappa$ (axis variable), bound on [Cyclic convolution](cyclic-convolution.md): The variable of axis $\kappa$ in the target polynomial ring.
- $\Phi$ (layout map), bound on [Cyclic convolution](cyclic-convolution.md): The ring map sending $w$ to $\prod_\kappa \nu_\kappa^{\mu_\kappa}$, which is an isomorphism onto the target ring.
- $t$ (transform length), bound on [Cyclic convolution](cyclic-convolution.md): The even length of the transform, which counts the entries of each sequence it transforms.
- $\omega$ (primitive root), bound on [Cyclic convolution](cyclic-convolution.md): The complex number $e^{2\pi i/t}$, whose $t$-th power is 1.
- $F_t$ (one-axis transform), bound on [Cyclic convolution](cyclic-convolution.md): The map sending a sequence $u$ of length $t$ to the sequence $F_t u$ with the entries given in the sentence.
- $\sigma_j$ (phase factor), bound on [Cyclic convolution](cyclic-convolution.md): The unit-modulus phase $e^{\pi i j^2/t}$ attached to index $j$.
- $\rho$ (phase sequence), bound on [Cyclic convolution](cyclic-convolution.md): The function $\rho(\delta) = e^{-\pi i \delta^2/t}$, read as a sequence of length t modulo t.
- $\delta$ (integer argument), bound on [Cyclic convolution](cyclic-convolution.md): An integer at which the phase function $\rho$ is evaluated.
- $R'$ (target ring), bound on [Ring homomorphism and isomorphism](ring-homomorphism.md): The second ring, the target of a ring homomorphism.
- $\sigma$ (ring homomorphism), bound on [Ring homomorphism and isomorphism](ring-homomorphism.md): A map between rings that preserves sums, products and 1.
- $W$ (quotient ring W), bound on [Ring homomorphism and isomorphism](ring-homomorphism.md): The ring of complex polynomials in t in which every multiple of t^2-1 is zero.
- $t$ (indeterminate t), bound on [Ring homomorphism and isomorphism](ring-homomorphism.md): The indeterminate of W; on this page the letter denotes only this.
- $\alpha$ (constant coefficient), bound on [Ring homomorphism and isomorphism](ring-homomorphism.md): The constant coefficient of an element alpha + beta t of W.
- $\beta$ (linear coefficient), bound on [Ring homomorphism and isomorphism](ring-homomorphism.md): The coefficient of t in an element alpha + beta t of W.
- $s$ (square-one element), bound on [Ring homomorphism and isomorphism](ring-homomorphism.md): An element of the commutative target ring whose square is 1, the image of t.
- $W'$ (target ring W'), bound on [Ring homomorphism and isomorphism](ring-homomorphism.md): The ring C[y]/(y^2+1), the target of the example isomorphism.
- $\rho$ (substitution map), bound on [Ring homomorphism and isomorphism](ring-homomorphism.md): The homomorphism from W to C sending t to 1.
- $x$ (generator), bound on [Ring homomorphism and isomorphism](ring-homomorphism.md): The generator of the cyclic polynomial ring C[x]/(x^S-1).
- $g$ (monomial image of x), bound on [Ring homomorphism and isomorphism](ring-homomorphism.md): The monomial that the map Phi sends x to.
- $e_i$ (monomial exponent), bound on [Ring homomorphism and isomorphism](ring-homomorphism.md): The exponent of x_i in a monomial of the target basis.
- $D$ (number of axes), bound on [Chinese-remainder map](chinese-remainder-map.md): The number of cyclic axes, which is the number of pairwise coprime axis lengths.
- $\lambda_i$ (axis length), bound on [Chinese-remainder map](chinese-remainder-map.md): The number of positions on axis $i$, the number of values its coordinate takes.
- $x$ (generator indeterminate), bound on [Chinese-remainder map](chinese-remainder-map.md): A formal symbol, never evaluated, whose powers index the positions of the one-dimensional ring.
- $x_i$ (axis indeterminate), bound on [Chinese-remainder map](chinese-remainder-map.md): The indeterminate of axis $i$ in the multidimensional ring.
- $\eta_i$ (axis exponent), bound on [Chinese-remainder map](chinese-remainder-map.md): The exponent of $x_i$ in a monomial of the multidimensional ring.
- $\nu$ (power exponent), bound on [Chinese-remainder map](chinese-remainder-map.md): A nonnegative integer exponent of $\Phi(x)$.
- $e$ (coefficient index), bound on [Chinese-remainder map](chinese-remainder-map.md): An ordinary coefficient index in $[0,\Lambda)$, the position of a coefficient in the one-dimensional ring.
- $a$ (first exponent), bound on [Chinese-remainder map](chinese-remainder-map.md): The smaller of two exponents of $\Phi(x)$ compared for equality, an integer with $0\le a<\Lambda$.
- $b$ (second exponent), bound on [Chinese-remainder map](chinese-remainder-map.md): The larger of two exponents of $\Phi(x)$ compared for equality, an integer with $a<b<\Lambda$.
- $\gamma_i$ (axis coordinate), bound on [Chinese-remainder map](chinese-remainder-map.md): The coordinate of the index $e$ on axis $i$, an integer in $[0,\lambda_i)$.
- $k$ (exponent), bound on [Chinese-remainder map](chinese-remainder-map.md): A nonnegative integer exponent of $x_i$, the power to which the indeterminate of axis $i$ is raised.
- $\sigma$ (row index), bound on [Chinese-remainder map](chinese-remainder-map.md): The row index of the transform matrix $A_i$, running from $0$ to $\lambda_i-1$.
- $A_i$ (axis transform matrix), bound on [Chinese-remainder map](chinese-remainder-map.md): The $\lambda_i\times\lambda_i$ matrix with entry $\omega_i^{\sigma\eta}$ in row $\sigma$ and column $\eta$, the transform on axis $i$.
- $\otimes$ (Kronecker product), bound on [Chinese-remainder map](chinese-remainder-map.md): The Kronecker (tensor) product of matrices, which combines the one-axis transforms into a transform on all axes.
- $\odot$ (pointwise product), bound on [Pointwise product](pointwise-product.md): The operation giving $a\odot b$, the sequence whose entry at each position is the product of the two entries at that position.
- $P$ (normalized product), bound on [Pointwise product](pointwise-product.md): The map sending two ring entries to their product divided by $r$, the paper's normalized product.
- $m$ (summation index), bound on [Opposite transform](opposite-transform.md): A dummy summation index running from $0$ to $q-1$ that names an input position of a vector; it counts nothing.
- $n$ (second summation index), bound on [Opposite transform](opposite-transform.md): A second dummy summation index running from $0$ to $q-1$ that names an input position of a second vector.
- $u'$ (second vector), bound on [Opposite transform](opposite-transform.md): A second vector of $q$ complex numbers, paired with $u$ in a convolution.
- $M$ (cyclic address count), bound on [Opposite transform](opposite-transform.md): The number of cyclic addresses of each array, which counts the entries along the cyclic axes.
- $f$ (first input array), bound on [Opposite transform](opposite-transform.md): The first of the two disk-grid ring arrays whose convolution is taken.
- $g$ (second input array), bound on [Opposite transform](opposite-transform.md): The second of the two disk-grid ring arrays whose convolution is taken.
- $\sigma$ (condition), bound on [Iverson bracket](iverson-bracket.md): A statement that is either true or false, and whose truth decides whether its bracket is 1 or 0.
- $c$ (log exponent), bound on [Near-linear time](near-linear-time.md): A fixed real number, the power to which the logarithm factor of a near-linear bound is raised.
- $\sigma$ (negacyclic convolution), bound on [Negacyclic convolution](negacyclic-convolution.md): The sequence of n complex numbers that is the negacyclic convolution of a and b.
- $J$ (small operator), bound on [Neumann series](neumann-series.md): The linear operator whose powers the series sums; the paper takes $J = N - I$.
- $\xi$ (term index), bound on [Neumann series](neumann-series.md): The index numbering the terms of the series, a nonnegative integer.
- $\Xi$ (term count), bound on [Neumann series](neumann-series.md): The number of terms in a partial sum of the series.
- $\Psi$ (partial sum), bound on [Neumann series](neumann-series.md): An arbitrary partial sum of the series with $\Xi$ terms, used in the error identity.
- $W$ (limit operator), bound on [Neumann series](neumann-series.md): The limit of the partial sums, which is the inverse $(I+J)^{-1}$.
- $\sigma$ (norm exponent), bound on [Neumann series](neumann-series.md): The exponent $\alpha^2\theta$ in the bound $\|J\|<2^{-\sigma}$.
- $\alpha$ (construction parameter), bound on [Neumann series](neumann-series.md): A parameter of the paper's construction, not the address letter of earlier pages.
- $\theta$ (construction parameter), bound on [Neumann series](neumann-series.md): A parameter of the paper's construction, entering the exponent $\sigma=\alpha^2\theta$.
- $N$ (paper's operator), bound on [Neumann series](neumann-series.md): The operator $I+J$ of the paper, with $J=N-I$; the letter changes meaning from earlier pages.
- $\|\cdot\|$ (operator norm), bound on [Neumann series](neumann-series.md): The operator norm induced by the array norm, so $\|J\|=\sup_{\|\upsilon\|\le 1}\|J\upsilon\|$.
- $\Xi$ (sample space), bound on [Probability](probability.md): The finite set of all possible outcomes of the experiment.
- $\mathcal{A}$ (event), bound on [Probability](probability.md): An event, a subset of the sample space consisting of the outcomes in which the event occurs.
- $\mathcal{B}$ (second event), bound on [Probability](probability.md): A second event, also a subset of the sample space.
- $\Pr$ (probability), bound on [Probability](probability.md): The function giving the probability $\Pr(\mathcal{A})$ of an event $\mathcal{A}$, a real number between 0 and 1.
- $\mathcal{W}$ (sample space), bound on [Independence of events](independence.md): The finite set of possible outcomes of an experiment.
- $\Pr$ (probability function), bound on [Independence of events](independence.md): The function that assigns each event a number between 0 and 1.
- $\mathcal{C}$ (event), bound on [Independence of events](independence.md): An event, that is, a subset of the sample space, here the first of two events being compared.
- $\mathcal{D}$ (second event), bound on [Independence of events](independence.md): An event, that is, a subset of the sample space, here the second of two events being compared.
- $|\mathcal{C}|$ (outcome count), bound on [Independence of events](independence.md): The number of outcomes in the event $\mathcal{C}$.
- $\sigma$ (half-length output index), bound on [Radix-two factorization](radix-two-factorization.md): The output index of a half-length transform, with $0 \le \sigma < q/2$, so that the full output index is $\ell = 2\sigma + b$.
- $\mathrm{rev}$ (bit-reversal map), bound on [Radix-two factorization](radix-two-factorization.md): The map sending an index $\ell$ with $0 \le \ell < q$ to the integer whose $\lg q$ binary digits are those of $\ell$ in reverse order.
- $\sigma$ (axis index), bound on [Multidimensional transform](multidimensional-transform.md): The index of one transform axis, an integer from 1 to D.
- $Y$ (output array), bound on [Multidimensional transform](multidimensional-transform.md): The array of values that the multidimensional transform produces from X.
- $\varrho$ (input position), bound on [Multidimensional transform](multidimensional-transform.md): A tuple of D coordinates labelling one position in the input array X.
- $\varpi$ (output position), bound on [Multidimensional transform](multidimensional-transform.md): A tuple of D coordinates labelling one position in the output array Y.
- $\mathcal{F}$ (multidimensional transform), bound on [Multidimensional transform](multidimensional-transform.md): The map sending the input array X to the output array Y by the multidimensional transform formula.
- $k$ (radix-two exponent), bound on [Multidimensional transform](multidimensional-transform.md): The exponent with t_sigma equal to 2^k, which counts the radix-two levels of the axis transform.
- $W$ (target length), bound on [Gaussian resampling](gaussian-resampling.md): The number of entries of the resampled vector, a power of two greater than $q$.
- $\sigma$ (Gaussian width), bound on [Gaussian resampling](gaussian-resampling.md): The width of the Gaussian weights, an integer at least 2 with $\sigma^2<p$.
- $k$ (output index), bound on [Gaussian resampling](gaussian-resampling.md): The index of an entry of a length-$W$ output vector, running from $0$ to $W-1$.
- $\Psi$ (first Gaussian map), bound on [Gaussian resampling](gaussian-resampling.md): The map sending a length-$q$ vector to a length-$W$ vector by Gaussian-weighted sums with weight $\exp(-\pi\sigma^{-2}(j-qk/W)^2)$.
- $\Xi$ (second Gaussian map), bound on [Gaussian resampling](gaussian-resampling.md): The map sending a length-$q$ vector to a length-$W$ vector by Gaussian-weighted sums with weight $\exp(-\pi\sigma^{2}(Wj/q-k)^2)$.
- $\mathcal{J}$ (selection map), bound on [Gaussian resampling](gaussian-resampling.md): The map that picks, for each $j<q$, the entry of a length-$W$ vector at the integer nearest $Wj/q$.
- $\Upsilon$ (diagonal correction), bound on [Gaussian resampling](gaussian-resampling.md): The diagonal map multiplying entry $j$ by the factor that cancels the weight of $\Xi$ at position $j$.
- $\mathcal{N}$ (middle map), bound on [Gaussian resampling](gaussian-resampling.md): The length-$q$ map $\mathcal J\,\Xi\,\Upsilon$, which is close to the identity.
- $\mathcal{X}$ (deviation from identity), bound on [Gaussian resampling](gaussian-resampling.md): The difference $I-\mathcal N$, whose norm is below one half.
- $\mathcal{E}$ (first contraction), bound on [Gaussian resampling](gaussian-resampling.md): The map $\Psi/2$ from length $q$ to length $W$, which is a contraction.
- $\mathcal{U}$ (second contraction), bound on [Gaussian resampling](gaussian-resampling.md): The map $2^{1-2\sigma^2}\,\Upsilon\mathcal N^{-1}\mathcal J$ from length $W$ to length $q$, which is a contraction.
- $\Pi_q$ (length-q coordinate permutation), bound on [Gaussian resampling](gaussian-resampling.md): The permutation of length-$q$ vectors whose $j$-th entry is entry $Wj \bmod q$ of the input.
- $\Pi_W$ (length-W coordinate permutation), bound on [Gaussian resampling](gaussian-resampling.md): The permutation of length-$W$ vectors whose $k$-th entry is entry $-qk \bmod W$ of the input.
- $\sigma_j$ (standard basis vector), bound on [Standard basis vector](standard-basis-vector.md): The vector of $F^m$ with entry $1$ at coordinate $j$ and $0$ at every other coordinate.
- $a$ (matrix rank), bound on [Matrix rank](matrix-rank.md): The rank of $A$ over the rationals, the number of linearly independent rows of $A$.
- $E_1$ (left lower triangular factor), bound on [Matrix rank](matrix-rank.md): An invertible lower triangular rational matrix, the left factor in $A = E_1 \Pi E_2$.
- $E_2$ (right lower triangular factor), bound on [Matrix rank](matrix-rank.md): An invertible lower triangular rational matrix, the right factor in $A = E_1 \Pi E_2$.
- $\Pi$ (partial permutation matrix), bound on [Matrix rank](matrix-rank.md): The matrix with at most one 1 in each row and column, whose number of ones is the rank $a$.
- $J$ (second field vector), bound on [Matrix rank](matrix-rank.md): The vector $(J_1, \ldots, J_m)$ of $m$ address fields, which the shear reads and leaves unchanged.
- $\gamma$ (first field value), bound on [Matrix rank](matrix-rank.md): The value of the field $H_i$ before one update.
- $\delta$ (second field value), bound on [Matrix rank](matrix-rank.md): The value of the field $J_j$ before one update.
- $W$ (wire count), bound on [Matrix rank](matrix-rank.md): The number of wires of the paper's circuit, including its scratch wires.
- $M_v$ (vertex matrix), bound on [Matrix rank](matrix-rank.md): The rational $m \times m$ matrix carried by the vertex $v$.
- $A_e$ (edge matrix), bound on [Matrix rank](matrix-rank.md): The difference of the matrices at the two ends of the edge $e$.
- $A_{ij}$ (matrix entry), bound on [Symmetric matrix](symmetric-matrix.md): The entry of the matrix $A$ in row $i$ and column $j$, an element of $F$.
- $A^{\top}$ (transpose), bound on [Symmetric matrix](symmetric-matrix.md): The matrix obtained from $A$ by exchanging rows and columns, whose entry in row $i$ and column $j$ is $A_{ji}$.
- $S$ (three-element subset), bound on [Symmetric matrix](symmetric-matrix.md): A three-element subset of a finite set, one of the two triples compared for neighbourhood.
- $T$ (three-element subset), bound on [Symmetric matrix](symmetric-matrix.md): A three-element subset of a finite set, the second triple compared with $S$.
- $V$ (vector space), bound on [Eigenvalue](eigenvalue.md): The vector space on which the linear operator T acts, over the field F.
- $\theta$ (eigenvalue), bound on [Eigenvalue](eigenvalue.md): A scalar for which T maps some nonzero vector e to the multiple theta e.
- $e$ (eigenvector), bound on [Eigenvalue](eigenvalue.md): A nonzero vector of V that T maps to a multiple of itself.
- $\mathbb{Q}$ (rational numbers), bound on [Eigenvalue](eigenvalue.md): The set of rational numbers.
- $h$ (coordinate count), bound on [Eigenvalue](eigenvalue.md): The number of coordinates of each vector in Q^h, at least 2.
- $\langle x,y\rangle$ (bilinear value), bound on [Eigenvalue](eigenvalue.md): The number that the bilinear form assigns to the pair of vectors x and y.
- $\mathsf{T}$ (transpose), bound on [Eigenvalue](eigenvalue.md): The transpose of a column vector x, the row with the same entries.
- $J$ (all-one matrix), bound on [Eigenvalue](eigenvalue.md): The h by h matrix with every entry equal to 1.
- $\mathbf{1}$ (all-ones vector), bound on [Eigenvalue](eigenvalue.md): The vector in Q^h with every entry equal to 1.
- $c$ (average entry), bound on [Eigenvalue](eigenvalue.md): The average of the entries of x, which is the coefficient of the all-ones vector in its split.
- $x_0$ (zero-sum part), bound on [Eigenvalue](eigenvalue.md): The part of x whose entries sum to zero in the split x = c 1 + x_0.
- $\langle x,y\rangle$ (bilinear form), bound on [Bilinear form](bilinear-form.md): The scalar in F that the form assigns to the vectors x and y of E.
- $U$ (subspace), bound on [Bilinear form](bilinear-form.md): A subspace of E whose orthogonal complement is taken.
- $U^\perp$ (orthogonal complement), bound on [Bilinear form](bilinear-form.md): The set of vectors of E orthogonal to every vector of U.
- $e_j$ (basis vector), bound on [Bilinear form](bilinear-form.md): The j-th vector of the fixed basis of E.
- $M^{\top}$ (transpose), bound on [Bilinear form](bilinear-form.md): The matrix obtained from M by swapping its rows and columns.
- $x_i$ (coordinate), bound on [Bilinear form](bilinear-form.md): The i-th coordinate of the vector x in the basis e_1 through e_m.
- $y_j$ (coordinate of y), bound on [Bilinear form](bilinear-form.md): The j-th coordinate of the vector y in the basis e_1 through e_m.
- $\Psi$ (form matrix), bound on [Bilinear form](bilinear-form.md): The m by m matrix whose entry in row i and column j is the form value of e_i and e_j.
- $[h]$ (index set), bound on [Bilinear form](bilinear-form.md): The set of the first h positive integers.
- $T$ (triple), bound on [Bilinear form](bilinear-form.md): A three-element subset of [h], one of the triples whose indicator vectors are used.
- $t_T$ (indicator vector), bound on [Bilinear form](bilinear-form.md): The 0-1 vector with entry 1 at each element of the triple T and 0 elsewhere.
- $S$ (second triple), bound on [Bilinear form](bilinear-form.md): A second three-element subset of [h], whose indicator vector is t_S.
- $X$ (vector space), bound on [Orthogonal complement](orthogonal-complement.md): A vector space over $F$ on which the bilinear form is defined.
- $\langle\cdot,\cdot\rangle$ (bilinear form), bound on [Orthogonal complement](orthogonal-complement.md): The bilinear form on $X$ whose value $\langle\xi,\eta\rangle$ defines orthogonality.
- $W$ (larger label), bound on [Orthogonal complement](orthogonal-complement.md): The larger of the two labels on an edge, which contains the smaller label $U$.
- $t_T$ (indicator vector), bound on [Indicator vector](indicator-vector.md): The indicator vector of the triple T: entry 1 at each position of T, entry 0 elsewhere.
- $S$ (triple), bound on [Indicator vector](indicator-vector.md): A single three-element subset of [h], one of the two triples in a neighbor pair.
- $T$ (triple), bound on [Indicator vector](indicator-vector.md): A single three-element subset of [h]; on the ground-set page T names all triples.
- $e$ (position), bound on [Indicator vector](indicator-vector.md): An element of the ground set [h], a position of the indicator vector.
- $J$ (all-ones matrix), bound on [Indicator vector](indicator-vector.md): The h by h matrix whose entries are all 1.
- $\mathbb{Q}$ (rational numbers), bound on [Indicator vector](indicator-vector.md): The field of rational numbers; Q^h is the set of h-tuples of them.
- $\sigma$ (triple choice), bound on [Line spanned by a vector](line-spanned-by-vector.md): An ordered choice of three triples, which indexes one label, its vector and its data banks.
- $u_\sigma$ (tensor vector), bound on [Line spanned by a vector](line-spanned-by-vector.md): The vector $t_{\sigma_1}\otimes t_{\sigma_2}\otimes t_{\sigma_3}$, a tensor product of three indicator vectors.
- $U_\sigma$ (triple label), bound on [Line spanned by a vector](line-spanned-by-vector.md): The line $\operatorname{span}\{u_\sigma\}$, the label attached to the choice $\sigma$.
- $X_\sigma$ (data bank X), bound on [Line spanned by a vector](line-spanned-by-vector.md): The data bank indexed by $\sigma$ that carries the label $U_\sigma$ between stages, starting at $U_\sigma$ and ending at $F$.
- $Y_\sigma$ (data bank Y), bound on [Line spanned by a vector](line-spanned-by-vector.md): The second data bank indexed by $\sigma$, paired with $X_\sigma$, starting at zero and ending at $U_\sigma^\perp$.
- $\langle\cdot,\cdot\rangle$ (bilinear form), bound on [Line spanned by a vector](line-spanned-by-vector.md): The bilinear form on $E$, linear in each argument, whose values decide orthogonality and nondegeneracy.
- $U$ (label), bound on [Subspace labels](subspace-labels.md): A label of a wire, a nondegenerate subspace of the fixed space E.
- $U'$ (smaller label), bound on [Subspace labels](subspace-labels.md): The smaller of the two labels joined by an edge.
- $C_U$ (label frame), bound on [Subspace labels](subspace-labels.md): The invertible operator on arrays carried by a vertex with label U.
- $\mathcal W$ (Hadamard matrix), bound on [Subspace labels](subspace-labels.md): The Hadamard matrix of order 2, which satisfies W^2 = I.
- $\mathrm{hw}$ (Hamming weight), bound on [Subspace labels](subspace-labels.md): The number of ones in a binary vector.
- $P_U$ (label projection), bound on [Subspace labels](subspace-labels.md): The projection onto the label U along its orthogonal complement U^perp, taken over F_2 for binary labels.
- $X_v$ (translation), bound on [Subspace labels](subspace-labels.md): The operator that shifts a function of addresses by the binary vector v.
- $\varpi$ (identity coefficient), bound on [Subspace labels](subspace-labels.md): The coefficient of the identity in a translation kernel.
- $\varsigma$ (translation coefficient), bound on [Subspace labels](subspace-labels.md): The coefficient of the translation in a translation kernel.
- $\varrho$ (residual dimension), bound on [Subspace labels](subspace-labels.md): The number of vectors in an orthonormal basis of an edge residual, which counts the kernels used on that edge.
- $v_s$ (basis vector), bound on [Subspace labels](subspace-labels.md): The s-th vector of an orthonormal basis of an edge residual.
- $s$ (basis index), bound on [Subspace labels](subspace-labels.md): An index numbering the basis vectors of an edge residual.
- $s'$ (second basis index), bound on [Subspace labels](subspace-labels.md): A second index numbering the basis vectors of an edge residual.
- $\mathcal T$ (triple set), bound on [Subset-intersection network](subset-intersection-network.md): The set of all three-element subsets of the ground set $[h]$, whose members are the triples.
- $\sigma$ (triple of triples), bound on [Subset-intersection network](subset-intersection-network.md): A tuple of three triples, which indexes the entries of a bank.
- $\xi$ (source vector), bound on [Subset-intersection network](subset-intersection-network.md): The vector, indexed by triples, of the entries of the source bank along the varying coordinate.
- $\eta$ (target vector), bound on [Subset-intersection network](subset-intersection-network.md): The vector, indexed by triples, of the entries of the target bank along the varying coordinate.
- $A_{ST}$ (side wire), bound on [Subset-intersection network](subset-intersection-network.md): The scratch wire attached to an ordered neighbouring pair of triples $(S,T)$.
- $C_\ell$ (central wire), bound on [Subset-intersection network](subset-intersection-network.md): The scratch wire attached to the element $\ell$ of the ground set.
- $\ell$ (ground element), bound on [Subset-intersection network](subset-intersection-network.md): An element of the ground set $[h]$, which names one central wire.
- $\mathbf p$ (label vector), bound on [Subset-intersection network](subset-intersection-network.md): A vector of the rational space $E$ on which the label form is defined.
- $\mathbf q$ (second label vector), bound on [Subset-intersection network](subset-intersection-network.md): A second vector of the rational space $E$, paired with $\mathbf p$ by the label form.
- $U'^{*}$ (dual space), bound on [Subset-intersection network](subset-intersection-network.md): The dual space of the smaller label $U'$, the space of linear functionals on $U'$.
- $x$ (control vector), bound on [Scratch storage](scratch-storage.md): The control vector, whose entry at triple $T$ is $x_T$.
- $y$ (target vector), bound on [Scratch storage](scratch-storage.md): The target vector, whose entry at triple $S$ is $y_S$.
- $a$ (starting side values), bound on [Scratch storage](scratch-storage.md): The vector of starting values of the side wires.
- $c$ (starting central values), bound on [Scratch storage](scratch-storage.md): The vector of starting values of the central wires.
- $V$ (copy), bound on [Scratch storage](scratch-storage.md): The operation that adds $x_T$ to $W_{ST}$ for each neighbouring pair.
- $J$ (side injection), bound on [Scratch storage](scratch-storage.md): The operation that adds to $y_S$ the side wires over the neighbours of $S$.
- $G$ (gather), bound on [Scratch storage](scratch-storage.md): The operation that adds $x_T$ to each central wire $C_\ell$ with $\ell\in T$.
- $R$ (scatter), bound on [Scratch storage](scratch-storage.md): The operation that adds to $y_S$ the central wires $C_\ell$ with $\ell\in S$.
- $\tau$ (fixed exponent), bound on [Address-field interchange](address-interchange.md): A fixed number below 1, the exponent in the cost bound $O(Vu^{\tau})$.
- $x$ (first field block), bound on [Address-field interchange](address-interchange.md): The bits of the first of the two address fields, read as a block at matching positions.
- $y$ (second field block), bound on [Address-field interchange](address-interchange.md): The bits of the second of the two address fields, read as a block at matching positions.
- $m$ (pieces per level), bound on [Address-field interchange](address-interchange.md): A fixed integer at least 2, the number of pieces each field is cut into at each level.
- $k$ (level count), bound on [Address-field interchange](address-interchange.md): The number of levels of the recursion, the logarithm to base m of the field width u.
- $s$ (smaller calls), bound on [Address-field interchange](address-interchange.md): The number of smaller calls one call makes, equal to the sum of the edge ranks.
- $\vartheta_j$ (time per unit volume), bound on [Address-field interchange](address-interchange.md): The time per unit volume of a call on width $m^j$, bounded by the recurrence above.
- $j$ (level index), bound on [Address-field interchange](address-interchange.md): The level of a call, so a call on width $m^j$ sits at level $j$.
- $\sigma$ (first bit), bound on [Exclusive or](xor.md): A bit, a value 0 or 1, the first operand of the exclusive or.
- $\sigma'$ (second bit), bound on [Exclusive or](xor.md): A bit, a value 0 or 1, the second operand of the exclusive or.
- $\langle\cdot,\cdot\rangle$ (bilinear form), bound on [Gram matrix](gram-matrix.md): The bilinear form on the vector space, whose values on pairs of vectors fill the Gram matrix.
- $\sigma$ (list length), bound on [Gram matrix](gram-matrix.md): The number of vectors in the list, which is the number of rows and columns of the Gram matrix.
- $\mathbf{v}_i$ (list vector), bound on [Gram matrix](gram-matrix.md): The i-th vector of the list, an element of the vector space.
- $\mathcal{G}$ (Gram matrix), bound on [Gram matrix](gram-matrix.md): The sigma-by-sigma matrix whose entry in row i and column j is the value of the form on the i-th and j-th vectors.
- $c_j$ (coefficient), bound on [Gram matrix](gram-matrix.md): The scalar coefficient of the j-th list vector in a vector of the span.
- $\mathrm{supp}$ (support), bound on [Complex phase network](complex-phase-network.md): The set of coordinates at which a binary vector is 1.
- $\mathrm{wt}$ (Hamming weight), bound on [Complex phase network](complex-phase-network.md): The number of coordinates at which a binary vector is 1, read as an integer.
- $[b]$ (integer representative), bound on [Complex phase network](complex-phase-network.md): The integer 0 or 1 that represents a field element b of the binary field.
- $H$ (normalized Hadamard matrix), bound on [Complex phase network](complex-phase-network.md): The 2 by 2 matrix whose tensor powers give the frames of the phase network.
- $q_U$ (phase exponent), bound on [Complex phase network](complex-phase-network.md): The phase exponent of an address x under label U, the Hamming weight of its projection modulo 4.
- $C_U$ (phase frame), bound on [Complex phase network](complex-phase-network.md): The frame of a vertex with label U, an operator on arrays of addresses.
- $P_W$ (projection onto W), bound on [Complex phase network](complex-phase-network.md): The projection onto a nondegenerate subspace W along its orthogonal complement.
- $\mathrm{diag}_x$ (diagonal operator), bound on [Complex phase network](complex-phase-network.md): The operator that multiplies the value at each address x by f(x).
- $U$ (tail label), bound on [Complex phase network](complex-phase-network.md): The label at the tail of an edge.
- $V$ (head label), bound on [Complex phase network](complex-phase-network.md): The label at the head of an edge.
- $\perp$ (orthogonal sum), bound on [Complex phase network](complex-phase-network.md): A B means that A and B are orthogonal subspaces meeting only in zero, with A+B their orthogonal sum.
- $\Delta$ (orthogonal residual), bound on [Complex phase network](complex-phase-network.md): The orthogonal complement of the smaller label of an edge inside the larger one.
- $\mathcal O$ (orthonormal basis), bound on [Complex phase network](complex-phase-network.md): An orthonormal basis of the orthogonal residual, a set of vectors v with v dot v equal to 1 that are pairwise orthogonal.
- $\varepsilon_v$ (edge sign), bound on [Complex phase network](complex-phase-network.md): The sign in {1, -1} that matches the weight of basis vector v on an edge, up to sign for the edge direction.
- $\tau_0$ (first kernel coefficient), bound on [Complex phase network](complex-phase-network.md): The complex number (1+i)/2, the diagonal coefficient of a two-point kernel.
- $\tau_1$ (second kernel coefficient), bound on [Complex phase network](complex-phase-network.md): The complex number (1-i)/2, the off-diagonal coefficient of a two-point kernel.
- $X_v$ (translation by v), bound on [Complex phase network](complex-phase-network.md): The operator sending a function f to (X_v f)(x) = f(x+v) on addresses.
- $K_v$ (two-point kernel), bound on [Complex phase network](complex-phase-network.md): The operator tau_0 I + tau_1 X_v, one factor of an edge change.
- $U_\delta$ (route label), bound on [Complex phase network](complex-phase-network.md): The label span(e_1, ..., e_delta) on the route from {0} to the full space.
- $e_\delta$ (standard basis vector), bound on [Complex phase network](complex-phase-network.md): The vector with a single 1 at position delta.
- $D$ (number of axes), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The number of transform axes that the layer acts on, one selected bit on each.
- $\delta$ (chunk width), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The number of consecutive address bits in each transform axis (chunk).
- $o$ (selected offset), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The position of the selected bit within its chunk, counted from the least significant end.
- $H_0$ (two-point map), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The two-point map $H_0(u,v)=((u+v)/2,(u-v)/2)$, as a $2\times2$ matrix.
- $F_q$ (length-q transform), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The discrete Fourier transform on $q$ values, normalized by $1/q$.
- $q$ (number of values), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The number of values that the transform $F_q$ acts on.
- $j$ (input index), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The index of an input value in the transform $F_q$.
- $k$ (output index), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The index of an output coordinate of the transform $F_q$.
- $\mathcal{H}$ (normalized Hadamard matrix), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The $2\times2$ Hadamard matrix with the $1/\sqrt2$ normalization.
- $\Delta$ (diagonal phase matrix), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The diagonal matrix $\mathrm{diag}(1,i)$.
- $X$ (bit-flip matrix), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The $2\times2$ matrix that swaps the two basis states of one bit.
- $I$ (identity matrix), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The $2\times2$ identity matrix.
- $\lambda$ (identity coefficient), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The coefficient of $I$ in $C$, equal to $(1+i)/2$.
- $\mu$ (bit-flip coefficient), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The coefficient of $X$ in $C$, equal to $(1-i)/2$.
- $C$ (two-point kernel), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The two-by-two operator $\mathcal H\Delta\mathcal H$, equal to $\lambda I+\mu X$.
- $\Delta_D$ (address phase operator), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The diagonal operator $\Delta^{\otimes D}$ that multiplies each address by $i$ to the number of selected bits equal to 1 there.
- $p$ (working precision), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The working precision in bits: the inputs lie on the grid $2^{-p}\mathbb Z[i]$.
- $s$ (number of H_0 factors), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The number of individual factors $H_0$ applied, which refines the grid to $2^{-(p+s)}$.
- $\Delta$ (guard width), bound on [Guard-width bound](guard-width-bound.md): The number of extra fractional and integer bits reserved per real component, which bounds the depth of every value.
- $u$ (first input value), bound on [Guard-width bound](guard-width-bound.md): The first of the two values that the two-point map combines.
- $v$ (second input value), bound on [Guard-width bound](guard-width-bound.md): The second of the two values that the two-point map combines.
- $d$ (axis bound), bound on [Guard-width bound](guard-width-bound.md): A bound on the number D of selected bits in a layer, so that D is at most d.
- $\ell$ (depth), bound on [Guard-width bound](guard-width-bound.md): The number of operations on a chain that follows an operand from an input into a value.
- $m$ (splitting factor), bound on [Guard-width bound](guard-width-bound.md): The factor by which a call divides the axis count.
- $e$ (group size), bound on [Guard-width bound](guard-width-bound.md): The number of selected axes in a group that the recursion splits.
- $A$ (depth bound), bound on [Guard-width bound](guard-width-bound.md): The bound on the number of operations on any chain within a group, as a function of its size.
- $E$ (gate budget), bound on [Guard-width bound](guard-width-bound.md): The most gate operations charged at a node of the recursion.
- $k$ (internal levels), bound on [Guard-width bound](guard-width-bound.md): The number of internal levels of the recursion.
- $B$ (level factor), bound on [Guard-width bound](guard-width-bound.md): The growth factor $s+E$ that each recursion level multiplies a bound by.
- $x$ (real bound), bound on [Guard-width bound](guard-width-bound.md): A real number at least one, used as a generic bound in the level inequality.
- $\nu$ (exponent), bound on [Guard-width bound](guard-width-bound.md): The least positive integer $j$ with $m^j\ge B$.
- $t$ (shift count), bound on [Guard-width bound](guard-width-bound.md): The number of places a shift moves, equal to $\lfloor D/2\rfloor$.
- $\lfloor$ (floor), bound on [Guard-width bound](guard-width-bound.md): The largest integer not exceeding its argument.
- $C_0$ (depth constant), bound on [Guard-width bound](guard-width-bound.md): The constant $128mB^2$ in the depth bound $C_0d^{C_1}$.
- $C_1$ (depth exponent), bound on [Guard-width bound](guard-width-bound.md): The exponent $\max\{20,
u+3\}$ of $d$ in the depth bound.
- $\varepsilon$ (growth exponent), bound on [Guard-width bound](guard-width-bound.md): The exponent in $d=\Theta(p^{arepsilon})$, chosen so that $arepsilon C_1<1$.
- $d$ (selected-bit bound), bound on [Numerical layer](numerical-layer.md): An upper bound on the number $D$ of selected bits, so that $D \le d$.
- $e$ (selected axis count), bound on [Numerical layer](numerical-layer.md): The number of selected axes that a call acts on.
- $m$ (division factor), bound on [Numerical layer](numerical-layer.md): The fixed integer by which a call divides its number of selected axes.
- $s$ (smaller-call count), bound on [Numerical layer](numerical-layer.md): The number of smaller calls that one call makes.
- $\lambda'$ (cost exponent), bound on [Numerical layer](numerical-layer.md): A fixed exponent below one in the layer cost $O(V d^{\lambda'})$.
- $\log_m$ (base-m logarithm), bound on [Numerical layer](numerical-layer.md): The exponent to which $m$ must be raised to give $x$.
- $\omega$ (outcome), bound on [Union bound](union-bound.md): An element of the outcome set Ω, one possible outcome.
- $\mathcal{X}$ (finite set), bound on [Union bound](union-bound.md): A generic finite set, whose elements are counted by |X|.
- $|\mathcal{X}|$ (set size), bound on [Union bound](union-bound.md): The number of elements of the finite set X.
- $E_i$ (event), bound on [Union bound](union-bound.md): The i-th event, a subset of Ω; for the guards it is the set of addresses whose i-th guard is bad.
- $m$ (event count), bound on [Union bound](union-bound.md): The number of events E_1 through E_m.
- $i$ (event index), bound on [Union bound](union-bound.md): An index numbering the events, running from 1 to m.
- $c(\omega)$ (containing-event count), bound on [Union bound](union-bound.md): The number of indices i for which the outcome ω lies in E_i.
- $f$ (selected bit count), bound on [Union bound](union-bound.md): The number of selected bit positions of the addition.
- $K$ (segment width), bound on [Union bound](union-bound.md): The number of consecutive bits in each segment.
- $y$ (address chunk y), bound on [Union bound](union-bound.md): One of the two chunks of each address, a block of its coordinates.
- $z$ (address chunk z), bound on [Union bound](union-bound.md): The other of the two chunks of each address.
- $g_i$ (guard value of y-segment), bound on [Union bound](union-bound.md): The integer formed by the upper K-1 bits of the i-th segment of y.
- $h_i$ (guard value of z-segment), bound on [Union bound](union-bound.md): The analogous guard value formed from the i-th segment of z.
- $\delta_{\mathrm{bad}}$ (capped bad bound), bound on [Union bound](union-bound.md): The bound min{1, 80(f-1)/2^K} on the bad fraction, capped at one.
- $D$ (participating axis count), bound on [Transform round](transform-round.md): The number of participating axes, the axes that take a butterfly step in the round.
- $i$ (axis index), bound on [Transform round](transform-round.md): An index naming one of the participating axes.
- $\ell_i$ (current axis length), bound on [Transform round](transform-round.md): The current recursive length of axis i: the number of entries it holds at the level processed.
- $\beta_i$ (branch bit), bound on [Transform round](transform-round.md): The branch bit, 0 or 1, that the round writes on axis i.
- $\nu_i$ (twiddle index), bound on [Transform round](transform-round.md): The twiddle index on axis i, an integer from 0 to the half length minus one.
- $h$ (highest unprocessed bit), bound on [Transform round](transform-round.md): The position of the highest unprocessed address bit on axis i, which receives the branch bit.
- $x_v$ (address bit), bound on [Transform round](transform-round.md): The bit of axis i in still unprocessed slot v.
- $\omega_\ell$ (root of unity), bound on [Transform round](transform-round.md): The root $y^{2r/\ell}$, a primitive $\ell$-th root of unity in the polynomial ring.
- $\eta$ (twiddle exponent), bound on [Transform round](transform-round.md): The exponent of y at an address, so that the round multiplies each record by y to the power eta.
- $e$ (quotient), bound on [Transform round](transform-round.md): The integer quotient of eta by r: the number of whole multiples of r in eta.
- $\delta$ (remainder), bound on [Transform round](transform-round.md): The remainder of eta on division by r, from 0 to r minus 1.
- $c_j$ (coefficient), bound on [Transform round](transform-round.md): The coefficient of y to the power j in a record.
- $\mathcal{B}$ (parallel butterfly), bound on [Transform round](transform-round.md): The operator that applies H_0 on every participating axis.
- $\mathcal{M}_\eta$ (monomial operation), bound on [Transform round](transform-round.md): The operator that multiplies each record by y to the power eta at its address.
- $d$ (chunk count bound), bound on [Tape procedure](tape-procedure.md): An upper bound on the number of equal-width address chunks whose selected bits one pass handles.
- $A_e$ (edge matrix), bound on [Bit procedure](bit-procedure.md): The matrix attached to edge e, the difference of the matrices at its endpoints.
- $\oplus$ (exclusive or), bound on [Bit procedure](bit-procedure.md): Addition over the binary field, applied bit by bit.
- $\theta$ (capped log exponent), bound on [Bit procedure](bit-procedure.md): The capped logarithm max(0, log_m(s/W)) of s/W, which is below tau.
- $\mathcal{E}_\ell$ (role endpoint operator), bound on [Endpoint operator](endpoint-operator.md): The operator $D_{\mathrm{sink}(\rho(\ell))}D_{\mathrm{source}(\ell)}^{-1}$ that the frames at the ends of the route of role $\ell$ give to its array.
- $q$ (radix), bound on [Address shear](address-shear.md): A fixed odd prime, the radix in which each digit of a field is written.
- $b$ (digits per field), bound on [Address shear](address-shear.md): The number of radix-$q$ digits in each field, so it counts digits.
- $M'$ (second matrix), bound on [Address shear](address-shear.md): Another rational $m\times m$ matrix, whose shear is composed with that of $M$.
- $e$ (chunk digit count), bound on [Address shear](address-shear.md): The number of digits in a chunk at recursion depth $k$, equal to $m^k$.
- $F_k$ (time per unit volume), bound on [Address shear](address-shear.md): The time per unit volume at recursion depth $k$.
- $M$ (record count), bound on [Stable radix sort](stable-radix-sort.md): The number of records in the full stream, a count of records, so every rank is an integer from 0 to M-1.
- $w$ (key width), bound on [Stable radix sort](stable-radix-sort.md): The number of bits in each key, a count of bits, which is also the number of passes.
- $q$ (record key), bound on [Stable radix sort](stable-radix-sort.md): The key of a record, a string of w bits written as q_{w-1} through q_0.
- $q_t$ (key bit), bound on [Stable radix sort](stable-radix-sort.md): The bit of the key at position t, which is 0 or 1 and has weight 2^t.
- $t$ (bit position), bound on [Stable radix sort](stable-radix-sort.md): A bit position of the key, counted from 0 at the least significant bit, which also indexes the pass that sorts by that bit.
- $A_{\mathrm{rect}}$ (size parameter), bound on [Stable radix sort](stable-radix-sort.md): The paper's size parameter for its integers, which bounds the number of bits in the destination keys.
- $\Psi$ (address), bound on [Destination rank](destination-rank.md): The address of a record, given by its three chunk values $\Psi_1$, $\Psi_2$, $\Psi_3$.
- $\Psi'$ (destination address), bound on [Destination rank](destination-rank.md): The destination address of the record at $\Psi$, the address to which it moves.
- $\operatorname{rank}$ (rank), bound on [Destination rank](destination-rank.md): The position of the record at an address among the records in stream order, counted from 0.
- $\sigma$ (chunk stride), bound on [Destination rank](destination-rank.md): The amount the rank changes when a chunk rises by one with the other two fixed; $\sigma_1$, $\sigma_2$, $\sigma_3$ are the strides of chunks 1, 2 and 3.
- $\mathcal{E}$ (exceptional addresses), bound on [Destination rank](destination-rank.md): The set of addresses whose records the correction moves.
- $\Xi$ (correction), bound on [Destination rank](destination-rank.md): The permutation of addresses by which the correction moves records.
- $T_0$ (ideal permutation), bound on [Destination rank](destination-rank.md): The permutation of addresses that the packed addition should perform.
- $S_0$ (packed approximation), bound on [Destination rank](destination-rank.md): The packed addition that agrees with the ideal permutation $T_0$ off the exceptional addresses.
- $R$ (payload bits), bound on [Destination rank](destination-rank.md): The number of payload bits in each record.
- $V$ (stream bit count), bound on [Destination rank](destination-rank.md): The number of bits in the stream, $MR$.
- $F_s$ (Fourier transform), bound on [Transform identity with retained permutations](transform-identity.md): The normalized discrete Fourier transform of length $s$, applied to vectors of length $s$.
- $F_t$ (Fourier transform), bound on [Transform identity with retained permutations](transform-identity.md): The normalized discrete Fourier transform of length $t$.
- $\Pi$ (coordinate permutation), bound on [Transform identity with retained permutations](transform-identity.md): A permutation that rearranges the entries of a vector by their positions.
- $\Pi_c$ (retained permutation), bound on [Transform identity with retained permutations](transform-identity.md): The permutation of entries of a length-$s$ vector that sends position $j$ to position $cj$ modulo $s$.
- $c$ (unit multiplier), bound on [Transform identity with retained permutations](transform-identity.md): A unit modulo $s$ that defines the retained permutation $\Pi_c$.
- $\chi$ (inverse of t), bound on [Transform identity with retained permutations](transform-identity.md): An integer with $\chi t\equiv 1 \pmod s$, so it inverts $t$ modulo $s$.
- $j'$ (second position), bound on [Transform identity with retained permutations](transform-identity.md): A second position in $\{0,\dots,s-1\}$, compared with $j$.
- $u'$ (second vector), bound on [Transform identity with retained permutations](transform-identity.md): A second vector of length $s$, paired with $u$ in a pointwise product.
- $A$ (linear contraction), bound on [Transform identity with retained permutations](transform-identity.md): A linear map from $\mathbb{C}^s$ to $\mathbb{C}^t$ in the lemma.
- $B_0$ (linear contraction), bound on [Transform identity with retained permutations](transform-identity.md): A linear map from $\mathbb{C}^t$ to $\mathbb{C}^s$ in the lemma.
- $\Psi$ (generic linear map), bound on [Transform identity with retained permutations](transform-identity.md): A generic linear map, used to define contractions.
- $\theta$ (relative gap), bound on [Transform identity with retained permutations](transform-identity.md): The ratio $t/s$ minus one, which the lemma requires to exceed $p/\alpha^4$.
- $\Upsilon$ (left inverse of Gamma), bound on [Transform identity with retained permutations](transform-identity.md): A linear map with $\Upsilon\Gamma=I$, built from $N^{-1}$ and a diagonal scaling.
- $\mathcal{L}$ (transform layout), bound on [Transform layout](transform-layout.md): The permutation of record addresses that places the selected bits of the participating axes at one common offset.
- $D$ (participating axis count), bound on [Transform layout](transform-layout.md): The number of participating axes of a round, which is the number of chunks that share one offset.
- $K$ (chunk width), bound on [Transform layout](transform-layout.md): The number of consecutive address bits in each chunk.
- $\upsilon$ (chunk offset), bound on [Transform layout](transform-layout.md): The position of the selected bit within its chunk, counted from the least significant end.
- $\varsigma$ (round bit position), bound on [Transform layout](transform-layout.md): The position, counted from the least significant end, of the bit on which a round acts.
- $\mathbf{x}$ (box address), bound on [Padded transform box](padded-transform-box.md): An address naming one entry of the box, with axis coordinates $x_1,\dots,x_D$.
- $W_s$ (valid length), bound on [Padded transform box](padded-transform-box.md): The number of data entries along axis $s$, the valid length of that axis.
- $A_s$ (axis forward map), bound on [Padded transform box](padded-transform-box.md): The one-dimensional forward map of axis $s$, from length-$W_s$ to length-$t_s$ vectors.
- $B_{0,s}$ (axis backward map), bound on [Padded transform box](padded-transform-box.md): The one-dimensional backward map of axis $s$, from length-$t_s$ to length-$W_s$ vectors.
- $\sigma$ (coordinate index), bound on [Cyclic coordinate](cyclic-coordinate.md): An integer from 1 to d that names one coordinate of the array.
- $n_\sigma$ (cyclic length), bound on [Cyclic coordinate](cyclic-coordinate.md): The number of positions along coordinate sigma before its indices wrap around.
- $\varkappa$ (shortened-coordinate count), bound on [Cyclic coordinate](cyclic-coordinate.md): The number of coordinates whose length is r/2 in the padded box.
- $T$ (box size), bound on [Cyclic coordinate](cyclic-coordinate.md): The number of entries of the padded box, a power of two; on this page only, not the three-element subsets of other pages.
- $\upsilon$ (twist position), bound on [Cyclic coordinate](cyclic-coordinate.md): An integer position from 0 to r-1 on the last coordinate, at which the phase twist acts.
- $\upsilon'$ (second position), bound on [Cyclic coordinate](cyclic-coordinate.md): A second position on the last coordinate, paired with upsilon in a sum.
- $\upsilon''$ (reduced position), bound on [Cyclic coordinate](cyclic-coordinate.md): The position in the range from 0 to r-1 that equals the sum of upsilon and upsilon' minus r when the sum wraps.
- $\rho$ (prime), bound on [Prime number](prime-number.md): A prime number, the integer whose divisors are classified.
- $\sigma$ (second prime), bound on [Prime number](prime-number.md): A second prime number, distinct from rho.
- $\xi$ (divisor), bound on [Prime number](prime-number.md): A positive integer that divides another integer.
- $\eta$ (cofactor), bound on [Prime number](prime-number.md): The integer that multiplies the divisor to give the integer being divided.
- $\Upsilon$ (logical bit volume), bound on [Logical bit volume](logical-bit-volume.md): The number of bits in a padded transform box, counting every entry at its record width.
- $Q$ (entry count), bound on [Logical bit volume](logical-bit-volume.md): The number of entries in the padded transform box.
- $\chi$ (record width), bound on [Logical bit volume](logical-bit-volume.md): The number of bits in one record of the padded transform box.
- $V$ (paper's bit volume), bound on [Logical bit volume](logical-bit-volume.md): The paper's name for the same count of bits as the logical bit volume.
- $b$ (bit length), bound on [Cost table](cost-table.md): The rounded-up base-2 logarithm of $n$, which counts the bits of $n$.
- $T$ (padded cell count), bound on [Cost table](cost-table.md): The number of cells of the padded box, a power of two in $[4n/b, 8n/b)$.
- $d$ (axis count), bound on [Cost table](cost-table.md): The number of axes of the padded box.
- $K$ (chunk width), bound on [Cost table](cost-table.md): The number of bits in each address chunk.
- $\ell$ (axis exponent), bound on [Cost table](cost-table.md): The exponent with $r = 2^{\ell}$, which counts the factors of two in $r$.
- $\epsilon$ (dimension exponent), bound on [Cost table](cost-table.md): A fixed positive exponent, equal to $2^{-75}$.
- $c$ (chunk exponent), bound on [Cost table](cost-table.md): A fixed positive exponent, equal to $2^{-56}$.
- $\tau$ (exchange exponent), bound on [Cost table](cost-table.md): The exponent $1-2^{-50}$ in the cost of a chunk exchange.
- $\lambda'$ (round exponent), bound on [Cost table](cost-table.md): The exponent $1-2^{-54}$ in the cost of a simultaneous round.
- $\delta$ (small exponent), bound on [Cost table](cost-table.md): A fixed small exponent, equal to $1/16$.
- $\alpha$ (line-map factor), bound on [Cost table](cost-table.md): The factor that scales the cost of the line maps.
- $N$ (input bit length), bound on [Established O(n log n) multiplier](established-multiplier.md): The number of bits in each input of the multiplier, the count of input bits.
- $f$ (integer polynomial), bound on [Signed coefficient packing](signed-packing.md): The first factor, an integer polynomial in $y$ with $r$ coefficients.
- $g$ (integer polynomial), bound on [Signed coefficient packing](signed-packing.md): The second factor, an integer polynomial in $y$ with $r$ coefficients.
- $f_j$ (coefficient of f), bound on [Signed coefficient packing](signed-packing.md): The integer coefficient of $y^j$ in $f$.
- $g_j$ (coefficient of g), bound on [Signed coefficient packing](signed-packing.md): The integer coefficient of $y^j$ in $g$.
- $p$ (coefficient bit bound), bound on [Signed coefficient packing](signed-packing.md): The number of bits in a bound on the coefficient magnitudes, so that each coefficient has absolute value at most $2^p$.
- $h$ (ordinary product), bound on [Signed coefficient packing](signed-packing.md): The ordinary product $fg$ of the two integer polynomials.
- $h_j$ (coefficient of h), bound on [Signed coefficient packing](signed-packing.md): The integer coefficient of $y^j$ in $h$.
- $B$ (block base), bound on [Signed coefficient packing](signed-packing.md): The block base $2^{4p}$, the value substituted for $y$ and the modulus of the congruence used for recovery.
- $\sigma$ (centered residue), bound on [Signed coefficient packing](signed-packing.md): The unique integer in $[-B/2, B/2)$ congruent to $f(B)\,g(B)$ modulo $B$.
- $\sigma$ (bit position), bound on [Schoolbook multiplication](schoolbook-multiplication.md): An integer from 0 to n-1 giving the position of a bit of y, counted from the least significant end.
- $y_\sigma$ (bit of y), bound on [Schoolbook multiplication](schoolbook-multiplication.md): The bit of y at position sigma, which is 0 or 1.
- $\zeta_\sigma$ (partial product), bound on [Schoolbook multiplication](schoolbook-multiplication.md): The copy of x shifted left by sigma places when y_sigma is 1, and 0 when y_sigma is 0.
- $\varphi$ (input array), bound on [Convolution over the polynomial ring](polynomial-ring-convolution.md): The first input array of records; $\varphi_a$ is its record at address $a$.
- $\psi$ (second input array), bound on [Convolution over the polynomial ring](polynomial-ring-convolution.md): The second input array of records; $\psi_b$ is its record at address $b$.
- $a$ (record address), bound on [Convolution over the polynomial ring](polynomial-ring-convolution.md): An address of the first input array, which indexes its records.
- $b$ (record address), bound on [Convolution over the polynomial ring](polynomial-ring-convolution.md): An address of the second input array, which indexes its records.
- $t_i$ (axis length), bound on [Convolution over the polynomial ring](polynomial-ring-convolution.md): The length of axis $i$, the number of positions on that axis.
- $\mu$ (record count), bound on [Convolution over the polynomial ring](polynomial-ring-convolution.md): The number of records in an array, the product of the axis lengths.
- $\omega_t$ (axis root of unity), bound on [Convolution over the polynomial ring](polynomial-ring-convolution.md): A root of unity of order $t$ on an axis of length $t$, equal to $y^{2r/t}$.
- $\hat{u}$ (forward transform), bound on [Convolution over the polynomial ring](polynomial-ring-convolution.md): The forward transform of an array $u$, with entries $\hat u_j$.
- $\check{u}$ (opposite transform), bound on [Convolution over the polynomial ring](polynomial-ring-convolution.md): The opposite transform of an array $u$, with entries $\check u_c$.
- $j$ (frequency address), bound on [Convolution over the polynomial ring](polynomial-ring-convolution.md): An integer index of a transform entry, one entry per axis.
- $k$ (summation index), bound on [Convolution over the polynomial ring](polynomial-ring-convolution.md): The index of the sum on an axis, running over the $t$ positions of that axis.
- $\star$ (normalized convolution), bound on [Convolution over the polynomial ring](polynomial-ring-convolution.md): The convolution of two arrays divided by $r\mu$, the product of the record length and the record count.
- $\odot$ (entrywise product), bound on [Convolution over the polynomial ring](polynomial-ring-convolution.md): The product of two arrays entry by entry, divided by the record length $r$.
- $\varphi_1$ (real integer polynomial), bound on [Convolution over the polynomial ring](polynomial-ring-convolution.md): The integer polynomial of degree less than $r$ whose $2^{-p}$-scaled value is the real part of $\varphi$.
- $\varphi_2$ (imaginary integer polynomial), bound on [Convolution over the polynomial ring](polynomial-ring-convolution.md): The integer polynomial of degree less than $r$ whose $2^{-p}$-scaled value is the imaginary part of $\varphi$.
- $\psi_1$ (real part of psi), bound on [Convolution over the polynomial ring](polynomial-ring-convolution.md): The integer polynomial of degree less than $r$ whose $2^{-p}$-scaled value is the real part of $\psi$.
- $\psi_2$ (imaginary part of psi), bound on [Convolution over the polynomial ring](polynomial-ring-convolution.md): The integer polynomial of degree less than $r$ whose $2^{-p}$-scaled value is the imaginary part of $\psi$.
- $\ell$ (record length exponent), bound on [Convolution over the polynomial ring](polynomial-ring-convolution.md): The integer exponent with $r=2^\ell$, the base-two logarithm of the record length.
- $\circledast$ (normalized cyclic convolution), bound on [Normalized cyclic convolution](normalized-cyclic-convolution.md): The cyclic convolution divided by the sequence length $s$, so $f \circledast g = \frac{1}{s}(f \ast g)$.
- $\cdot$ (entrywise product), bound on [Normalized cyclic convolution](normalized-cyclic-convolution.md): The product of two vectors taken position by position.
- $j'$ (second input index), bound on [Normalized cyclic convolution](normalized-cyclic-convolution.md): The position of an entry of $g$ paired with the position $j$ of $f$ in the sum for a transform entry.
- $m$ (chirp argument), bound on [Normalized cyclic convolution](normalized-cyclic-convolution.md): A free integer at which the chirp phase $\chi_m$ is evaluated; this letter changes meaning here and is not the order of a root.
- $\sigma$ (chirp position), bound on [Bluestein's chirp identity](bluestein-chirp-identity.md): An integer position at which the chirp is evaluated, which may be negative or at least $q$.
- $\hat u$ (scaled input), bound on [Bluestein's chirp identity](bluestein-chirp-identity.md): The vector $u$ with each coordinate divided by its chirp entry.
- $\ast$ (cyclic convolution), bound on [Bluestein's chirp identity](bluestein-chirp-identity.md): The cyclic convolution of two length-$q$ sequences, with indices taken modulo $q$.
- $\cdot$ (coordinatewise product), bound on [Bluestein's chirp identity](bluestein-chirp-identity.md): The product of two vectors taken entry by entry.
- $\sigma$ (digit scale), bound on [Normalization scales](normalization-scales.md): The factor $2^{-b-2}$ by which each digit is scaled, so that a stored value is $\sigma$ times its digit.
- $\hat f$ (first digit array), bound on [Normalization scales](normalization-scales.md): The integer array of digits of the first input, with entries from $0$ to $2^b-1$.
- $\hat g$ (second digit array), bound on [Normalization scales](normalization-scales.md): The integer array of digits of the second input, with entries from $0$ to $2^b-1$.
- $m$ (digit count), bound on [Normalization scales](normalization-scales.md): The number of digits of each input, which is also the number of entries of each digit array.
- $\mathcal M_t$ (middle transform), bound on [Middle transform](middle-transform.md): The operator on vectors of length $t$ whose $k$-th output is the $(-sk \bmod t)$-th output of the normalized Fourier transform $F_t$.
- $\varsigma$ (chirp factor), bound on [Middle transform](middle-transform.md): The unit complex number $\varsigma_j=\exp(-\pi i s j^2/t)$ attached to each integer $j$.
- $\zeta$ (twist root), bound on [Phase twist](phase-twist.md): The root of unity $e^{\pi i/r}$ of order $2r$, whose powers multiply the coefficients in the twist.
- $e$ (Euler's number), bound on [Phase twist](phase-twist.md): The base of the natural exponential, so that $e^{i\theta} = \cos\theta + i\sin\theta$.
- $j$ (record position), bound on [Phase twist](phase-twist.md): The position of a coefficient in a record, counted from 0 to r-1; on this page it replaces the convolution's input index.
- $j_1$ (first coefficient position), bound on [Phase twist](phase-twist.md): The position of the first of the two coefficients being multiplied.
- $j_2$ (second coefficient position), bound on [Phase twist](phase-twist.md): The position of the second of the two coefficients being multiplied.
- $b$ (bit length), bound on [Prime source lengths](prime-source-lengths.md): The number of binary digits of $n$, $b=\lceil\log_2 n\rceil$.
- $T$ (padded box size), bound on [Prime source lengths](prime-source-lengths.md): The number of cells of the padded box, the product of the axis lengths.
- $i$ (axis index), bound on [Prime source lengths](prime-source-lengths.md): The index of an axis, running from 1 to $d$.
- $\epsilon$ (size exponent), bound on [Prime source lengths](prime-source-lengths.md): A fixed constant exponent that sets the number of axes, $d=\lfloor b^{\epsilon}\rfloor$.
- $u$ (longest axis length), bound on [Prime source lengths](prime-source-lengths.md): The common length of the longest axes, a power of two, $u=2^\ell$.
- $w$ (short axis count), bound on [Prime source lengths](prime-source-lengths.md): The number of axes whose length is $u/2$.
- $p$ (working precision), bound on [Prime source lengths](prime-source-lengths.md): The working precision in bits, $p=6b$.
- $\eta$ (slack fraction), bound on [Prime source lengths](prime-source-lengths.md): The slack fraction of the prime-interval bound, $\eta=1/(4d)$ on this page.
- $\xi$ (real scale), bound on [Prime source lengths](prime-source-lengths.md): The real point at which the prime-interval bound is applied.
- $h_p$ (last-place unit), bound on [Exact coefficient recovery](recovery-and-error.md): The size $2^{-p}$ of one unit in the last place of a value with $p$ fractional bits.
- $m$ (nearest integer), bound on [Exact coefficient recovery](recovery-and-error.md): The integer nearest to a computed value that lies within $1/2$ of it.
- $\mathcal{B}$ (bilinear map), bound on [Exact coefficient recovery](recovery-and-error.md): The bilinear map whose approximate products are bounded.
- $f'$ (approximate first operand), bound on [Exact coefficient recovery](recovery-and-error.md): The computed approximation of the first operand $f$.
- $g'$ (approximate second operand), bound on [Exact coefficient recovery](recovery-and-error.md): The computed approximation of the second operand $g$.
- $E_s$ (source-transform error), bound on [Exact coefficient recovery](recovery-and-error.md): The error bound, in units of $h_p$, of each source transform, equal to $9\cdot2^\gamma T\log_2T$.
- $E_{\rm ring}$ (ring-stage error), bound on [Exact coefficient recovery](recovery-and-error.md): The error bound, in units of $h_p$, of the polynomial-ring convolution stage.
- $E_{\varpi}$ (scaled product error), bound on [Exact coefficient recovery](recovery-and-error.md): The error bound, in units of $h_p$, of the first scaled product $\tilde\varpi$.
- $\tilde\varpi$ (computed digit convolution), bound on [Exact coefficient recovery](recovery-and-error.md): The computed approximation of the normalized digit convolution $\varpi$.
- $\gamma$ (construction constant), bound on [Exact coefficient recovery](recovery-and-error.md): The construction constant of the source, $2d\alpha^2$.
- $d$ (number of axes), bound on [Exact coefficient recovery](recovery-and-error.md): The number of axes of the padded box, equal to $\lfloor b^{\epsilon}\rfloor$.
- $\alpha$ (construction factor), bound on [Exact coefficient recovery](recovery-and-error.md): The ceiling of $(12d^2b)^{1/4}$, the parameter $\alpha$ in the constant $\gamma$.
- $\varpi$ (normalized digit convolution), bound on [Exact coefficient recovery](recovery-and-error.md): The convolution of the two scaled digit arrays divided by $S$.
- $w$ (paper's digit convolution), bound on [Exact coefficient recovery](recovery-and-error.md): The paper's name for the normalized digit convolution $\varpi$.
- $\Xi_1$ (first procedure), bound on [Schedule](schedule.md): The first of three tape procedures in the example schedule, the one applied first.
- $\Xi_2$ (second procedure), bound on [Schedule](schedule.md): The second of three tape procedures in the example schedule, applied after the first.
- $\Xi_3$ (third procedure), bound on [Schedule](schedule.md): The third of three tape procedures in the example schedule, applied last.
- $h$ (ground set size), bound on [Bit construction](bit-construction.md): The number of elements in the ground set $[h]$, which is 100 here.
- $\mathcal{K}$ (set of triples), bound on [Bit construction](bit-construction.md): The set of all three-element subsets of the ground set $[h]$.
- $S$ (triple), bound on [Bit construction](bit-construction.md): A member of $\mathcal K$, that is, a three-element subset of $[h]$.
- $T$ (triple), bound on [Bit construction](bit-construction.md): A member of $\mathcal K$, that is, a three-element subset of $[h]$.
- $t_T$ (indicator vector), bound on [Bit construction](bit-construction.md): The 0-1 vector of length $h$ whose entries are 1 exactly at the elements of the triple $T$.
- $z_b$ (neighbour count), bound on [Bit construction](bit-construction.md): The number of neighbours of a fixed triple $T$, which is the number of triples meeting $T$ in exactly one element.
- $X$ (source bank), bound on [Bit construction](bit-construction.md): The bank of scalars with one entry $\xi_T$ per triple, which the invocation reads.
- $Y$ (target bank), bound on [Bit construction](bit-construction.md): The bank of scalars with one entry $\eta_S$ per triple, which the invocation updates.
- $\xi_T$ (source entry), bound on [Bit construction](bit-construction.md): The scalar entry of the source bank $X$ indexed by the triple $T$.
- $\eta_S$ (target entry), bound on [Bit construction](bit-construction.md): The scalar entry of the target bank $Y$ indexed by the triple $S$.
- $W_{ST}$ (side wire), bound on [Bit construction](bit-construction.md): The scratch wire carrying one scalar for each neighbour pair $(S,T)$.
- $C_\ell$ (central wire), bound on [Bit construction](bit-construction.md): The scratch wire carrying one scalar for each ground element $\ell$.
- $\binom{n}{k}$ (binomial coefficient), bound on [Bit construction](bit-construction.md): The number of $k$-element subsets of an $n$-element set.
- $t_S$ (triple indicator vector), bound on [Complex construction](complex-construction.md): The indicator vector of the triple S, the 0-1 vector with a one in each position of S.
- $C_*$ (extra central wire), bound on [Complex construction](complex-construction.md): The extra central wire that gathers the sum of all source values.
- $\varpi_{ST}$ (central coefficient), bound on [Complex construction](complex-construction.md): The central coefficient of x_T in y_S, equal to (|S ∩ T| − 1)/2.
- $W_c$ (total wire count), bound on [Complex construction](complex-construction.md): The total number of wires in the complex construction.
- $s_c$ (smaller-call count), bound on [Complex construction](complex-construction.md): The total number of smaller calls, the recursive calls made on the edges.
- $N$ (bank entry count), bound on [Complex construction](complex-construction.md): The number of entries in each data bank, v^3.
- $I$ (invocation count), bound on [Complex construction](complex-construction.md): The number of invocations, 3v^2.
- $v$ (triple count), bound on [Complex construction](complex-construction.md): The number of triples, the binomial coefficient of h choose 3.
- $z_c$ (neighbour count), bound on [Complex construction](complex-construction.md): The number of neighbours of a fixed triple in the complex construction.
- $c_c$ (central wire count), bound on [Complex construction](complex-construction.md): The number of central wires in each invocation of the complex construction.
- $m$ (label dimension), bound on [Complex construction](complex-construction.md): The dimension of the label space, h^3.
- $L_c$ (dimension lost), bound on [Complex construction](complex-construction.md): The dimension lost on the central-wire edges of the complex construction.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Subset-intersection network](subset-intersection-network.md): A linear network on the three-element subsets of a ground set, whose wires carry scalars and whose gates combine them by intersection size, so that it swaps two banks while cancelling arbitrary scratch values.
  Shown as: Rank-saving recursion *<predicate>* Subset-intersection network
- [Address-field interchange](address-interchange.md): A tape procedure that swaps two disjoint contiguous address fields of an array in time that grows like a power of the field width, rather than linearly.
  Shown as: Rank-saving recursion *<predicate>* Address-field interchange
- [Numerical layer](numerical-layer.md): A layer of the transform calculation in which a simultaneous butterfly is applied to a chosen set of selected axes.
  Shown as: Rank-saving recursion *<predicate>* Numerical layer
- [Stream](stream.md): A sequence of records that a procedure reads or writes in order, one position at a time, on a tape.
  Shown as: Rank-saving recursion *<predicate>* Stream
- [Incidence](incidence.md): The relation that a gate and a wire have when the wire touches the gate.
  Shown as: Rank-saving recursion *<predicate>* Incidence
- [Complex construction](complex-construction.md): The construction of a subset-intersection network whose scalars are Gaussian dyadics, with neighbours chosen among distinct triples.
  Shown as: Rank-saving recursion *<predicate>* Complex construction
- [Bit construction](bit-construction.md): The construction of a subset-intersection network whose scalars lie in the binary field, with neighbours chosen by intersection size one.
  Shown as: Rank-saving recursion *<predicate>* Bit construction
- [Bilinear form](bilinear-form.md): A bilinear map from a vector space and itself to its scalars; a space with such a form is nondegenerate when the form has no nonzero vector orthogonal to everything, and two vectors are orthogonal when the form vanishes on them.
  Shown as: Rank-saving recursion *<predicate>* Bilinear form

## Pages that build on this one

- Family parameter: A parameter that indexes a family of constructions and controls their sizes.
- Integer multiplication below n log n: A deterministic fixed-tape machine that multiplies two n-bit integers exactly in O(n (lg n)^(1−κ)) time with κ = 2^−182, which disproves the n log n optimality conjecture in this model.

## Other pages you may link to

- [Integer](integer.md)
- [Logarithm](logarithm.md)
- [Base-2 logarithm](base-two-logarithm.md)
- [Root of unity](root-of-unity.md)
- [Running time cost](running-time-cost.md)
- [Exact integer multiplication](exact-integer-multiplication.md)
- [Convolution](convolution.md)
- [Payload](payload.md)
- [Mathematical induction](mathematical-induction.md)
- [Little-o notation](little-o-notation.md)
- [Address](address.md)
- [Truncation](truncation.md)
- [Array](array.md)
- [Array norm](array-norm.md)
- [Ceiling function](ceiling-function.md)
- [Big-Theta notation](big-theta-notation.md)
- [Extended real numbers](extended-reals.md)
- [Supremum](supremum.md)
- [Telescoping identity](telescoping-identity.md)
- [Mixed-radix digits](mixed-radix-digits.md)
- [Fixed-width digit blocks](fixed-width-digit-blocks.md)
- [Exceptional set](exceptional-set.md)
- [Big-Omega notation](big-omega-notation.md)
- [Bit-reversed index order](bit-reversed-order.md)
- [Directed graph](directed-graph.md)
- [Linear algebra basics](linear-algebra-basics.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Transform axis](transform-axis.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Linear contraction](linear-contraction.md)
- [Bilinear map](bilinear-map.md)
- [Coprime](coprime.md)
- [Bézout's identity](bezout-identity.md)
- [Cyclic group](cyclic-group.md)
- [Order of an element](order-of-element.md)
- [Diagonal scaling](diagonal-scaling.md)
- [Frequency domain](frequency-domain.md)
- [Projection along a subspace](projection-along-subspace.md)
- [Closed disk in the complex plane](complex-disk.md)
- [Linear functional](linear-functional.md)
- [Dual space](dual-space.md)
- [Floor function](floor-function.md)
- [Bijection](bijection.md)
- [Permutation](permutation.md)
- [Address field](address-field.md)
- [Linear networks and frames](linear-network-frames.md)
- [Logical array](logical-array.md)
- [Cyclic shift](cyclic-shift.md)
- [Butterfly](butterfly.md)
- [Radix-digit convolution](radix-digit-convolution.md)
- [Ground set](ground-set.md)
- [Gate and terminal of a network](network-gate-terminal.md)
- [Tensor product](tensor-product.md)
- [Carry propagation](carry-propagation.md)
- [Congruence](congruence-modulo.md)
- [Schönhage–Strassen multiplication](schonhage-strassen.md)
- [Ring](ring.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md)
- [Limit inferior](limit-inferior.md)
- [The n log n optimality conjecture](n-log-n-conjecture.md)
- [Fixed-tape machine model](fixed-tape-model.md)
- [Binary field](binary-field.md)
- [Modular inverse](modular-inverse.md)
- [Binary change of basis](binary-change-of-basis.md)
- [Bit network](bit-network.md)
- [Phase factor](phase-factor.md)
- [Gaussian dyadics](gaussian-dyadics.md)
- [Two-point kernel](two-point-kernel.md)
- [Gaussian integer](gaussian-integer.md)
- [Polynomial ring](polynomial-ring.md)
- [Grid numerator](grid-numerator.md)
- [Chinese remainder theorem](chinese-remainder-theorem.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Ring homomorphism and isomorphism](ring-homomorphism.md)
- [Chinese-remainder map](chinese-remainder-map.md)
- [Forward transform](forward-transform.md)
- [Pointwise product](pointwise-product.md)
- [Opposite transform](opposite-transform.md)
- [Iverson bracket](iverson-bracket.md)
- [Axis line](axis-line.md)
- [Near-linear time](near-linear-time.md)
- [Negacyclic convolution](negacyclic-convolution.md)
- [Neumann series](neumann-series.md)
- [Probability](probability.md)
- [Independence of events](independence.md)
- [Radix-two factorization](radix-two-factorization.md)
- [Multidimensional transform](multidimensional-transform.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Standard basis vector](standard-basis-vector.md)
- [Matrix rank](matrix-rank.md)
- [Symmetric matrix](symmetric-matrix.md)
- [Eigenvalue](eigenvalue.md)
- [Orthogonal complement](orthogonal-complement.md)
- [Indicator vector](indicator-vector.md)
- [Line spanned by a vector](line-spanned-by-vector.md)
- [Subspace labels](subspace-labels.md)
- [Scratch storage](scratch-storage.md)
- [Exclusive or](xor.md)
- [Gram matrix](gram-matrix.md)
- [Complex phase network](complex-phase-network.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Guard-width bound](guard-width-bound.md)
- [Union bound](union-bound.md)
- [Transform round](transform-round.md)
- [Tape procedure](tape-procedure.md)
- [Bit procedure](bit-procedure.md)
- [Endpoint operator](endpoint-operator.md)
- [Address shear](address-shear.md)
- [Stable radix sort](stable-radix-sort.md)
- [Destination rank](destination-rank.md)
- [Transform identity with retained permutations](transform-identity.md)
- [Transform layout](transform-layout.md)
- [Padded transform box](padded-transform-box.md)
- [Cyclic coordinate](cyclic-coordinate.md)
- [Prime number](prime-number.md)
- [Logical bit volume](logical-bit-volume.md)
- [Cost table](cost-table.md)
- [Established O(n log n) multiplier](established-multiplier.md)
- [Signed coefficient packing](signed-packing.md)
- [Schoolbook multiplication](schoolbook-multiplication.md)
- [Centered residue](centered-residue.md)
- [Convolution over the polynomial ring](polynomial-ring-convolution.md)
- [Normalized cyclic convolution](normalized-cyclic-convolution.md)
- [Bluestein's chirp identity](bluestein-chirp-identity.md)
- [Normalization scales](normalization-scales.md)
- [Middle transform](middle-transform.md)
- [Phase twist](phase-twist.md)
- [Prime source lengths](prime-source-lengths.md)
- [Exact coefficient recovery](recovery-and-error.md)
- [Schedule](schedule.md)
- [Family parameter](family-parameter.md)
- [Packed selected-bit addition](packed-bit-addition.md)
- [Integer multiplication below n log n](main-theorem.md)

## Evidence from the sources

- "the total number s of smaller calls satisfies s < W m" (paper)

## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- $s$ means smaller-call count here, but real number on [Ceiling function](ceiling-function.md), which this page builds on: Different: $s$ means smaller-call count on rank-saving-recursion but real number on Ceiling function. The later page should use another letter for smaller-call count, or say explicitly where $s$ keeps this meaning instead of real number.
- $s$ means smaller-call count here, but input index on [Discrete Fourier transform](discrete-fourier-transform.md), which this page builds on: Different: $s$ means smaller-call count on rank-saving-recursion but input index on Discrete Fourier transform. The later page should use another letter for smaller-call count, or say explicitly where $s$ keeps this meaning instead of input index.
- $s$ means smaller-call count here, but coefficient index on [Array norm](array-norm.md), which this page builds on: Different: $s$ means smaller-call count on rank-saving-recursion but coefficient index on Array norm. The later page should use another letter for smaller-call count, or say explicitly where $s$ keeps this meaning instead of coefficient index.
- $s$ means smaller-call count here, but number of H_0 factors on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md), which this page builds on: Different: $s$ means smaller-call count on rank-saving-recursion but number of H_0 factors on Simultaneous butterfly layer. The later page should use another letter for smaller-call count, or say explicitly where $s$ keeps this meaning instead of number of H_0 factors.
- $s$ means smaller-call count here, but coefficient count on [Transform axis](transform-axis.md), which this page builds on: Different: $s$ means smaller-call count on rank-saving-recursion but coefficient count on Transform axis. The later page should use another letter for smaller-call count, or say explicitly where $s$ keeps this meaning instead of coefficient count.
- $s$ means smaller-call count here, but first pair value on [Truncation](truncation.md), which this page builds on: Different: $s$ means smaller-call count on rank-saving-recursion but first pair value on Truncation. The later page should use another letter for smaller-call count, or say explicitly where $s$ keeps this meaning instead of first pair value.
- $s$ means smaller-call count here, but basis index on [Subspace labels](subspace-labels.md), which this page builds on: Different: $s$ means smaller-call count on rank-saving-recursion but basis index on Subspace labels. The later page should use another letter for smaller-call count, or say explicitly where $s$ keeps this meaning instead of basis index.
- $s$ means smaller-call count here, but common length on [Mixed-radix digits](mixed-radix-digits.md), which this page builds on: Different: $s$ means smaller-call count on rank-saving-recursion but common length on Mixed-radix digits. The later page should use another letter for smaller-call count, or say explicitly where $s$ keeps this meaning instead of common length.
- $s$ means smaller-call count here, but first position on [Telescoping identity](telescoping-identity.md), which this page builds on: Different: $s$ means smaller-call count on rank-saving-recursion but first position on Telescoping identity. The later page should use another letter for smaller-call count, or say explicitly where $s$ keeps this meaning instead of first position.
- $W$ means wire count here, but source bank on [Bit network](bit-network.md), which this page builds on: Different: $W$ means wire count on rank-saving-recursion but source bank on Bit network. The later page should use another letter for wire count, or say explicitly where $W$ keeps this meaning instead of source bank.
- $W$ means wire count here, but position set on [Permutation](permutation.md), which this page builds on: Different: $W$ means wire count on rank-saving-recursion but position set on Permutation. The later page should use another letter for wire count, or say explicitly where $W$ keeps this meaning instead of position set.
- $W$ means wire count here, but target set on [Bijection](bijection.md), which this page builds on: Different: $W$ means wire count on rank-saving-recursion but target set on Bijection. The later page should use another letter for wire count, or say explicitly where $W$ keeps this meaning instead of target set.
- $W$ means wire count here, but output space on [Bilinear map](bilinear-map.md), which this page builds on: Different: $W$ means wire count on rank-saving-recursion but output space on Bilinear map. The later page should use another letter for wire count, or say explicitly where $W$ keeps this meaning instead of output space.
- $W$ means wire count here, but cyclic group order on [Cyclic group](cyclic-group.md), which this page builds on: Different: $W$ means wire count on rank-saving-recursion but cyclic group order on Cyclic group. The later page should use another letter for wire count, or say explicitly where $W$ keeps this meaning instead of cyclic group order.
- $W$ means wire count here, but family product on [Coprime](coprime.md), which this page builds on: Different: $W$ means wire count on rank-saving-recursion but family product on Coprime. The later page should use another letter for wire count, or say explicitly where $W$ keeps this meaning instead of family product.
- $W$ means wire count here, but row index of P' on [Tensor product](tensor-product.md), which this page builds on: Different: $W$ means wire count on rank-saving-recursion but row index of P' on Tensor product. The later page should use another letter for wire count, or say explicitly where $W$ keeps this meaning instead of row index of P'.
- $W$ means wire count here, but ambient space on [Projection along a subspace](projection-along-subspace.md), which this page builds on: Different: $W$ means wire count on rank-saving-recursion but ambient space on Projection along a subspace. The later page should use another letter for wire count, or say explicitly where $W$ keeps this meaning instead of ambient space.
- $W$ means wire count here, but larger label on [Orthogonal complement](orthogonal-complement.md), which this page builds on: Different: $W$ means wire count on rank-saving-recursion but larger label on Orthogonal complement. The later page should use another letter for wire count, or say explicitly where $W$ keeps this meaning instead of larger label.
- $W$ means wire count here, but second butterfly entry on [Synthetic polynomial transforms](synthetic-transforms.md), which this page builds on: Different: $W$ means wire count on rank-saving-recursion but second butterfly entry on Synthetic polynomial transforms. The later page should use another letter for wire count, or say explicitly where $W$ keeps this meaning instead of second butterfly entry.
- $m$ means label dimension here, but bit count on [Integer](integer.md), which this page builds on: Different: $m$ means label dimension on rank-saving-recursion but bit count on Integer. The later page should use another letter for label dimension, or say explicitly where $m$ keeps this meaning instead of bit count.
- $m$ means label dimension here, but coordinate count on [Linear algebra basics](linear-algebra-basics.md), which this page builds on: Different: $m$ means label dimension on rank-saving-recursion but coordinate count on Linear algebra basics. The later page should use another letter for label dimension, or say explicitly where $m$ keeps this meaning instead of coordinate count.
- $m$ means label dimension here, but order on [Root of unity](root-of-unity.md), which this page builds on: Different: $m$ means label dimension on rank-saving-recursion but order on Root of unity. The later page should use another letter for label dimension, or say explicitly where $m$ keeps this meaning instead of order.
- $m$ means label dimension here, but pieces per level on [Address-field interchange](address-interchange.md), which this page builds on: Different: $m$ means label dimension on rank-saving-recursion but pieces per level on Address-field interchange. The later page should use another letter for label dimension, or say explicitly where $m$ keeps this meaning instead of pieces per level.
- $m$ means label dimension here, but tail start on [Limit inferior](limit-inferior.md), which this page builds on: Different: $m$ means label dimension on rank-saving-recursion but tail start on Limit inferior. The later page should use another letter for label dimension, or say explicitly where $m$ keeps this meaning instead of tail start.
- $m$ means label dimension here, but division factor on [Numerical layer](numerical-layer.md), which this page builds on: Different: $m$ means label dimension on rank-saving-recursion but division factor on Numerical layer. The later page should use another letter for label dimension, or say explicitly where $m$ keeps this meaning instead of division factor.
- $F$ means nondegenerate space here, but generic formula on [Exceptional set](exceptional-set.md), which this page builds on: Different: $F$ means nondegenerate space on rank-saving-recursion but generic formula on Exceptional set. The later page should use another letter for nondegenerate space, or say explicitly where $F$ keeps this meaning instead of generic formula.
- $F$ means nondegenerate space here, but field on [Linear algebra basics](linear-algebra-basics.md), which this page builds on: Different: $F$ means nondegenerate space on rank-saving-recursion but field on Linear algebra basics. The later page should use another letter for nondegenerate space, or say explicitly where $F$ keeps this meaning instead of field.
- $F$ means nondegenerate space here, but real elements on [Extended real numbers](extended-reals.md), which this page builds on: Different: $F$ means nondegenerate space on rank-saving-recursion but real elements on Extended real numbers. The later page should use another letter for nondegenerate space, or say explicitly where $F$ keeps this meaning instead of real elements.
- $U$ means label here, but source set on [Bijection](bijection.md), which this page builds on: Different: $U$ means label on rank-saving-recursion but source set on Bijection. The later page should use another letter for label, or say explicitly where $U$ keeps this meaning instead of source set.
- $U$ means label here, but first argument space on [Bilinear map](bilinear-map.md), which this page builds on: Different: $U$ means label on rank-saving-recursion but first argument space on Bilinear map. The later page should use another letter for label, or say explicitly where $U$ keeps this meaning instead of first argument space.
- $U$ means label here, but vector space on [Dual space](dual-space.md), which this page builds on: Different: $U$ means label on rank-saving-recursion but vector space on Dual space. The later page should use another letter for label, or say explicitly where $U$ keeps this meaning instead of vector space.
- $U$ means label here, but first butterfly entry on [Synthetic polynomial transforms](synthetic-transforms.md), which this page builds on: Different: $U$ means label on rank-saving-recursion but first butterfly entry on Synthetic polynomial transforms. The later page should use another letter for label, or say explicitly where $U$ keeps this meaning instead of first butterfly entry.
- $V$ means padded volume here, but vertex set on [Directed graph](directed-graph.md), which this page builds on: Different: $V$ means padded volume on rank-saving-recursion but vertex set on Directed graph. The later page should use another letter for padded volume, or say explicitly where $V$ keeps this meaning instead of vertex set.
- $V$ means padded volume here, but stored bit volume on [Array](array.md), which this page builds on: Different: $V$ means padded volume on rank-saving-recursion but stored bit volume on Array. The later page should use another letter for padded volume, or say explicitly where $V$ keeps this meaning instead of stored bit volume.
- $V$ means padded volume here, but stream volume on [Payload](payload.md), which this page builds on: Different: $V$ means padded volume on rank-saving-recursion but stream volume on Payload. The later page should use another letter for padded volume, or say explicitly where $V$ keeps this meaning instead of stream volume.
- $V$ means padded volume here, but stored bit volume on [Big-Theta notation](big-theta-notation.md), which this page builds on: Different: $V$ means padded volume on rank-saving-recursion but stored bit volume on Big-Theta notation. The later page should use another letter for padded volume, or say explicitly where $V$ keeps this meaning instead of stored bit volume.
- $V$ means padded volume here, but stored bit volume on [Cyclic shift](cyclic-shift.md), which this page builds on: Different: $V$ means padded volume on rank-saving-recursion but stored bit volume on Cyclic shift. The later page should use another letter for padded volume, or say explicitly where $V$ keeps this meaning instead of stored bit volume.
- $V$ means padded volume here, but vector space on [Eigenvalue](eigenvalue.md), which this page builds on: Different: $V$ means padded volume on rank-saving-recursion but vector space on Eigenvalue. The later page should use another letter for padded volume, or say explicitly where $V$ keeps this meaning instead of vector space.
- $V$ means padded volume here, but second argument space on [Bilinear map](bilinear-map.md), which this page builds on: Different: $V$ means padded volume on rank-saving-recursion but second argument space on Bilinear map. The later page should use another letter for padded volume, or say explicitly where $V$ keeps this meaning instead of second argument space.
- $V$ means padded volume here, but copy on [Scratch storage](scratch-storage.md), which this page builds on: Different: $V$ means padded volume on rank-saving-recursion but copy on Scratch storage. The later page should use another letter for padded volume, or say explicitly where $V$ keeps this meaning instead of copy.
- $V$ means padded volume here, but vector space on [Linear functional](linear-functional.md), which this page builds on: Different: $V$ means padded volume on rank-saving-recursion but vector space on Linear functional. The later page should use another letter for padded volume, or say explicitly where $V$ keeps this meaning instead of vector space.
- $V$ means padded volume here, but larger nested subspace on [Projection along a subspace](projection-along-subspace.md), which this page builds on: Different: $V$ means padded volume on rank-saving-recursion but larger nested subspace on Projection along a subspace. The later page should use another letter for padded volume, or say explicitly where $V$ keeps this meaning instead of larger nested subspace.
- $V$ means padded volume here, but head label on [Complex phase network](complex-phase-network.md), which this page builds on: Different: $V$ means padded volume on rank-saving-recursion but head label on Complex phase network. The later page should use another letter for padded volume, or say explicitly where $V$ keeps this meaning instead of head label.
- $\mu$ means source dimension sum here, but bit-flip coefficient on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md), which this page builds on: Different: $\mu$ means source dimension sum on rank-saving-recursion but bit-flip coefficient on Simultaneous butterfly layer. The later page should use another letter for source dimension sum, or say explicitly where $\mu$ keeps this meaning instead of bit-flip coefficient.
- $e$ means chunk digit count here, but integer on [Congruence](congruence-modulo.md), which this page builds on: Different: $e$ means chunk digit count on rank-saving-recursion but integer on Congruence. The later page should use another letter for chunk digit count, or say explicitly where $e$ keeps this meaning instead of integer.
- $e$ means chunk digit count here, but eigenvector on [Eigenvalue](eigenvalue.md), which this page builds on: Different: $e$ means chunk digit count on rank-saving-recursion but eigenvector on Eigenvalue. The later page should use another letter for chunk digit count, or say explicitly where $e$ keeps this meaning instead of eigenvector.
- $e$ means chunk digit count here, but quotient on [Transform round](transform-round.md), which this page builds on: Different: $e$ means chunk digit count on rank-saving-recursion but quotient on Transform round. The later page should use another letter for chunk digit count, or say explicitly where $e$ keeps this meaning instead of quotient.
- $e$ means chunk digit count here, but bit position on [Two-point kernel](two-point-kernel.md), which this page builds on: Different: $e$ means chunk digit count on rank-saving-recursion but bit position on Two-point kernel. The later page should use another letter for chunk digit count, or say explicitly where $e$ keeps this meaning instead of bit position.
- $e$ means chunk digit count here, but position on [Indicator vector](indicator-vector.md), which this page builds on: Different: $e$ means chunk digit count on rank-saving-recursion but position on Indicator vector. The later page should use another letter for chunk digit count, or say explicitly where $e$ keeps this meaning instead of position.
- $e$ means chunk digit count here, but last position on [Telescoping identity](telescoping-identity.md), which this page builds on: Different: $e$ means chunk digit count on rank-saving-recursion but last position on Telescoping identity. The later page should use another letter for chunk digit count, or say explicitly where $e$ keeps this meaning instead of last position.
- $e$ means chunk digit count here, but selected axis count on [Numerical layer](numerical-layer.md), which this page builds on: Different: $e$ means chunk digit count on rank-saving-recursion but selected axis count on Numerical layer. The later page should use another letter for chunk digit count, or say explicitly where $e$ keeps this meaning instead of selected axis count.
- $q$ means radix here, but transform length on [Discrete Fourier transform](discrete-fourier-transform.md), which this page builds on: Different: $q$ means radix on rank-saving-recursion but transform length on Discrete Fourier transform. The later page should use another letter for radix, or say explicitly where $q$ keeps this meaning instead of transform length.
- $q$ means radix here, but number of values on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md), which this page builds on: Different: $q$ means radix on rank-saving-recursion but number of values on Simultaneous butterfly layer. The later page should use another letter for radix, or say explicitly where $q$ keeps this meaning instead of number of values.
- $\gamma$ means linear-work constant here, but third entry on [Permutation](permutation.md), which this page builds on: Different: $\gamma$ means linear-work constant on rank-saving-recursion but third entry on Permutation. The later page should use another letter for linear-work constant, or say explicitly where $\gamma$ keeps this meaning instead of third entry.
- $\gamma$ means linear-work constant here, but scalar on [Linear algebra basics](linear-algebra-basics.md), which this page builds on: Different: $\gamma$ means linear-work constant on rank-saving-recursion but scalar on Linear algebra basics. The later page should use another letter for linear-work constant, or say explicitly where $\gamma$ keeps this meaning instead of scalar.
- $\gamma$ means linear-work constant here, but first integer on [Coprime](coprime.md), which this page builds on: Different: $\gamma$ means linear-work constant on rank-saving-recursion but first integer on Coprime. The later page should use another letter for linear-work constant, or say explicitly where $\gamma$ keeps this meaning instead of first integer.
- $\gamma$ means linear-work constant here, but block offset on [Synthetic polynomial transforms](synthetic-transforms.md), which this page builds on: Different: $\gamma$ means linear-work constant on rank-saving-recursion but block offset on Synthetic polynomial transforms. The later page should use another letter for linear-work constant, or say explicitly where $\gamma$ keeps this meaning instead of block offset.
- $\tau$ means power-saving exponent here, but sequence term on [Extended real numbers](extended-reals.md), which this page builds on: Different: $\tau$ means power-saving exponent on rank-saving-recursion but sequence term on Extended real numbers. The later page should use another letter for power-saving exponent, or say explicitly where $\tau$ keeps this meaning instead of sequence term.
- $\sigma$ means saving ratio here, but triple on [Bit network](bit-network.md), which this page builds on: Different: $\sigma$ means saving ratio on rank-saving-recursion but triple on Bit network. The later page should use another letter for saving ratio, or say explicitly where $\sigma$ keeps this meaning instead of triple.
- $\sigma$ means saving ratio here, but output role on [Linear networks and frames](linear-network-frames.md), which this page builds on: Different: $\sigma$ means saving ratio on rank-saving-recursion but output role on Linear networks and frames. The later page should use another letter for saving ratio, or say explicitly where $\sigma$ keeps this meaning instead of output role.
- $\sigma$ means saving ratio here, but permutation on [Permutation](permutation.md), which this page builds on: Different: $\sigma$ means saving ratio on rank-saving-recursion but permutation on Permutation. The later page should use another letter for saving ratio, or say explicitly where $\sigma$ keeps this meaning instead of permutation.
- $\sigma$ means saving ratio here, but source element on [Bijection](bijection.md), which this page builds on: Different: $\sigma$ means saving ratio on rank-saving-recursion but source element on Bijection. The later page should use another letter for saving ratio, or say explicitly where $\sigma$ keeps this meaning instead of source element.
- $\sigma$ means saving ratio here, but selected bit values on [Binary change of basis](binary-change-of-basis.md), which this page builds on: Different: $\sigma$ means saving ratio on rank-saving-recursion but selected bit values on Binary change of basis. The later page should use another letter for saving ratio, or say explicitly where $\sigma$ keeps this meaning instead of selected bit values.
- $\sigma$ means saving ratio here, but three-element subset on [Binary field](binary-field.md), which this page builds on: Different: $\sigma$ means saving ratio on rank-saving-recursion but three-element subset on Binary field. The later page should use another letter for saving ratio, or say explicitly where $\sigma$ keeps this meaning instead of three-element subset.
- $\sigma$ means saving ratio here, but class member on [Congruence](congruence-modulo.md), which this page builds on: Different: $\sigma$ means saving ratio on rank-saving-recursion but class member on Congruence. The later page should use another letter for saving ratio, or say explicitly where $\sigma$ keeps this meaning instead of class member.
- $\sigma$ means saving ratio here, but index bit on [Butterfly](butterfly.md), which this page builds on: Different: $\sigma$ means saving ratio on rank-saving-recursion but index bit on Butterfly. The later page should use another letter for saving ratio, or say explicitly where $\sigma$ keeps this meaning instead of index bit.
- $\sigma$ means saving ratio here, but offset on [Cyclic shift](cyclic-shift.md), which this page builds on: Different: $\sigma$ means saving ratio on rank-saving-recursion but offset on Cyclic shift. The later page should use another letter for saving ratio, or say explicitly where $\sigma$ keeps this meaning instead of offset.
- $\sigma$ means saving ratio here, but dummy index on [Discrete Fourier transform](discrete-fourier-transform.md), which this page builds on: Different: $\sigma$ means saving ratio on rank-saving-recursion but dummy index on Discrete Fourier transform. The later page should use another letter for saving ratio, or say explicitly where $\sigma$ keeps this meaning instead of dummy index.
- $\sigma$ means saving ratio here, but residue bit count on [Schönhage–Strassen multiplication](schonhage-strassen.md), which this page builds on: Different: $\sigma$ means saving ratio on rank-saving-recursion but residue bit count on Schönhage–Strassen multiplication. The later page should use another letter for saving ratio, or say explicitly where $\sigma$ keeps this meaning instead of residue bit count.
- $\sigma$ means saving ratio here, but element on [Order of an element](order-of-element.md), which this page builds on: Different: $\sigma$ means saving ratio on rank-saving-recursion but element on Order of an element. The later page should use another letter for saving ratio, or say explicitly where $\sigma$ keeps this meaning instead of element.
- $\sigma$ means saving ratio here, but order of an element on [Cyclic group](cyclic-group.md), which this page builds on: Different: $\sigma$ means saving ratio on rank-saving-recursion but order of an element on Cyclic group. The later page should use another letter for saving ratio, or say explicitly where $\sigma$ keeps this meaning instead of order of an element.
- $\sigma$ means saving ratio here, but member index on [Coprime](coprime.md), which this page builds on: Different: $\sigma$ means saving ratio on rank-saving-recursion but member index on Coprime. The later page should use another letter for saving ratio, or say explicitly where $\sigma$ keeps this meaning instead of member index.
- $\sigma$ means saving ratio here, but numerator on [Gaussian dyadics](gaussian-dyadics.md), which this page builds on: Different: $\sigma$ means saving ratio on rank-saving-recursion but numerator on Gaussian dyadics. The later page should use another letter for saving ratio, or say explicitly where $\sigma$ keeps this meaning instead of numerator.
- $\sigma$ means saving ratio here, but column index on [Tensor product](tensor-product.md), which this page builds on: Different: $\sigma$ means saving ratio on rank-saving-recursion but column index on Tensor product. The later page should use another letter for saving ratio, or say explicitly where $\sigma$ keeps this meaning instead of column index.
- $\sigma$ means saving ratio here, but triple of triples on [Subset-intersection network](subset-intersection-network.md), which this page builds on: Different: $\sigma$ means saving ratio on rank-saving-recursion but triple of triples on Subset-intersection network. The later page should use another letter for saving ratio, or say explicitly where $\sigma$ keeps this meaning instead of triple of triples.
- $\sigma$ means saving ratio here, but example functional on [Dual space](dual-space.md), which this page builds on: Different: $\sigma$ means saving ratio on rank-saving-recursion but example functional on Dual space. The later page should use another letter for saving ratio, or say explicitly where $\sigma$ keeps this meaning instead of example functional.
- $\sigma$ means saving ratio here, but triple choice on [Line spanned by a vector](line-spanned-by-vector.md), which this page builds on: Different: $\sigma$ means saving ratio on rank-saving-recursion but triple choice on Line spanned by a vector. The later page should use another letter for saving ratio, or say explicitly where $\sigma$ keeps this meaning instead of triple choice.
- $\sigma$ means saving ratio here, but positive constant on [Fixed-tape machine model](fixed-tape-model.md), which this page builds on: Different: $\sigma$ means saving ratio on rank-saving-recursion but positive constant on Fixed-tape machine model. The later page should use another letter for saving ratio, or say explicitly where $\sigma$ keeps this meaning instead of positive constant.
- $\sigma$ means saving ratio here, but generic real number on [Extended real numbers](extended-reals.md), which this page builds on: Different: $\sigma$ means saving ratio on rank-saving-recursion but generic real number on Extended real numbers. The later page should use another letter for saving ratio, or say explicitly where $\sigma$ keeps this meaning instead of generic real number.
- $\sigma$ means saving ratio here, but list length on [Gram matrix](gram-matrix.md), which this page builds on: Different: $\sigma$ means saving ratio on rank-saving-recursion but list length on Gram matrix. The later page should use another letter for saving ratio, or say explicitly where $\sigma$ keeps this meaning instead of list length.
- $\sigma$ means saving ratio here, but axis index on [Multidimensional transform](multidimensional-transform.md), which this page builds on: Different: $\sigma$ means saving ratio on rank-saving-recursion but axis index on Multidimensional transform. The later page should use another letter for saving ratio, or say explicitly where $\sigma$ keeps this meaning instead of axis index.
- $\sigma$ means saving ratio here, but shift count on [Synthetic polynomial transforms](synthetic-transforms.md), which this page builds on: Different: $\sigma$ means saving ratio on rank-saving-recursion but shift count on Synthetic polynomial transforms. The later page should use another letter for saving ratio, or say explicitly where $\sigma$ keeps this meaning instead of shift count.
- $\sigma$ means saving ratio here, but half-length output index on [Radix-two factorization](radix-two-factorization.md), which this page builds on: Different: $\sigma$ means saving ratio on rank-saving-recursion but half-length output index on Radix-two factorization. The later page should use another letter for saving ratio, or say explicitly where $\sigma$ keeps this meaning instead of half-length output index.
- $\sigma$ means saving ratio here, but condition on [Iverson bracket](iverson-bracket.md), which this page builds on: Different: $\sigma$ means saving ratio on rank-saving-recursion but condition on Iverson bracket. The later page should use another letter for saving ratio, or say explicitly where $\sigma$ keeps this meaning instead of condition.
- $\beta$ means one-digit cost constant here, but second entry on [Permutation](permutation.md), which this page builds on: Different: $\beta$ means one-digit cost constant on rank-saving-recursion but second entry on Permutation. The later page should use another letter for one-digit cost constant, or say explicitly where $\beta$ keeps this meaning instead of second entry.
- $\beta$ means one-digit cost constant here, but place count on [Mixed-radix digits](mixed-radix-digits.md), which this page builds on: Different: $\beta$ means one-digit cost constant on rank-saving-recursion but place count on Mixed-radix digits. The later page should use another letter for one-digit cost constant, or say explicitly where $\beta$ keeps this meaning instead of place count.
- The quotation does not support the claim it is attached to (unsupported): "Hence the smaller calls are counted for the [Bit construction](bit-construction.md) as $s=Wm-\mu+2\mathcal L$, and" cites "Its deficit from Wb m is N − 2Lb > 0.": The quotation concerns a deficit from Wb m equal to N - 2Lb > 0, not the smaller-call count s = Wm - mu + 2L for the Bit construction. Say only what the source supports, or cite the passage that supports the claim.

## Previous version (revise it)

It has 779 words. Fix the problems by restructuring rather than appending: keep the rewrite within 973 words, a quarter more, unless a problem cannot be fixed without more. Pages that grow with every repair stop being self-contained explanations of one concept.

Rank-saving recursion is the scheme that gives the power saving in the logarithmic factor of [Integer multiplication below n log n](main-theorem.md). A call splits into $s$ smaller calls, each on $1/W$ of its data, where $s$ is the total number of smaller calls and $W$ is the number of wires of the network. The step it presents is $s<Wm$, where $m$ is the dimension of the space that holds all labels (the letter $m$ changes meaning here), so each level multiplies the cost per unit of data by $s/W<m$.

The recursion is set in a fixed nondegenerate space $F$ of a [Bilinear form](bilinear-form.md), a space with no nonzero vector orthogonal to all of $F$, of dimension $m$ (the letter $m$ changes meaning here). Each vertex carries a label, a nondegenerate subspace $U$ of $F$: $U\cap U^\bot=\{0\}$, where $U^\bot$ is the set of vectors orthogonal to all of $U$. Then $F=U\oplus U^\bot$, and $P_U$ denotes the projection onto $U$ along $U^\bot$. <cite data-source="paper">The subspaces at adjacent vertices are nested.</cite>

A wire runs from its source vertex, through the gates that touch it in time order, to its sink vertex. A touching of a gate and a wire is an [Incidence](incidence.md). A gate's label is shared by its wires: <cite data-source="paper">the latter assignment being common to every wire at that gate</cite>. The recursion runs on the wires of the [Subset-intersection network](subset-intersection-network.md); each wire's fixed place is its role.

Arrays are split by rows, where a row is the complete ordered suffix of the address fields at a fixed prefix and row index. <cite data-source="paper">Distribute rows cyclically among the W roles</cite>, padding the row count to a multiple of $W$. Let $V$ be the stored volume after padding, so each role stream holds $V/W$ bits. Rank-saving recursion gives each smaller call one [Stream](stream.md) of volume $V/W$.

An edge $\varphi$ is a segment of a wire between consecutive vertices, with tail label $U_{\rm t}$ and head label $U_{\rm h}$. Its signed change is $\Delta_\varphi=\dim U_{\rm h}-\dim U_{\rm t}$ (the letter $\Delta$ changes meaning here). Its rank is the rational rank of $P_{\rm h}-P_{\rm t}$, the dimension over $\mathbb Q$ of its column span. For nested labels, with $U$ inside $U'$ and $U$ nondegenerate, $U'=U\oplus(U'\cap U^\bot)$, and $P_{U'}-P_U$ is zero on $U$ and on $U'^\bot$ and the identity on $U'\cap U^\bot$. So its rank is $\dim U'-\dim U$. Reversing an edge negates the matrix, so every edge has rank $|\Delta_\varphi|$. <cite data-source="paper">will require a smaller interchanges.</cite> Rank-saving recursion reduces its calls to the [Address-field interchange](address-interchange.md), one per unit of edge rank. Hence <cite data-source="paper">The number of recursive calls is the sum of the edge ranks, exactly s.</cite>

Along a wire, the signed change telescopes across each [Incidence](incidence.md) to the sink dimension minus the source dimension. In the bit construction each sink label is the orthogonal complement of its source label, so each wire's two dimensions sum to $m$. Let $\mu$ be the sum of the source dimensions (the paper writes $N$ for $\mu$). The sinks then contribute $Wm-\mu$, and <cite data-source="paper">Thus the signed dimension changes will sum to W m − 2N</cite>, that is, $\sum_\varphi\Delta_\varphi=Wm-2\mu$.

Call an edge decreasing when its head label is smaller. For a decreasing edge $\varphi$, let $\mathrm{loss}_\varphi=\dim U_{\rm t}-\dim U_{\rm h}>0$ be its dimension loss, and let $\mathcal L$ be the total of these losses. On a decreasing edge $|\Delta_\varphi|=-\Delta_\varphi=\Delta_\varphi+2\,\mathrm{loss}_\varphi$; on other edges $|\Delta_\varphi|=\Delta_\varphi$. Summing, <cite data-source="paper">of absolute changes is W m − 2N + 2L.</cite> So $\sum_\varphi|\Delta_\varphi|=Wm-2\mu+2\mathcal L$.

In the [Bit construction](bit-construction.md), the $\mu$ first-stage source edges are exceptions. <cite data-source="paper">the first gate on Xa has label exactly Ua</cite>, so each such edge has rank one (its matrix is $2P_U$ for a line $U$) while its signed change is zero. Hence the smaller calls are counted for the [Bit construction](bit-construction.md) as $s=Wm-\mu+2\mathcal L$, and <cite data-source="paper">Its deficit from Wb m is N − 2Lb > 0.</cite>

The paper's instance uses <cite data-source="paper">with the ground-set size changed to h = 100.</cite> <cite data-source="paper">The loss ratios have the exact values</cite> $\mathcal L/\mu=100/539$, and <cite data-source="paper">In particular, both are smaller than 1/2.</cite> So $s=Wm-\frac{339}{539}\mu<Wm$. The same signed-sum identity is checked on the [Complex construction](complex-construction.md), with ratio $101/539$.

Write $\mathrm{cost}(V,e)$ for the time to interchange two chunks of $e$ digits in a fixed radix $q$ on a stored volume $V$, where $e$ is the digit count of each chunk (the letter $e$ changes meaning here). A call on chunks of $me$ digits makes $s$ calls on chunks of $e$ digits, each on a stream of volume $V/W$. <cite data-source="paper">Splitting, merging, gates, and triangular operations have total cost</cite> $O(V)$. Linear work is $\gamma V$ for a constant $\gamma$, so
$$\mathrm{cost}(V,me)\le s\,\mathrm{cost}(V/W,e)+\gamma V.\tag{1}$$
The same recursion applies to a [Numerical layer](numerical-layer.md), where the parameter counts selected axes instead of digits.

Choose $\tau\in(0,1)$ with $s/W<m^\tau$, which makes $\tau$ the power-saving exponent. This is possible since $m^\tau\to m>s/W$ as $\tau\to1$. Put $\sigma=(s/W)m^{-\tau}<1$. Let $\beta V$ bound the cost of one digit, and let $\Xi\ge\max(\beta,\gamma/(1-\sigma))$ be a constant.

Claim: $\mathrm{cost}(V,m^k)\le\Xi V(m^k)^\tau$ for all $k\ge0$. The case $k=0$ holds by the choice of $\beta$. For the step, (1) with $e=m^k$ gives $\mathrm{cost}(V,m^{k+1})\le s\,\Xi(V/W)(m^k)^\tau+\gamma V=\sigma\,\Xi V(m^{k+1})^\tau+\gamma V$. Since $(m^{k+1})^\tau\ge1$ and $\gamma\le(1-\sigma)\Xi$, this is at most $\Xi V(m^{k+1})^\tau$. So the cost is $O(Ve^\tau)$ with $\tau<1$.

The strict inequality makes $\sigma<1$, so the linear term $\gamma V$ is absorbed at each level. If $s=Wm$, no $\tau<1$ works. Toy example, not the paper's values: $W=4$, $s=6$, $m=2$ gives $s/W=1.5<2$, so $\tau=0.6$ works ($2^{0.6}\approx1.52$).

## Answer

The answer is two files: the page body as markdown (not JSON), and a JSON object with the symbols the page binds and its relations to its prerequisite pages. In JSON strings, write each backslash of LaTeX twice (`"\\kappa"`). The JSON follows this schema:

```json
{
  "$defs": {
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

Write the body to `exegenius/tasks/0852-write-rank-saving-recursion.answer.md` and the JSON to `exegenius/tasks/0852-write-rank-saving-recursion.answer.json`, then run `exegenius submit 0852-write-rank-saving-recursion` in the project directory. If submit rejects the answer, fix the answer and submit again.
