# exegenius task 0117-write-signed-packing

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
- Exact integer multiplication
- The n log n optimality conjecture (also: Schönhage–Strassen conjecture)
- Established O(n log n) multiplier (also: Harvey–van der Hoeven multiplier)
- Radix-digit convolution
- Discrete Fourier transform (also: normalized Fourier transform, transform)
- Gaussian resampling (also: Harvey–van der Hoeven resampling, Gaussian weights)
- Synthetic polynomial transforms (also: Nussbaumer polynomial transforms, polynomial transforms, Nussbaumer and Quandalle)
- Polynomial ring modulo y^r + 1 (also: negacyclic polynomial ring)
  - $y$ (polynomial variable): The indeterminate of the polynomial ring, whose powers act as roots of unity.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Linear networks and frames (also: roles, frames)
- Address-field interchange (also: power-width interchange, tape procedure for interchanging address chunks)
- Gaussian dyadics
- Address field (also: address chunk, chunk, target chunk)
- Transform axis (also: axis, remaining axes)
- Linear algebra basics (also: linear algebra: invertible linear operator, matrix, inverse, matrix, linear map)
- Binary field (also: finite field F2, F_2, finite field F_2)
- Binary change of basis
- Bit procedure
- Butterfly
- Congruence (also: congruence modulo B, modulo)
- Linear contraction (also: contraction)
- Cyclic shift (also: controlled cyclic shift)
- Convolution
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
- Limit inferior
- Line spanned by a vector
- Multidimensional transform (also: multidimensional transforms with power-of-two axes)
- Array norm (also: norm of an array)
- Opposite transform (also: opposite-sign transform)
- Payload
- Phase factor (also: phase factors and scalar corrections)
- Polynomial ring
- Matrix rank (also: rational rank)
- Schoolbook multiplication
- Scratch storage (also: scratch values, scratch chunk, scratch wires)
- Tensor product (also: tensor power)
- Truncation
- Union bound
- Exclusive or (also: XOR)

## This page

Concept: Signed coefficient packing
Gloss: Encoding polynomial coefficients, including negative ones, as one large integer by fixed-width blocks, so that polynomial multiplication becomes integer multiplication.
Also called: Kronecker substitution

## Where the argument relies on this page

- Convolution on the remaining axes over the polynomial ring is computed with synthetic transforms, a pointwise product, and packed integer products. (on [Convolution over the polynomial ring](polynomial-ring-convolution.md))
- The recovered coefficient error is below one half, so rounding returns the exact integer coefficients. (on [Exact coefficient recovery](recovery-and-error.md))

## Symbols already bound on earlier pages

The symbols in the names of the concepts the reader knows are listed with those concepts above.

