# exegenius task 0503-write-linear-contraction

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

Concept: Linear contraction
Gloss: A linear map that does not increase the maximum modulus of any vector, so that errors pass through it without growing.
Also called: contraction

## Where the argument relies on this page

- The recovered coefficient error is strictly below $1/2$, so rounding returns the exact integer coefficients. (on [Exact coefficient recovery](recovery-and-error.md))

## Symbols already bound on earlier pages

The symbols in the names of the concepts the reader knows are listed with those concepts above.

- $b$ (base), bound on [Logarithm](logarithm.md): The fixed number, greater than 1, to which the logarithm is taken.
- $y$ (positive number), bound on [Logarithm](logarithm.md): The positive number whose logarithm to base $b$ is taken.
- $n$ (integer argument), bound on [Logarithm](logarithm.md): The positive integer whose base-2 logarithm $\lg n$ is taken.
- $n$ (argument), bound on [Base-2 logarithm](base-two-logarithm.md): A positive integer whose base-2 logarithm is taken.
- $\lg$ (base-2 logarithm), bound on [Base-2 logarithm](base-two-logarithm.md): The base-2 logarithm of $n$, the least integer $k$ with $2^k \ge n$, but at least 1.
- $z$ (complex number), bound on [Root of unity](root-of-unity.md): A complex number that is tested for being a root of unity.
- $m$ (order), bound on [Root of unity](root-of-unity.md): The order of $z$, the least positive integer with $z^m = 1$, which also counts the distinct powers of $z$.
- $y$ (polynomial variable), bound on [Root of unity](root-of-unity.md): The variable of the polynomial ring $\mathbb{C}[y]/(y^4+1)$, which is a root of unity in that ring.
- $n$ (input length), bound on [Running time cost](running-time-cost.md): The number of cells holding an input, that is, the length of the input string.
- $A$ (machine), bound on [Running time cost](running-time-cost.md): The single machine whose running time the main theorem bounds.
- $\kappa$ (fixed exponent constant), bound on [Running time cost](running-time-cost.md): A fixed constant, equal to $2^{-182}$, that sets the exponent $1-\kappa$ in the running time bound.
- $T_A$ (running time cost), bound on [Running time cost](running-time-cost.md): The running time cost of machine A as a function of the input length n: the largest number of steps A takes on any input of that length.
- $M$ (scanning machine), bound on [Running time cost](running-time-cost.md): The example machine that reads cells from left to right and halts at the first cell holding 1 or at the last cell.
- $x$ (first input), bound on [Exact integer multiplication](exact-integer-multiplication.md): The first binary input string, of length $n$.
- $y$ (second input), bound on [Exact integer multiplication](exact-integer-multiplication.md): The second binary input string, of length $n$.
- $n$ (input length), bound on [Exact integer multiplication](exact-integer-multiplication.md): The number of bits in each of the two inputs $x$ and $y$.
- $\mathrm{val}$ (value function), bound on [Exact integer multiplication](exact-integer-multiplication.md): $\mathrm{val}(x)$ is the nonnegative integer value of a binary string $x$, with the leftmost bit most significant.
- $k$ (padded length), bound on [Exact integer multiplication](exact-integer-multiplication.md): The number of bits in a padded binary string, that is, the length to which $\mathrm{bin}_k$ pads.
- $z$ (padded integer), bound on [Exact integer multiplication](exact-integer-multiplication.md): A nonnegative integer with $z < 2^k$ that is written in binary.
- $\mathrm{bin}_k$ (padded binary representation), bound on [Exact integer multiplication](exact-integer-multiplication.md): $\mathrm{bin}_k(z)$ is the binary representation of $z$ padded on the left with zeros to length $k$.
- $\#$ (separator), bound on [Exact integer multiplication](exact-integer-multiplication.md): A separator symbol placed between $x$ and $y$ in the input, marking where $x$ ends and $y$ begins.
- $a$ (first input sequence), bound on [Convolution](convolution.md): The first input sequence, of length n.
- $b$ (second input sequence), bound on [Convolution](convolution.md): The second input sequence, of length n.
- $n$ (sequence length), bound on [Convolution](convolution.md): The number of entries in each input sequence.
- $m$ (output position), bound on [Convolution](convolution.md): The position of an output entry of the convolution.
- $i$ (first input position), bound on [Convolution](convolution.md): The position in a of the input entry that combines to an output entry.
- $j$ (second input position), bound on [Convolution](convolution.md): The position in b of the input entry that combines to an output entry.
- $c$ (convolution), bound on [Convolution](convolution.md): The convolution of a and b, a sequence of length 2n-1.
- $t$ (step index), bound on [Mathematical induction](mathematical-induction.md): The number of recursion levels passed, a nonnegative integer.
- $q$ (level ratio), bound on [Mathematical induction](mathematical-induction.md): The fixed positive real ratio by which one level may multiply a bound.
- $g_t$ (level bound), bound on [Mathematical induction](mathematical-induction.md): A bound on the cost after t levels.
- $\lambda$ (evaluation point), bound on [Little-o notation](little-o-notation.md): The real point at which the functions are evaluated, taken to infinity.
- $\varphi$ (bounded function), bound on [Little-o notation](little-o-notation.md): The function being bounded.
- $\psi$ (comparison function), bound on [Little-o notation](little-o-notation.md): The comparison function, positive for all large $\lambda$.
- $A$ (multiplication machine), bound on [Little-o notation](little-o-notation.md): The deterministic Turing machine with a fixed number of tapes that multiplies two n-bit integers exactly.
- $\kappa$ (saving exponent), bound on [Little-o notation](little-o-notation.md): The fixed positive constant 2^{-182} in the saving exponent $1-\kappa$.
- $T_A$ (running time), bound on [Little-o notation](little-o-notation.md): The running time of machine A on inputs of length n.
- $C$ (constant factor), bound on [Little-o notation](little-o-notation.md): A constant factor in the big-O bound on $T_A(n)$.
- $c_A$ (conjecture constant), bound on [Little-o notation](little-o-notation.md): A positive constant in the conjectured lower bound for machine A.
- $N$ (entry count), bound on [Address](address.md): The number of entries in an array, which counts every stored entry once.
- $d$ (address length), bound on [Address](address.md): The number of bits in each address of an array.
- $\alpha$ (address), bound on [Address](address.md): A string of d bits that labels one entry of the array.
- $p$ (precision), bound on [Truncation](truncation.md): The number of fractional binary places kept, which sets the grid spacing to $2^{-p}$.
- $z$ (coefficient list), bound on [Truncation](truncation.md): A finite list of complex numbers, called coefficients.
- $Q_p$ (truncation map), bound on [Truncation](truncation.md): The map that truncates each real and imaginary part of each coefficient of a list toward zero to the grid $2^{-p}\mathbb{Z}$.
- $\|\cdot\|_\infty$ (maximum norm), bound on [Truncation](truncation.md): The largest complex modulus of any coefficient of a list.
- $H$ (layer), bound on [Truncation](truncation.md): The operation that applies a two-point map to each pair of entries whose addresses differ in one of several selected bits, in one pass.
- $\alpha$ (first paired value), bound on [Truncation](truncation.md): The first of the two values that the layer combines in each pair.
- $\beta$ (second paired value), bound on [Truncation](truncation.md): The second of the two values that the layer combines in each pair.
- $X$ (array), bound on [Array norm](array-norm.md): A finite array of complex values.
- $u$ (array entry), bound on [Array norm](array-norm.md): An entry of the array X, a complex number.
- $\|X\|$ (array norm), bound on [Array norm](array-norm.md): The largest modulus |u| over all entries u of the array X.
- $y$ (polynomial variable), bound on [Array norm](array-norm.md): The variable of the polynomials in the ring modulo y^r + 1.
- $r$ (coefficient count), bound on [Array norm](array-norm.md): The number of coefficients in each representative of a ring element, equal to the degree of the modulus y^r + 1.
- $g$ (ring element), bound on [Array norm](array-norm.md): An element of the polynomial ring modulo y^r + 1.
- $t$ (coefficient index), bound on [Array norm](array-norm.md): The index of a coefficient of a representative, running from 0 to r-1.
- $\kappa$ (real input), bound on [Ceiling function](ceiling-function.md): The real number whose ceiling is taken.
- $u$ (function), bound on [Big-Theta notation](big-theta-notation.md): A function from input sizes to nonnegative real numbers, whose growth is being compared with that of $h$.
- $h$ (comparison function), bound on [Big-Theta notation](big-theta-notation.md): A second function of the same kind as $u$, against which the growth of $u$ is measured.
- $N$ (input size), bound on [Big-Theta notation](big-theta-notation.md): The number of bits in the input, a count of its bit positions.
- $\Theta$ (Big-Theta), bound on [Big-Theta notation](big-theta-notation.md): The notation stating that $u$ and $h$ have the same order up to constant factors for large inputs.
- $C_1$ (lower factor), bound on [Big-Theta notation](big-theta-notation.md): A positive real constant multiplying $h$ in the lower bound.
- $C_2$ (upper factor), bound on [Big-Theta notation](big-theta-notation.md): A positive real constant multiplying $h$ in the upper bound.
- $N_0$ (threshold input size), bound on [Big-Theta notation](big-theta-notation.md): An input size from which both inequalities hold.
- $\kappa$ (saving exponent), bound on [Big-Theta notation](big-theta-notation.md): The fixed positive exponent saving in the bound, equal to $2^{-182}$ in the paper.
- $\mathbb{R}$ (real numbers), bound on [Extended real numbers](extended-reals.md): The set of real numbers, to which the two infinite values are added to form the extended reals.
- $\overline{\mathbb{R}}$ (extended real numbers), bound on [Extended real numbers](extended-reals.md): The set of extended real numbers, the real numbers together with positive infinity and negative infinity.
- $+\infty$ (positive infinity), bound on [Extended real numbers](extended-reals.md): The added value that is larger than every real number.
- $-\infty$ (negative infinity), bound on [Extended real numbers](extended-reals.md): The added value that is smaller than every real number.
- $\tau$ (real number), bound on [Extended real numbers](extended-reals.md): A generic real number, used when the order and arithmetic of the extended reals are stated.
- $C$ (set of extended reals), bound on [Extended real numbers](extended-reals.md): An arbitrary set of extended real numbers, whose infimum and supremum are taken.
- $\delta$ (sequence position), bound on [Extended real numbers](extended-reals.md): The position of a term in a sequence of extended real numbers, running over 1, 2, 3, and so on.
- $\Sigma$ (set of reals), bound on [Supremum](supremum.md): A nonempty set of real numbers whose supremum is taken.
- $\chi$ (set element), bound on [Supremum](supremum.md): An arbitrary element of the set $\Sigma$.
- $\Omega$ (upper bound), bound on [Supremum](supremum.md): A real number that is an upper bound of the set $\Sigma$.
- $\iota_k$ (sequence term), bound on [Telescoping identity](telescoping-identity.md): The number at position k of the sequence, for k from 0 to o.
- $k$ (term index), bound on [Telescoping identity](telescoping-identity.md): The position of a term in the sequence, running from 0 to o.
- $o$ (last index), bound on [Telescoping identity](telescoping-identity.md): The index of the last term of the sequence, so the sequence has o+1 terms.
- $\beta$ (number of places), bound on [Mixed-radix digits](mixed-radix-digits.md): The number of places in the system, a positive integer.
- $\lambda_j$ (place length), bound on [Mixed-radix digits](mixed-radix-digits.md): The number of values the digit at place $j$ can take.
- $j$ (place index), bound on [Mixed-radix digits](mixed-radix-digits.md): A position among the places, running from 1 to the number of places.
- $\Lambda$ (product of lengths), bound on [Mixed-radix digits](mixed-radix-digits.md): The product of all the place lengths, the number of distinct digit strings the system can write.
- $w_j$ (place value), bound on [Mixed-radix digits](mixed-radix-digits.md): The weight of place $j$, the product of the lengths of the places below it.
- $\nu$ (integer being written), bound on [Mixed-radix digits](mixed-radix-digits.md): A nonnegative integer less than $\Lambda$, whose expansion is sought.
- $e_j$ (digit), bound on [Mixed-radix digits](mixed-radix-digits.md): The digit of an expansion at place $j$, an integer from $0$ to $\lambda_j-1$.
- $e'_j$ (second digit), bound on [Mixed-radix digits](mixed-radix-digits.md): The digit at place $j$ of a second expansion of the same integer.
- $i$ (summation index), bound on [Mixed-radix digits](mixed-radix-digits.md): A place index ranging over the places below a given place $j$.
- $F$ (field), bound on [Linear algebra basics](linear-algebra-basics.md): A set with addition and multiplication in which every nonzero element has a multiplicative inverse, the scalars of the vector space.
- $x$ (vector), bound on [Linear algebra basics](linear-algebra-basics.md): A vector over $F$; the letter stands for an arbitrary vector.
- $y$ (second vector), bound on [Linear algebra basics](linear-algebra-basics.md): A vector over $F$, a second arbitrary vector.
- $c$ (scalar), bound on [Linear algebra basics](linear-algebra-basics.md): A scalar in $F$, multiplying vectors.
- $d$ (second scalar), bound on [Linear algebra basics](linear-algebra-basics.md): A scalar in $F$, added to another scalar in the axiom $(c+d)x=cx+dx$.
- $m$ (coordinate count), bound on [Linear algebra basics](linear-algebra-basics.md): The number of coordinates in each vector of $F^m$, so the length of the tuples.
- $j$ (coordinate index), bound on [Linear algebra basics](linear-algebra-basics.md): The index that runs from 1 to $m$ and labels the coordinates $x_j$ of a vector.
- $i$ (output coordinate index), bound on [Linear algebra basics](linear-algebra-basics.md): The index of a coordinate of the output $Ax$.
- $A$ (matrix), bound on [Linear algebra basics](linear-algebra-basics.md): An $m	imes m$ matrix with entries in $F$.
- $B$ (inverse candidate), bound on [Linear algebra basics](linear-algebra-basics.md): A matrix that may serve as the inverse of $A$.
- $I$ (identity matrix), bound on [Linear algebra basics](linear-algebra-basics.md): The $m	imes m$ matrix with ones on the diagonal and zeros elsewhere.
- $T$ (linear map), bound on [Linear algebra basics](linear-algebra-basics.md): A linear map from one vector space over $F$ to another.
- $S$ (inverse map), bound on [Linear algebra basics](linear-algebra-basics.md): A linear map that serves as the inverse of a linear operator $T$ when $ST=TS=\mathrm{id}$.
- $\mathrm{id}$ (identity map), bound on [Linear algebra basics](linear-algebra-basics.md): The map sending every vector to itself.
- $T^{-1}$ (inverse operator), bound on [Linear algebra basics](linear-algebra-basics.md): The unique inverse of an invertible linear operator $T$.
- $v$ (vertex), bound on [Linear algebra basics](linear-algebra-basics.md): A vertex of the network, the endpoint of an edge.
- $u$ (vertex), bound on [Linear algebra basics](linear-algebra-basics.md): A vertex of the network, the starting point of an edge.
- $D_v$ (frame of vertex v), bound on [Linear algebra basics](linear-algebra-basics.md): The frame of vertex $v$, an invertible linear operator on arrays.
- $D_u$ (frame of vertex u), bound on [Linear algebra basics](linear-algebra-basics.md): The frame of vertex $u$, an invertible linear operator on arrays.
- $g$ (logical array), bound on [Linear algebra basics](linear-algebra-basics.md): The array the computation means, before any change of representation.
- $\Phi_M$ (matrix frame), bound on [Linear algebra basics](linear-algebra-basics.md): The frame built from a matrix $M$ by a shear of address pairs.
- $M$ (matrix), bound on [Linear algebra basics](linear-algebra-basics.md): A matrix from which the shear frame $\Phi_M$ is built.
- $H$ (address chunk), bound on [Linear algebra basics](linear-algebra-basics.md): A binary address chunk, one of the two fields of an address pair.
- $K$ (second address chunk), bound on [Linear algebra basics](linear-algebra-basics.md): A binary address chunk, the second field of an address pair.
- $q$ (transform length), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The number of coordinates of each vector the transform acts on, so it counts the entries of a vector.
- $\omega$ (primitive root of unity), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The primitive q-th root of unity $e^{-2\pi i/q}$, a complex number whose q-th power is 1.
- $u$ (input vector), bound on [Discrete Fourier transform](discrete-fourier-transform.md): A vector of q complex numbers, the argument of the transform.
- $s$ (input index), bound on [Discrete Fourier transform](discrete-fourier-transform.md): An integer index from 0 to q-1 that numbers the input coordinates.
- $\ell$ (output index), bound on [Discrete Fourier transform](discrete-fourier-transform.md): An integer index from 0 to q-1 that numbers the output coordinates.
- $F_q$ (discrete Fourier transform), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The map sending a vector of q complex numbers to its normalized discrete Fourier transform, with coordinates given by the weighted sum above.
- $F_q^+$ (positive-sign transform), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The transform with the positive sign in the exponent, which inverts F_q up to the factor q.
- $\nu$ (second input index), bound on [Discrete Fourier transform](discrete-fourier-transform.md): A second integer index from 0 to q-1 that numbers the input coordinates in the inverse identity.
- $K$ (linear map on q-vectors), bound on [Discrete Fourier transform](discrete-fourier-transform.md): A linear map from q-vectors to q-vectors, which is tested for being a contraction.
- $i$ (imaginary unit), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The imaginary unit, the square root of minus one, used in the complex exponent and coordinates.
- $D$ (axis count), bound on [Transform axis](transform-axis.md): The number of axes of the array, which is also the number of coordinates in each address.
- $x_i$ (axis coordinate), bound on [Transform axis](transform-axis.md): The coordinate of an address along axis $i$, an integer from 0 to $t_i - 1$.
- $t_i$ (axis length), bound on [Transform axis](transform-axis.md): The length of axis $i$, the number of values its coordinate takes.
- $s$ (modulus exponent), bound on [Transform axis](transform-axis.md): The power of two $s$ in the modulus $y^s+1$ of the polynomial that stores one coordinate.
- $y$ (polynomial indeterminate), bound on [Transform axis](transform-axis.md): The indeterminate of the polynomial modulo $y^s+1$; its powers serve as roots of unity on the remaining axes.
- $y$ (polynomial variable), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The variable of the polynomial ring $R_r$, in which $y^r$ is identified with $-1$.
- $R_r$ (record ring), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The ring of polynomials with complex coefficients in $y$, modulo $y^r+1$, whose elements are records.
- $r$ (record length), bound on [Synthetic polynomial transforms](synthetic-transforms.md): A power of two, the number of complex coefficients in a record.
- $c_d$ (coefficient), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The coefficient of $y^d$ in a record.
- $d$ (coefficient position), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The position of a coefficient in a record, running from $0$ to $r-1$.
- $s$ (shift amount), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The number of places a shift moves each coefficient, with $0 \le s < 2r$.
- $\nu_d$ (wrap count), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The number of times a shift carries the coefficient at position $d$ past position $r-1$.
- $N$ (transform length), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The number of entries in the transform, a power of two dividing $2r$.
- $\omega_N$ (primitive root), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The root $y^{2r/N}$ of $R_r$, a primitive $N$-th root of unity.
- $e_j$ (input record), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The $j$-th record of the input list.
- $Z$ (transformed list), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The output list of records produced by the transform.
- $\delta$ (half block size), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The number of positions in half of a block at a level, taking the values $1, 2, \dots, N/2$.
- $\tau$ (butterfly offset), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The offset of a butterfly pair within the first half of its block, from $0$ to $\delta-1$.
- $\theta$ (twiddle factor), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The power of $\omega_N$ that multiplies one entry of a butterfly.
- $\log_2$ (base-2 logarithm), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The logarithm to base 2, so $\log_2 N$ is the number of levels of the fast method.
- $\lg$ (base-2 logarithm), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The logarithm to base 2.
- $\kappa$ (running time exponent constant), bound on [Synthetic polynomial transforms](synthetic-transforms.md): A fixed positive constant in the exponent of the running time bound.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Linear algebra basics](linear-algebra-basics.md): Vector spaces over a field, linear maps and matrices, and the inverse of an invertible linear operator.
  Shown as: Linear contraction *<predicate>* Linear algebra basics
