# exegenius task 0085-write-radix-digit-convolution

Project directory: `/mnt/openai-nlogn` (paths below are relative to it)

Write one page of an explanatory wiki. The wiki explains a target result from source documents to a specific reader, one concept per page, in reading order.

- Write for this reader's next uncertainty: at each point, give what they need to follow, and no more. The task lists the step of the argument this page presents, its motivations, and the pages around it. They are material for deciding what to say, not a list to cover: explain the transitions this reader would find hard, and leave familiar ones to ordinary sentences.
- Open with a sentence that says what the concept is and what it is for on the way to the target.
- If the page presents a step of the argument, say how its method shows its claim, and give its main motivation in a sentence. Add another motivation only if the reader would be stuck without it.
- Explain the page's concept so that this reader can follow it using only what they already understand (listed below), what this page itself explains, and the linked prerequisite pages.
- Define any other technical term on this page, where it is first used.
- Say what each symbol denotes where you introduce it: what it stands for, and for a size or count, what it counts ("$r$, the number of complex coefficients in a record", not "a power of two $r$"). A use in an example ("take $r = 4$") does not say what $r$ denotes. Symbols listed as already bound can be used without restating them: the page shows the reader their meanings. Using one of those letters with another meaning confuses readers: pick another letter, or say on the page that the letter changes meaning here.
- Link each prerequisite page the first time you rely on it, using the exact markdown link given. You may also link the other pages listed. Submit rejects links to anything else in the wiki; external URLs are allowed.
- For each prerequisite page, give a relation: the prerequisite's id, a predicate, and the sentence that links or names it, copied exactly. Use the sentence where the page relies on it; do not add a sentence for the purpose. The page shows the relation as "<this page's concept> *<predicate>* <prerequisite>", so pick a predicate that makes that a true sentence, with this page's concept as subject: "is reduced to", "computes its transforms by", "is based on", "follows from", "bounds the cost of". Build the predicate from the sentence's own words (other forms of a word count: "reduces" for "reduced"), and pick one that says what the prerequisite does for this page: "uses" says little.
- Stay accurate to the sources. The paragraphs around the evidence are given below; read further in the sources only if they are not enough. State only what the sources support or what is standard background; do not invent results, constants or attributions.
- Cite the results and constants a reader may want to check, right after the claim: `<cite data-source="id">text copied word for word from that source</cite>`. Readers see these as "(see p. 5)"-style references, hidden until they ask for them, so the sentence must read complete without the quoted words: write "the cost is $O(n \log n)$ <cite …>…</cite>", not "the paper states the cost as <cite …>…</cite>". Submit rejects a citation right after "that", "as", "states", "says", "is", "gives", "reads" or a colon, and text not found in the named source. Do not cite common background.
- Keep the page short. The task gives its word limit, counted without mathematics and citations, and submit rejects a longer page. Give a small worked example where it makes the idea clearer. No filler, no rhetorical flourishes, no announcing what the page will do.
- Write mathematics in LaTeX: $...$ inline, $$...$$ on its own lines for display.
- Do not write a title heading, a prerequisites list or a sources section: those are added automatically. Use ## subheadings only if the page is long.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader has completed an undergraduate computer science degree: big-O analysis, polynomials and complex numbers, and Turing machines with tapes, plus the discrete mathematics and first linear algebra course that such a degree requires. For the paper this means modular arithmetic, gcd and primes, roots of unity, binary arithmetic over F2 with Hamming weight, and basic vector-space and matrix facts (subspaces, rank, projections, dot product, eigenvalues) at first-course depth. Bilinear forms, tensor products, finite-field and ring theory, the Chinese remainder theorem, Newton iteration and the Fourier and convolution machinery beyond the basics are treated as not known.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes (also: multitape Turing machine)
- Fixed-tape machine model (also: fixed finite-tape model, fixed-tape machine)
- Exact integer multiplication
- The n log n optimality conjecture (also: Schönhage–Strassen conjecture)
- Established O(n log n) multiplier (also: Harvey–van der Hoeven multiplier)
- Discrete Fourier transform (also: normalized Fourier transform, transforms)
- Cyclic convolution (also: convolution, normalized cyclic convolution, cyclic product (cyclic convolution))
- Signed coefficient packing (also: Kronecker substitution)
- Subspace labels
- Linear networks and frames (also: roles, frames)
- Subset-intersection network (also: three-element subset network)
- Address-field interchange (also: power-width interchange)
- Address shear
- Rank-saving recursion (also: recursive saving)
- Gaussian dyadics
- Complex phase network (also: phase-frame identity)
- Mathematical induction (also: induction, proof by induction, inductive proof)
- Logarithms and floor and ceiling functions (also: floor function, ceiling function, integer part, log base 2, lg)
- Binary representation of integers (also: binary string, bit string, base-2 representation, binary digits, bits)
- Dyadic rationals (also: binary fractions, dyadic numbers)
- Modular arithmetic (also: congruence modulo m, residues modulo m, integers modulo m, remainder arithmetic)
- Greatest common divisor and coprimality (also: gcd, relatively prime, coprime, Euclidean algorithm)
- Prime numbers (also: primes, primality, prime factorization)
- Roots of unity (also: n-th roots of unity, primitive root of unity, unit roots, powers of a root of unity)
- Binary field F2 and XOR arithmetic (also: GF(2), field of two elements, mod-2 arithmetic, exclusive or, XOR, Boolean addition)
- Hamming weight (also: popcount, number of ones, weight of a binary vector, wt(x))
- Vector spaces and subspaces (also: linear subspace, span, basis, linear independence, dimension)
- Matrices and linear maps (also: matrix multiplication, matrix inverse, transpose, identity matrix, linear transformation)
- Matrix rank (also: rank, rank of a linear map, column rank, row rank)
- Projection onto a subspace (also: projection matrix, idempotent linear map, orthogonal projection)
- Dot product and orthogonality (also: inner product, scalar product, orthogonal vectors, perpendicular vectors, orthogonal complement)
- Eigenvalues and eigenvectors (also: eigenvalue, eigenvector, spectrum, characteristic polynomial)
- Bilinear form (also: bilinear space, nondegenerate form)
- Tensor product (also: tensor product of spaces)