- $D_v$ (frame), bound on [Linear networks and frames](linear-network-frames.md): The invertible linear operator on arrays attached to vertex $v$ of a network, so that the stored array at $v$ is $D_v g$.
- $g$ (logical array), bound on [Linear networks and frames](linear-network-frames.md): The array a wire is meant to represent before any frame is applied.
- $G$ (pointwise gate), bound on [Linear networks and frames](linear-network-frames.md): A fixed linear map that combines the entries of several wires at each address.
- $n$ (input length), bound on [Fixed-tape machine model](fixed-tape-model.md): The number of bits in each of the two input integers.
- $A$ (fixed machine), bound on [Fixed-tape machine model](fixed-tape-model.md): A fixed multiplication machine, whose alphabet and tape count do not depend on the input.
- $T_A$ (running time), bound on [Fixed-tape machine model](fixed-tape-model.md): The worst-case running time of machine A as a function of the input length n.
- $c_A$ (lower-bound constant), bound on [Fixed-tape machine model](fixed-tape-model.md): A positive constant, depending on machine A, in the eventual lower bound T_A(n) >= c_A n log n.
- $N_A$ (threshold input length), bound on [Fixed-tape machine model](fixed-tape-model.md): The input length from which the lower bound for machine A holds.
- $x$ (first input string), bound on [Exact integer multiplication](exact-integer-multiplication.md): A binary string of length n, the first input to the product.
- $y$ (second input string), bound on [Exact integer multiplication](exact-integer-multiplication.md): A binary string of length n, the second input to the product.
- $n$ (input length), bound on [Exact integer multiplication](exact-integer-multiplication.md): The number of bits in each input string.
- $n$ (input length), bound on [The n log n optimality conjecture](n-log-n-conjecture.md): The number of bits in each of the two input integers.
- $A$ (multiplication machine), bound on [The n log n optimality conjecture](n-log-n-conjecture.md): A fixed Turing machine that computes exact products.
- $T_A$ (running time), bound on [The n log n optimality conjecture](n-log-n-conjecture.md): The worst-case running time of A on inputs of two n-bit integers, as a number of steps.
- $c_A$ (lower-bound constant), bound on [The n log n optimality conjecture](n-log-n-conjecture.md): A positive constant in the lower bound that must hold for machine A.
- $N_A$ (threshold length), bound on [The n log n optimality conjecture](n-log-n-conjecture.md): The input length from which the lower bound for machine A must hold.
- $\lg n$ (binary logarithm), bound on [The n log n optimality conjecture](n-log-n-conjecture.md): The base-2 logarithm of n, rounded up to an integer and never below 1.
- $\kappa$ (saving exponent), bound on [The n log n optimality conjecture](n-log-n-conjecture.md): The specific positive constant by which the main theorem's running time falls below n lg n.
- $N$ (input bit length), bound on [Established O(n log n) multiplier](established-multiplier.md): The number of bits in each of the two binary inputs of the multiplier.
- $u$ (field width), bound on [Address-field interchange](address-interchange.md): The number of bits in each address field.
- $V$ (stored volume), bound on [Address-field interchange](address-interchange.md): The number of stored bits in the array.
- $\tau$ (width exponent), bound on [Address-field interchange](address-interchange.md): A fixed number below one in the cost bound $O(V u^{\tau})$.
- $x$ (first field), bound on [Address-field interchange](address-interchange.md): The value of the first field, a block of bits at matching positions.
- $y$ (second field), bound on [Address-field interchange](address-interchange.md): The value of the second field, a block of bits at matching positions.
- $\oplus$ (bitwise XOR), bound on [Address-field interchange](address-interchange.md): Bitwise exclusive or of two blocks of bits.
- $\mathbb{D}$ (Gaussian dyadics), bound on [Gaussian dyadics](gaussian-dyadics.md): The set of numbers $a/2^k$, with $a$ a Gaussian integer and $k \ge 0$ an integer.
- $a$ (Gaussian integer numerator), bound on [Gaussian dyadics](gaussian-dyadics.md): A Gaussian integer, the numerator of a Gaussian dyadic over a power of two.
- $k$ (denominator exponent), bound on [Gaussian dyadics](gaussian-dyadics.md): A non-negative integer, so that $2^k$ is the denominator.
- $q$ (transform length), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The number of coordinates of each vector the transform acts on, a positive integer.
- $\omega$ (primitive root of unity), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The complex number $e^{-2\pi i/q}$, a primitive $q$-th root of unity.
- $u$ (input vector), bound on [Discrete Fourier transform](discrete-fourier-transform.md): A vector of $q$ complex numbers, the input to the transform.
- $j$ (input index), bound on [Discrete Fourier transform](discrete-fourier-transform.md): An index of the input coordinates, running from 0 to q-1.
- $k$ (output index), bound on [Discrete Fourier transform](discrete-fourier-transform.md): An index of the output coordinates, running from 0 to q-1.
- $F_q$ (Fourier transform), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The discrete Fourier transform of length q, the map sending u to F_q u.
- $F_q^+$ (positive-sign transform), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The same map with the positive sign in the exponent, with omega replaced by its inverse.
- $n$ (input length), bound on [Radix-digit convolution](radix-digit-convolution.md): The number of bits in each input.
- $b$ (digit width), bound on [Radix-digit convolution](radix-digit-convolution.md): The number of bits in each digit.
- $q$ (digits per input), bound on [Radix-digit convolution](radix-digit-convolution.md): The number of radix-$2^b$ digits in each input.
- $x$ (first input), bound on [Radix-digit convolution](radix-digit-convolution.md): The first input, a binary string of $n$ bits.
- $y$ (second input), bound on [Radix-digit convolution](radix-digit-convolution.md): The second input, a binary string of $n$ bits.
- $x_i$ (digit of x), bound on [Radix-digit convolution](radix-digit-convolution.md): The digit of $x$ at position $i$, of weight $(2^b)^i$.
- $y_i$ (digit of y), bound on [Radix-digit convolution](radix-digit-convolution.md): The digit of $y$ at position $i$, of weight $(2^b)^i$.
- $i$ (digit position), bound on [Radix-digit convolution](radix-digit-convolution.md): The position of a digit, running from $0$ to $q-1$.
- $j$ (coefficient position), bound on [Radix-digit convolution](radix-digit-convolution.md): The position of a product coefficient, running from $0$ to $2q-2$.
- $z$ (formal variable), bound on [Radix-digit convolution](radix-digit-convolution.md): A formal variable in which each input is written as a polynomial whose coefficients are its digits.
- $c_j$ (product coefficient), bound on [Radix-digit convolution](radix-digit-convolution.md): The integer coefficient of $z^j$ in the product of the two digit polynomials.
- $r$ (record length), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The number of complex coefficients in a record, a power of two at least 2.
- $R_r$ (record ring), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The ring of polynomials with complex coefficients in which $y^r$ is identified with $-1$.
- $y$ (polynomial variable), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The polynomial variable whose powers serve as the roots of unity.
- $c_i$ (record coefficient), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The coefficient of $y^i$ in the record being shifted.
- $i$ (coefficient position), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The position of a coefficient in a record, from 0 to r-1.
- $a$ (shift amount), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The number of places a signed shift moves each coefficient, an integer with 0 \le a < 2r.
- $t$ (transform length), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The number of entries in the transform, a power of two dividing 2r.
- $\omega_t$ (transform root), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The primitive t-th root of unity $y^{2r/t}$ in the record ring.
- $z$ (transform input), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The input list of t records to be transformed.
- $Z$ (transform output), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The transform of the input z, a list of t entries.
- $j$ (output index), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The index of an entry of the transform, from 0 to t-1.
- $k$ (input index), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The index of an entry of the input, from 0 to t-1.
- $q$ (transform length), bound on [Gaussian resampling](gaussian-resampling.md): the number of entries of the vector that a transform of length q acts on.
- $F_q$ (normalized transform), bound on [Gaussian resampling](gaussian-resampling.md): the normalized discrete Fourier transform of length q.
- $s$ (source length), bound on [Gaussian resampling](gaussian-resampling.md): the number of entries in the source vector, which is the length of the transform being replaced.
- $t$ (resampled length), bound on [Gaussian resampling](gaussian-resampling.md): the power-of-two number of entries in the resampled vector, greater than s.
- $\theta$ (relative gap), bound on [Gaussian resampling](gaussian-resampling.md): the relative gap t/s - 1 between the two lengths.
- $\alpha$ (Gaussian width), bound on [Gaussian resampling](gaussian-resampling.md): a positive integer parameter that sets the width of the Gaussian weights.
- $p$ (precision), bound on [Gaussian resampling](gaussian-resampling.md): a positive integer precision parameter of the approximations.
- $P_s$ (source reordering), bound on [Gaussian resampling](gaussian-resampling.md): the permutation of length-s vectors that reorders their entries by multiplying each position by t modulo s.
- $P_t$ (target reordering), bound on [Gaussian resampling](gaussian-resampling.md): the permutation of length-t vectors that reorders their entries by multiplying each position by -s modulo t.
- $A$ (forward contraction), bound on [Gaussian resampling](gaussian-resampling.md): the linear contraction from length-s vectors to length-t vectors that appears in the identity.
- $B$ (backward contraction), bound on [Gaussian resampling](gaussian-resampling.md): the linear contraction from length-t vectors to length-s vectors that appears in the identity.
- $y$ (polynomial variable), bound on [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md): The indeterminate of the polynomial ring, whose powers act as roots of unity.
- $r$ (record length), bound on [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md): The number of complex coefficients in a polynomial record, a power of two.
- $R_r$ (polynomial ring), bound on [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md): The ring $\mathbb{C}[y]/(y^r+1)$ studied on this page.
- $z$ (ring element), bound on [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md): An element of the ring, written as a polynomial with complex coefficients.
- $z_k$ (coefficient), bound on [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md): The k-th complex coefficient of the representative of z, for 0 <= k < r.
- $s$ (shift amount), bound on [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md): The number of positions by which the coefficient list moves under multiplication by y^s, with 0 <= s < r.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Established O(n log n) multiplier](established-multiplier.md): The known fixed-tape integer multiplier running in O(n log n) time, used here only as a black-box subroutine.
  Shown as: Signed coefficient packing *<predicate>* Established O(n log n) multiplier
