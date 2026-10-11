# exegenius task 0794-write-chinese-remainder-theorem

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
- Radix-digit convolution (also: radix-digit coefficients)
- Discrete Fourier transform (also: normalized Fourier transform, transform, Fourier transform, normalized form, frequency order)
- Synthetic polynomial transforms (also: Nussbaumer polynomial transforms, polynomial transforms, Nussbaumer and Quandalle, the paper's representation)
- Polynomial ring modulo y^r + 1 (also: negacyclic polynomial ring, quotient ring)
  - $y$ (polynomial variable): The indeterminate of the polynomial ring, whose powers act as roots of unity.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Linear networks and frames (also: roles, frames, network of wires and gates, network, vertex, edge, source and sink vertices, Edge change, network, frame of a gate, role, data banks X_τ and Y_τ)
- Gaussian dyadics
- Carry propagation (also: carry scan)
- Address field (also: address chunk, chunk, target chunk, selected address bits)
- Transform axis (also: axis, remaining axes, reduction axis, participating axis)
- Linear algebra basics (also: linear algebra: invertible linear operator, matrix, inverse, matrix, linear map, usual axioms, basis)
- Bilinear map (also: bilinear product, bilinear contraction)
- Binary field (also: finite field F2, F_2, finite field F_2, copy step, exclusive or and AND)
- Binary change of basis (also: residual basis of directions)
- Butterfly (also: two-point butterfly map, two-point map, Butterfly operation)
- Congruence (also: congruence modulo B, modulo, modulo arithmetic, residue, modulo (mod 4), residue class)
- Linear contraction (also: contraction)
- Cyclic shift (also: controlled cyclic shift, signed shifts)
- Convolution
- Coprime (also: gcd, pairwise coprime, coprime (gcd))
- Running time cost (also: cost, linear-cost update, bit-complexity bound, linear tape time)
- Gate and terminal of a network (also: gate applied pointwise, pointwise linear gate, sink)
- Gaussian integer
- Grid numerator (also: grid numerators)
- Ground set (also: finite set, sets)
- Modular inverse (also: invertible modulo q, unit modulo M_i, invertible modulo n)
- Two-point kernel (also: kernel)
- Limit inferior
- Little-o notation (also: limit as lambda tends to infinity)
- Mixed-radix digits (also: mixed-radix digit, digit)
- Array norm (also: norm of an array, coefficient bound, norm of a vector)
- Payload (also: record)
- Phase factor (also: phase factors and scalar corrections, phase frames)
- Polynomial ring (also: polynomial suffix)
- Tensor product (also: tensor power)
- Truncation
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
- Cyclic group (also: cyclic group of order S)
- Order of an element (also: multiplicative order)
- Diagonal scaling
- Extended real numbers
- Frequency domain
- Incidence
- Mathematical induction (also: induction)
- Integer
- Ring
- Projection along a subspace
- Root of unity (also: roots of unity, primitive root of unity)
- Supremum
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
- Real numbers (also: Real number)

## This page

Concept: Chinese remainder theorem
Gloss: For pairwise coprime moduli, a system of congruences has a solution, unique modulo the product of the moduli.
Also called: CRT

## Where the argument relies on this page

- The radix-digit coefficients are placed on distinct prime cyclic axes by a Chinese-remainder map that preserves convolution. (on [Chinese-remainder map](chinese-remainder-map.md))

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

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Congruence](congruence-modulo.md): Two integers are congruent modulo m when their difference is divisible by m; a residue is the class of an integer modulo m.
  Shown as: Chinese remainder theorem *<predicate>* Congruence
- [Coprime](coprime.md): Two integers are coprime when their greatest common divisor is 1; a set of integers is pairwise coprime when every two of them are coprime.
  Shown as: Chinese remainder theorem *<predicate>* Coprime

## Pages that build on this one

- Cyclic convolution: The product of two sequences in which indices wrap around modulo the sequence length.
- Cost table: The list of separate running-time terms of an algorithm, each a power of the input size, whose sum bounds the total time.

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
- [Incidence](incidence.md)
- [Tensor product](tensor-product.md)
- [Carry propagation](carry-propagation.md)
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
- [Bilinear form](bilinear-form.md)
- [Orthogonal complement](orthogonal-complement.md)
- [Indicator vector](indicator-vector.md)
- [Line spanned by a vector](line-spanned-by-vector.md)
- [Subspace labels](subspace-labels.md)
- [Subset-intersection network](subset-intersection-network.md)
- [Scratch storage](scratch-storage.md)
- [Address-field interchange](address-interchange.md)
- [Exclusive or](xor.md)
- [Gram matrix](gram-matrix.md)
- [Complex phase network](complex-phase-network.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Guard-width bound](guard-width-bound.md)
- [Numerical layer](numerical-layer.md)
- [Union bound](union-bound.md)
- [Transform round](transform-round.md)
- [Tape procedure](tape-procedure.md)
- [Stream](stream.md)
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
- [Bit construction](bit-construction.md)
- [Complex construction](complex-construction.md)
- [Rank-saving recursion](rank-saving-recursion.md)
- [Family parameter](family-parameter.md)
- [Packed selected-bit addition](packed-bit-addition.md)
- [Integer multiplication below n log n](main-theorem.md)

