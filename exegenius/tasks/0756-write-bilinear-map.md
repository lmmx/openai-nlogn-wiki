# exegenius task 0756-write-bilinear-map

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
- Linear contraction (also: contraction)
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

Concept: Bilinear map
Gloss: A map that is linear in each of two vector arguments separately, such as the product of two polynomials.
Also called: bilinear product, bilinear contraction

## Where the argument relies on this page

- A linear network on the three-element subsets of a ground set exchanges two banks of values and restores its scratch wires. (on [Subset-intersection network](subset-intersection-network.md))
- Convolution on the remaining axes over the polynomial ring is computed by two forward synthetic transforms, a pointwise product, an opposite transform, and packed integer products. (on [Convolution over the polynomial ring](polynomial-ring-convolution.md))

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

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Linear algebra basics](linear-algebra-basics.md): Vector spaces over a field, linear maps and matrices, and the inverse of an invertible linear operator.
  Shown as: Bilinear map *<predicate>* Linear algebra basics
- [Array](array.md): A finite collection of entries, each stored at an address and carrying a payload.
  Shown as: Bilinear map *<predicate>* Array
- [Array norm](array-norm.md): The maximum modulus over all entries of an array of complex values; an array has norm at most one exactly when every entry has modulus at most one.
  Shown as: Bilinear map *<predicate>* Array norm

## Pages that build on this one

- Bilinear form: A bilinear map from a vector space and itself to its scalars; a space with such a form is nondegenerate when the form has no nonzero vector orthogonal to everything, and two vectors are orthogonal when the form vanishes on them.
- Exact coefficient recovery: The error analysis showing that the computed convolution coefficients are within a half of their true integer values, so rounding recovers them exactly.

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
- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Transform axis](transform-axis.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Linear contraction](linear-contraction.md)
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

- "The exact map P is bilinear and satisfies" (paper)

## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The quotation does not support the claim it is attached to (unsupported): "the bound $\|P(\xi,\zeta)\|\le\|\xi\|\,\|\zeta\|$," cites "by the coefficient bound in": The fragment only refers to a coefficient bound; it does not state the inequality ||P(xi,zeta)|| <= ||xi|| ||zeta||, nor that P is a contraction. Say only what the source supports, or cite the passage that supports the claim.
- $V$ means second argument space here, but stored bit volume on [Array](array.md), which this page builds on: Different: $V$ means second argument space on bilinear-map but stored bit volume on Array. The later page should use another letter for second argument space, or say explicitly where $V$ keeps this meaning instead of stored bit volume.
- $V$ means second argument space here, but stream volume on [Payload](payload.md), which this page builds on: Different: $V$ means second argument space on bilinear-map but stream volume on Payload. The later page should use another letter for second argument space, or say explicitly where $V$ keeps this meaning instead of stream volume.
- $V$ means second argument space here, but vertex set on [Directed graph](directed-graph.md), which this page builds on: Different: $V$ means second argument space on bilinear-map but vertex set on Directed graph. The later page should use another letter for second argument space, or say explicitly where $V$ keeps this meaning instead of vertex set.

## Previous version (revise it)

It has 379 words. Fix the problems by restructuring rather than appending: keep the rewrite within 473 words, a quarter more, unless a problem cannot be fixed without more. Pages that grow with every repair stop being self-contained explanations of one concept.

A bilinear map takes one vector from each of two vector spaces and returns a vector in a third, linear in each argument while the other is held fixed. The paper's error analysis uses one to bound the error of a product of two approximate values, one operand at a time.

A bilinear map is defined through the linear maps of [Linear algebra basics](linear-algebra-basics.md): fixing one argument must give a linear map in the other. Here $U$ and $V$ are the argument spaces and $W$ is the output space, over the scalar field $F$. Let $\pi\colon U\times V\to W$ send each pair $(\xi,\zeta)$, with $\xi\in U$ and $\zeta\in V$, to a vector $\pi(\xi,\zeta)$ in $W$. The map $\pi$ is *bilinear* when $\xi\mapsto\pi(\xi,\zeta)$ is linear for each fixed $\zeta$, and $\zeta\mapsto\pi(\xi,\zeta)$ is linear for each fixed $\xi$.

Let $U=V=\mathbb{C}^2$ and $W=\mathbb{C}$, and let $\pi$ send a pair of vectors to the sum of their coordinatewise products. Then $\pi\big((1,2),(3,4)\big)=1\cdot 3+2\cdot 4=11$, and doubling the first argument doubles the output: $\pi\big((2,4),(3,4)\big)=22$. Adding a constant breaks bilinearity: $(\xi,\zeta)\mapsto\pi(\xi,\zeta)+1$ sends $(0,\zeta)$ to $1$, but a linear map in $\xi$ must send $0$ to $0$.

In the paper, $U$, $V$, and $W$ are spaces of [Array](array.md) values, so a bilinear map is applied to arrays. A bilinear map is a *bilinear contraction* when it is bounded in the [Array norm](array-norm.md): $\|\pi(\xi,\zeta)\|\le\|\xi\|\,\|\zeta\|$. For arrays whose entries are records (polynomials in $y$ modulo $y^r+1$), the norm is the largest coefficient modulus: <cite data-source="paper">over Rr , the same notation denotes the maximum over all coefficients in all entries.</cite> A *disk array* is an array of norm at most one, so every entry has modulus at most one.

The paper's error analysis works with an exact bilinear map $P$: the pointwise product, which multiplies the two entries at each address, with products of records taken modulo $y^r+1$ and then divided by $r$. <cite data-source="paper">The exact map P is bilinear and satisfies</cite> the bound $\|P(\xi,\zeta)\|\le\|\xi\|\,\|\zeta\|$, <cite data-source="paper">by the coefficient bound in</cite> Lemma 17, so $P$ is a bilinear contraction.

Let $\xi'$ and $\zeta'$ be computed approximations of $\xi$ and $\zeta$, and suppose all four are disk arrays. With one operand fixed, linearity gives $\pi(\xi',\zeta)-\pi(\xi,\zeta)=\pi(\xi'-\xi,\zeta)$, and if $\zeta$ is a disk array, $\|\pi(\xi'-\xi,\zeta)\|\le\|\xi'-\xi\|$. So <cite data-source="paper">replacing one operand changes the output by at most the norm</cite> of the difference.

Splitting the change into two single-operand changes,
$$\pi(\xi',\zeta')-\pi(\xi,\zeta)=\pi(\xi'-\xi,\zeta')+\pi(\xi,\zeta'-\zeta).$$
The first term is bounded using the disk bound on $\zeta'$: $\|\pi(\xi'-\xi,\zeta')\|\le\|\xi'-\xi\|\,\|\zeta'\|\le\|\xi'-\xi\|$. The second is bounded by the disk bound on $\xi$: $\|\pi(\xi,\zeta'-\zeta)\|\le\|\xi\|\,\|\zeta'-\zeta\|\le\|\zeta'-\zeta\|$. Adding them gives
$$\|\pi(\xi',\zeta')-\pi(\xi,\zeta)\|\le\|\xi'-\xi\|+\|\zeta'-\zeta\|.$$
<cite data-source="paper">When all four operands are in the disk, their two errors therefore add.</cite>

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

Write the body to `exegenius/tasks/0756-write-bilinear-map.answer.md` and the JSON to `exegenius/tasks/0756-write-bilinear-map.answer.json`, then run `exegenius submit 0756-write-bilinear-map` in the project directory. If submit rejects the answer, fix the answer and submit again.
