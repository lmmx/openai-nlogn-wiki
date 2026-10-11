# exegenius task 0558-write-probability

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
- Cyclic convolution
- Chinese-remainder map (also: Agarwal–Cooley map, coefficient layout, generator)
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
- Opposite transform (also: opposite-sign transform)
- Payload (also: record)
- Phase factor (also: phase factors and scalar corrections, phase frames)
- Polynomial ring (also: polynomial suffix)
- Ring homomorphism and isomorphism (also: ring homomorphism and ring isomorphism)
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
- Chinese remainder theorem (also: CRT)
- Cyclic group (also: cyclic group of order S)
- Order of an element (also: multiplicative order)
- Diagonal scaling
- Extended real numbers
- Frequency domain
- Incidence
- Mathematical induction (also: induction)
- Integer
- Ring
- Pointwise product
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
- Forward transform (also: forward procedure)
- Iverson bracket
- Axis line (also: line)
- Near-linear time
- Negacyclic convolution
- Neumann series
- Real numbers (also: Real number)

## This page

Concept: Probability
Gloss: A number between 0 and 1 assigned to each event, additive over disjoint events, with 1 for the certain event.
Also called: probability in general

## Where the argument relies on this page

- The total number $s$ of smaller calls satisfies $s < Wm$, so each recursive level saves a strict power. (on [Rank-saving recursion](rank-saving-recursion.md))
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
- $m'$ (output coordinate count), bound on [Linear contraction](linear-contraction.md): The number of coordinates of each output vector of the linear map $L$.
- $\|L\|$ (operator norm), bound on [Linear contraction](linear-contraction.md): The largest value of $\|Lx\|$ over all vectors $x$ with $\|x\| \le 1$.
- $\eta$ (error vector), bound on [Linear contraction](linear-contraction.md): The difference between the computed input and the exact input $x$, so that the computed input is $x + \eta$.
- $\pi$ (bilinear map), bound on [Bilinear map](bilinear-map.md): The map sending each pair (e,d) of arguments to a vector pi(e,d) in K, linear in each argument while the other is fixed.
- $E$ (first argument space), bound on [Bilinear map](bilinear-map.md): The vector space containing the first argument e of the bilinear map.
- $H$ (second argument space), bound on [Bilinear map](bilinear-map.md): The vector space containing the second argument d of the bilinear map.
- $K$ (output space), bound on [Bilinear map](bilinear-map.md): The vector space containing the values pi(e,d) of the bilinear map.
- $e$ (first argument), bound on [Bilinear map](bilinear-map.md): An element of the first argument space E.
- $d$ (second argument), bound on [Bilinear map](bilinear-map.md): An element of the second argument space H.
- $\beta$ (first integer), bound on [Coprime](coprime.md): One of the two integers whose greatest common divisor is taken, not both zero.
- $\gamma$ (second integer), bound on [Coprime](coprime.md): The other integer whose greatest common divisor with beta is taken, not both zero with it.
- $\gcd$ (greatest common divisor), bound on [Coprime](coprime.md): The function giving the largest positive integer that divides both of two integers.
- $N$ (family size), bound on [Coprime](coprime.md): The number of integers in the family nu_1 through nu_N.
- $\nu_u$ (family member), bound on [Coprime](coprime.md): The u-th integer of the family, for an index u in 1 through N.
- $u$ (family index), bound on [Coprime](coprime.md): A position in the family, taking values from 1 to N.
- $v$ (second family index), bound on [Coprime](coprime.md): A second position in the family, different from u in the coprimality condition.
- $\operatorname{lcm}$ (least common multiple), bound on [Coprime](coprime.md): The function giving the smallest positive integer divisible by each of its integer arguments.
- $t$ (prefix index), bound on [Coprime](coprime.md): The number of leading family members used in a least common multiple L_t.
- $L_t$ (prefix least common multiple), bound on [Coprime](coprime.md): The least common multiple of the first t family members.
- $\mathbb{Z}$ (integers), bound on [Coprime](coprime.md): The set of all integers.
- $g$ (all-ones tuple), bound on [Coprime](coprime.md): The all-ones tuple (1,...,1), one entry per family member, whose order is the least common multiple of the family.
- $e$ (multiple), bound on [Coprime](coprime.md): The least positive integer with e g = 0, which is the order of the element g.
- $d$ (number of source lengths), bound on [Coprime](coprime.md): The number of lengths s_1 through s_d in the split.
- $s_i$ (source length), bound on [Coprime](coprime.md): The i-th of the pairwise coprime axis lengths.
- $S$ (combined axis length), bound on [Coprime](coprime.md): The product s_1 through s_d, which is the length of the combined cyclic axis.
- $P_i$ (prefix product), bound on [Coprime](coprime.md): The product of the lengths s_1 through s_{i-1}, with P_1 equal to 1.
- $\mu_i$ (inverse of prefix product), bound on [Coprime](coprime.md): An integer with P_i mu_i congruent to 1 modulo s_i, the inverse of P_i modulo s_i.
- $d$ (greatest common divisor), bound on [Bézout's identity](bezout-identity.md): The greatest common divisor of beta and gamma, the largest positive integer dividing both.
- $\mu$ (Bézout coefficient of beta), bound on [Bézout's identity](bezout-identity.md): The integer multiplying beta in the Bézout combination.
- $\nu$ (Bézout coefficient of gamma), bound on [Bézout's identity](bezout-identity.md): The integer multiplying gamma in the Bézout combination.
- $e$ (least positive combination), bound on [Bézout's identity](bezout-identity.md): The least positive integer of the form beta times mu' plus gamma times nu'.
- $\mu'$ (trial coefficient), bound on [Bézout's identity](bezout-identity.md): A trial integer multiplying beta in the proof, not yet known to be a Bézout coefficient.
- $\nu'$ (trial coefficient), bound on [Bézout's identity](bezout-identity.md): A trial integer multiplying gamma in the proof, not yet known to be a Bézout coefficient.
- $\kappa$ (integer quotient), bound on [Bézout's identity](bezout-identity.md): The integer quotient when beta is divided by e.
- $\tau$ (remainder), bound on [Bézout's identity](bezout-identity.md): The remainder when beta is divided by e, which lies between 0 and e minus 1.
- $\kappa$ (group order), bound on [Cyclic group](cyclic-group.md): The number of elements of the cyclic group $C_\kappa$, which is its order.
- $\tau$ (generator), bound on [Cyclic group](cyclic-group.md): A fixed element of the group; its powers give every element of the cyclic group $C_\kappa$.
- $C_\kappa$ (cyclic group), bound on [Cyclic group](cyclic-group.md): The group with $\kappa$ elements, namely the powers $\tau^0$ through $\tau^{\kappa-1}$ of the generator.
- $\nu$ (exponent), bound on [Cyclic group](cyclic-group.md): An integer exponent saying which power of the generator $\tau$ is meant.
- $\kappa_1$ (factor order), bound on [Cyclic group](cyclic-group.md): The order of the first cyclic factor $C_{\kappa_1}$, one of two coprime factors of $\kappa$.
- $\kappa_2$ (second factor order), bound on [Cyclic group](cyclic-group.md): The order of the second cyclic factor $C_{\kappa_2}$, the other of two coprime factors of $\kappa$.
- $\mathcal{I}$ (coordinate label set), bound on [Diagonal scaling](diagonal-scaling.md): The finite set of labels, one for each coordinate of the vectors.
- $\iota$ (coordinate label), bound on [Diagonal scaling](diagonal-scaling.md): An element of the label set $\mathcal{I}$, naming one coordinate of a vector.
- $\tau_\iota$ (coordinate scalar), bound on [Diagonal scaling](diagonal-scaling.md): The fixed scalar of $F$ by which the diagonal scaling multiplies coordinate $\iota$.
- $\Delta_\tau$ (diagonal scaling), bound on [Diagonal scaling](diagonal-scaling.md): The linear operator on $F^{\mathcal I}$ that multiplies each coordinate $\iota$ by its own scalar $\tau_\iota$.
- $\Theta$ (projection along C), bound on [Projection along a subspace](projection-along-subspace.md): The map sending each vector $x$ of $X$ to its component $x_U$ in $U$, for the chosen $U$ and $C$.
- $C$ (complementary subspace), bound on [Projection along a subspace](projection-along-subspace.md): A subspace of $X$ that meets $U$ only in zero and whose sum with $U$ is all of $X$.
- $x_U$ (component in U), bound on [Projection along a subspace](projection-along-subspace.md): The part of the vector $x$ lying in $U$ in the splitting $x = x_U + x_C$.
- $x_C$ (component in C), bound on [Projection along a subspace](projection-along-subspace.md): The part of the vector $x$ lying in $C$ in the splitting $x = x_U + x_C$.
- $\Theta_U$ (projection along orthogonal complement), bound on [Projection along a subspace](projection-along-subspace.md): The projection $\Theta$ with $C = U^\perp$, defined when $U$ is nondegenerate.
- $A$ (source set), bound on [Bijection](bijection.md): The source set, whose elements are the inputs of the map f.
- $B$ (target set), bound on [Bijection](bijection.md): The target set, whose elements are the outputs of the map f.
- $f$ (map), bound on [Bijection](bijection.md): The map from the source set A to the target set B, which is a bijection when it is one-to-one and onto.
- $s$ (source element), bound on [Bijection](bijection.md): An element of the source set A, the input to the map f.
- $s'$ (second source element), bound on [Bijection](bijection.md): A second element of the source set A, used to state the one-to-one condition.
- $w$ (target element), bound on [Bijection](bijection.md): An element of the target set B, which the onto condition requires to be hit by some element of A.
- $E$ (subset of source), bound on [Bijection](bijection.md): A subset of the source set A, whose image under a bijection is compared with the image of its complement.
- $S$ (position set), bound on [Permutation](permutation.md): A finite set of positions, the set whose elements a permutation rearranges.
- $\pi$ (permutation), bound on [Permutation](permutation.md): The map from S to S that sends each position to its new position.
- $u$ (address), bound on [Permutation](permutation.md): The position of one entry in an array.
- $A$ (array), bound on [Permutation](permutation.md): An array of entries stored at addresses, the object that an address permutation moves.
- $u$ (field width), bound on [Address field](address-field.md): The number of bits in each of the two fields being interchanged.
- $u$ (earlier vertex), bound on [Linear networks and frames](linear-network-frames.md): The earlier of the two vertices joined by an edge, the vertex the edge leaves.
- $G$ (pointwise linear gate), bound on [Linear networks and frames](linear-network-frames.md): A gate that combines its inputs by a fixed linear combination, applied separately at each address.
- $t$ (gate input count), bound on [Linear networks and frames](linear-network-frames.md): The number of input arrays a gate takes.
- $s$ (input index), bound on [Linear networks and frames](linear-network-frames.md): The position of an input of a gate, running from 1 to t.
- $\alpha$ (input weight), bound on [Linear networks and frames](linear-network-frames.md): The fixed weight with which a gate multiplies its input s, the same at every address.
- $\ell$ (input wire), bound on [Linear networks and frames](linear-network-frames.md): An input wire of the network.
- $\theta$ (supplied array), bound on [Linear networks and frames](linear-network-frames.md): The physical array supplied on an input wire.
- $\mathrm{source}$ (source vertex), bound on [Linear networks and frames](linear-network-frames.md): The source vertex of an input wire.
- $\mathrm{sink}$ (sink vertex), bound on [Linear networks and frames](linear-network-frames.md): The sink vertex of an output role.
- $\rho$ (role permutation), bound on [Linear networks and frames](linear-network-frames.md): The permutation of roles that sends each input role to an output role.
- $\varepsilon$ (routing sign), bound on [Linear networks and frames](linear-network-frames.md): The fixed sign by which the network multiplies the value routed from input role $\ell$.
- $x$ (route vertex), bound on [Linear networks and frames](linear-network-frames.md): A vertex on a route, numbered in order from the source to the sink.
- $H$ (first address field), bound on [Linear networks and frames](linear-network-frames.md): The first of two address fields, written as a vector.
- $K$ (second address field), bound on [Linear networks and frames](linear-network-frames.md): The second of two address fields, written as a vector; not a frame.
- $L$ (block length), bound on [Cyclic shift](cyclic-shift.md): The number of positions in the block, a count of positions.
- $t$ (position), bound on [Cyclic shift](cyclic-shift.md): A position in the block, numbered from 0 to L-1.
- $v_t$ (stored value), bound on [Cyclic shift](cyclic-shift.md): The value stored at position t of the block.
- $s$ (offset), bound on [Cyclic shift](cyclic-shift.md): An integer taken modulo L that gives the amount of rotation.
- $V$ (stored bit volume), bound on [Cyclic shift](cyclic-shift.md): The number of bits held in the array, which the cost bound is linear in.
- $H_0$ (butterfly map), bound on [Butterfly](butterfly.md): The two-point map sending a pair of values to its half-sum and half-difference.
- $\delta$ (first input value), bound on [Butterfly](butterfly.md): The first of the two input values of the butterfly.
- $\theta$ (second input value), bound on [Butterfly](butterfly.md): The second of the two input values of the butterfly.
- $b$ (index bit), bound on [Butterfly](butterfly.md): The index bit, a binary digit of the position, that the level of the transform processes.
- $b$ (digit width), bound on [Radix-digit convolution](radix-digit-convolution.md): The number of bits in each digit, a positive integer.
- $N$ (digit count), bound on [Radix-digit convolution](radix-digit-convolution.md): The number of digits in each input.
- $x_i$ (digit of x), bound on [Radix-digit convolution](radix-digit-convolution.md): The digit of $x$ at position $i$, with weight $(2^b)^i$.
- $y_j$ (digit of y), bound on [Radix-digit convolution](radix-digit-convolution.md): The digit of $y$ at position $j$, with weight $(2^b)^j$.
- $z$ (formal variable), bound on [Radix-digit convolution](radix-digit-convolution.md): The indeterminate of the polynomials $P_x$ and $P_y$, which is set to $2^b$ to recover the inputs.
- $P_x$ (polynomial of x), bound on [Radix-digit convolution](radix-digit-convolution.md): The polynomial in $z$ whose coefficients are the digits of $x$.
- $P_y$ (polynomial of y), bound on [Radix-digit convolution](radix-digit-convolution.md): The polynomial in $z$ whose coefficients are the digits of $y$.
- $c_k$ (product coefficient), bound on [Radix-digit convolution](radix-digit-convolution.md): The integer coefficient of $z^k$ in the product $P_x(z)P_y(z)$, which is the $k$-th entry of the convolution of the digit sequences.
- $h$ (ground set size), bound on [Ground set](ground-set.md): The number of elements of the ground set, so it counts those elements.
- $T$ (three-element subsets), bound on [Ground set](ground-set.md): The set of all three-element subsets of $[h]$.
- $P$ (matrix), bound on [Tensor product](tensor-product.md): A matrix whose entry in row i and column j is p_{ij}, the matrix whose tensor powers are taken.
- $Q$ (second matrix), bound on [Tensor product](tensor-product.md): A second matrix, the right factor in the tensor product P\otimes Q.
- $i$ (row index), bound on [Tensor product](tensor-product.md): The index of a row of a matrix, here also the index of a block-row and of a coordinate.
- $j$ (column index), bound on [Tensor product](tensor-product.md): The index of a column of a matrix, here also the index of a block-column.
- $m$ (tensor power count), bound on [Tensor product](tensor-product.md): The number of factors in a tensor power, which counts the coordinates the operator acts on.
- $t$ (address bit string), bound on [Tensor product](tensor-product.md): A bit string of length m that is an address on m coordinates.
- $f$ (function on addresses), bound on [Tensor product](tensor-product.md): A function on addresses of m coordinates, the input that the operator transforms.
- $s$ (output address), bound on [Tensor product](tensor-product.md): An output address of m coordinates, a bit string whose bit at coordinate i is s_i.
- $Q_0$ (radix), bound on [Carry propagation](carry-propagation.md): The number of values a digit can take, $2^b$, which is the base in which each digit is written.
- $d_t$ (output digit), bound on [Carry propagation](carry-propagation.md): The base-$Q_0$ digit of the output at position $t$, with $0 \le d_t < Q_0$.
- $e_t$ (carry), bound on [Carry propagation](carry-propagation.md): The amount carried into position $t$ from the lower positions.
- $\tau$ (processed positions), bound on [Carry propagation](carry-propagation.md): The number of low positions already processed, so that the sums run over $t < \tau$.
- $B$ (modulus), bound on [Congruence](congruence-modulo.md): A positive integer, the modulus modulo which congruence is taken.
- $d$ (first integer), bound on [Congruence](congruence-modulo.md): An integer, the first of the two integers compared for congruence.
- $e$ (second integer), bound on [Congruence](congruence-modulo.md): An integer, the second of the two integers compared for congruence.
- $\mathbb{Z}$ (integers), bound on [Congruence](congruence-modulo.md): The set of all integers.
- $\nu$ (class member), bound on [Congruence](congruence-modulo.md): An integer congruent to d modulo B, a member of the residue class of d.
- $\delta$ (remainder), bound on [Congruence](congruence-modulo.md): The integer in {0,...,B-1} that is the remainder of a residue class.
- $d'$ (congruent first integer), bound on [Congruence](congruence-modulo.md): An integer congruent to d modulo B.
- $e'$ (congruent second integer), bound on [Congruence](congruence-modulo.md): An integer congruent to e modulo B.
- $u_j$ (input coefficient), bound on [Congruence](congruence-modulo.md): The input coefficient at position j of the sum being formed.
- $n$ (input length), bound on [Schönhage–Strassen multiplication](schonhage-strassen.md): The number of bits in each of the two input integers.
- $m$ (modulus exponent), bound on [Schönhage–Strassen multiplication](schonhage-strassen.md): The positive integer exponent that defines the modulus $2^m+1$ of the Fermat-type residue ring.
- $R$ (ring), bound on [Ring](ring.md): A set with an addition and a multiplication satisfying the axioms listed on this page.
- $a$ (ring element), bound on [Ring](ring.md): An element of the ring $R$, one of the arguments of its addition and multiplication.
- $b$ (ring element), bound on [Ring](ring.md): An element of the ring $R$, one of the arguments of its addition and multiplication.
- $c$ (ring element), bound on [Ring](ring.md): An element of the ring $R$, one of the arguments of its addition and multiplication.
- $y$ (polynomial variable), bound on [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md): The indeterminate of the polynomial ring, whose powers act as roots of unity.
- $r$ (record length), bound on [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md): The number of complex coefficients in a polynomial record, a power of two.
- $P$ (ring element), bound on [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md): An element of the ring $R_r$, given by its representative of degree less than $r$.
- $e$ (coefficient position), bound on [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md): The position of a coefficient in a representative, running from 0 to r-1.
- $d_e$ (coefficient), bound on [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md): The complex coefficient of $y^e$ in $P$, the entry at position e of the coefficient list.
- $\tau$ (root of unity), bound on [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md): An element of the ring whose positive integer power equals 1.
- $\nu$ (exponent), bound on [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md): The positive integer power to which a root of unity is raised to give 1, counting the factors of the product.
- $\chi$ (sequence term), bound on [Limit inferior](limit-inferior.md): The $k$-th term of a sequence of real numbers.
- $k$ (term index), bound on [Limit inferior](limit-inferior.md): The position of a term in a sequence, an index counting from 1.
- $m$ (tail start position), bound on [Limit inferior](limit-inferior.md): The position from which the tail of a sequence starts.
- $\tau_m$ (tail infimum), bound on [Limit inferior](limit-inferior.md): The infimum of the terms from position $m$ on, the largest number at most all of them.
- $\varepsilon$ (positive tolerance), bound on [Limit inferior](limit-inferior.md): A positive real number used as a tolerance in a limit criterion.
- $\mathcal{T}_A(n)$ (worst-case time), bound on [Limit inferior](limit-inferior.md): The worst-case running time of machine $A$ on inputs of $n$ bits.
- $\delta_A$ (lower-bound constant), bound on [Limit inferior](limit-inferior.md): A positive real constant in the lower bound for machine $A$.
- $\Gamma_A$ (input length threshold), bound on [Limit inferior](limit-inferior.md): The input length beyond which the lower bound for machine $A$ is required to hold.
- $\kappa$ (bound exponent), bound on [Limit inferior](limit-inferior.md): The fixed exponent $2^{-182}$ in the main time bound.
- $C$ (bound constant), bound on [Limit inferior](limit-inferior.md): A constant in the big-O time bound of the main result.
- $\log$ (base-2 logarithm), bound on [The n log n optimality conjecture](n-log-n-conjecture.md): The base-2 logarithm, as used in the expression $n \log n$.
- $\lg n$ (binary logarithm), bound on [The n log n optimality conjecture](n-log-n-conjecture.md): The base-2 logarithm of n rounded up to an integer and never below 1.
- $c_A$ (lower-bound constant), bound on [The n log n optimality conjecture](n-log-n-conjecture.md): A positive constant in the lower bound that must hold for machine A.
- $N_A$ (threshold length), bound on [The n log n optimality conjecture](n-log-n-conjecture.md): The input length from which the lower bound for machine A must hold.
- $\kappa$ (saving exponent), bound on [The n log n optimality conjecture](n-log-n-conjecture.md): The fixed positive constant in the exponent 1 - kappa of the main theorem's running time, equal to 2^{-182}.
- $n$ (input bit length), bound on [Fixed-tape machine model](fixed-tape-model.md): The number of bits in each of the two input integers, a count of bits.
- $c_A$ (lower-bound constant), bound on [Fixed-tape machine model](fixed-tape-model.md): A positive constant, depending on the machine A, in its eventual lower bound.
- $N_A$ (bound threshold), bound on [Fixed-tape machine model](fixed-tape-model.md): The input length from which the eventual lower bound for machine A holds.
- $\lg$ (base-2 logarithm), bound on [Fixed-tape machine model](fixed-tape-model.md): The base-2 logarithm, so that $\lg n$ stands for $\log_2 n$.
- $\mathbb{F}_2$ (binary field), bound on [Binary field](binary-field.md): The field with the two elements $0$ and $1$, with addition given by exclusive or and multiplication by AND.
- $\oplus$ (exclusive or), bound on [Binary field](binary-field.md): The addition of the binary field, which gives $1$ exactly when its two bits differ.
- $\tau$ (field element), bound on [Binary field](binary-field.md): An arbitrary element of the binary field, so it is $0$ or $1$.
- $K$ (example matrix), bound on [Binary field](binary-field.md): The $2 \times 2$ matrix over the binary field used in the example, with rows $(1, 1)$ and $(0, 1)$.
- $\beta$ (integer to invert), bound on [Modular inverse](modular-inverse.md): The integer whose inverse modulo M is sought.
- $M$ (modulus), bound on [Modular inverse](modular-inverse.md): A positive integer, the modulus of the inverse.
- $\mu$ (inverse), bound on [Modular inverse](modular-inverse.md): An integer whose product with beta is congruent to 1 modulo M.
- $\nu$ (quotient integer), bound on [Modular inverse](modular-inverse.md): The integer with beta mu - 1 = nu M, the quotient (beta mu - 1)/M.
- $i$ (axis index), bound on [Modular inverse](modular-inverse.md): The position of an axis among the axes.
- $M_i$ (axis length), bound on [Modular inverse](modular-inverse.md): The number of values the coordinate along axis i takes.
- $S$ (product of lengths), bound on [Modular inverse](modular-inverse.md): The product of all the axis lengths M_i.
- $\pi_i$ (prefix product), bound on [Modular inverse](modular-inverse.md): The product of the lengths of the axes before axis i.
- $\mu_i$ (inverse of prefix product), bound on [Modular inverse](modular-inverse.md): The inverse of pi_i modulo M_i.
- $\xi$ (generator), bound on [Modular inverse](modular-inverse.md): A generator of a cyclic group of order S, whose powers make up the group.
- $\xi_i$ (axis generator), bound on [Modular inverse](modular-inverse.md): A generator of a cyclic group of order M_i.
- $\kappa$ (positive exponent), bound on [Modular inverse](modular-inverse.md): A positive integer exponent under which the image becomes 1.
- $M$ (change-of-basis matrix), bound on [Binary change of basis](binary-change-of-basis.md): An invertible $m\times m$ matrix over $\mathbb F_2$ that specifies the change of basis.
- $\nu$ (bit column), bound on [Binary change of basis](binary-change-of-basis.md): The column of values of the selected bits, each an element of $\mathbb F_2$.
- $\kappa$ (address), bound on [Binary change of basis](binary-change-of-basis.md): A vector in $\mathbb F_2^m$, one address of the selected bits.
- $P_M$ (address permutation), bound on [Binary change of basis](binary-change-of-basis.md): The permutation of arrays of addresses that moves the value at each address $\kappa$ to $M\kappa$.
- $\mathrm{GL}(m,\mathbb F_2)$ (invertible matrices), bound on [Binary change of basis](binary-change-of-basis.md): The set of invertible $m\times m$ matrices over $\mathbb F_2$.
- $\chi$ (source bank), bound on [Bit network](bit-network.md): The source bank, a vector with one bit for each triple.
- $\chi_T$ (source bit), bound on [Bit network](bit-network.md): The bit that the source bank holds at the triple $T$.
- $\nu$ (target bank), bound on [Bit network](bit-network.md): The target bank, a vector with one bit for each triple.
- $\nu_S$ (target bit), bound on [Bit network](bit-network.md): The bit that the target bank holds at the triple $S$.
- $\delta_{ST}$ (side wire), bound on [Bit network](bit-network.md): The scratch wire of an ordered neighbouring pair $(S,T)$.
- $C_e$ (central wire), bound on [Bit network](bit-network.md): The scratch wire attached to the element $e$ of $[h]$.
- $\zeta$ (phase factor), bound on [Phase factor](phase-factor.md): A complex number of modulus one, multiplied into coefficients.
- $\tau$ (complex number), bound on [Phase factor](phase-factor.md): A complex number written as alpha plus beta i.
- $\alpha$ (real part), bound on [Phase factor](phase-factor.md): The real part of the complex number tau.
- $\beta$ (imaginary part), bound on [Phase factor](phase-factor.md): The imaginary part of the complex number tau, a real number.
- $s$ (address), bound on [Phase factor](phase-factor.md): An address in a butterfly layer, whose selected bits determine the phase applied to its value.
- $D$ (selected bit count), bound on [Phase factor](phase-factor.md): The number of selected bits of an address in a layer.
- $C$ (forward kernel), bound on [Phase factor](phase-factor.md): The 2 by 2 matrix called the forward kernel.
- $Z$ (sign matrix), bound on [Phase factor](phase-factor.md): The diagonal matrix diag(1,-1), which negates the entry whose bit is 1.
- $\mathbb{D}$ (Gaussian dyadics), bound on [Gaussian dyadics](gaussian-dyadics.md): The set of numbers $\delta/2^e$ with $\delta$ a Gaussian integer and $e\ge 0$ an integer.
- $\mathbb{Z}[i]$ (Gaussian integers), bound on [Gaussian dyadics](gaussian-dyadics.md): The set of complex numbers whose real and imaginary parts are integers.
- $\delta$ (Gaussian integer numerator), bound on [Gaussian dyadics](gaussian-dyadics.md): The Gaussian integer numerator of a Gaussian dyadic $\delta/2^e$.
- $e$ (denominator exponent), bound on [Gaussian dyadics](gaussian-dyadics.md): The number of factors of two in the denominator of a Gaussian dyadic, a nonnegative integer.
- $\nu$ (second numerator), bound on [Gaussian dyadics](gaussian-dyadics.md): The Gaussian integer numerator of the second Gaussian dyadic $\nu/2^{e'}$.
- $e'$ (second denominator exponent), bound on [Gaussian dyadics](gaussian-dyadics.md): The number of factors of two in the denominator of the second Gaussian dyadic.
- $\tau$ (common exponent), bound on [Gaussian dyadics](gaussian-dyadics.md): The larger of the two denominator exponents, which gives the power of two in a common denominator.
- $K$ (two-point kernel matrix), bound on [Two-point kernel](two-point-kernel.md): The $2\times 2$ matrix $\delta I+\kappa X$ that defines the two-point kernel.
- $\delta$ (diagonal coefficient), bound on [Two-point kernel](two-point-kernel.md): The coefficient of $I$ in $K$, a complex number.
- $\kappa$ (off-diagonal coefficient), bound on [Two-point kernel](two-point-kernel.md): The coefficient of $X$ in $K$, a complex number.
- $X$ (bit flip), bound on [Two-point kernel](two-point-kernel.md): The $2\times 2$ matrix that interchanges the two entries of a pair.
- $d$ (address length), bound on [Two-point kernel](two-point-kernel.md): The number of bits in a binary address, a count.
- $\nu$ (address), bound on [Two-point kernel](two-point-kernel.md): An integer whose binary form with $d$ bits is one address of an array.
- $e$ (bit position), bound on [Two-point kernel](two-point-kernel.md): The index of the address bit along which the kernel acts, counted from the least significant bit.
- $\oplus$ (bitwise exclusive or), bound on [Two-point kernel](two-point-kernel.md): The operation giving the bitwise exclusive or of two addresses.
- $\chi$ (array), bound on [Two-point kernel](two-point-kernel.md): An array of complex values, with one entry for each address.
- $K_e$ (kernel along a bit), bound on [Two-point kernel](two-point-kernel.md): The operator on arrays that applies $K$ to each pair of entries whose addresses differ in bit $e$.
- $i$ (imaginary unit), bound on [Gaussian integer](gaussian-integer.md): The complex number whose square is $-1$.
- $\mathbb{Z}[i]$ (Gaussian integers), bound on [Gaussian integer](gaussian-integer.md): The set of all Gaussian integers.
- $\mathbb{Z}[i,1/2]$ (dyadic Gaussian integers), bound on [Gaussian integer](gaussian-integer.md): The Gaussian integers divided by powers of two.
- $y$ (indeterminate), bound on [Polynomial ring](polynomial-ring.md): The formal variable of the polynomials in the ring.
- $f$ (modulus polynomial), bound on [Polynomial ring](polynomial-ring.md): The monic complex polynomial whose multiples count as zero.
- $m$ (modulus degree), bound on [Polynomial ring](polynomial-ring.md): The number of coefficients in each representative, which is the degree of $f$.
- $R$ (polynomial ring modulo f), bound on [Polynomial ring](polynomial-ring.md): The ring of classes of complex polynomials in $y$, where multiples of $f$ are zero.
- $r$ (modulus exponent), bound on [Polynomial ring](polynomial-ring.md): The exponent of $y$ in the modulus $y^r+1$, a power of two at least 2.
- $u$ (representative), bound on [Polynomial ring](polynomial-ring.md): The unique polynomial of degree less than $m$ in a class.
- $u_t$ (coefficient), bound on [Polynomial ring](polynomial-ring.md): The complex coefficient of $y^t$ in the representative $u$.
- $t$ (coefficient index), bound on [Polynomial ring](polynomial-ring.md): The index of a coefficient, running from 0 to $m-1$.
- $e$ (power exponent), bound on [Polynomial ring](polynomial-ring.md): The exponent of $y$ in a power $y^e$ that is reduced when $e \ge m$.
- $s$ (shift exponent), bound on [Polynomial ring](polynomial-ring.md): The integer exponent in a shift $y^s$ by which a coefficient list is moved.
- $\mathbb{Z}$ (integers), bound on [Grid numerator](grid-numerator.md): The set of integers, whose elements are the whole numbers, which may be negative.
- $\chi$ (number of congruences), bound on [Chinese remainder theorem](chinese-remainder-theorem.md): The number of congruences in the system, a positive integer.
- $\nu$ (congruence index), bound on [Chinese remainder theorem](chinese-remainder-theorem.md): An index numbering the congruences, running from 1 to $\chi$.
- $\kappa_\nu$ (modulus), bound on [Chinese remainder theorem](chinese-remainder-theorem.md): The modulus of the $\nu$-th congruence, a positive integer.
- $\delta_\nu$ (residue), bound on [Chinese remainder theorem](chinese-remainder-theorem.md): The residue of the $\nu$-th congruence, an integer.
- $\tau$ (solution), bound on [Chinese remainder theorem](chinese-remainder-theorem.md): An unknown integer, which is a solution when it satisfies every congruence of the system.
- $\Lambda$ (product of moduli), bound on [Chinese remainder theorem](chinese-remainder-theorem.md): The product of the moduli $\kappa_1,\dots,\kappa_\chi$, a positive integer.
- $\pi_\nu$ (inverse of cofactor), bound on [Chinese remainder theorem](chinese-remainder-theorem.md): An integer that inverts $\Lambda/\kappa_\nu$ modulo $\kappa_\nu$.
- $f$ (first input sequence), bound on [Cyclic convolution](cyclic-convolution.md): The first of the two sequences of length n whose cyclic convolution is taken.
- $g$ (second input sequence), bound on [Cyclic convolution](cyclic-convolution.md): The second of the two sequences of length n whose cyclic convolution is taken.
- $\ast$ (cyclic convolution), bound on [Cyclic convolution](cyclic-convolution.md): The operation sending two sequences of length n to their cyclic convolution.
- $w$ (formal variable), bound on [Cyclic convolution](cyclic-convolution.md): The variable whose powers index the entries of the polynomial that represents a sequence.
- $d$ (number of axes), bound on [Cyclic convolution](cyclic-convolution.md): The number of pairwise coprime factors of n, which is the number of axes of the multidimensional cyclic convolution.
- $\kappa$ (axis index), bound on [Cyclic convolution](cyclic-convolution.md): The index of an axis, running from 1 to d.
- $n_\kappa$ (axis length), bound on [Cyclic convolution](cyclic-convolution.md): The length of axis kappa, the number of values its coordinate takes, a factor of n.
- $\mu_\kappa$ (layout exponent), bound on [Cyclic convolution](cyclic-convolution.md): An integer invertible modulo n_kappa, which sets the exponent of axis kappa in the layout map.
- $\Phi$ (coefficient layout map), bound on [Cyclic convolution](cyclic-convolution.md): The map sending the cyclic ring to the multidimensional ring, which places each coefficient at an array position.
- $\nu_\kappa$ (axis variable), bound on [Cyclic convolution](cyclic-convolution.md): The formal variable of axis kappa in the multidimensional ring.
- $\varepsilon$ (exponent offset), bound on [Cyclic convolution](cyclic-convolution.md): The amount by which a reduced exponent exceeds n.
- $\chi_j$ (chirp factor), bound on [Cyclic convolution](cyclic-convolution.md): The phase factor e^{pi i j^2/t} of input position j.
- $\tau$ (reflected chirp), bound on [Cyclic convolution](cyclic-convolution.md): The function tau(delta) of an integer delta, read as a sequence of length t.
- $QFt$ (middle transform), bound on [Cyclic convolution](cyclic-convolution.md): The Fourier-type middle factor of the paper's equation (35).
- $Q$ (quotient ring), bound on [Ring homomorphism and isomorphism](ring-homomorphism.md): The ring of complex polynomials in $t$ in which $t^2=1$.
- $t$ (indeterminate), bound on [Ring homomorphism and isomorphism](ring-homomorphism.md): The indeterminate of $Q$, whose square is 1 in $Q$.
- $Q'$ (target ring), bound on [Ring homomorphism and isomorphism](ring-homomorphism.md): The ring of complex polynomials in $y$ in which $y^2=-1$.
- $y$ (target indeterminate), bound on [Ring homomorphism and isomorphism](ring-homomorphism.md): The indeterminate of $Q'$.
- $u$ (constant coefficient), bound on [Ring homomorphism and isomorphism](ring-homomorphism.md): The complex constant term of an element $u+vy$ of $Q'$.
- $v$ (linear coefficient), bound on [Ring homomorphism and isomorphism](ring-homomorphism.md): The complex coefficient of $y$ in an element $u+vy$ of $Q'$.
- $\theta$ (homomorphism), bound on [Ring homomorphism and isomorphism](ring-homomorphism.md): A map from one ring to another that preserves both operations.
- $\xi$ (element), bound on [Ring homomorphism and isomorphism](ring-homomorphism.md): An arbitrary element of the domain ring.
- $\eta$ (second element), bound on [Ring homomorphism and isomorphism](ring-homomorphism.md): An arbitrary element of the domain ring.
- $\alpha$ (coefficient), bound on [Ring homomorphism and isomorphism](ring-homomorphism.md): The complex constant term of an element $\alpha+\delta t$ of $Q$.
- $\delta$ (linear coefficient), bound on [Ring homomorphism and isomorphism](ring-homomorphism.md): The complex coefficient of $t$ in an element $\alpha+\delta t$ of $Q$.
- $\rho$ (reduction map), bound on [Ring homomorphism and isomorphism](ring-homomorphism.md): The map from $Q$ to $\mathbb{C}$ sending $\alpha+\delta t$ to $\alpha+\delta$.
- $S$ (cycle length), bound on [Ring homomorphism and isomorphism](ring-homomorphism.md): A positive integer by which the paper's cyclic ring is reduced.
- $x$ (indeterminate), bound on [Chinese-remainder map](chinese-remainder-map.md): The indeterminate of the one-dimensional ring, whose powers index positions.
- $x_i$ (axis indeterminate), bound on [Chinese-remainder map](chinese-remainder-map.md): The indeterminate of axis i in the multidimensional target ring.
- $\eta_i$ (axis exponent), bound on [Chinese-remainder map](chinese-remainder-map.md): The exponent of x_i in a monomial of the target ring, an integer from 0 to lambda_i minus 1 for basis monomials.
- $e$ (coefficient index), bound on [Chinese-remainder map](chinese-remainder-map.md): An ordinary coefficient index, an integer from 0 to Lambda minus 1.
- $\nu$ (exponent), bound on [Chinese-remainder map](chinese-remainder-map.md): A nonnegative integer exponent of Phi(x) in the order argument.
- $\gamma_i$ (axis coordinate), bound on [Chinese-remainder map](chinese-remainder-map.md): The coordinate of the index e on axis i, an integer in [0, lambda_i).
- $m$ (sequence length), bound on [Pointwise product](pointwise-product.md): The number of entries in each sequence, so $m$ counts the entries.
- $u$ (first input sequence), bound on [Pointwise product](pointwise-product.md): The first of the two input sequences, of length $m$.
- $v$ (second input sequence), bound on [Pointwise product](pointwise-product.md): The second of the two input sequences, of length $m$.
- $j$ (entry index), bound on [Pointwise product](pointwise-product.md): An index naming one position in each sequence, with $0 \le j < m$.
- $w$ (pointwise product), bound on [Pointwise product](pointwise-product.md): The sequence of length $m$ whose entry at each index is the product of the entries of $u$ and $v$ at that index.
- $r$ (ring size), bound on [Pointwise product](pointwise-product.md): A power of two that counts the complex coefficients in an entry, since each entry is a polynomial of degree less than $r$.
- $y$ (indeterminate), bound on [Pointwise product](pointwise-product.md): The indeterminate of the quotient ring $\mathbb{C}[y]/(y^r+1)$ whose elements are the entries.
- $P$ (normalized pointwise product), bound on [Pointwise product](pointwise-product.md): The map that sends two entries to their product in the ring divided by $r$.
- $f$ (disk-grid ring array), bound on [Opposite transform](opposite-transform.md): One of the two disk-grid ring arrays whose convolution the synthetic transforms compute.
- $g$ (second disk-grid ring array), bound on [Opposite transform](opposite-transform.md): The second of the two disk-grid ring arrays whose convolution the synthetic transforms compute.
- $M$ (pointwise product count), bound on [Opposite transform](opposite-transform.md): The number of pointwise polynomial products, a count that is not the record count of earlier pages.

## Pages that build on this one

- Independence of events: Two events are independent when the probability that both occur equals the product of their probabilities.

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

## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

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

Write the body to `exegenius/tasks/0558-write-probability.answer.md` and the JSON to `exegenius/tasks/0558-write-probability.answer.json`, then run `exegenius submit 0558-write-probability` in the project directory. If submit rejects the answer, fix the answer and submit again.
