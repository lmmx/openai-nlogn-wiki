# exegenius task 0754-write-synthetic-transforms

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
- Exact integer multiplication (also: exact multiplication, Binary product)
- Discrete Fourier transform (also: normalized Fourier transform, transform, Fourier transform, normalized form, frequency order)
- Transform axis (also: axis, remaining axes, reduction axis, participating axis)
- Linear algebra basics (also: linear algebra: invertible linear operator, matrix, inverse, matrix, linear map, usual axioms, basis)
- Convolution
- Running time cost (also: cost, linear-cost update, bit-complexity bound, linear tape time)
- Little-o notation (also: limit as lambda tends to infinity)
- Mixed-radix digits (also: mixed-radix digit, digit)
- Array norm (also: norm of an array, coefficient bound, norm of a vector)
- Payload (also: record)
- Truncation
- Address (also: binary addresses, least significant end)
- Array (also: disk array, disk-grid ring array)
- Logarithm (also: logarithm lg)
- Base-2 logarithm (also: logarithm and ceiling)
- Ceiling function
- Big-Theta notation
- Extended real numbers
- Mathematical induction (also: induction)
- Integer
- Root of unity (also: roots of unity, primitive root of unity)
- Supremum
- Telescoping identity (also: signed dimension changes, source and sink dimensions)
- Fixed-width digit blocks (also: B-adic blocks)
- Exceptional set (also: bad addresses)
- Big-Omega notation
- Bit-reversed index order
- Directed graph (also: directed graph (vertices))
- Real numbers (also: Real number)

## This page

Concept: Synthetic polynomial transforms
Gloss: Fourier-type transforms whose roots of unity are powers of y in a polynomial ring, so that multiplying by a root is a signed shift of coefficients.
Also called: Nussbaumer polynomial transforms, polynomial transforms, Nussbaumer and Quandalle, the paper's representation

## This page in the argument

The step: The transforms are synthetic polynomial transforms whose roots of unity are powers of $y$.
How: evaluate the transforms with polynomial roots of unity
Why: Roots of unity that are powers of the variable cost only shifts and signs, so each transform reduces to address rearrangement and two-point butterflies. (the sources leave this for the reader to work out: spell it out)

Its sub-steps, in order:

- The transforms are the synthetic polynomial transforms of Nussbaumer and Quandalle.

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

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Discrete Fourier transform](discrete-fourier-transform.md): The map sending a vector of q values to its q values weighted by powers of a q-th root of unity, normalized by 1/q.
  Shown as: Synthetic polynomial transforms *<predicate>* Discrete Fourier transform
- [Bit-reversed index order](bit-reversed-order.md): The order of array positions obtained by reversing the binary digits of each index.
  Shown as: Synthetic polynomial transforms *<predicate>* Bit-reversed index order

## Pages that build on this one

- Polynomial ring modulo y^r + 1: The ring of polynomials with complex coefficients in which y^r is identified with −1, so that y has order 2r and wrap-around flips a sign.
- Multidimensional transform: A Fourier transform over several axes at once, computed by transforming along each axis in turn.
- Gaussian resampling: A technique that replaces a Fourier transform of arbitrary length by transforms whose axis lengths are powers of two, using Gaussian weights to move between the two sets of frequencies.
- Transform layout: A permutation of address bits that places the selected bits of all participating axes at a common offset in consecutive chunks, so that a simultaneous butterfly layer applies to each transform round.
- Convolution over the polynomial ring: The normalized product of two arrays of records in the polynomial ring, computed by two forward synthetic transforms, a pointwise product, and an opposite transform.

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
- [Directed graph](directed-graph.md)
- [Linear algebra basics](linear-algebra-basics.md)
- [Transform axis](transform-axis.md)
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
- [Incidence](incidence.md)
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

- "These are the synthetic polynomial transforms of Nussbaumer and Quandalle and" (paper)

## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The quotation does not support the claim it is attached to (unsupported): ", and attributes the method:" cites "The polynomial roots and radix-two butterflies belong to the fast polynomial-transform method": The claim asserts that the source attributes the method to someone; the quotation says the roots and butterflies belong to the fast polynomial-transform method and attributes nothing to any person. Say only what the source supports, or cite the passage that supports the claim.
- $\rho$ means coefficient position here, but exponent on [Discrete Fourier transform](discrete-fourier-transform.md), which this page builds on: Different: $\rho$ means coefficient position on synthetic-transforms but exponent on Discrete Fourier transform. The later page should use another letter for coefficient position, or say explicitly where $\rho$ keeps this meaning instead of exponent.
- $\sigma$ means shift count here, but dummy index on [Discrete Fourier transform](discrete-fourier-transform.md), which this page builds on: Different: $\sigma$ means shift count on synthetic-transforms but dummy index on Discrete Fourier transform. The later page should use another letter for shift count, or say explicitly where $\sigma$ keeps this meaning instead of dummy index.
- $f$ means input list here, but input vector on [Discrete Fourier transform](discrete-fourier-transform.md), which this page builds on: Different: $f$ means input list on synthetic-transforms but input vector on Discrete Fourier transform. The later page should use another letter for input list, or say explicitly where $f$ keeps this meaning instead of input vector.
- $j$ means entry index here, but coordinate index on [Linear algebra basics](linear-algebra-basics.md), which this page builds on: Different: $j$ means entry index on synthetic-transforms but coordinate index on Linear algebra basics. The later page should use another letter for entry index, or say explicitly where $j$ keeps this meaning instead of coordinate index.
- $j$ means entry index here, but input position in b on [Convolution](convolution.md), which this page builds on: Different: $j$ means entry index on synthetic-transforms but input position in b on Convolution. The later page should use another letter for entry index, or say explicitly where $j$ keeps this meaning instead of input position in b.
- $\eta$ means half-size here, but scalar on [Linear algebra basics](linear-algebra-basics.md), which this page builds on: Different: $\eta$ means half-size on synthetic-transforms but scalar on Linear algebra basics. The later page should use another letter for half-size, or say explicitly where $\eta$ keeps this meaning instead of scalar.
- $\gamma$ means block offset here, but scalar on [Linear algebra basics](linear-algebra-basics.md), which this page builds on: Different: $\gamma$ means block offset on synthetic-transforms but scalar on Linear algebra basics. The later page should use another letter for block offset, or say explicitly where $\gamma$ keeps this meaning instead of scalar.

## Previous version (revise it)

It has 958 words. Fix the problems by restructuring rather than appending: keep the rewrite within 1197 words, a quarter more, unless a problem cannot be fixed without more. Pages that grow with every repair stop being self-contained explanations of one concept.

Synthetic polynomial transforms are Fourier-type transforms whose roots of unity are powers of a polynomial variable $y$, so multiplying a value by a root only moves its coefficients and changes some signs. They are the normalized Fourier transforms that the convolutions in the proof of [Integer multiplication below n log n](main-theorem.md) need, and the sign-and-shift roots make those transforms cost only moves and additions. The source's main result is <cite data-source="paper">a deterministic algorithm that multiplies two n-bit integers in</cite> $O(n(\lg n)^{1-\kappa})$ time, where $\kappa$ is a fixed positive constant.

## Records and signed shifts

Write $R_r = \mathbb{C}[y]/(y^r+1)$ for the ring of polynomials in the variable $y$ with complex coefficients, in which $y^r$ is identified with $-1$. Here $r \ge 2$ is a power of two, and $r$ is the number of complex coefficients in a record. This is the [polynomial ring modulo $y^r+1$](polynomial-ring-mod-yr-plus-1.md). A record is an element of $R_r$, stored as its $r$ coefficients $c_\rho$, one for each power $y^\rho$, where the position $\rho$ runs from $0$ to $r-1$.

Let $\sigma$, with $0 \le \sigma < 2r$, be the number of places a shift moves each coefficient. For a coefficient at position $\rho$, let $\mu_\rho = \lfloor (\rho+\sigma)/r \rfloor$ be the number of times the shift carries it past position $r-1$, where $\lfloor x \rfloor$ is the largest integer not exceeding $x$. Since $\rho+\sigma = \mu_\rho r + ((\rho+\sigma) \bmod r)$, we get $y^{\rho+\sigma} = (y^r)^{\mu_\rho} y^{(\rho+\sigma) \bmod r} = (-1)^{\mu_\rho} y^{(\rho+\sigma) \bmod r}$, and so

$$y^\sigma \sum_{\rho=0}^{r-1} c_\rho y^\rho = \sum_{\rho=0}^{r-1} (-1)^{\mu_\rho}\, c_\rho\, y^{(\rho+\sigma) \bmod r}.$$

Here $(\rho+\sigma) \bmod r$ is the remainder of $\rho+\sigma$ on division by $r$, a position in $\{0,\dots,r-1\}$. Since $\rho \le r-1$ and $\sigma < 2r$, each $\mu_\rho$ is $0$, $1$ or $2$. So multiplying by $y^\sigma$ moves each coefficient $\sigma$ places along the list, cyclically, and negates those that wrap past the end an odd number of times. No rounding or multiplication is needed.

For example, take $r = 4$ and $\sigma = 2$. Then $y^2(c_0 + c_1 y + c_2 y^2 + c_3 y^3) = -c_2 - c_3 y + c_0 y^2 + c_1 y^3$, so $(c_0, c_1, c_2, c_3)$ becomes $(-c_2, -c_3, c_0, c_1)$.

## Roots of unity

