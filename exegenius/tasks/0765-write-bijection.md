# exegenius task 0765-write-bijection

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
- Synthetic polynomial transforms (also: Nussbaumer polynomial transforms, polynomial transforms, Nussbaumer and Quandalle, the paper's representation)
- Transform axis (also: axis, remaining axes, reduction axis, participating axis)
- Linear algebra basics (also: linear algebra: invertible linear operator, matrix, inverse, matrix, linear map, usual axioms, basis)
- Bilinear map (also: bilinear product, bilinear contraction)
- Linear contraction (also: contraction)
- Convolution
- Coprime (also: gcd, pairwise coprime, coprime (gcd))
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
- Bézout's identity (also: Bezout's identity)
- Big-Theta notation
- Cyclic group (also: cyclic group of order S)
- Order of an element (also: multiplicative order)
- Diagonal scaling
- Extended real numbers
- Frequency domain
- Mathematical induction (also: induction)
- Integer
- Projection along a subspace
- Root of unity (also: roots of unity, primitive root of unity)
- Supremum
- Telescoping identity (also: signed dimension changes, source and sink dimensions)
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

Concept: Bijection
Gloss: A map that is one-to-one and onto, so that every element of the target is hit by exactly one element of the source.

## Where the argument relies on this page

- Two disjoint contiguous address fields of $u$ bits in an array can be interchanged in $O(V u^{\tau})$ time for a fixed $\tau<1$, where $V$ is the stored bit volume. (on [Address-field interchange](address-interchange.md))
- Each tape procedure is a fixed linear network that exchanges two banks of values and restores its scratch values. (on [Linear networks and frames](linear-network-frames.md))

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

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Floor function](floor-function.md): The greatest integer that is not greater than a given real number.
  Shown as: Bijection *<predicate>* Floor function
- [Exceptional set](exceptional-set.md): The set of addresses at which a generic formula must be replaced by a special rule; the generic formula is correct everywhere outside it.
  Shown as: Bijection *<predicate>* Exceptional set

## Pages that build on this one

- Permutation: A bijection of a finite set onto itself, which rearranges the positions of a sequence.
- Transform identity with retained permutations: The Gaussian resampling identity in which the source and target coordinate permutations are kept as part of the formula, so that they cancel across a convolution instead of being executed as sorts.

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

- "bijection" (paper)

## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The quotation does not support the claim it is attached to (unsupported): "Its update lines each change one chunk of each address, and" cites "so each line is a bijection of the rectangle": The quotation only says each line is a bijection of the rectangle; it says nothing about update lines changing one chunk of each address. Say only what the source supports, or cite the passage that supports the claim.
- The quotation does not support the claim it is attached to (unsupported): "(The paper's $B$ is $G$.)" cites "The ideal map T0 preserves all guard values and therefore preserves B.": The quotation mentions B as a set preserved by T0 but does not identify B with G, which is what the claim asserts. Say only what the source supports, or cite the passage that supports the claim.
- $\xi$ means target element here, but real argument on [Floor function](floor-function.md), which this page builds on: Different: $\xi$ means target element on bijection but real argument on Floor function. The later page should use another letter for target element, or say explicitly where $\xi$ keeps this meaning instead of real argument.

## Previous version (revise it)

It has 437 words. Fix the problems by restructuring rather than appending: keep the rewrite within 546 words, a quarter more, unless a problem cannot be fixed without more. Pages that grow with every repair stop being self-contained explanations of one concept.

A bijection is a map that can be undone: it sends different inputs to different outputs and misses no output. Rearranging stored data by a bijection, such as a [Permutation](permutation.md), moves every value and loses or duplicates none.

A set is a collection of distinct objects. Let $U$ and $W$ be sets, the source set $U$ and the target set $W$, and let $f\colon U\to W$ be a map, which sends each element $\sigma$ of $U$ to an element $f(\sigma)$ of $W$. The map $f$ is a bijection when it is one-to-one and onto:

- one-to-one: if $f(\sigma)=f(\sigma')$ for $\sigma,\sigma'\in U$, then $\sigma=\sigma'$;
- onto: for every $\xi\in W$ there is some $\sigma\in U$ with $f(\sigma)=\xi$, so every target is hit.

So each $\xi\in W$ is hit by exactly one $\sigma\in U$, and the inverse $f^{-1}\colon W\to U$ sends $\xi$ to that $\sigma$. Thus $f^{-1}(f(\sigma))=\sigma$: applying $f^{-1}$ undoes $f$.

**Example.** Take $U=W=\{0,1,2,3\}$ and $f(\sigma)=\sigma+1 \bmod 4$, where $a \bmod 4$ is the remainder of $a$ after division by $4$. Then $0\mapsto1$, $1\mapsto2$, $2\mapsto3$, $3\mapsto0$, so each target is hit once and $f$ is a bijection. A non-example is illustrated using the [Floor function](floor-function.md): the map $f_2(\sigma)=\lfloor \sigma/2\rfloor$ on the same sets is not a bijection, because $f_2(0)=f_2(1)=0$ and the targets $2$ and $3$ are never hit, so it has no inverse.

For a subset $G\subseteq U$, the set of elements singled out by the argument, write $G^c=U\setminus G$ for its complement. If $f$ is a bijection of $U$ onto $W$, then $f(G^c)=W\setminus f(G)$: the images of $G$ and $G^c$ are disjoint by one-to-one and cover $W$ by onto. So if two bijections $f$ and $g$ of $U$ onto itself agree outside $G$, then $f(G)=g(G)$, and if also $g(G)=G$, then $f(G)=G$.

The paper uses this in its address-field interchange, which <cite data-source="paper">interchanges two disjoint contiguous address fields of u bits in an array</cite>. Its update lines each change one chunk of each address, and <cite data-source="paper">so each line is a bijection of the rectangle</cite>. Two bijections of the rectangle, $S_0$ (the one its update lines compose to) and $T_0$ (the ideal one), agree outside $G$, the [Exceptional set](exceptional-set.md) of bad addresses, so they are compared on the complement of $G$. <cite data-source="paper">Both T0 and S0 are bijections, and they agree off B.</cite> (The paper's $B$ is $G$.) <cite data-source="paper">The ideal map T0 preserves all guard values and therefore preserves B.</cite> <cite data-source="paper">Taking complements in the finite rectangle gives</cite> $S_0(G^c)=T_0(G^c)=G^c$, so $S_0(G)=G$. Its intermediate steps are not moves: <cite data-source="paper">Although its final effect is an exact permutation, its intermediate steps form pointwise XOR combinations of data.</cite>

The second use is a tape procedure, a fixed procedure on one-dimensional Turing machine tapes that rearranges the bits stored on them. Its padded address set $\Gamma$ is a set of integer addresses on which the step acts. The paper states that <cite data-source="paper">bijection of P: for fixed controls and spectators it is a cyclic permutation of the valid target interval</cite>. For the valid interval $\{0,1,2,3\}$ and offset $1$, this is the map $f$ above, and rotating back by $-1$ undoes it. The paper also gives <cite data-source="paper">An inverse is explicit</cite>, so the stored data can be recovered after the step.

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

Write the body to `exegenius/tasks/0765-write-bijection.answer.md` and the JSON to `exegenius/tasks/0765-write-bijection.answer.json`, then run `exegenius submit 0765-write-bijection` in the project directory. If submit rejects the answer, fix the answer and submit again.