## Evidence from the sources

- "Chinese remainder theorem" (paper)

## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- $J$ means number of congruences here, but family size on [Coprime](coprime.md), which this page builds on: Different: $J$ means number of congruences on chinese-remainder-theorem but family size on Coprime. The later page should use another letter for number of congruences, or say explicitly where $J$ keeps this meaning instead of family size.
- $J$ means number of congruences here, but digit count on [Radix-digit convolution](radix-digit-convolution.md), which this page builds on: Different: $J$ means number of congruences on chinese-remainder-theorem but digit count on Radix-digit convolution. The later page should use another letter for number of congruences, or say explicitly where $J$ keeps this meaning instead of digit count.
- $J$ means number of congruences here, but block length on [Cyclic shift](cyclic-shift.md), which this page builds on: Different: $J$ means number of congruences on chinese-remainder-theorem but block length on Cyclic shift. The later page should use another letter for number of congruences, or say explicitly where $J$ keeps this meaning instead of block length.
- $\sigma$ means congruence index here, but dummy index on [Discrete Fourier transform](discrete-fourier-transform.md), which this page builds on: Different: $\sigma$ means congruence index on chinese-remainder-theorem but dummy index on Discrete Fourier transform. The later page should use another letter for congruence index, or say explicitly where $\sigma$ keeps this meaning instead of dummy index.
- $\sigma$ means congruence index here, but class member on [Congruence](congruence-modulo.md), which this page builds on: Different: $\sigma$ means congruence index on chinese-remainder-theorem but class member on Congruence. The later page should use another letter for congruence index, or say explicitly where $\sigma$ keeps this meaning instead of class member.
- $\sigma$ means congruence index here, but index bit on [Butterfly](butterfly.md), which this page builds on: Different: $\sigma$ means congruence index on chinese-remainder-theorem but index bit on Butterfly. The later page should use another letter for congruence index, or say explicitly where $\sigma$ keeps this meaning instead of index bit.
- $\sigma$ means congruence index here, but offset on [Cyclic shift](cyclic-shift.md), which this page builds on: Different: $\sigma$ means congruence index on chinese-remainder-theorem but offset on Cyclic shift. The later page should use another letter for congruence index, or say explicitly where $\sigma$ keeps this meaning instead of offset.
- $\sigma$ means congruence index here, but permutation on [Permutation](permutation.md), which this page builds on: Different: $\sigma$ means congruence index on chinese-remainder-theorem but permutation on Permutation. The later page should use another letter for congruence index, or say explicitly where $\sigma$ keeps this meaning instead of permutation.
- $\sigma$ means congruence index here, but source element on [Bijection](bijection.md), which this page builds on: Different: $\sigma$ means congruence index on chinese-remainder-theorem but source element on Bijection. The later page should use another letter for congruence index, or say explicitly where $\sigma$ keeps this meaning instead of source element.
- $W_\sigma$ means modulus here, but prefix product on [Coprime](coprime.md), which this page builds on: Different: $W_\sigma$ means modulus on chinese-remainder-theorem but prefix product on Coprime. The later page should use another letter for modulus, or say explicitly where $W_\sigma$ keeps this meaning instead of prefix product.
- $Y$ means unknown integer here, but common multiple on [Coprime](coprime.md), which this page builds on: Different: $Y$ means unknown integer on chinese-remainder-theorem but common multiple on Coprime. The later page should use another letter for unknown integer, or say explicitly where $Y$ keeps this meaning instead of common multiple.
- $\Gamma$ means product of moduli here, but padded address set on [Bijection](bijection.md), which this page builds on: Different: $\Gamma$ means product of moduli on chinese-remainder-theorem but padded address set on Bijection. The later page should use another letter for product of moduli, or say explicitly where $\Gamma$ keeps this meaning instead of padded address set.
- $D$ means difference of solutions here, but axis count on [Transform axis](transform-axis.md), which this page builds on: Different: $D$ means difference of solutions on chinese-remainder-theorem but axis count on Transform axis. The later page should use another letter for difference of solutions, or say explicitly where $D$ keeps this meaning instead of axis count.

## Previous version (revise it)

It has 540 words. Fix the problems by restructuring rather than appending: keep the rewrite within 675 words, a quarter more, unless a problem cannot be fixed without more. Pages that grow with every repair stop being self-contained explanations of one concept.

The Chinese remainder theorem says when a system of congruences has a solution, and how many solutions it has. It is the arithmetic fact behind the [Chinese-remainder map](chinese-remainder-map.md), which relabels the positions of a [cyclic convolution](cyclic-convolution.md) so that it becomes a multidimensional one.

The theorem concerns a system of [congruences](congruence-modulo.md) with pairwise coprime moduli. Let $J$ be the number of congruences. Index them by $\sigma=1,\dots,J$. For each $\sigma$, let $W_\sigma$ be the modulus, a positive integer, and $\varrho_\sigma$ the residue, an integer. The unknown is an integer $Y$, and $Y$ is a solution when

