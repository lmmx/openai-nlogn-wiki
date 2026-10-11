# exegenius task 0108-write-gaussian-resampling

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
- Synthetic polynomial transforms (also: Nussbaumer polynomial transforms, polynomial transforms, Nussbaumer and Quandalle)
- Linear networks and frames (also: roles, frames)
- Address-field interchange (also: power-width interchange, tape procedure for interchanging address chunks)
- Gaussian dyadics
- Address field (also: address chunk, chunk, target chunk)
- Transform axis (also: axis, remaining axes)
- Linear algebra basics (also: linear algebra: invertible linear operator, matrix, inverse, matrix, linear map)
- Binary field (also: finite field F2, F_2, finite field F_2)
- Binary change of basis
- Bit procedure
- Cyclic shift (also: controlled cyclic shift)
- Convolution
- Running time cost (also: cost)
- Cost table
- Stable radix sort
- Destination rank
- Endpoint operator
- Gate and terminal of a network
- Gaussian integer
- Ground set
- Indicator vector
- Limit inferior
- Line spanned by a vector
- Multidimensional transform (also: multidimensional transforms with power-of-two axes)
- Payload
- Phase factor (also: phase factors and scalar corrections)
- Matrix rank (also: rational rank)
- Schoolbook multiplication
- Scratch storage (also: scratch values, scratch chunk, scratch wires)
- Tensor product (also: tensor power)
- Truncation
- Union bound
- Exclusive or (also: XOR)

## This page

Concept: Gaussian resampling
Gloss: A technique that replaces a Fourier transform of arbitrary length by transforms whose axis lengths are powers of two, using Gaussian weights to move between the two sets of frequencies.
Also called: Harvey–van der Hoeven resampling, Gaussian weights

## This page in the argument

The step: The Fourier transforms in the convolution are replaced by multidimensional transforms whose axis lengths are powers of two.
How: resample Gaussian weights onto power-of-two axes
Why: Power-of-two axis lengths let the later steps use butterfly layers and polynomial transforms. (the sources leave this for the reader to work out: spell it out)

Its sub-steps, in order:

- The Fourier transforms needed for the convolution become multidimensional transforms with power-of-two axes.

It serves these steps, from the main result down:

- Exact multiplication of two $n$-bit integers runs in $O(n(\lg n)^{1-\kappa})$ time on one deterministic fixed-tape machine, with $\kappa = 2^{-182}$.; how: reduce exact multiplication to radix-digit convolution, compute that convolution with fast tape transforms, and check that the output is exact (on [Integer multiplication below n log n](main-theorem.md))

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

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Discrete Fourier transform](discrete-fourier-transform.md): The map sending a vector of q values to its q values weighted by powers of a q-th root of unity, normalized by 1/q.
  Shown as: Gaussian resampling *<predicate>* Discrete Fourier transform
- [Radix-digit convolution](radix-digit-convolution.md): Writing both integers as polynomials in a power of two whose coefficients are their digits, so that their product is a polynomial convolution of short coefficients.
  Shown as: Gaussian resampling *<predicate>* Radix-digit convolution
- [Synthetic polynomial transforms](synthetic-transforms.md): Fourier-type transforms whose roots of unity are powers of y in a polynomial ring, so that multiplying by a root is a signed shift of coefficients.
  Shown as: Gaussian resampling *<predicate>* Synthetic polynomial transforms
- [Multidimensional transform](multidimensional-transform.md): A Fourier transform over several axes at once, computed by transforming along each axis in turn.
  Shown as: Gaussian resampling *<predicate>* Multidimensional transform

## Pages that build on this one

- Transform identity with retained permutations: The Gaussian resampling identity in which the source and target coordinate permutations are kept as part of the formula, so that they cancel across a convolution instead of being executed as sorts.
- Prime source lengths: Distinct odd primes chosen close to the powers of two that are the padded axis lengths, so that their product fills a fixed fraction of the padded box.

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
- [Established O(n log n) multiplier](established-multiplier.md)
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
- [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md)
- [Butterfly](butterfly.md)
- [Opposite transform](opposite-transform.md)
- [Polynomial ring](polynomial-ring.md)
- [Array norm](array-norm.md)
- [Grid numerator](grid-numerator.md)
- [Linear contraction](linear-contraction.md)
- [Congruence](congruence-modulo.md)
- [Signed coefficient packing](signed-packing.md)
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

- "it replaces the Fourier transforms needed for this convolution by multidimensional transforms whose" (paper)

## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- [Synthetic polynomial transforms](synthetic-transforms.md) is now a prerequisite: link it where "synthetic transforms" is used: "whereas the synthetic transforms"
- The reader cannot follow this step: "so the lengths must be changed before the transform layers can be applied." (The page gives no reason why the lengths must be changed before the transform layers can be applied, and the sentence is garbled.)
- The reader cannot follow this step: "Let $P_s$ be the permutation of length-$s$ vectors that reorders their entries by multiplying each position by $t$ modulo $s$" (Multiplying positions by t modulo s is a bijection only when t and s have no common factor. The page never states or justifies this, so the reader cannot check that P_s is a permutation.)
- The reader cannot follow this step: "P_s F_s = 2^{2\alpha^2}\, B\, P_t F_t\, A." (The page gives no proof of the identity. The sentence introducing it is garbled ("The one-dimensional identity is. It applies when."), and the page never says which operators A and B exist or how they are constructed, so the reader cannot check that the identity holds.)
- The reader cannot follow this step: "A transform whose length is a power of two splits into one layer of two-point butterflies for each factor of two in its length" (The page asserts that a power-of-two transform factors into butterfly layers but gives no argument, and the reader profile does not cover the fast Fourier transform factorization.)
- Say what $F_s$ denotes where it is first used (for a size or count, what it counts): "P_s F_s = 2^{2\alpha^2}\, B\, P_t F_t\, A." (The page defines F_q for a generic positive integer q, but never says that F_s is the length-s transform; the reader would have to infer it by substituting s for q.)
- Say what $F_t$ denotes where it is first used (for a size or count, what it counts): "P_s F_s = 2^{2\alpha^2}\, B\, P_t F_t\, A." (The page defines F_q for a generic positive integer q, but never says that F_t is the length-t transform; the reader would have to infer it by substituting t for q.)
- "multidimensional transforms with power-of-two axes" is the concept [Multidimensional transform](multidimensional-transform.md), now a prerequisite: link it where the term is used.

## Previous version (revise it)

It has 391 words. Fix the problems by restructuring rather than appending: keep the rewrite within 488 words, a quarter more, unless a problem cannot be fixed without more. Pages that grow with every repair stop being self-contained explanations of one concept.

Gaussian resampling replaces the transforms of the [Discrete Fourier transform](discrete-fourier-transform.md) of arbitrary length by transforms whose axis lengths are powers of two, using Gaussian weights to move between the two sets of frequencies. In the integer product it is the step that changes the Fourier transforms of the convolution into multidimensional transforms with power-of-two axes, following the reduction of Harvey and van der Hoeven.

<cite data-source="paper">Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients</cite>. Gaussian resampling replaces the transforms needed to compute the [Radix-digit convolution](radix-digit-convolution.md) by power-of-two transforms. The <cite data-source="paper">transform lengths needed for the integer product are pairwise coprime</cite>, whereas the synthetic transforms <cite data-source="paper">use powers of two</cite>, so the lengths must be changed before the transform layers can be applied.

For a positive integer $q$, write $F_q$ for the normalized discrete Fourier transform of length $q$. Let $s$ be the number of entries in the source vector, which is the length of the transform being replaced, and let $t$ be a power of two greater than $s$, the number of entries in the resampled vector. Write $\theta = t/s - 1$ for the relative gap between the two lengths. The integer $\alpha$ is a width parameter that sets how wide the Gaussian weights are, and the integer $p$ is a precision parameter.

Let $P_s$ be the permutation of length-$s$ vectors that reorders their entries by multiplying each position by $t$ modulo $s$, and let $P_t$ be the permutation of length-$t$ vectors that reorders their entries by multiplying each position by $-s$ modulo $t$.

The one-dimensional identity is <cite data-source="paper">Lemma 19 (Resampling without executing the two permutations)</cite>. It applies when <cite data-source="paper">with gcd(s, t) = 1 and</cite> <cite data-source="paper">θ := t/s − 1 > p/α4</cite>. $A$ maps length-$s$ vectors to length-$t$ vectors and $B$ maps length-$t$ vectors back to length-$s$ vectors, and neither increases the maximum modulus of an entry. With these operators the identity reads

$$P_s F_s = 2^{2\alpha^2}\, B\, P_t F_t\, A.$$

The two permutations stay on the two sides of the identity instead of being carried out as sorts.

Powers of two matter because of the later steps. A transform whose length is a power of two splits into one layer of two-point butterflies for each factor of two in its length, where a butterfly replaces two entries by their sum and their difference, up to a scale factor. For example, a transform of length $t = 8$ is computed in $3$ layers of $4$ butterflies each, and each layer touches all $8$ entries once, so it costs one pass over the data. The polynomial transforms of the later steps keep this layered structure: <cite data-source="paper">as roots of unity in the remaining axes, and multiplication by such a root is a signed shift of the</cite> coefficient list.

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

Write the body to `exegenius/tasks/0108-write-gaussian-resampling.answer.md` and the JSON to `exegenius/tasks/0108-write-gaussian-resampling.answer.json`, then run `exegenius submit 0108-write-gaussian-resampling` in the project directory. If submit rejects the answer, fix the answer and submit again.