- [Supremum](supremum.md): The least upper bound of a set of real numbers.
  Shown as: Linear contraction *<predicate>* Supremum

## Pages that build on this one

- Guard-width bound: An explicit number of extra fractional and integer bits that makes every intermediate coefficient of a butterfly layer exact, so that a single final truncation suffices.

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

- "both transforms are contractions." (paper)

## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The reader cannot follow this step: "only the errors introduced at each step accumulate, and the recovery step needs their total below $1/2$" (The page asserts that the errors introduced at successive steps add up, and that their total must stay below 1/2 for recovery, but gives no argument for the accumulation (no triangle inequality is stated) and no justification for the threshold; the threshold is only in the linked recovery page, which is not pointed to at this sentence.)
- Say what $m'$ denotes where it is first used: the page uses it before saying so in "$m'$ is the number of coordinates of its output vectors"
- Say what $\eta$ denotes where it is first used: the page uses it before saying so in "where $x$ is the exact input and $\eta$ is the error vector"
- Say what $k$ denotes where it is first used (for a size or count, what it counts): "has entries $\omega^{jk}/q$" (The page never says what k indexes or over which range; it appears only inside the transform entries and as the subscript of the output (F_q u)_k.)

## Previous version (revise it)

It has 271 words. Fix the problems by restructuring rather than appending: keep the rewrite within 338 words, a quarter more, unless a problem cannot be fixed without more. Pages that grow with every repair stop being self-contained explanations of one concept.