Let $N$ be a power of two dividing $2r$, the number of entries in the transform. The letter $j$ changes meaning here: it is an index running from $0$ to $N-1$ that numbers the entries, not the coordinate index of earlier pages. The root $\omega_N = y^{2r/N}$ is a primitive $N$-th root of unity in $R_r$, meaning $\omega_N^N = 1$ and $\omega_N^j \ne 1$ for $0<j<N$. The subscript keeps this polynomial root apart from the complex root $\omega$ of the Discrete Fourier transform page. First, $\omega_N^N = y^{2r} = (y^r)^2 = 1$. For $0<j<N$, write $\omega_N^j = y^a$ with $a = 2rj/N$, an integer with $0<a<2r$. If $a<r$, then $y^a$ is a basis element other than $1$, so its constant coefficient is $0$. If $a=r$, then $\omega_N^j=-1 \ne 1$. If $r<a<2r$, then $y^a=-y^{a-r}$, where $1 \le a-r < r$, so again its constant coefficient is $0$. In every case $\omega_N^j \ne 1$. Each power $\omega_N^j$ with $0 \le j < N$ is thus a shift by $2rj/N < 2r$ places, so multiplying by it is a signed shift. For example, with $N=4$ and $r=2$, $\omega_4 = y$ and $\omega_4^2 = y^2 = -1$, so multiplying by $\omega_4^2$ negates both coefficients of a record.

## The transform

The input is $f = (f_0,\dots,f_{N-1})$, a list of $N$ records, and $f_j$ is its $j$-th entry. The output is $Z = (Z_0,\dots,Z_{N-1})$, the transformed list. The letter $\ell$ is the output index, from $0$ to $N-1$.

$$Z_\ell = \frac{1}{N}\sum_{j=0}^{N-1} \omega_N^{j\ell}\, f_j.$$

A synthetic polynomial transform is a polynomial-ring form of the [Discrete Fourier transform](discrete-fourier-transform.md), with its roots taken in $R_r$. The source says <cite data-source="paper">These are the synthetic polynomial transforms of Nussbaumer and Quandalle</cite>, and attributes the method: <cite data-source="paper">The polynomial roots and radix-two butterflies belong to the fast polynomial-transform method</cite> of Nussbaumer and Quandalle.

## Why the roots make the transform cheap

Every root in the transform is a power of $y$, so every multiplication by a root is a signed shift with no arithmetic. The fast method computes $Z$ in $\log_2 N$ levels, where $\log_2 N$ is the base-2 logarithm of $N$. The transform first orders the records by [bit-reversed index order](bit-reversed-order.md), an address rearrangement that moves stored records without arithmetic. A level has half-size $\eta$, the number of positions in each half of a block, taking the values $1, 2, 4, \dots, N/2$, and groups the records into blocks of $2\eta$ consecutive positions. In each block, each offset $\gamma$ from $0$ to $\eta-1$ gives a pair of entries $U$ and $W$ at positions $\gamma$ and $\gamma+\eta$ of the block. Let $\theta = \omega_N^{\gamma N/(2\eta)}$ be the twiddle of that butterfly, a power of $\omega_N$. The pair is replaced by

$$(U+\theta W,\ U-\theta W).$$

This replacement is a [two-point butterfly](butterfly.md): it forms the sum and the difference of two entries, after one of them is multiplied by a twiddle. Since $\gamma<\eta$, the exponent $\gamma N/(2\eta)$ is below $N$, so $\theta = y^{r\gamma/\eta}$, because $(2r/N)\cdot\gamma N/(2\eta) = r\gamma/\eta$. Thus $\theta$ is a signed shift by $r\gamma/\eta$ places. This number is an integer because $\eta$ is a power of two at most $N/2$, and $N/2$ divides $r$ since $N$ divides $2r$. Forming $\theta W$ is therefore a signed shift with no multiplication. The butterfly costs one record addition and one record subtraction, each of $r$ coefficient additions. In a complex transform the same twiddle would be a genuine complex multiplication. The source states the cost as <cite data-source="paper">the transform calculation consists of address rearrangements, signed</cite> <cite data-source="paper">shifts, and two-point butterfly operations</cite>.

Each level has $N/2$ butterflies, and there are $\log_2 N$ levels. The transform therefore uses $O(Nr\log_2 N)$ coefficient additions and moves and no coefficient multiplication. After the level with $\eta = N/2$, the records hold the unnormalized sums, which are $N$ times $Z_\ell$, so the factor $1/N$ is applied last.

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

Write the body to `exegenius/tasks/0754-write-synthetic-transforms.answer.md` and the JSON to `exegenius/tasks/0754-write-synthetic-transforms.answer.json`, then run `exegenius submit 0754-write-synthetic-transforms` in the project directory. If submit rejects the answer, fix the answer and submit again.
