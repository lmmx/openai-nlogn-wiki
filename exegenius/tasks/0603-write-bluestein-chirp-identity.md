# exegenius task 0603-write-bluestein-chirp-identity

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
- Synthetic polynomial transforms (also: Nussbaumer polynomial transforms, polynomial transforms, Nussbaumer and Quandalle, the paper's representation)
- Polynomial ring modulo y^r + 1 (also: negacyclic polynomial ring, quotient ring)
  - $y$ (polynomial variable): The indeterminate of the polynomial ring, whose powers act as roots of unity.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
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
- Transform identity with retained permutations (also: target permutation, coordinate permutations, retained order)
- Carry propagation (also: carry scan)
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
- Mixed-radix digits (also: mixed-radix digit, digit)
- Multidimensional transform (also: multidimensional transforms with power-of-two axes)
- Array norm (also: norm of an array, coefficient bound, norm of a vector)
- Normalized cyclic convolution
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

Concept: Bluestein's chirp identity
Gloss: An identity that rewrites a Fourier transform as a cyclic convolution multiplied by chirp factors, so that it can be computed with convolution.
Also called: chirp identity

## This page in the argument

The step: The middle transform, including its target permutation, becomes a normalized cyclic convolution.
How: rewrite the transform as a cyclic convolution multiplied by chirp factors
Why: A chirp factorisation turns the middle transform into a cyclic convolution, which the earlier steps already compute. (the sources leave this for the reader to work out: spell it out)

Its sub-steps, in order:

- Bluestein’s chirp identity converts the middle transform, including its target permutation, into normalized cyclic convolution.

It serves these steps, from the main result down:

- Exact multiplication of two $n$-bit integers runs in $O(n(\lg n)^{1-\kappa})$ time on one deterministic fixed-tape machine, with $\kappa = 2^{-182}$.; how: reduce exact multiplication to radix-digit convolution, compute that convolution with fast tape transforms, and recover the exact product (on [Integer multiplication below n log n](main-theorem.md))

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
- $\Omega$ (sample space), bound on [Independence of events](independence.md): The finite set of all possible outcomes of the experiment.
- $\mathcal{C}$ (first event), bound on [Independence of events](independence.md): An event, that is, a subset of the sample space.
- $\mathcal{D}$ (second event), bound on [Independence of events](independence.md): An event, that is, a subset of the sample space.
- $\Pr$ (probability function), bound on [Independence of events](independence.md): The function giving the probability of each event.
- $|\mathcal{C}|$ (event size), bound on [Independence of events](independence.md): The number of outcomes in the event C, a count.
- $\mathcal{C}\cap\mathcal{D}$ (both events occurring), bound on [Independence of events](independence.md): The event that both C and D occur, the set of outcomes lying in both.
- $N$ (entry count), bound on [Multidimensional transform](multidimensional-transform.md): The number of entries of the array, the product of the axis lengths.
- $Y$ (output array), bound on [Multidimensional transform](multidimensional-transform.md): The output array of the transform.
- $\mathcal F$ (multidimensional transform), bound on [Multidimensional transform](multidimensional-transform.md): The multidimensional transform, which sends an input array X to its transform Y.
- $s$ (axis index), bound on [Multidimensional transform](multidimensional-transform.md): The index of one axis, running from 1 to D.
- $\nu$ (input position), bound on [Multidimensional transform](multidimensional-transform.md): A position in the input array, a tuple of D coordinates with the s-th coordinate between 0 and t_s minus 1.
- $\kappa$ (output position), bound on [Multidimensional transform](multidimensional-transform.md): A position in the output array, a tuple of D coordinates with the same bounds as a position in the input array.
- $\pi$ (circle constant), bound on [Multidimensional transform](multidimensional-transform.md): The ratio of a circle's circumference to its diameter.
- $y$ (polynomial variable), bound on [Multidimensional transform](multidimensional-transform.md): The variable of the polynomial that stores one coordinate of the array.
- $s$ (source length), bound on [Gaussian resampling](gaussian-resampling.md): The number of entries in the source vector, the length of the transform being replaced.
- $t$ (resampled length), bound on [Gaussian resampling](gaussian-resampling.md): The number of entries in the resampled vector, a power of two greater than $s$.
- $\ell$ (halving count), bound on [Gaussian resampling](gaussian-resampling.md): The number of halvings of a transform length, so that the length is $2^\ell$.
- $\alpha$ (Gaussian width), bound on [Gaussian resampling](gaussian-resampling.md): The integer width of the Gaussian weights.
- $\theta$ (relative gap), bound on [Gaussian resampling](gaussian-resampling.md): The relative gap $t/s-1$ between the two lengths.
- $u$ (generic source vector), bound on [Gaussian resampling](gaussian-resampling.md): A generic vector of length $s$, on which $P_s$ acts.
- $v$ (generic resampled vector), bound on [Gaussian resampling](gaussian-resampling.md): A generic vector of length $t$, on which $P_t$ acts.
- $j$ (source position), bound on [Gaussian resampling](gaussian-resampling.md): An index position of a length-$s$ vector, running from $0$ to $s-1$ in the permutation.
- $k$ (resampled position), bound on [Gaussian resampling](gaussian-resampling.md): An index position of a length-$t$ vector in the permutation $P_t$.
- $P_s$ (source permutation), bound on [Gaussian resampling](gaussian-resampling.md): The coordinate permutation of length-$s$ vectors defined by $(P_s u)_j = u_{tj \bmod s}$.
- $P_t$ (resampled permutation), bound on [Gaussian resampling](gaussian-resampling.md): The coordinate permutation of length-$t$ vectors defined by $(P_t v)_k = v_{-sk \bmod t}$.
- $E$ (map into length t), bound on [Gaussian resampling](gaussian-resampling.md): A linear contraction from length-$s$ vectors to length-$t$ vectors, in the identity.
- $U$ (map back to s), bound on [Gaussian resampling](gaussian-resampling.md): A linear contraction from length-$t$ vectors to length-$s$ vectors, in the identity.
- $\Sigma$ (first resampling map), bound on [Gaussian resampling](gaussian-resampling.md): One of the two maps from length-$s$ to length-$t$ vectors used in the proof.
- $\Gamma$ (second resampling map), bound on [Gaussian resampling](gaussian-resampling.md): The other of the two maps from length-$s$ to length-$t$ vectors used in the proof.
- $N$ (near-identity map), bound on [Gaussian resampling](gaussian-resampling.md): A map built from $\Gamma$ and Gaussian corrections, close to the identity.
- $a$ (rational rank), bound on [Matrix rank](matrix-rank.md): The rational rank of $A$, the number of its linearly independent rows, which is also the number of ones in $\Pi$.
- $E_1$ (left lower factor), bound on [Matrix rank](matrix-rank.md): An invertible lower triangular matrix, the left factor in the factorization $A = E_1 \Pi E_2$.
- $E_2$ (right lower factor), bound on [Matrix rank](matrix-rank.md): An invertible lower triangular matrix, the right factor in the factorization $A = E_1 \Pi E_2$.
- $\Pi$ (partial permutation matrix), bound on [Matrix rank](matrix-rank.md): The matrix in the factorization with at most one 1 in each row and column and zeros elsewhere.
- $H$ (first field vector), bound on [Matrix rank](matrix-rank.md): The vector $(H_1, \ldots, H_m)$ of $m$ address fields that the shear updates.
- $D$ (second field vector), bound on [Matrix rank](matrix-rank.md): The vector $(D_1, \ldots, D_m)$ of $m$ address fields, which the shear reads without changing.
- $s$ (row index), bound on [Matrix rank](matrix-rank.md): The row of a one in $\Pi$, which is also the index of the field $H_s$ it updates.
- $\ell$ (column index), bound on [Matrix rank](matrix-rank.md): The column of a one in $\Pi$, which is also the index of the field $D_\ell$ it uses.
- $W$ (wire count), bound on [Matrix rank](matrix-rank.md): The number of wires in the network, which counts the edges that carry edge changes.
- $\theta$ (eigenvalue), bound on [Eigenvalue](eigenvalue.md): A scalar in F for which the operator T maps some nonzero vector e to the multiple θe.
- $V$ (operator space), bound on [Eigenvalue](eigenvalue.md): The vector space on which the linear operator T acts.
- $e$ (eigenvector), bound on [Eigenvalue](eigenvalue.md): A nonzero vector of V that the operator T maps to a multiple of itself.
- $J$ (all-one matrix), bound on [Eigenvalue](eigenvalue.md): The h by h matrix with every entry equal to 1.
- $\mathbf{1}$ (all-one vector), bound on [Eigenvalue](eigenvalue.md): The vector in Q^h whose entries are all equal to 1.
- $d$ (zero-sum vector), bound on [Eigenvalue](eigenvalue.md): A vector in Q^h whose entries sum to zero.
- $E$ (vector space), bound on [Bilinear form](bilinear-form.md): A vector space over the field $F$ of scalars, on which the bilinear form is defined.
- $\xi$ (vector), bound on [Bilinear form](bilinear-form.md): A vector of $E$.
- $\eta$ (vector), bound on [Bilinear form](bilinear-form.md): A vector of $E$.
- $U$ (subspace), bound on [Bilinear form](bilinear-form.md): A subspace of $E$, whose orthogonal complement is taken.
- $U^\perp$ (orthogonal complement), bound on [Bilinear form](bilinear-form.md): The set of vectors of $E$ orthogonal to every vector of $U$.
- $\xi_1$ (first coordinate), bound on [Bilinear form](bilinear-form.md): The first coordinate of the vector $\xi$ in $\mathbb{Q}^2$.
- $\xi_2$ (second coordinate), bound on [Bilinear form](bilinear-form.md): The second coordinate of the vector $\xi$ in $\mathbb{Q}^2$.
- $\eta_1$ (first coordinate), bound on [Bilinear form](bilinear-form.md): The first coordinate of the vector $\eta$ in $\mathbb{Q}^2$.
- $\eta_2$ (second coordinate), bound on [Bilinear form](bilinear-form.md): The second coordinate of the vector $\eta$ in $\mathbb{Q}^2$.
- $e_i$ (basis vector), bound on [Bilinear form](bilinear-form.md): The $i$-th vector of the fixed basis of $E$.
- $A$ (form matrix), bound on [Bilinear form](bilinear-form.md): The $m\times m$ matrix of the form in the chosen basis.
- $\mathsf{T}$ (transpose), bound on [Bilinear form](bilinear-form.md): The operation turning a column of coordinates into the row with the same entries.
- $J$ (all-one matrix), bound on [Bilinear form](bilinear-form.md): The $h\times h$ matrix whose entries are all $1$.
- $\mathbf{1}$ (all-one vector), bound on [Bilinear form](bilinear-form.md): The column of $h$ ones.
- $T'$ (second triple), bound on [Bilinear form](bilinear-form.md): A second triple, another three-element subset of $[h]$.
- $S$ (triple S), bound on [Indicator vector](indicator-vector.md): A three-element subset of the ground set, called a triple, paired with T as a candidate neighbor.
- $T$ (triple T), bound on [Indicator vector](indicator-vector.md): A three-element subset of the ground set, called a triple, whose indicator vector is discussed.
- $t_T$ (indicator vector of T), bound on [Indicator vector](indicator-vector.md): The 0-1 vector with an entry 1 in each position of T and 0 elsewhere.
- $J$ (all-ones matrix), bound on [Indicator vector](indicator-vector.md): The h by h matrix with every entry equal to 1.
- $\mathbb{F}_2$ (binary field), bound on [Indicator vector](indicator-vector.md): The field with two elements, 0 and 1, in which 1+1=0.
- $\mathbb{Q}$ (rational numbers), bound on [Indicator vector](indicator-vector.md): The field of rational numbers.
- $K$ (scalar field), bound on [Line spanned by a vector](line-spanned-by-vector.md): The field of scalars over which the vector space E is taken.
- $E$ (vector space), bound on [Line spanned by a vector](line-spanned-by-vector.md): A vector space over K, containing the nonzero vector v.
- $v$ (nonzero vector), bound on [Line spanned by a vector](line-spanned-by-vector.md): A nonzero vector of E whose scalar multiples form a line; here it is a vector, not a vertex.
- $\operatorname{span}\{v\}$ (line spanned by v), bound on [Line spanned by a vector](line-spanned-by-vector.md): The set of all scalar multiples cv of the nonzero vector v, a one-dimensional subspace.
- $c'$ (second scalar), bound on [Line spanned by a vector](line-spanned-by-vector.md): A second scalar, an element of K, used with c in the closure and bilinearity computations.
- $\mathbb{R}$ (real numbers), bound on [Line spanned by a vector](line-spanned-by-vector.md): The field of real numbers.
- $\tau$ (choice of three triples), bound on [Line spanned by a vector](line-spanned-by-vector.md): A triple (tau_1, tau_2, tau_3) of three-element subsets of the ground set, selecting one label.
- $u_\tau$ (triple tensor product), bound on [Line spanned by a vector](line-spanned-by-vector.md): The tensor product of the indicator vectors of the three triples in tau.
- $U_\tau$ (triple label line), bound on [Line spanned by a vector](line-spanned-by-vector.md): The line spanned by u_tau, the label attached to the choice tau.
- $X_\tau$ (data bank X), bound on [Line spanned by a vector](line-spanned-by-vector.md): One of the two data banks of the network, which carries the label U_tau at the start.
- $Y_\tau$ (data bank Y), bound on [Line spanned by a vector](line-spanned-by-vector.md): The other of the two data banks of the network, which carries the label at the end.
- $U'$ (smaller label), bound on [Subspace labels](subspace-labels.md): The smaller of the two labels on an edge, contained in the larger label $U$.
- $\oplus$ (direct sum), bound on [Subspace labels](subspace-labels.md): The sum of two subspaces that meet only in zero, so that each vector of the sum is uniquely a vector of one plus a vector of the other.
- $u_1$ (component in U'), bound on [Subspace labels](subspace-labels.md): The part of a vector $u\in U$ lying in the subspace $U'$.
- $u_2$ (component in U' perp), bound on [Subspace labels](subspace-labels.md): The part of a vector $u\in U$ lying in the orthogonal complement $U'^\perp$.
- $C_U$ (frame of a label), bound on [Subspace labels](subspace-labels.md): The invertible operator on arrays attached to a vertex whose label is $U$, the change of representation at that vertex.
- $P_U$ (label projection), bound on [Subspace labels](subspace-labels.md): The projection onto the binary label $U$ along $U^\perp$, computed over $\mathbb F_2$.
- $\mathrm{wt}$ (Hamming weight), bound on [Subspace labels](subspace-labels.md): The number of ones in a binary vector, computed as an integer.
- $H$ (Hadamard matrix), bound on [Subspace labels](subspace-labels.md): The $2\times 2$ matrix with entries $\pm 1/\sqrt2$ that defines the frame $C_U$ through its tensor powers.
- $\tau$ (kernel coefficient tau), bound on [Subspace labels](subspace-labels.md): The first Gaussian dyadic coefficient of the translation kernel $\tau I+\delta X_v$.
- $\delta$ (kernel coefficient delta), bound on [Subspace labels](subspace-labels.md): The second Gaussian dyadic coefficient of the translation kernel $\tau I+\delta X_v$.
- $X_v$ (translation operator), bound on [Subspace labels](subspace-labels.md): The operator that shifts a function of addresses by the vector $v$, so that $(X_vf)(x)=f(x+v)$.
- $v$ (shift vector), bound on [Subspace labels](subspace-labels.md): A vector in $\mathbb F_2^m$ by which a translation shifts addresses (this letter changes meaning on this page).
- $f$ (function of addresses), bound on [Subspace labels](subspace-labels.md): A function from addresses in $\mathbb F_2^m$ to values, which a translation shifts (this letter changes meaning on this page).
- $\varrho$ (residual dimension), bound on [Subspace labels](subspace-labels.md): The number of vectors in the orthonormal basis of an edge residual, which equals the dimension of the residual, the number of kernels on that edge.
- $\top$ (transpose), bound on [Subspace labels](subspace-labels.md): The transpose of a matrix or vector.
- $T'$ (second triple), bound on [Subspace labels](subspace-labels.md): A second three-element subset of the ground set, compared with a triple $T$.
- $\mathcal T$ (set of triples), bound on [Subset-intersection network](subset-intersection-network.md): The set of all three-element subsets of the ground set $[h]$.
- $X$ (bank X), bound on [Subset-intersection network](subset-intersection-network.md): One of the two banks of scalars, with entries $X_\tau$ indexed by triples of triples.
- $Y$ (bank Y), bound on [Subset-intersection network](subset-intersection-network.md): The second of the two banks of scalars, with entries $Y_\tau$.
- $\tau$ (bank index), bound on [Subset-intersection network](subset-intersection-network.md): A triple of triples, indexing the entries of a bank.
- $\xi$ (source vector), bound on [Subset-intersection network](subset-intersection-network.md): The vector of one bank's entries along the varying coordinate, read by a forward invocation.
- $\eta$ (target vector), bound on [Subset-intersection network](subset-intersection-network.md): The vector of the other bank's entries along the varying coordinate, updated by a forward invocation.
- $W_{ST}$ (side wire), bound on [Subset-intersection network](subset-intersection-network.md): The scratch wire for an ordered pair of neighbouring triples $(S,T)$.
- $C_\ell$ (central wire), bound on [Subset-intersection network](subset-intersection-network.md): The scratch wire attached to an element $\ell$ of the ground set.
- $\ell$ (ground element), bound on [Subset-intersection network](subset-intersection-network.md): An element of the ground set $[h]$, whose central wire is $C_\ell$.
- $\delta$ (vector of E), bound on [Subset-intersection network](subset-intersection-network.md): A vector of the ambient space $E=\mathbb Q^h$, an argument of the bit network form.
- $U'$ (larger label), bound on [Subset-intersection network](subset-intersection-network.md): The larger of the two nested labels on an edge, which contains the smaller label $U$.
- $x$ (control vector), bound on [Scratch storage](scratch-storage.md): The vector of control values, with one entry $x_T$ for each triple $T$.
- $y$ (target vector), bound on [Scratch storage](scratch-storage.md): The vector of target values, with one entry $y_S$ for each triple $S$.
- $a$ (starting side values), bound on [Scratch storage](scratch-storage.md): The starting values of the side wires $W_{ST}$.
- $c$ (starting central values), bound on [Scratch storage](scratch-storage.md): The starting values of the central wires $C_\ell$.
- $V$ (copy operator), bound on [Scratch storage](scratch-storage.md): The operator that adds each control value $x_T$ to the side wire $W_{ST}$ of each neighbouring pair $(S,T)$.
- $J$ (side injection), bound on [Scratch storage](scratch-storage.md): The operator that adds to $y_S$ the side wires $W_{ST}$ summed over the neighbours $T$ of $S$.
- $G$ (gather operator), bound on [Scratch storage](scratch-storage.md): The operator that adds each control value $x_T$ to every central wire $C_\ell$ with $\ell$ in $T$.
- $R$ (scatter operator), bound on [Scratch storage](scratch-storage.md): The operator that adds to $y_S$ the central wires $C_\ell$ summed over the elements $\ell$ of $S$.
- $S$ (triple), bound on [Scratch storage](scratch-storage.md): A three-element subset of the ground set, indexing a target value $y_S$.
- $T$ (triple), bound on [Scratch storage](scratch-storage.md): A three-element subset of the ground set, indexing a control value $x_T$.
- $W_{ST}$ (side wire), bound on [Scratch storage](scratch-storage.md): The auxiliary wire of a neighbouring pair $(S,T)$ of triples.
- $C_\ell$ (central wire), bound on [Scratch storage](scratch-storage.md): The auxiliary wire attached to the element $\ell$ of the ground set.
- $\ell$ (ground element), bound on [Scratch storage](scratch-storage.md): An element of the ground set, indexing the central wires $C_\ell$.
- $x$ (first field), bound on [Address-field interchange](address-interchange.md): One of the two disjoint address fields being interchanged, read as a block of bits.
- $y$ (second field), bound on [Address-field interchange](address-interchange.md): The other of the two disjoint address fields being interchanged, read as a block of bits.
- $\oplus$ (exclusive or), bound on [Address-field interchange](address-interchange.md): Bitwise exclusive or: the sum modulo 2 of two bits, taken position by position.
- $m$ (integer base), bound on [Address-field interchange](address-interchange.md): A fixed integer at least 2, the base in which the field width is written as a power.
- $k$ (number of levels), bound on [Address-field interchange](address-interchange.md): The number of levels in the recursion on the width, so that a width $u=m^k$ has $k=\log_m u$ levels.
- $W$ (piece count), bound on [Address-field interchange](address-interchange.md): The number of equal pieces the volume is cut into at each call, at least 2.
- $s$ (call count), bound on [Address-field interchange](address-interchange.md): The number of smaller calls that one call makes.
- $j$ (recursion depth), bound on [Address-field interchange](address-interchange.md): The number of levels below the top call, counting from 0 at the top.
- $\tau$ (exponent), bound on [Address-field interchange](address-interchange.md): A fixed number in $(0,1)$, the exponent of the bound $O(V u^{\tau})$.
- $\delta$ (first bit), bound on [Exclusive or](xor.md): A bit, one of the two inputs to the exclusive or.
- $\epsilon$ (second bit), bound on [Exclusive or](xor.md): A bit, the other input to the exclusive or.
- $\oplus$ (XOR operation), bound on [Exclusive or](xor.md): The exclusive-or operation, the bitwise sum modulo 2 of two bits, applied at each position to bit strings of equal length.
- $\Delta$ (orthogonal residual), bound on [Complex phase network](complex-phase-network.md): The orthogonal residual of an edge, the orthogonal complement of its smaller label inside its larger label.
- $\mathcal{O}$ (residual basis), bound on [Complex phase network](complex-phase-network.md): An orthonormal basis of the residual $\Delta$, whose vectors give one two-point kernel each.
- $V$ (head label), bound on [Complex phase network](complex-phase-network.md): The label at the head of an edge, whose frame is applied last along that edge.
- $\varepsilon_v$ (kernel sign), bound on [Complex phase network](complex-phase-network.md): The sign, plus or minus one, that decides whether the kernel for basis vector $v$ on this edge is forward or inverse.
- $\Theta_v$ (two-point kernel), bound on [Complex phase network](complex-phase-network.md): The operator $\tau_0 I+\tau_1 X_v$ for a binary vector $v$, a translation kernel.
- $\tau_0$ (kernel coefficient), bound on [Complex phase network](complex-phase-network.md): The complex number $(1+i)/2$, the coefficient of the identity in a two-point kernel.
- $\tau_1$ (kernel coefficient), bound on [Complex phase network](complex-phase-network.md): The complex number $(1-i)/2$, the coefficient of the translation in a two-point kernel.
- $P_W$ (label projection), bound on [Complex phase network](complex-phase-network.md): The projection onto a nondegenerate subspace $W$ along its orthogonal complement $W^\perp$.
- $\mathrm{diag}_x$ (diagonal operator), bound on [Complex phase network](complex-phase-network.md): The operator on functions of addresses that multiplies the value at each address $x$ by a given function of $x$.
- $[b]$ (integer representative), bound on [Complex phase network](complex-phase-network.md): The integer, zero or one, that represents a binary value $b$.
- $\mathrm{supp}$ (support), bound on [Complex phase network](complex-phase-network.md): The set of coordinates at which a binary vector is one.
- $e_\delta$ (standard basis vector), bound on [Complex phase network](complex-phase-network.md): The address with a single one at position $\delta$, one of the standard basis vectors of $\mathbb F_2^m$.
- $\delta$ (route step), bound on [Complex phase network](complex-phase-network.md): The index of a step along the coordinate route, running from one to $m$.
- $\delta$ (chunk width), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The number of consecutive address bits in each chunk, one chunk per transform axis.
- $o$ (selected offset), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The position of the selected bit within its chunk, counted from the least significant end, with $0\le o<\delta$.
- $\mathcal{H}$ (normalized Hadamard matrix), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The $2\times2$ matrix $\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$, equal to $\sqrt2\,H_0$.
- $\Delta$ (diagonal phase matrix), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The diagonal $2\times2$ matrix $\mathrm{diag}(1,i)$ that multiplies one basis entry by $i$.
- $X$ (bit-flip matrix), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The $2\times2$ matrix swapping the two coordinates of a bit.
- $C$ (two-point kernel), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The $2\times2$ matrix $\mathcal{H}\Delta\mathcal{H}=\lambda I+\mu X$ acting on one selected bit.
- $\lambda$ (identity coefficient), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The complex coefficient $(1+i)/2$ of the identity $I$ in $C$.
- $\mu$ (bit-flip coefficient), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The complex coefficient $(1-i)/2$ of the bit flip $X$ in $C$.
- $\Delta_D$ (phase operator), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The diagonal operator on $D$ selected bits that multiplies each address by $i$ raised to the number of selected bits equal to 1 there.
- $\Delta$ (guard width), bound on [Guard-width bound](guard-width-bound.md): The count of extra fractional and integer bits reserved per real component, so $p+\Delta$ fractional bits are kept.
- $u$ (first input value), bound on [Guard-width bound](guard-width-bound.md): The first of the two complex input values of the two-point map.
- $v$ (second input value), bound on [Guard-width bound](guard-width-bound.md): The second of the two complex input values of the two-point map.
- $\ell$ (value depth), bound on [Guard-width bound](guard-width-bound.md): The number of arithmetic operations on a chain computing a value from an input.
- $e$ (group size), bound on [Guard-width bound](guard-width-bound.md): The number of selected axes in a group that the recursion splits.
- $A$ (operation bound), bound on [Guard-width bound](guard-width-bound.md): An upper bound on the number of operations on any chain within a group of e axes.
- $m$ (division factor), bound on [Guard-width bound](guard-width-bound.md): The factor by which a call of the complex phase network divides the number of axes.
- $\eta$ (gate constant), bound on [Guard-width bound](guard-width-bound.md): The constant $64(W+m+1)^3$ bounding the operations for gates and corrections at one node.
- $\beta$ (operation growth factor), bound on [Guard-width bound](guard-width-bound.md): The constant $s+\eta$ by which each recursion level multiplies a bound.
- $\nu$ (exponent of the factor), bound on [Guard-width bound](guard-width-bound.md): The least integer $j\ge1$ with $m^j\ge\beta$.
- $C_0$ (depth constant), bound on [Guard-width bound](guard-width-bound.md): The constant $128m\beta^2$ in the depth bound $C_0d^{C_1}$.
- $C_1$ (depth exponent), bound on [Guard-width bound](guard-width-bound.md): The constant $\max\{20,\nu+3\}$ in the depth bound $C_0d^{C_1}$.
- $d$ (axis bound), bound on [Numerical layer](numerical-layer.md): An upper bound on the number $D$ of selected axes in a layer.
- $\lambda'$ (cost exponent), bound on [Numerical layer](numerical-layer.md): A fixed exponent below one in the layer's cost bound.
- $e$ (axes per call), bound on [Numerical layer](numerical-layer.md): The number of selected axes that a call acts on.
- $s$ (smaller-call count), bound on [Numerical layer](numerical-layer.md): The number of smaller calls that one call makes.
- $W$ (role count), bound on [Numerical layer](numerical-layer.md): The number of roles among which rows are distributed.
- $m$ (division factor), bound on [Numerical layer](numerical-layer.md): The fixed integer by which each call divides its number of axes.
- $\Omega$ (outcome set), bound on [Union bound](union-bound.md): The finite set of all outcomes, of which the events are subsets.
- $|X|$ (set size), bound on [Union bound](union-bound.md): The number of elements of the set X.
- $E_i$ (event), bound on [Union bound](union-bound.md): One of the m events, a subset of the outcome set.
- $m$ (event count), bound on [Union bound](union-bound.md): The number of events E_1 through E_m, which here also counts the guards.
- $\Pr$ (probability), bound on [Union bound](union-bound.md): The probability, under the uniform choice of an outcome, that the chosen outcome lies in the given set.
- $f$ (selected bit count), bound on [Union bound](union-bound.md): The number of selected bit positions, which fixes the number of guards 2(f-1).
- $K$ (segment width), bound on [Union bound](union-bound.md): The number of bits in each segment.
- $y$ (address chunk y), bound on [Union bound](union-bound.md): One of the two address chunks, which holds the segment that gives each guard g_i.
- $z$ (address chunk z), bound on [Union bound](union-bound.md): The second address chunk, which holds the segment that gives each guard h_i.
- $g_i$ (guard value g), bound on [Union bound](union-bound.md): The guard value of pair i taken from chunk y, the segment with its lowest bit removed.
- $h_i$ (guard value h), bound on [Union bound](union-bound.md): The guard value of pair i taken from chunk z, defined in the same way as g_i.
- $\delta_{\mathrm{bad}}$ (capped bad fraction), bound on [Union bound](union-bound.md): The bound on the bad fraction of addresses, capped at one.
- $i$ (axis index), bound on [Transform round](transform-round.md): The index of a participating axis, one of the $D$ axes.
- $\ell_i$ (current axis length), bound on [Transform round](transform-round.md): The current recursive length of axis $i$: the number of entries that axis holds at the level the round processes.
- $\beta_i$ (branch bit), bound on [Transform round](transform-round.md): The bit the round writes on axis $i$, recording which output of the butterfly an entry is.
- $\nu_i$ (twiddle index), bound on [Transform round](transform-round.md): The index of the twiddle on axis $i$, an integer with $0\le\nu_i<\ell_i/2$.
- $\eta$ (twiddle exponent), bound on [Transform round](transform-round.md): The exponent of the twiddle at an address, an integer taken modulo $2r$.
- $e$ (quotient of exponent), bound on [Transform round](transform-round.md): The integer quotient of $\eta$ by $r$, which counts the whole multiples of $r$ in $\eta$.
- $\delta$ (remainder of exponent), bound on [Transform round](transform-round.md): The remainder of $\eta$ on division by $r$, with $0\le\delta<r$.
- $\mathcal{H}$ (parallel butterfly), bound on [Transform round](transform-round.md): The butterfly applied on every participating axis at once.
- $\mathcal{J}_\eta$ (monomial operation), bound on [Transform round](transform-round.md): The operation multiplying each record at an address by $y^\eta$.
- $v_0$ (path start vertex), bound on [Endpoint operator](endpoint-operator.md): The first vertex of the three-vertex path, where the route starts.
- $v_1$ (path middle vertex), bound on [Endpoint operator](endpoint-operator.md): The middle vertex of the three-vertex path, whose frame cancels in the composed change.
- $v_2$ (path end vertex), bound on [Endpoint operator](endpoint-operator.md): The last vertex of the three-vertex path, where the route ends.
- $m$ (field count), bound on [Address shear](address-shear.md): The number of fields in each address vector, which is also the size of the square matrix M.
- $H$ (first address vector), bound on [Address shear](address-shear.md): The vector of m address fields that the shear changes.
- $D$ (second address vector), bound on [Address shear](address-shear.md): The vector of m address fields that the shear leaves unchanged.
- $q$ (radix), bound on [Address shear](address-shear.md): A fixed odd prime, the base in which the digits of each field are written.
- $b$ (digits per field), bound on [Address shear](address-shear.md): The number of radix-q digits in each field.
- $\mathbb{Z}$ (integers), bound on [Address shear](address-shear.md): The set of all integers.
- $M$ (shear matrix), bound on [Address shear](address-shear.md): A fixed m by m matrix with rational entries, which determines the shear.
- $a$ (rational rank), bound on [Address shear](address-shear.md): The number of linearly independent rows of M over the rational numbers.
- $\Phi_M$ (shear permutation), bound on [Address shear](address-shear.md): The permutation of array entries that moves the entry at address (H,D) to (H+MD,D).
- $E_1$ (left lower-triangular factor), bound on [Address shear](address-shear.md): An invertible lower-triangular rational matrix, the left factor of M.
- $E_2$ (right lower-triangular factor), bound on [Address shear](address-shear.md): An invertible lower-triangular rational matrix, the right factor of M.
- $\Pi$ (pivot matrix), bound on [Address shear](address-shear.md): A 0/1 matrix with at most one 1 in each row and column, with exactly a ones.
- $e$ (chunk digit count), bound on [Address shear](address-shear.md): The number of radix-q digits in each interchanged chunk, which is m^k at recursion depth k.
- $w$ (key width), bound on [Stable radix sort](stable-radix-sort.md): The number of bits in a record's key, which is also the number of passes.
- $M$ (record count), bound on [Stable radix sort](stable-radix-sort.md): The number of records being sorted.
- $q$ (key), bound on [Stable radix sort](stable-radix-sort.md): The key of a record, a w-bit nonnegative integer written with bits q_{w-1} down to q_0.
- $q_t$ (key bit), bound on [Stable radix sort](stable-radix-sort.md): The bit of a key with weight 2^t, taking the value 0 or 1.
- $t$ (bit position), bound on [Stable radix sort](stable-radix-sort.md): A bit position of a key, running over 0, 1, ..., w-1, which also numbers the passes.
- $A_{\mathrm{rect}}$ (integer bit bound), bound on [Stable radix sort](stable-radix-sort.md): The source's bound on the number of bits in its integers, which the padded destination key width may not exceed.
- $q$ (address before move), bound on [Destination rank](destination-rank.md): The address of a record before the move.
- $q'$ (address after move), bound on [Destination rank](destination-rank.md): The address of the same record after the move.
- $h$ (chunk index), bound on [Destination rank](destination-rank.md): The index of a chunk of an address, taking the value 1, 2 or 3.
- $q_h$ (current chunk value), bound on [Destination rank](destination-rank.md): The value of chunk $h$ in the address $q$ before the move.
- $q'_h$ (destination chunk value), bound on [Destination rank](destination-rank.md): The value of chunk $h$ in the address $q'$ after the move.
- $\sigma_h$ (record stride), bound on [Destination rank](destination-rank.md): The amount by which the rank changes when chunk $h$ rises by one with the other two chunks fixed.
- $B$ (exceptional addresses), bound on [Destination rank](destination-rank.md): The set of exceptional addresses, whose records the correction extracts.
- $A_{\mathrm{rect}}$ (rectangular bit bound), bound on [Destination rank](destination-rank.md): A bound on the number of bits in each integer the rectangular routine handles.
- $R$ (payload bits), bound on [Destination rank](destination-rank.md): The number of payload bits in a record.
- $\Gamma$ (coordinate selection), bound on [Transform identity with retained permutations](transform-identity.md): The map that selects, for each position $j$ of a length-$s$ vector, the coordinate of a length-$t$ vector nearest $tj/s$.
- $\Lambda$ (diagonal scaling), bound on [Transform identity with retained permutations](transform-identity.md): The diagonal scaling on length-$s$ vectors that multiplies each entry by its own nonzero factor.
- $\Upsilon$ (left inverse of T), bound on [Transform identity with retained permutations](transform-identity.md): The map $\Lambda N^{-1}\Gamma$ from length-$t$ to length-$s$ vectors, which satisfies $\Upsilon T=I$.
- $\Pi$ (coordinate permutation), bound on [Transform identity with retained permutations](transform-identity.md): A permutation that rearranges the entries of a vector.
- $R$ (retained permutation), bound on [Transform identity with retained permutations](transform-identity.md): The coordinate permutation $(R_cz)_j=z_{cj}$ for a unit $c$ modulo $s$, applied on each axis, which the identity keeps.
- $\chi$ (modular inverse), bound on [Transform identity with retained permutations](transform-identity.md): An integer with $\chi t\equiv 1 \pmod s$, that is, an inverse of $t$ modulo $s$.
- $\Psi$ (linear map), bound on [Transform identity with retained permutations](transform-identity.md): A generic linear map, which is a contraction when its outputs have norm at most that of its inputs.
- $A$ (forward contraction), bound on [Transform identity with retained permutations](transform-identity.md): A linear contraction from length-$s$ vectors to length-$t$ vectors.
- $B_0$ (backward contraction), bound on [Transform identity with retained permutations](transform-identity.md): A linear contraction from length-$t$ vectors to length-$s$ vectors.
- $w$ (complex vector), bound on [Transform identity with retained permutations](transform-identity.md): A complex vector, the argument of the permutation $P_t$ in this page's notation.
- $\gcd$ (greatest common divisor), bound on [Transform identity with retained permutations](transform-identity.md): The largest integer dividing both $s$ and $t$.
- $\mathcal{L}$ (transform layout), bound on [Transform layout](transform-layout.md): The permutation of record addresses that gathers the selected bits into chunks at a common offset.
- $W_s$ (valid length), bound on [Padded transform box](padded-transform-box.md): The number of data entries along axis $s$, which is the valid length of that axis.
- $E$ (entry count), bound on [Padded transform box](padded-transform-box.md): The number of entries of the box, counting valid and zero entries alike.
- $\mathbf{e}$ (address), bound on [Padded transform box](padded-transform-box.md): A tuple of coordinates, one for each axis, naming one entry of the box.
- $d$ (number of cyclic coordinates), bound on [Cyclic coordinate](cyclic-coordinate.md): The number of cyclic coordinates of an array, a positive integer.
- $\nu$ (coordinate index), bound on [Cyclic coordinate](cyclic-coordinate.md): The index naming one cyclic coordinate, running from 1 to d.
- $\Lambda_\nu$ (cyclic length), bound on [Cyclic coordinate](cyclic-coordinate.md): The number of positions along coordinate nu before its indices wrap around.
- $\kappa$ (last-axis position), bound on [Cyclic coordinate](cyclic-coordinate.md): An integer from 0 to r-1 giving a position along the last cyclic coordinate.
- $\kappa'$ (second last-axis position), bound on [Cyclic coordinate](cyclic-coordinate.md): A second integer from 0 to r-1 giving a position along the last cyclic coordinate.
- $p$ (prime), bound on [Prime number](prime-number.md): A prime number, an integer greater than one with no positive divisors other than one and itself.
- $q$ (second prime), bound on [Prime number](prime-number.md): A prime number different from p, used in the coprimality argument.
- $a$ (divisor), bound on [Prime number](prime-number.md): A positive integer that divides another integer.
- $m$ (dividend), bound on [Prime number](prime-number.md): An integer that a divisor a divides.
- $k$ (cofactor), bound on [Prime number](prime-number.md): An integer with m equal to a times k.
- $\Upsilon$ (logical bit volume), bound on [Logical bit volume](logical-bit-volume.md): The number of bits in a padded transform box, counting every entry at its record width.
- $\chi$ (record width), bound on [Logical bit volume](logical-bit-volume.md): The number of bits in one record of the box.
- $b$ (bit length of n), bound on [Cost table](cost-table.md): The rounded-up base-2 logarithm of n, which is the number of bits of n.
- $p$ (working precision), bound on [Cost table](cost-table.md): The working precision in bits, p = 6b, so that p = Theta(log n).
- $T$ (padded box cell count), bound on [Cost table](cost-table.md): The number of cells of the padded box, a power of two with 4n/b <= T < 8n/b.
- $V$ (logical bit volume), bound on [Cost table](cost-table.md): The logical bit volume V = Tp of the padded box, which is Theta(n) bits.
- $\epsilon$ (size exponent), bound on [Cost table](cost-table.md): A fixed positive rational exponent, 2^{-75} in the paper's choice, with d = Theta(p^epsilon).
- $c$ (chunk exponent), bound on [Cost table](cost-table.md): A fixed positive rational exponent, 2^{-56} in the paper's choice, with K = Theta(p^{epsilon c}).
- $\delta$ (resampling exponent), bound on [Cost table](cost-table.md): A fixed rational exponent, 1/16 in the paper's choice, in the powers of the Gaussian and chirp rows.
- $\alpha$ (line-map factor), bound on [Cost table](cost-table.md): The factor of the Gaussian line-map cost, with alpha = Theta(p^{1/4+epsilon/2}).
- $K$ (chunk width), bound on [Cost table](cost-table.md): The width of the address chunks, in bits, K = floor(d^c) = Theta(p^{epsilon c}).
- $r$ (largest axis length), bound on [Cost table](cost-table.md): The largest axis length of the padded box, a power of two, whose base-two logarithm is ell.
- $N$ (input bit length), bound on [Established O(n log n) multiplier](established-multiplier.md): The number of bits in each input, which is the count the multiplier's cost is measured in.
- $\log$ (base-2 logarithm), bound on [Established O(n log n) multiplier](established-multiplier.md): The base-2 logarithm, the power to which 2 must be raised to give the argument.
- $f$ (first polynomial), bound on [Signed coefficient packing](signed-packing.md): The first input, an integer polynomial whose coefficients are the $f_j$.
- $g$ (second polynomial), bound on [Signed coefficient packing](signed-packing.md): The second input, an integer polynomial whose coefficients are the $g_j$.
- $f_j$ (coefficient of f), bound on [Signed coefficient packing](signed-packing.md): The integer coefficient of $y^j$ in $f$.
- $g_j$ (coefficient of g), bound on [Signed coefficient packing](signed-packing.md): The integer coefficient of $y^j$ in $g$.
- $j$ (coefficient position), bound on [Signed coefficient packing](signed-packing.md): The position of a coefficient in a record, running from 0 to r-1.
- $p$ (magnitude exponent), bound on [Signed coefficient packing](signed-packing.md): The number of bits in the magnitude bound on a coefficient, so each coefficient has magnitude at most $2^p$.
- $B$ (block base), bound on [Signed coefficient packing](signed-packing.md): The base $2^{4p}$ of the packing, at which each coefficient occupies one block of $4p$ bits.
- $h$ (product polynomial), bound on [Signed coefficient packing](signed-packing.md): The ordinary product $fg$, a polynomial whose coefficients are the $h_j$.
- $h_j$ (product coefficient), bound on [Signed coefficient packing](signed-packing.md): The coefficient of $y^j$ in the product $h$.
- $h_0$ (constant coefficient), bound on [Signed coefficient packing](signed-packing.md): The coefficient of $y^0$ in $h$, the constant term of the product.
- $c$ (centered residue), bound on [Signed coefficient packing](signed-packing.md): The unique integer in $[-B/2, B/2)$ congruent to $f(B)\,g(B)$ modulo $B$.
- $i$ (summation index), bound on [Signed coefficient packing](signed-packing.md): The index of the sum that gives $h_j$, running over the positions $0$ to $r-1$ of $f$.
- $\kappa$ (exponent gap), bound on [Schoolbook multiplication](schoolbook-multiplication.md): A fixed constant, $2^{-182}$, which sets the saving in the exponent $1-\kappa$ of the bound.
- $\lg$ (base-2 logarithm), bound on [Schoolbook multiplication](schoolbook-multiplication.md): The base-2 logarithm, applied to the input length n.
- $\kappa$ (modulus), bound on [Centered residue](centered-residue.md): A positive integer, the modulus by which residues are taken.
- $\nu$ (integer to reduce), bound on [Centered residue](centered-residue.md): The integer whose residue modulo $\kappa$ is taken.
- $\tau$ (centered residue), bound on [Centered residue](centered-residue.md): The integer in $[-\kappa/2, \kappa/2)$ that is congruent to $\nu$ modulo $\kappa$.
- $\varphi$ (input record), bound on [Convolution over the polynomial ring](polynomial-ring-convolution.md): The first of the two input records, a polynomial in y of degree less than r with complex coefficients.
- $\psi$ (input record), bound on [Convolution over the polynomial ring](polynomial-ring-convolution.md): The second of the two input records, a polynomial in y of degree less than r with complex coefficients.
- $\Theta$ (forward transform), bound on [Convolution over the polynomial ring](polynomial-ring-convolution.md): The forward transform along the remaining axes, normalized by 1/t on each axis of length t.
- $\Theta^{+}$ (opposite transform), bound on [Convolution over the polynomial ring](polynomial-ring-convolution.md): The opposite transform along the remaining axes, which uses the inverse roots of unity in place of those of the forward transform.
- $\nu$ (record count), bound on [Convolution over the polynomial ring](polynomial-ring-convolution.md): The number of records in the array along the remaining axes, which counts the product of the remaining axis lengths.
- $\star$ (normalized convolution), bound on [Convolution over the polynomial ring](polynomial-ring-convolution.md): The normalized convolution of two arrays of records, the cyclic convolution divided by r times the record count.
- $\odot$ (normalized entrywise product), bound on [Convolution over the polynomial ring](polynomial-ring-convolution.md): The product of two records divided by r, taken entry by entry on two arrays.
- $\varphi_1$ (real integer part), bound on [Convolution over the polynomial ring](polynomial-ring-convolution.md): The integer polynomial whose coefficients, after scaling by 2^p, give the real part of the input record varphi.
- $\varphi_2$ (imaginary integer part), bound on [Convolution over the polynomial ring](polynomial-ring-convolution.md): The integer polynomial whose coefficients, after scaling by 2^p, give the imaginary part of the input record varphi.
- $\psi_1$ (real integer part), bound on [Convolution over the polynomial ring](polynomial-ring-convolution.md): The integer polynomial whose coefficients, after scaling by 2^p, give the real part of the input record psi.
- $\psi_2$ (imaginary integer part), bound on [Convolution over the polynomial ring](polynomial-ring-convolution.md): The integer polynomial whose coefficients, after scaling by 2^p, give the imaginary part of the input record psi.
- $\mathcal{P}$ (storage map), bound on [Convolution over the polynomial ring](polynomial-ring-convolution.md): The fixed map sending each frequency address to the position where both forward transforms store that frequency.
- $j$ (position index), bound on [Convolution over the polynomial ring](polynomial-ring-convolution.md): A frequency address of a transform entry, or a coefficient position in the reduction step, a nonnegative integer index.
- $e$ (wrap exponent), bound on [Convolution over the polynomial ring](polynomial-ring-convolution.md): An integer exponent of y, which may be at least r, so that y^e wraps around with a sign flip.
- $\circledast$ (normalized cyclic convolution), bound on [Normalized cyclic convolution](normalized-cyclic-convolution.md): The cyclic convolution of two sequences divided by their common length $s$.
- $s$ (sequence length), bound on [Normalized cyclic convolution](normalized-cyclic-convolution.md): The number of entries in each input sequence, which is also the length of the transform.
- $F_s$ (normalized transform), bound on [Normalized cyclic convolution](normalized-cyclic-convolution.md): The normalized discrete Fourier transform of length $s$.
- $\chi$ (chirp phase), bound on [Normalized cyclic convolution](normalized-cyclic-convolution.md): The phase $e^{\pi i m^2/q}$ at an integer $m$, which has period $q$ when $q$ is even.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Discrete Fourier transform](discrete-fourier-transform.md): The map sending a vector of q values to its q values weighted by powers of a q-th root of unity, normalized by 1/q.
  Shown as: Bluestein's chirp identity *<predicate>* Discrete Fourier transform
- [Cyclic convolution](cyclic-convolution.md): The product of two sequences in which indices wrap around modulo the sequence length.
  Shown as: Bluestein's chirp identity *<predicate>* Cyclic convolution
- [Transform identity with retained permutations](transform-identity.md): The Gaussian resampling identity in which the source and target coordinate permutations are kept as part of the formula, so that they cancel across a convolution instead of being executed as sorts.
  Shown as: Bluestein's chirp identity *<predicate>* Transform identity with retained permutations
- [Normalized cyclic convolution](normalized-cyclic-convolution.md): A cyclic convolution divided by the transform length, the normalization for which a Fourier transform turns convolution into pointwise product.
  Shown as: Bluestein's chirp identity *<predicate>* Normalized cyclic convolution
- [Logarithm](logarithm.md): The exponent to which a fixed base must be raised to give a positive number; lg n is the logarithm to base 2.
  Shown as: Bluestein's chirp identity *<predicate>* Logarithm
- [Negacyclic convolution](negacyclic-convolution.md): A convolution in which indices that wrap around the sequence length pick up a minus sign.
  Shown as: Bluestein's chirp identity *<predicate>* Negacyclic convolution

## Pages that build on this one

- Middle transform: The transform on the target lengths that sits between the two Gaussian resampling maps, which Bluestein's identity turns into a cyclic convolution.
- Phase twist: A coefficientwise multiplication by roots of unity that converts the last cyclic coordinate into a polynomial ring, so its wrap-around becomes the negative wrap of that ring.

## Other pages you may link to

- [Integer](integer.md)
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
- [Ring homomorphism and isomorphism](ring-homomorphism.md)
- [Chinese-remainder map](chinese-remainder-map.md)
- [Forward transform](forward-transform.md)
- [Pointwise product](pointwise-product.md)
- [Opposite transform](opposite-transform.md)
- [Iverson bracket](iverson-bracket.md)
- [Axis line](axis-line.md)
- [Near-linear time](near-linear-time.md)
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

- "Bluestein’s chirp identity converts the middle transform" (paper)

## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- Explain "the paper" inline where it is used: "The paper credits this conversion to, whose reference is" (its concept depends on this page, so it cannot be a prerequisite)
- The reader cannot follow this step: "Because $q$ is even, $2\tau+q$ is even, so the ratio is $1$" (Needs e to the power of i times pi times an even integer equals 1, which is Euler's formula for imaginary exponents. The reader profile does not cover it and the page does not state it.)
- The reader cannot follow this step: "(F_q u)_\ell = \frac{1}{\chi_\ell}\cdot\frac{1}{q}\sum_{j=0}^{q-1}\hat u_j\,\chi_{\ell-j}" (The page never writes the coordinates of F_q, so the reader cannot check this formula, including the 1/q normalization and the sign of the exponent, from what the page gives.)
- The reader cannot follow this step: "Here $\chi_0=1$ and $\chi_1=e^{\pi i/2}=i$" (Needs Euler's formula for the exponential of an imaginary number, which the reader does not have from the profile or the page.)
- The reader cannot follow this step: "so that it is never executed as a separate sort" (The formula shown contains no permutation, and the page does not show how the target permutation is kept inside it, so the reader cannot check the claim.)
- The reader cannot follow this step: "The paper says that" (The claim is missing: the sentence has no content after it, so the reader cannot check what the paper says.)
- The reader cannot follow this step: "because it is that of the convolution plus $O(q)$" (The page never gives the cost bound of the cyclic convolution, so the reader cannot check that the transform's bound equals it.)
- The reader cannot follow this step: "So a transform rewritten as convolution can be computed by that machinery." (The page does not say what the paper's convolution machinery is, so the reader cannot check that it applies.)
- Say what $e$ denotes where it is first used (for a size or count, what it counts): "$\chi_\tau = e^{\pi i \tau^2/q}$" (The base e of the exponential (Euler's number) is not in the reader profile and the page never says what e denotes.)
- Say what $\cdot$ denotes where it is first used: the page uses it before saying so in "where $\cdot$ is coordinatewise multiplication"
- Say what $F_2$ denotes where it is first used (for a size or count, what it counts): "Directly, $(F_2u)_0=(1+3)/2=2$" (Read as F_q at q=2, but the reader knows F_2 as the binary field, and the page never says that F_2 here is the transform of length 2.)
- Explain "QFt" inline: its concept depends on this page, so it cannot be a prerequisite.
- "negacyclic convolution" is the concept [Negacyclic convolution](negacyclic-convolution.md), now a prerequisite: link it where the term is used.

## Previous version (revise it)

It has 543 words. Fix the problems by restructuring rather than appending: keep the rewrite within 678 words, a quarter more, unless a problem cannot be fixed without more. Pages that grow with every repair stop being self-contained explanations of one concept.

Bluestein's chirp identity rewrites the [Discrete Fourier transform](discrete-fourier-transform.md) $F_q$ as a convolution multiplied by chirp factors. It reduces the transform to a [cyclic convolution](cyclic-convolution.md), so any method that computes that convolution also computes the transform. In the paper, it converts the middle transform into a [normalized cyclic convolution](normalized-cyclic-convolution.md).

The middle transform is the factor QFt in the paper's equation (35). The paper states that <cite data-source="paper">The factor QFt in (35) can be computed from a cyclic convolution and two pointwise phase multiplications.</cite> QFt is the Fourier transform with its output frequencies relabelled by the paper's target permutation. The paper's statement of the identity is <cite data-source="paper">Bluestein’s chirp identity converts the middle transform, including its target permutation,</cite> into normalized cyclic convolution. The paper computes convolution in later sections: <cite data-source="paper">Sections 6 and 7 compute convolution on the remaining axes over this polynomial ring.</cite> So a transform rewritten as convolution can be computed by that machinery.

Throughout, $q$ is even, as the identity requires. For sequences of length $q$, $\ast$ and $\circledast$ are cyclic and normalized cyclic convolution, with indices taken modulo $q$. Here $x \bmod q$ denotes the remainder of the integer $x$ on division by $q$, the position in $\{0,\dots,q-1\}$ reached by $x$ on a cycle of $q$ positions.

Here $\tau$ is the integer position of a chirp entry, which may be negative or larger than $q-1$. The chirp is the vector $\chi$ whose entry at each integer $\tau$ is $\chi_\tau = e^{\pi i \tau^2/q}$. So $\chi = (\chi_0,\dots,\chi_{q-1})$, and every entry has modulus $1$, because $\pi\tau^2/q$ is real.

Since $(\tau+q)^2-\tau^2 = q(2\tau+q)$, we get $\chi_{\tau+q}/\chi_\tau = e^{\pi i(2\tau+q)}$. Because $q$ is even, $2\tau+q$ is even, so the ratio is $1$ and $\chi_{\tau+q}=\chi_\tau$. Hence $\chi_\tau$ depends only on $\tau \bmod q$. For odd $q$ the ratio is $-1$, so each wrapped index picks up a sign. The sum below would then be a negacyclic convolution, and the identity would need that sign change.

For integers $j$ and $\ell$, the identity $2j\ell = j^2+\ell^2-(\ell-j)^2$ gives $e^{-2\pi i j\ell/q} = \chi_{\ell-j}/(\chi_j\chi_\ell)$. Here $j$ and $\ell$ are the input and output indices of $F_q$. Write $\hat u = \frac{1}{\chi}\cdot u$, so $\hat u_j = u_j/\chi_j$. Then
$$(F_q u)_\ell = \frac{1}{\chi_\ell}\cdot\frac{1}{q}\sum_{j=0}^{q-1}\hat u_j\,\chi_{\ell-j}.$$
By periodicity $\chi_{\ell-j}=\chi_{(\ell-j)\bmod q}$, so the sum is $(\hat u\ast\chi)_\ell$. Hence
$$F_q u = \frac{1}{\chi}\cdot(\hat u\circledast\chi), \qquad \hat u = \frac{1}{\chi}\cdot u,$$
where $\cdot$ is coordinatewise multiplication. Both chirp multiplications have modulus $1$, so they change phases only. The only convolution is the middle one.

Worked example with $q=2$. Here $\chi_0=1$ and $\chi_1=e^{\pi i/2}=i$. Take $u=(1,3)$. Directly, $(F_2u)_0=(1+3)/2=2$ and $(F_2u)_1=(1-3)/2=-1$. By the identity, $\hat u = (1,\,-3i)$. Then $(\hat u\ast\chi)_0 = 1\cdot 1+(-3i)\cdot i = 4$ and $(\hat u\ast\chi)_1 = 1\cdot i+(-3i)\cdot 1 = -2i$, so $\hat u\circledast\chi = (2,\,-i)$. Multiplying by $\frac{1}{\chi} = (1,\,-i)$ gives $(2,\,-1)$, the same result.

The wrap-around is what makes the convolution cyclic. For $j>\ell$ the index $\ell-j$ is negative, and periodicity replaces $\chi_{\ell-j}$ by $\chi_{(\ell-j)\bmod q}$. The output $\ell$ is written at its own frequency label, with its factor $1/\chi_\ell$ applied there. The identity keeps the target permutation of the [transform identity with retained permutations](transform-identity.md) inside the formula, so that it is never executed as a separate sort. The paper says that <cite data-source="paper">The chirp identity below performs the frequency change in Q without applying Q as a separate permutation of the array.</cite>

The two chirp multiplications cost $O(q)$ operations, so the transform costs one cyclic convolution of length $q$ plus $O(q)$. The transform's cost bound is stated in terms of the [logarithm](logarithm.md) $\lg$ to base 2, because it is that of the convolution plus $O(q)$.

The paper credits this conversion to <cite data-source="paper">Bluestein’s conversion to convolution [4]</cite>, whose reference is <cite data-source="paper">L. I. Bluestein. A linear filtering approach to the computation of discrete Fourier transform.</cite>

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

Write the body to `exegenius/tasks/0603-write-bluestein-chirp-identity.answer.md` and the JSON to `exegenius/tasks/0603-write-bluestein-chirp-identity.answer.json`, then run `exegenius submit 0603-write-bluestein-chirp-identity` in the project directory. If submit rejects the answer, fix the answer and submit again.