- [Polynomial ring](polynomial-ring.md): The ring of polynomials in an indeterminate with complex coefficients, with the usual addition and multiplication, here reduced modulo a fixed polynomial.
  Shown as: Signed coefficient packing *<predicate>* Polynomial ring
- [Congruence](congruence-modulo.md): Two integers are congruent modulo m when their difference is divisible by m; a residue is the class of an integer modulo m.
  Shown as: Signed coefficient packing *<predicate>* Congruence

## Pages that build on this one

- Convolution over the polynomial ring: The normalized product of two arrays of records in the polynomial ring, computed by two forward synthetic transforms, a pointwise product, and an opposite transform.

## Other pages you may link to

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
- [Array norm](array-norm.md)
- [Grid numerator](grid-numerator.md)
- [Linear contraction](linear-contraction.md)
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

## Evidence from the sources

- "Signed coefficient packing is a form of Kronecker substitution" (paper)

## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The reader cannot follow this step: "product has magnitude below $B/2$." (The sentence is a fragment with no subject, and the magnitude bound it is meant to state is never given in terms of p and r. The reader cannot check that B = 2^(4p) is large enough for the coefficients of h, so the claim that the blocks do not overlap, and that one integer multiplication computes the whole product, is unverified.)
- The reader cannot follow this step: "The residue $c$ is the constant coefficient of $h$, since the bound identifies each coefficient." (This depends on the coefficient bound, which the page never states (see the previous gap), so the reader cannot check that the centered residue equals the constant coefficient of h.)
- "polynomial ring" is the concept [Polynomial ring](polynomial-ring.md), now a prerequisite: link it where the term is used.
- "congruence modulo B" is the concept [Congruence](congruence-modulo.md), now a prerequisite: link it where the term is used.