## This page

Concept: Radix-digit convolution
Gloss: Writing both integers as polynomials in a power of two whose coefficients are their digits, so that their product is a polynomial convolution of short coefficients.

## This page in the argument

The step: The exact product of two $n$-bit integers is obtained from the convolution of their radix-digit coefficients, computed by transforms on a fixed tape layout and then recovered and carried.
How: reduce the convolution by a Chinese-remainder map, Gaussian resampling, Bluestein's identity and a phase twist to a convolution over a polynomial ring, then recover coefficients and propagate carries
Why: Gaussian resampling connects the pairwise-coprime transform lengths of the product to the power-of-two lengths of the synthetic transforms, so the reduction chains these steps. (the sources leave this for the reader to work out: spell it out)

Its sub-steps, in order:

- The radix-digit coefficient list is placed on a product of distinct prime cyclic axes by a Chinese-remainder map that preserves convolution. (on [Chinese-remainder map](chinese-remainder-map.md))
- Gaussian resampling expresses each source Fourier transform through a power-of-two tensor transform. (on [Gaussian resampling](gaussian-resampling.md))
- The source and target coordinate permutations are retained in the transform identity, so they need not be executed as separate sorts. (on [Transform identity with retained permutations](transform-identity.md))
- Bluestein's chirp identity converts the middle transform, including its target permutation, into normalized cyclic convolution. (on [Bluestein's chirp identity](bluestein-chirp-identity.md))
- A phase twist changes the last cyclic coordinate into a polynomial ring modulo $y^r+1$, whose negative wrap gives the original cyclic wrap. (on [Phase twist](phase-twist.md))
- Convolution on the remaining axes over $\mathbb{C}[y]/(y^r+1)$ is computed by two forward synthetic transforms, a pointwise product, and an opposite transform. (on [Convolution over the polynomial ring](polynomial-ring-convolution.md))
- The source permutation retained during resampling cancels across the two forward source transforms, their pointwise product, and the opposite transform.
- The recovered coefficient error is strictly below $1/2$, so rounding recovers the integer coefficients exactly. (on [Exact coefficient recovery](recovery-and-error.md))
- Carries are propagated through the recovered coefficients to obtain the exact binary product. (on [Carry propagation](carry-propagation.md))

It serves these steps, from the main result down:

- A deterministic fixed-tape machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time, with $\kappa=2^{-182}$, below the $n\lg n$ conjecture in this model.; how: bound the cost of an exact multiplication whose transform layers are made cheap by two tape procedures, then fix parameters so every cost term fits (on [Integer multiplication below n log n](main-theorem.md))

## Symbols already bound on earlier pages

