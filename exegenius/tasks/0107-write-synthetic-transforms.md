# exegenius task 0107-write-synthetic-transforms

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

Concept: Synthetic polynomial transforms
Gloss: Fourier-type transforms whose roots of unity are powers of y in a polynomial ring, so that multiplying by a root is a signed shift of coefficients.
Also called: Nussbaumer polynomial transforms, polynomial transforms, Nussbaumer and Quandalle

## This page in the argument

The step: The transforms are synthetic polynomial transforms whose roots of unity are powers of the polynomial variable.
How: evaluate the transforms with polynomial roots of unity
Why: Roots of unity that are powers of the variable cost only shifts and signs, so each transform reduces to address rearrangement and two-point butterflies. (the sources leave this for the reader to work out: spell it out)

Its sub-steps, in order:

- The transforms are the synthetic polynomial transforms of Nussbaumer and Quandalle.

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

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Discrete Fourier transform](discrete-fourier-transform.md): The map sending a vector of q values to its q values weighted by powers of a q-th root of unity, normalized by 1/q.
  Shown as: Synthetic polynomial transforms *<predicate>* Discrete Fourier transform

## Pages that build on this one

- Gaussian resampling: A technique that replaces a Fourier transform of arbitrary length by transforms whose axis lengths are powers of two, using Gaussian weights to move between the two sets of frequencies.
- Polynomial ring modulo y^r + 1: The ring of polynomials with complex coefficients in which y^r is identified with −1, so that y has order 2r and wrap-around flips a sign.
- Transform layout: A permutation of address bits that places the selected bits of all participating axes at a common offset in consecutive chunks, so that a simultaneous butterfly layer applies to each transform round.
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
- [Radix-digit convolution](radix-digit-convolution.md)
- [Multidimensional transform](multidimensional-transform.md)
- [Gaussian resampling](gaussian-resampling.md)
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

- "These are the synthetic polynomial transforms of Nussbaumer and Quandalle and" (paper)

## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The reader cannot follow this step: "In the source's words, shifts, and two-point butterfly operations." (The sentence attributes the description of the cost to an unnamed source and is incomplete, so the reader cannot check the claim that the transform is counted in shifts and two-point butterfly operations.)
- The reader cannot follow this step: "(-1)^{\lfloor (i+a)/r \rfloor}\, c_i\, y^{(i+a) \bmod r}" (The displayed identity relies on floor and modulus, which the page never explains, and the page does not show why a shift with a between r and 2r, which can wrap twice, gives the stated signs. The reader cannot check it from the page.)
- Say what $\lfloor$ denotes where it is first used (for a size or count, what it counts): "(-1)^{\lfloor (i+a)/r \rfloor}" (The prose says a coefficient is negated when it wraps past the end, but nothing says what the floor brackets count.)
- Say what $\bmod$ denotes where it is first used (for a size or count, what it counts): "y^{(i+a) \bmod r}" (The prose says the shift is cyclic, but nothing says the exponent is reduced modulo r.)
- Say what $z_k$ denotes where it is first used (for a size or count, what it counts): "\omega_t^{jk}\, z_k" (Only implied by the list z=(z_0,...,z_{t-1}); nothing says that z_k is the k-th entry of z.)
- Say what $\log_2$ denotes where it is first used (for a size or count, what it counts): "has $\log_2 t$ levels" (The page's only other logarithm is written \lg n, bound on another page; nothing says what \log_2 denotes here.)
- Say what $\omega_4$ denotes where it is first used (for a size or count, what it counts): "Then $\omega_4 = y^2$" (The page defines \omega_t and takes t = 4 in the example, but never says that \omega_4 is \omega_t with t = 4.)

## Previous version (revise it)

It has 551 words. Fix the problems by restructuring rather than appending: keep the rewrite within 688 words, a quarter more, unless a problem cannot be fixed without more. Pages that grow with every repair stop being self-contained explanations of one concept.

Synthetic polynomial transforms are Fourier-type transforms whose roots of unity are powers of a polynomial variable, so that multiplying a value by a root only moves coefficients and changes some signs. They are the transforms that compute the convolutions in the proof of [Integer multiplication below n log n](main-theorem.md). The result is <cite data-source="paper">a deterministic algorithm that multiplies two n-bit integers in</cite> $O(n(\lg n)^{1-\kappa})$ time for a fixed constant $\kappa$, where $n$ is the bit length of the integers.

## Records and roots

Let $r \ge 2$ be a power of two, where $r$ is the number of complex coefficients in a record. Write $R_r = \mathbb{C}[y]/(y^r+1)$ for the ring of polynomials with complex coefficients in which $y^r$ is identified with $-1$, where $y$ is the polynomial variable. A record is an element of $R_r$, stored as its $r$ coefficients.

Since $y^r = -1$, a power of $y$ that runs past position $r-1$ wraps around with a sign change. The rule below uses three symbols. In it, $c_i$ is the coefficient of $y^i$ in the record, $i$ is its position, and $a$ is the number of places the shift moves each coefficient, with $0 \le a < 2r$:

$$y^a \sum_{i=0}^{r-1} c_i y^i = \sum_{i=0}^{r-1} (-1)^{\lfloor (i+a)/r \rfloor}\, c_i\, y^{(i+a) \bmod r}.$$

So multiplying by $y^a$ moves every coefficient $a$ places along the coefficient list, cyclically, and negates each coefficient that wraps past the end. This is a signed shift of the coefficient list, and it is exact: it involves no rounding and no multiplication.

Let $t$ be a power of two dividing $2r$, the number of entries in the transform. The root $\omega_t = y^{2r/t}$ is a primitive $t$-th root of unity in $R_r$. Indeed, $\omega_t^t = y^{2r} = 1$, and $\omega_t^{t/2} = y^r = -1$. Every power of $\omega_t$ is a power of $y$, so multiplying by any power of $\omega_t$ is a signed shift.

## The transform

<cite data-source="paper">We now implement the normalized Fourier transforms needed for convolution.</cite> The input $z=(z_0,\dots,z_{t-1})$ is a list of $t$ records in $R_r$.

Here $j$ and $k$ are indices running from $0$ to $t-1$, and $Z_j$ is the $j$-th entry of the transform $Z=(Z_0,\dots,Z_{t-1})$ of $z$, given by

$$Z_j = \frac{1}{t}\sum_{k=0}^{t-1} \omega_t^{jk}\, z_k.$$

A synthetic polynomial transform is a polynomial-ring form of the [Discrete Fourier transform](discrete-fourier-transform.md), with its roots taken in $R_r$. <cite data-source="paper">The polynomial roots and radix-two butterflies belong to the fast polynomial-transform method</cite> of Nussbaumer and Quandalle.

## Why the roots make the transform cheap

A radix-two transform of length $t$ has $\log_2 t$ levels. Each level pairs up entries and applies a two-point butterfly: one entry of the pair is multiplied by a power of $\omega_t$, and the pair is replaced by its sum and its difference. Because a power of $\omega_t$ is a signed shift, the multiplication inside each butterfly is only a rearrangement of coefficients with sign changes, and the butterfly costs one addition and one subtraction of records. Between levels, the entries are moved to new addresses, which is also a rearrangement. In the source's words, <cite data-source="paper">the transform calculation consists of address rearrangements, signed</cite> shifts, and two-point butterfly operations.

For example, take $r = 4$ and $t = 4$. Then $\omega_4 = y^2$, and $\omega_4^2 = y^4 = -1$. Multiplying a record by $\omega_4$ gives

$$\omega_4\,(c_0 + c_1 y + c_2 y^2 + c_3 y^3) = -c_2 - c_3 y + c_0 y^2 + c_1 y^3,$$

so the coefficient list $(c_0, c_1, c_2, c_3)$ becomes $(-c_2, -c_3, c_0, c_1)$. This is two moves and two negations, with no multiplication.

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

Write the body to `exegenius/tasks/0107-write-synthetic-transforms.answer.md` and the JSON to `exegenius/tasks/0107-write-synthetic-transforms.answer.json`, then run `exegenius submit 0107-write-synthetic-transforms` in the project directory. If submit rejects the answer, fix the answer and submit again.