A linear contraction is a linear map that acts on the vector spaces of [Linear algebra basics](linear-algebra-basics.md) and never increases the maximum modulus of a vector. It keeps errors from growing as they pass through a computation, which the exact-recovery step needs ([Exact coefficient recovery](recovery-and-error.md)).

Let $L\colon \mathbb{C}^m \to \mathbb{C}^{m'}$ be a linear map, where $m$ is the number of coordinates of its input vectors and $m'$ is the number of coordinates of its output vectors. For $x \in \mathbb{C}^m$, $\|x\|$ is its largest coordinate modulus. <cite data-source="paper">The vector norm is the maximum modulus of its coordinates.</cite>

$L$ is a linear contraction when $\|Lx\| \le \|x\|$ for every $x \in \mathbb{C}^m$. Its operator norm $\|L\|$ is defined through the [supremum](supremum.md) of $\|Lx\|$ over all $x$ with $\|x\| \le 1$. Thus $L$ is a contraction exactly when $\|L\| \le 1$.

Suppose the computed input is $x + \eta$ where $x$ is the exact input and $\eta$ is the error vector. By linearity, $L(x+\eta) - Lx = L\eta$, so $\|L(x+\eta) - Lx\| \le \|\eta\|$. <cite data-source="paper">A linear contraction propagates an input error without increasing it.</cite> In a chain of contractions, earlier errors do not grow; only the errors introduced at each step accumulate, and the recovery step needs their total below $1/2$.

The normalized transform $F_q$ of length $q$ has entries $\omega^{jk}/q$, where $\omega$ is a $q$-th root of unity, so $|\omega^{jk}| = 1$. Each output is $\frac{1}{q}\sum_j \omega^{jk} u_j$, so $|(F_q u)_k| \le \frac{1}{q}\sum_j |u_j| \le \|u\|$ and $\|F_q u\| \le \|u\|$. <cite data-source="paper">Each normalized Fourier transform above is a contraction, since each output averages inputs multiplied by complex numbers of modulus one.</cite>

For example, take $q = 2$ and $u = (1, i)$. The outputs are $\frac{1+i}{2}$ and $\frac{1-i}{2}$, each of modulus $\frac{\sqrt{2}}{2} \approx 0.71 \le 1 = \|u\|$. Unnormalized sums $(1+i, 1-i)$ have norm $\sqrt{2} > 1$, so the division by $q$ matters.

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

Write the body to `exegenius/tasks/0503-write-linear-contraction.answer.md` and the JSON to `exegenius/tasks/0503-write-linear-contraction.answer.json`, then run `exegenius submit 0503-write-linear-contraction` in the project directory. If submit rejects the answer, fix the answer and submit again.