The symbols in the names of the concepts the reader knows are listed with those concepts above.

- $a$ (numerator real part), bound on [Gaussian dyadics](gaussian-dyadics.md): The integer real part of the numerator a + bi of a Gaussian dyadic.
- $b$ (numerator imaginary part), bound on [Gaussian dyadics](gaussian-dyadics.md): The integer imaginary part of the numerator a + bi of a Gaussian dyadic.
- $k$ (denominator exponent), bound on [Gaussian dyadics](gaussian-dyadics.md): A non-negative integer; the denominator of a Gaussian dyadic is the power of two 2^k.
- $n$ (input length), bound on [Exact integer multiplication](exact-integer-multiplication.md): The common length of the two input strings, counting the bits of each input.
- $x$ (first input), bound on [Exact integer multiplication](exact-integer-multiplication.md): The first binary input string, of length n.
- $y$ (second input), bound on [Exact integer multiplication](exact-integer-multiplication.md): The second binary input string, of length n.
- $\mathrm{val}$ (value function), bound on [Exact integer multiplication](exact-integer-multiplication.md): The function mapping a binary string to the nonnegative integer whose binary digits it is.
- $k$ (padded width), bound on [Exact integer multiplication](exact-integer-multiplication.md): The number of bits in the padded binary representation, counting leading zeros.
- $\mathrm{bin}_k$ (padded binary representation), bound on [Exact integer multiplication](exact-integer-multiplication.md): The function giving the k-bit binary representation of a number z, padded with leading zeros.
- $n$ (input length), bound on [The n log n optimality conjecture](n-log-n-conjecture.md): The number of bits in each of the two input integers.
- $V$ (stored volume), bound on [Address-field interchange](address-interchange.md): The number of bits the array stores.
- $u$ (field width), bound on [Address-field interchange](address-interchange.md): The number of bits in each address field.
- $\tau$ (cost exponent), bound on [Address-field interchange](address-interchange.md): A fixed exponent less than 1 in the cost bound.
- $H$ (first address field), bound on [Address shear](address-shear.md): The first of the two address fields the shear updates, a vector of residues.
- $D$ (second address field), bound on [Address shear](address-shear.md): The second of the two address fields the shear updates, a vector of residues, left unchanged by the shear.
- $n$ (input length), bound on [Established O(n log n) multiplier](established-multiplier.md): The number of bits in each of the two binary input strings.
- $w$ (block width), bound on [Signed coefficient packing](signed-packing.md): The number of bits reserved for each coefficient in a packed integer.
- $f$ (packed polynomial), bound on [Signed coefficient packing](signed-packing.md): A polynomial with integer coefficients that is packed into an integer.
- $F$ (packed integer of f), bound on [Signed coefficient packing](signed-packing.md): The integer $f(2^w)$ obtained by packing the coefficients of $f$ into blocks of width $w$.
- $g$ (second polynomial), bound on [Signed coefficient packing](signed-packing.md): A second polynomial with integer coefficients, multiplied by $f$.
- $G$ (packed integer of g), bound on [Signed coefficient packing](signed-packing.md): The integer $g(2^w)$ obtained by packing the coefficients of $g$ into blocks of width $w$.
- $h$ (product polynomial), bound on [Signed coefficient packing](signed-packing.md): The product $fg$ of the two packed polynomials, whose coefficients the packed product recovers.
- $F$ (fixed bilinear space), bound on [Subspace labels](subspace-labels.md): The fixed vector space carrying the nondegenerate bilinear form, in which all labels are subspaces.
- $U$ (label), bound on [Subspace labels](subspace-labels.md): A nondegenerate subspace of $F$ attached to a wire or an edge of the network.
- $V$ (larger label), bound on [Subspace labels](subspace-labels.md): The label on the edge that contains the smaller label $U$.
- $R$ (orthogonal residual), bound on [Subspace labels](subspace-labels.md): The orthogonal complement of the smaller label inside the larger one, on an edge.
- $s$ (smaller-call count), bound on [Subset-intersection network](subset-intersection-network.md): The total number of smaller calls made by one call of the recursion.
- $W$ (stream shrink factor), bound on [Subset-intersection network](subset-intersection-network.md): The factor by which the volume of each stream shrinks, so each smaller call receives 1/W of the volume.
- $m$ (label space dimension), bound on [Subset-intersection network](subset-intersection-network.md): The dimension of the fixed space from which the subspace labels are drawn.
- $V$ (stored volume), bound on [Rank-saving recursion](rank-saving-recursion.md): The volume of stored data that one call acts on.
- $f$ (recursion parameter), bound on [Rank-saving recursion](rank-saving-recursion.md): The recursion parameter, counting field digits for address interchange or selected axes for a numerical layer.
- $m$ (fixed dimension), bound on [Rank-saving recursion](rank-saving-recursion.md): The dimension of a fixed space, counting its basis vectors.
- $W$ (stream division factor), bound on [Rank-saving recursion](rank-saving-recursion.md): The factor by which each stream's volume is divided.
- $s$ (smaller call count), bound on [Rank-saving recursion](rank-saving-recursion.md): The number of smaller calls that one call makes.
- $a$ (kernel scalar a), bound on [Complex phase network](complex-phase-network.md): One of the two scalars of a two-point kernel $aI+bX$.
- $b$ (kernel scalar b), bound on [Complex phase network](complex-phase-network.md): The other scalar of a two-point kernel $aI+bX$.
- $I$ (identity on two points), bound on [Complex phase network](complex-phase-network.md): The identity map on the two points of a kernel.
- $X$ (two-point swap), bound on [Complex phase network](complex-phase-network.md): The map that swaps the two points of a kernel.
- $t$ (sequence length), bound on [Cyclic convolution](cyclic-convolution.md): The number of entries in each of the two sequences, a positive integer.
- $a$ (first input sequence), bound on [Cyclic convolution](cyclic-convolution.md): The first sequence of t complex numbers, indexed from 0 to t-1.
- $b$ (second input sequence), bound on [Cyclic convolution](cyclic-convolution.md): The second sequence of t complex numbers, indexed from 0 to t-1.
- $i$ (index into a), bound on [Cyclic convolution](cyclic-convolution.md): The index of an entry of a, ranging over 0 to t-1.
- $j$ (index into b), bound on [Cyclic convolution](cyclic-convolution.md): The index of an entry of b, ranging over 0 to t-1.
- $k$ (index into c), bound on [Cyclic convolution](cyclic-convolution.md): The index of an entry of the output sequence c, ranging over 0 to t-1.
- $c$ (cyclic convolution), bound on [Cyclic convolution](cyclic-convolution.md): The output sequence a \ast b of length t, whose k-th entry is the sum of a_i b_j over all pairs with i+j congruent to k modulo t.
- $q$ (vector length), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The number of entries in a vector, which is the count the transform acts on.
- $\omega$ (root of unity), bound on [Discrete Fourier transform](discrete-fourier-transform.md): A primitive $q$-th root of unity, whose powers weight the entries of the transform.
- $x$ (input vector), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The vector of $q$ complex numbers that the transform takes as input.
- $X$ (transformed vector), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The vector of $q$ complex numbers that is the discrete Fourier transform of $x$.
- $j$ (input index), bound on [Discrete Fourier transform](discrete-fourier-transform.md): An index running from $0$ to $q-1$ over the input entries $x_j$.
- $k$ (output index), bound on [Discrete Fourier transform](discrete-fourier-transform.md): An index running from $0$ to $q-1$ over the output entries $X_k$.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Exact integer multiplication](exact-integer-multiplication.md): Given binary strings x and y of length n, output the 2n-bit binary representation of their product.
  Shown as: Radix-digit convolution *<predicate>* Exact integer multiplication
