# exegenius task 0750-write-supremum

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
- Convolution
- Running time cost (also: cost, linear-cost update, bit-complexity bound, linear tape time)
- Little-o notation (also: limit as lambda tends to infinity)
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
- Real numbers (also: Real number)

## This page

Concept: Supremum
Gloss: The least upper bound of a set of real numbers.

## Where the argument relies on this page

- The recovered coefficient error is strictly below $1/2$, so rounding returns the exact integer coefficients. (on [Exact coefficient recovery](recovery-and-error.md))

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

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Array norm](array-norm.md): The maximum modulus over all entries of an array of complex values; an array has norm at most one exactly when every entry has modulus at most one.
  Shown as: Supremum *<predicate>* Array norm

## Pages that build on this one

- Linear contraction: A linear map that does not increase the maximum modulus of any vector, so that errors pass through it without growing.

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

## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- $s$ means positive integer index here, but coefficient index on [Array norm](array-norm.md), which this page builds on: Different: $s$ means positive integer index on supremum but coefficient index on Array norm. The later page should use another letter for positive integer index, or say explicitly where $s$ keeps this meaning instead of coefficient index.
- $L$ means linear map here, but chunk width on [Payload](payload.md), which this page builds on: Different: $L$ means linear map on supremum but chunk width on Payload. The later page should use another letter for linear map, or say explicitly where $L$ keeps this meaning instead of chunk width.
- $u$ means input vector here, but entry on [Array norm](array-norm.md), which this page builds on: Different: $u$ means input vector on supremum but entry on Array norm. The later page should use another letter for input vector, or say explicitly where $u$ keeps this meaning instead of entry.

## Previous version (revise it)

It has 334 words. Fix the problems by restructuring rather than appending: keep the rewrite within 417 words, a quarter more, unless a problem cannot be fixed without more. Pages that grow with every repair stop being self-contained explanations of one concept.

The supremum is the least upper bound of a set of real numbers. The paper uses it for the largest value of a quantity over infinitely many inputs, and the [linear contraction](linear-contraction.md) bound on how errors pass through the computation is stated with it.

Let $\Sigma$ be a nonempty set of real numbers. Let $\chi$ denote an arbitrary element of $\Sigma$. Let $\Omega$ denote a real number. Call $\Omega$ an *upper bound* of $\Sigma$ when $\chi \le \Omega$ for every element $\chi$ of $\Sigma$. The supremum $\sup \Sigma$ is the least upper bound: it is an upper bound of $\Sigma$, and it is at most every other upper bound of $\Sigma$.

The supremum need not be an element of $\Sigma$. Take $\Sigma = \{\,1-2^{-s} : s \ge 1\,\} = \{1/2, 3/4, 7/8, \dots\}$, where $s$ is a positive integer index. Every element is less than $1$, so $1$ is an upper bound. Let $\Omega < 1$, and let $\varepsilon = 1-\Omega > 0$. Choose $s$ with $2^{-s} < \varepsilon$. Such an $s$ exists because $2^s \ge s+1$ for every integer $s \ge 0$ (by induction), so any $s$ with $s+1 > 1/\varepsilon$ gives $2^{-s} \le 1/(s+1) < \varepsilon$. Then $1-2^{-s} > \Omega$, so $\Omega$ is not an upper bound. Hence $\sup \Sigma = 1$, although $1 \notin \Sigma$.

For a linear map $L$, meaning a map that preserves sums and scalar multiples, the largest factor by which $L$ stretches a vector is its operator norm $\|L\|$. Here $u$ is one input vector, a finite list of complex numbers; earlier pages used the letter $u$ for a single array entry, so its meaning changes on this page. The paper defines the operator norm as a supremum over all vectors: $$\|L\| = \sup_{\|u\| \le 1} \|Lu\|.$$ The paper writes this as <cite data-source="paper">∥L∥ = sup∥u∥≤1 ∥Lu∥</cite>. The set of inputs is restricted by the [Array norm](array-norm.md) of $u$, the norm of a vector, which must be at most one. So $\|L\|$ is defined even when no vector attains the largest value.

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

Write the body to `exegenius/tasks/0750-write-supremum.answer.md` and the JSON to `exegenius/tasks/0750-write-supremum.answer.json`, then run `exegenius submit 0750-write-supremum` in the project directory. If submit rejects the answer, fix the answer and submit again.