## Previous version (revise it)

It has 466 words. Fix the problems by restructuring rather than appending: keep the rewrite within 582 words, a quarter more, unless a problem cannot be fixed without more. Pages that grow with every repair stop being self-contained explanations of one concept.

Signed coefficient packing is the encoding that turns a product of two polynomials with integer coefficients, some of them negative, into one integer product. It is the step that lets [convolution over the polynomial ring](polynomial-ring-convolution.md) compute its packed polynomial products with a single integer multiplication.

Here $y$ is the indeterminate of the polynomial ring. Let $r$ be the number of coefficients of each polynomial. Two polynomials $f$ and $g$ in $y$ with $r$ coefficients each are packed. Here $j$ indexes the coefficients, from $j = 0$ to $r-1$, so $f = \sum_{j=0}^{r-1} f_j y^j$. Let $p$ be the number of bits in the magnitude bound on a coefficient, so that every coefficient satisfies $|f_j| \le 2^p$.

<cite data-source="paper">Signed coefficient packing is a form of Kronecker substitution</cite>: the coefficients are written as blocks of one integer, and the polynomial is evaluated at the base of that integer. Packing fixes a block base $B = 2^{4p}$, and replaces $y$ by $B$. The integer $f(B) = \sum_{j=0}^{r-1} f_j B^j$ holds $f_j$ in the $j$-th block, and <cite data-source="paper">Every block has 4p bits</cite>. A negative $f_j$ needs no separate format: it borrows from the block above it, and $f(B)$ is simply a signed integer.

Evaluation at $B$ respects multiplication, so $f(B)\,g(B) = (fg)(B)$. The product $h = fg$ has at most $2r-1$ coefficients, so the single integer $f(B)\,g(B)$ holds all of $h$ in its blocks. One integer multiplication therefore computes the whole polynomial product.

Reading the blocks back requires the base to be large enough that no coefficient of $h$ spills into its neighbour. <cite data-source="paper">Every coefficient in any of these ordinary</cite> product has magnitude below $B/2$. Then the coefficients are recovered from the centered residues. Let $c$ be the unique integer in $[-B/2, B/2)$ with $f(B)\,g(B) \equiv c \pmod B$. The residue $c$ is the constant coefficient of $h$, since the bound identifies each coefficient <cite data-source="paper">by its centered residue modulo B0</cite>. Subtract $c$, divide by $B$, and repeat to read the next coefficient. Negative coefficients are recovered exactly this way, with no extra sign bit.

As a small example, take $B = 100$ instead of $2^{4p}$, which keeps the numbers short. Let $f = 3 - 2y$ and $g = 1 + 4y$. Then $f(100) = 3 - 200 = -197$ and $g(100) = 401$, so $f(100)\,g(100) = -78997$. The product is $h = fg = 3 + 10y - 8y^2$, and indeed $h(100) = 3 + 1000 - 80000 = -78997$. To decode, the centered residue of $-78997$ modulo $100$ is $3$; subtracting it and dividing by $100$ gives $-790$. The centered residue of $-790$ is $10$; subtracting it and dividing by $100$ gives $-8$. The coefficients $3$, $10$, $-8$ are recovered, with the negative one needing no special treatment.

Signed coefficient packing reduces its products to integer products, which the [Established O(n log n) multiplier](established-multiplier.md) computes. The multiplier is used as an ordinary subroutine: <cite data-source="paper">To multiply the polynomial records, we use the fixed-tape integer multiplier of Harvey and van</cite>, and the packing does not depend on how that multiplier works internally.

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

Write the body to `exegenius/tasks/0117-write-signed-packing.answer.md` and the JSON to `exegenius/tasks/0117-write-signed-packing.answer.json`, then run `exegenius submit 0117-write-signed-packing` in the project directory. If submit rejects the answer, fix the answer and submit again.