- [Discrete Fourier transform](discrete-fourier-transform.md): The map sending a vector of q values to its q values weighted by powers of a q-th root of unity, normalized by 1/q.
  Shown as: Radix-digit convolution *<predicate>* Discrete Fourier transform

## Pages that build on this one

- Gaussian resampling: A technique that replaces a Fourier transform of arbitrary length by transforms whose axis lengths are powers of two, using Gaussian weights to move between the two sets of frequencies.
- Chinese-remainder map: A relabeling of coefficient positions by mixed-radix digits for pairwise coprime lengths, which turns one cyclic convolution into a multidimensional cyclic convolution.
- Carry propagation: Converting the recovered integer radix-digit coefficients into a binary string by adding each coefficient to a carry from the previous position.
- Integer multiplication below n log n: A deterministic fixed-tape machine that multiplies two n-bit integers exactly in O(n (lg n)^(1−κ)) time with κ = 2^−182, which disproves the n log n optimality conjecture in this model.

## Other pages you may link to

- [Gaussian dyadics](gaussian-dyadics.md)
- [Linear networks and frames](linear-network-frames.md)
- [Fixed-tape machine model](fixed-tape-model.md)
- [The n log n optimality conjecture](n-log-n-conjecture.md)
- [Address-field interchange](address-interchange.md)
- [Address shear](address-shear.md)
- [Established O(n log n) multiplier](established-multiplier.md)
- [Signed coefficient packing](signed-packing.md)
- [Bilinear form](bilinear-form.md)
- [Subspace labels](subspace-labels.md)
- [Subset-intersection network](subset-intersection-network.md)
- [Rank-saving recursion](rank-saving-recursion.md)
- [Complex phase network](complex-phase-network.md)
- [Tensor product](tensor-product.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md)
- [Chinese-remainder map](chinese-remainder-map.md)
- [Bluestein's chirp identity](bluestein-chirp-identity.md)
- [Phase twist](phase-twist.md)
- [Convolution over the polynomial ring](polynomial-ring-convolution.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Guard-width bound](guard-width-bound.md)
- [Transform layout](transform-layout.md)
- [Exact coefficient recovery](recovery-and-error.md)
- [Packed selected-bit addition](packed-bit-addition.md)
- [Transform identity with retained permutations](transform-identity.md)
- [Prime source lengths](prime-source-lengths.md)
- [Carry propagation](carry-propagation.md)
- [Integer multiplication below n log n](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients" (paper)

  > Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients. Our starting point is the Gaussian-resampling reduction of Harvey and van der Hoeven [15]: it replaces the Fourier transforms needed for this convolution by multidimensional transforms whose axis lengths are powers of two. After a further conversion to convolution, one coordinate is stored as the coefficient list of a polynomial modulo y r + 1, with r a power of two. Powers of y then serve as roots of unity in the remaining axes, and multiplication by such a root is a signed shift of the coefficient list. These are the synthetic polynomial transforms of Nussbaumer and Quandalle and Nussbaumer [21, 20]. In this representation, the transform calculation consists of address rearrangements,


## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- "transforms" is the concept [Discrete Fourier transform](discrete-fourier-transform.md), now a prerequisite: link it where the term is used.

## Previous version (revise it)

It has 209 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 261 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

Radix-digit convolution reduces [exact integer multiplication](exact-integer-multiplication.md) to a convolution of short integer coefficients, which is the form that the later transforms act on.

Fix a digit width $k$, the number of bits in each digit, and a digit count $m$, the number of digits in each input, with $mk \ge n$. Write the first input in radix $2^k$ as $x = \sum_{j=0}^{m-1} x_j 2^{kj}$, where each digit $x_j$ is an integer in $[0, 2^k)$ and $x_0$ is the least significant digit. The second input $y$ is written in the same way, with digits $y_j$.

Digits become the coefficients of polynomials in an indeterminate $t$: $X(t) = \sum_j x_j t^j$ and $Y(t) = \sum_j y_j t^j$, with $x = X(2^k)$ and $y = Y(2^k)$. The product of these polynomials has coefficients $c_j = \sum_{i+l=j} x_i y_l$, the convolution of the two digit lists, and so $xy = \sum_j c_j 2^{kj}$. <cite data-source="paper">Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients</cite>

The convolution is the object that transforms can compute quickly on a fixed layout, which is why the reduction stops at this form rather than at the integer product. Each $c_j$ is less than $m 2^{2k}$, so it may be larger than a digit, and the sum $\sum_j c_j 2^{kj}$ is not yet a binary string. The coefficients must be combined by [carry propagation](carry-propagation.md) to give the binary product.

Take $x = 11$ and $y = 6$ with $k = 2$ and $m = 2$. Their digits are $x_0 = 3$, $x_1 = 2$, $y_0 = 2$ and $y_1 = 1$, so $c_0 = 3 \cdot 2 = 6$, $c_1 = 3 \cdot 1 + 2 \cdot 2 = 7$ and $c_2 = 2 \cdot 1 = 2$. Then $6 + 7 \cdot 4 + 2 \cdot 16 = 66 = 11 \cdot 6$. The coefficient $c_1 = 7$ exceeds the largest digit $2^k - 1 = 3$, so it must be carried.

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

Write the body to `exegenius/tasks/0085-write-radix-digit-convolution.answer.md` and the JSON to `exegenius/tasks/0085-write-radix-digit-convolution.answer.json`, then run `exegenius submit 0085-write-radix-digit-convolution` in the project directory. If submit rejects the answer, fix the answer and submit again.