$$Y \equiv \varrho_\sigma \pmod{W_\sigma} \qquad \text{for every } \sigma=1,\dots,J.$$

The theorem requires moduli that are pairwise [coprime](coprime.md): any two of $W_1,\dots,W_J$ have greatest common divisor $1$. Let $\Gamma = W_1W_2\cdots W_J$ be the product of all the moduli, a positive integer.

The statement is this. If the moduli are pairwise coprime, then the system has a solution, and an integer $Y'$ is also a solution exactly when $Y' \equiv Y \pmod{\Gamma}$. So the solutions form one residue class modulo $\Gamma$. Read as a map, this says that an integer modulo $\Gamma$ is determined by its residues modulo $W_1,\dots,W_J$, and that every tuple of such residues occurs.

Coprimality cannot be dropped. Take the moduli $2$ and $4$ with residues $0$ and $1$. The first congruence says $Y$ is even and the second says $Y$ is odd, so no solution exists.

Uniqueness. Suppose $Y$ and $Y'$ are both solutions, and let $D=Y'-Y$. Then every $W_\sigma$ divides $D$. We show by induction on $\sigma$ that $W_1W_2\cdots W_\sigma$ divides $D$. The case $\sigma=1$ holds. Suppose $D=W_1\cdots W_\sigma\,\Delta$ for an integer $\Delta$. The integer $W_{\sigma+1}$ shares no prime factor with $W_1\cdots W_\sigma$: a prime dividing both would divide some $W_{\sigma'}$ with $\sigma'\le\sigma$, since a prime dividing a product divides one of its factors, and that contradicts pairwise coprimality. Since $W_{\sigma+1}$ divides $D=W_1\cdots W_\sigma\,\Delta$ and is coprime to $W_1\cdots W_\sigma$, Euclid's lemma gives $W_{\sigma+1}\mid\Delta$. Hence $W_1\cdots W_{\sigma+1}$ divides $D$. Taking $\sigma=J$ gives $\Gamma\mid D$, so $Y'\equiv Y \pmod{\Gamma}$.

Existence. Fix $\sigma$. The integer $\Gamma/W_\sigma$ is the product of the other moduli. The argument above shows that $\Gamma/W_\sigma$ and $W_\sigma$ share no prime factor, so their greatest common divisor is $1$. By Bézout's identity there are integers $\varpi_\sigma$ and $\Xi_\sigma$ with $\varpi_\sigma\,\Gamma/W_\sigma+\Xi_\sigma\,W_\sigma=1$. Reducing modulo $W_\sigma$ gives $\varpi_\sigma\,\Gamma/W_\sigma\equiv 1 \pmod{W_\sigma}$. Put

$$Y=\sum_{\sigma=1}^{J}\varrho_\sigma\,\varpi_\sigma\,\frac{\Gamma}{W_\sigma}.$$

Fix $\sigma_0$ and reduce modulo $W_{\sigma_0}$. For $\sigma\ne\sigma_0$, the factor $\Gamma/W_\sigma$ contains $W_{\sigma_0}$, so that term is divisible by $W_{\sigma_0}$. The $\sigma_0$ term is congruent to $\varrho_{\sigma_0}$, because $\varpi_{\sigma_0}\,\Gamma/W_{\sigma_0}\equiv 1$. So $Y\equiv\varrho_{\sigma_0} \pmod{W_{\sigma_0}}$ for every $\sigma_0$.

For example, take $J=3$, moduli $3$, $4$, $5$ (pairwise coprime, so $\Gamma=60$), and residues $2$, $3$, $1$. Then $\Gamma/3=20$, $\Gamma/4=15$ and $\Gamma/5=12$. The inverses are $\varpi_1=2$, since $2\cdot 20=40\equiv 1 \pmod 3$; $\varpi_2=3$, since $3\cdot 15=45\equiv 1 \pmod 4$; and $\varpi_3=3$, since $3\cdot 12=36\equiv 1 \pmod 5$. So

$$Y = 2\cdot 2\cdot 20+3\cdot 3\cdot 15+1\cdot 3\cdot 12 = 80+135+36 = 251.$$

Since $251=4\cdot 60+11$, the solutions are exactly the integers $11+60k$ for integers $k$. Check: $11$ leaves remainder $2$ mod $3$, remainder $3$ mod $4$, and remainder $1$ mod $5$.

The paper uses the same kind of split. Agarwal and Cooley <cite data-source="paper">used the Chinese remainder theorem to convert one cyclic convolution into multidimensional</cite> cyclic convolution. The paper's map then places its coefficient list on distinct prime cyclic axes <cite data-source="paper">by a Chinese-remainder map that preserves convolution</cite>.

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

Write the body to `exegenius/tasks/0794-write-chinese-remainder-theorem.answer.md` and the JSON to `exegenius/tasks/0794-write-chinese-remainder-theorem.answer.json`, then run `exegenius submit 0794-write-chinese-remainder-theorem` in the project directory. If submit rejects the answer, fix the answer and submit again.
