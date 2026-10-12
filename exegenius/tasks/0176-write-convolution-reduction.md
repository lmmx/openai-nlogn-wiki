# exegenius task 0176-write-convolution-reduction

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
- A citation says where a claim comes from; it does not explain it. If the page's concept is an identity, a construction or a definition, state it. Explain how the concept works and how it shows its claim. For a result the page uses from prior work, say what the result states and why it applies here, and cite the source for its proof: the page need not reproduce it.
- Keep the page short. The task gives its word limit, counted without mathematics and citations, and submit rejects a longer page. Give a small worked example where it makes the idea clearer. No filler, no rhetorical flourishes, no announcing what the page will do.
- Write mathematics in LaTeX: $...$ inline, $$...$$ on its own lines for display.
- Do not write a title heading, a prerequisites list or a sources section: those are added automatically. Use ## subheadings only if the page is long.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader has an undergraduate computer science degree: big-O notation and worst-case time of Turing machines, polynomials and complex numbers, and the calculus the degree requires (limits, convergence of sequences and series, basic integrals). The same degree is taken to include introductory discrete mathematics (modular arithmetic, primes, induction, sets, graphs, recurrences) and a first course in linear algebra over the reals (vectors, subspaces, matrices, elimination, dot products), each at introductory depth. Fields in the abstract sense, tensor products, bilinear forms over general fields, Gaussian integers and the Chinese remainder theorem are not assumed.

The reader already understands these concepts:

- Big-O notation (also: O-notation)
- Multitape Turing machine (also: fixed-tape model)
- Complex numbers
- Polynomials
- Schönhage–Strassen n log n conjecture (also: n log n optimality conjecture)
- Harvey–van der Hoeven O(n log n) multiplication (also: Harvey and van der Hoeven multiplier)
- Discrete Fourier transform (also: Fourier transform, DFT, transform of length n)
- Primitive roots of unity (also: root of unity)
- Cyclic convolution (also: normalized cyclic convolution)
- Butterfly operation (also: two-point butterfly, H_0)
- Modular arithmetic (also: congruence, congruence modulo c, residue class, mod c arithmetic, integers modulo n)
- Prime numbers and greatest common divisors (also: primes, prime, gcd, greatest common divisor, coprime, relatively prime)
- Arithmetic modulo 2 and XOR (also: F_2, GF(2), Z/2Z, binary field, two-element field, exclusive or, parity, bitwise XOR)
- Dyadic rationals (also: binary fractions, numbers with power-of-two denominators, dyadic numbers, fixed-point binary fractions)
- Vector spaces, subspaces, bases and dimension (also: linear space, subspace, span, linear independence, basis, dimension, ordered basis)
- Linear maps, matrix operations and invertibility (also: linear transformation, linear operator, matrix product, transpose, invertible matrix, nonsingular matrix, inverse matrix, kernel, null space)
- Gaussian elimination (also: row reduction, Gauss-Jordan elimination, elimination, pivot)
- Triangular matrices (also: lower-triangular matrix, upper-triangular matrix, unit triangular matrix)
- Dot product and orthogonality in R^n (also: inner product, scalar product, orthogonal vectors, orthonormal basis, orthogonal complement)
- Permutations of a finite set (also: permutation, rearrangement, bijection of an index set, permutation matrix)
- Finite sets, subsets and intersections (also: set intersection, cardinality, subset, k-subset, binomial coefficient, power set)
- Graphs (also: undirected graph, vertices and edges, adjacency, neighbours, intersection graph, source and sink vertices of the network)
- Mathematical induction (also: induction, inductive proof, strong induction, proof by induction on n)
- Recurrence relations and divide-and-conquer recursion (also: recurrence, recursion equation, divide and conquer, recursive algorithm, cost recurrence, T(n) recurrence)
- Floor and ceiling functions (also: integer part, floor, ceiling, ⌊x⌋, ⌈x⌉)
- Logarithms base 2 (also: lg, log base 2, binary logarithm, log_2)
- Big-Omega and big-Theta notation (also: Omega notation, Theta notation, Ω, Θ, asymptotic lower bound, asymptotic tight bound)
- Limits and convergence of sequences and series (also: limit of a sequence, convergent sequence, convergent series, sum of a series, n tends to infinity)
- Geometric series (also: geometric sum, geometric progression sum, sum of powers of a ratio)
- Newton's method (also: Newton iteration, Newton-Raphson method, Newton reduction, Newton's root-finding iteration)
- Worst-case time complexity of a Turing machine (also: running time, worst-case running time, time bound, T_A(n), time on n-bit inputs)

## This page

Concept: Multiplication as convolution of digits
Gloss: Writing each integer in radix 2^b digits so that the integer product becomes a convolution of the digit sequences, which is then carried back to binary.
Also called: radix-digit convolution

## This page in the argument

The step: The integer product is the carried convolution of the radix-$2^b$ digit sequences of the two inputs.
How: write each input in radix digits, convolve the digit sequences, and carry the result back to binary
Why: Short digit coefficients let the transform machinery act on fixed-width records. (the sources leave this for the reader to work out: spell it out)

Its sub-steps, in order:

- Multiplication reduces to convolution of short integer coefficients.

It serves these steps, from the main result down:

- Two $n$-bit integers can be multiplied exactly in $O(n(\lg n)^{1-\kappa})$ worst-case time on a deterministic multitape Turing machine, for a fixed $\kappa=2^{-182}$.; how: reduce the product to a digit convolution, compute that convolution through transform layers whose tape cost saves a power, and recover the exact product by rounding (on [Integer multiplication in O(n(lg n)^(1-κ)) time](integer-multiplication-target.md))

## Symbols already bound on earlier pages

The symbols in the names of the concepts the reader knows are listed with those concepts above.

- $n$ (input bit length), bound on [Schönhage–Strassen n log n conjecture](nlogn-conjecture.md): The number of bits in each input integer; the count of bits in one operand.
- $\kappa$ (exponent gap), bound on [Schönhage–Strassen n log n conjecture](nlogn-conjecture.md): A fixed positive constant, the gap $\kappa = 2^{-182}$ in the exponent of the logarithm.
- $\kappa$ (exponent gap), bound on [Harvey–van der Hoeven O(n log n) multiplication](harvey-hoeven-multiplier.md): A fixed positive constant, $2^{-182}$, by which the logarithmic exponent of the target running time falls below 1.
- $n$ (root order), bound on [Primitive roots of unity](roots-of-unity.md): The order of the root, a positive integer that counts the positions of the transform it labels.
- $\omega$ (primitive root), bound on [Primitive roots of unity](roots-of-unity.md): A primitive $n$-th root of unity, the complex number that labels the positions of a transform.
- $k$ (power exponent), bound on [Primitive roots of unity](roots-of-unity.md): An integer exponent of the root, marking which power of $\omega$ is meant.
- $j$ (earlier exponent), bound on [Primitive roots of unity](roots-of-unity.md): An integer exponent of the root, the smaller of two powers compared in the distinctness argument.
- $n$ (sequence length), bound on [Discrete Fourier transform](fourier-transform.md): The count of entries in the input and output sequences, which is also the order of the root omega.
- $a$ (input sequence), bound on [Discrete Fourier transform](fourier-transform.md): The input list of complex numbers, whose length is n.
- $\hat a$ (output sequence), bound on [Discrete Fourier transform](fourier-transform.md): The list of transform values, one per position, whose length is n.
- $j$ (input index), bound on [Discrete Fourier transform](fourier-transform.md): The position of an input entry, running from 0 to n-1.
- $k$ (output index), bound on [Discrete Fourier transform](fourier-transform.md): The position of an output entry, running from 0 to n-1.
- $p$ (coefficient polynomial), bound on [Discrete Fourier transform](fourier-transform.md): The polynomial whose coefficient list is the input sequence a.
- $x$ (formal variable), bound on [Discrete Fourier transform](fourier-transform.md): A placeholder for a number to be substituted into the polynomial p.
- $u$ (first input value), bound on [Butterfly operation](butterfly-operation.md): The first of the two input values that the butterfly maps.
- $v$ (second input value), bound on [Butterfly operation](butterfly-operation.md): The second of the two input values that the butterfly maps.
- $H_0$ (butterfly map), bound on [Butterfly operation](butterfly-operation.md): The two-point map sending a pair of values to its half-sum and half-difference.
- $I$ (identity matrix), bound on [Butterfly operation](butterfly-operation.md): The $2\times 2$ identity matrix, which leaves every pair unchanged.
- $x$ (formal variable), bound on [Cyclic convolution](cyclic-convolution.md): A formal variable, an indeterminate not evaluated at any number, used as the placeholder of the polynomials a(x) and b(x).
- $r$ (sequence length), bound on [Cyclic convolution](cyclic-convolution.md): The number of complex coefficients in each input sequence, so both sequences have length r.
- $b$ (second input sequence), bound on [Cyclic convolution](cyclic-convolution.md): The second of the two input sequences, a list of r complex numbers.
- $c$ (cyclic convolution), bound on [Cyclic convolution](cyclic-convolution.md): The cyclic convolution of a and b, a sequence of r complex coefficients.
- $l$ (term index of b), bound on [Cyclic convolution](cyclic-convolution.md): An index running over 0 to r-1 that labels the terms of b in the reduced product.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Cyclic convolution](cyclic-convolution.md): The product of two sequences in which indices are taken modulo a fixed length, so each coefficient of the result is a sum of products over residues.
  Shown as: Multiplication as convolution of digits *<predicate>* Cyclic convolution

## Pages that build on this one

- Signed Kronecker packing: Encoding a polynomial with bounded signed coefficients as an integer by evaluating it at a large power of two, so that polynomial products become integer products.
- Integer multiplication in O(n(lg n)^(1-κ)) time: A deterministic multitape Turing machine that multiplies two n-bit integers exactly in O(n(lg n)^(1-κ)) worst-case time for a fixed κ = 2^(-182) > 0, beating the n log n conjecture in this model.

## Other pages you may link to

- [Schönhage–Strassen n log n conjecture](nlogn-conjecture.md)
- [Harvey–van der Hoeven O(n log n) multiplication](harvey-hoeven-multiplier.md)
- [Primitive roots of unity](roots-of-unity.md)
- [Discrete Fourier transform](fourier-transform.md)
- [Butterfly operation](butterfly-operation.md)
- [Polynomial ring modulo yʳ + 1](polynomial-ring-y.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Signed Kronecker packing](kronecker-packing.md)
- [Matrix rank](matrix-rank.md)
- [Linear network with restored auxiliary values](linear-network-exchange.md)
- [Lower-triangular factorization](lower-triangular-factorization.md)
- [Address shear](address-shear.md)
- [Fast address interchange](address-interchange.md)
- [Chinese-remainder address map](chinese-remainder-address-map.md)
- [Tensor product](tensor-product.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Recursive power saving](recursive-power-saving.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein's chirp identity](bluestein-chirp.md)
- [Exact recovery by rounding](rounding-recovery.md)
- [Integer multiplication in O(n(lg n)^(1-κ)) time](integer-multiplication-target.md)

## Evidence from the sources, with the paragraph around each quote

- "reduces multiplication to convolution of short integer coefficients" (paper)

  > Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients. Our starting point is the Gaussian-resampling reduction of Harvey and van der Hoeven \cite{HarveyHoeven2021}: it replaces the Fourier transforms needed for this convolution by multidimensional transforms whose axis lengths are powers of two. After a further conversion to convolution, one coordinate is stored as the coefficient list of a polynomial modulo $y^r+1$, with $r$ a power of two. Powers of $y$ then serve as roots of unity in the remaining axes, and multiplication by such a root is a signed shift of the coefficient list. These are the synthetic polynomial transforms of Nussbaumer and Quandalle and Nussbaumer~\cite{NussbaumerQuandalle1978,Nussbaumer1980}.


## Sources (read from disk as needed)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- $b$ means digit width here, but second input sequence on [Cyclic convolution](cyclic-convolution.md), which this page builds on: Use another letter for the digit width on convolution-reduction (for example w), since b is the second input sequence on cyclic-convolution.

## Previous version (revise it)

It has 313 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 391 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

Multiplication as convolution of digits is the reduction that turns an integer product into a convolution of short coefficient sequences, followed by a carry back to binary. It is the first step of the argument: the convolution is what the transform machinery later computes.

Let $b$ be the number of bits in one digit; here $b$ does not mean the second input sequence of the cyclic convolution page. Let $m$ be the number of digits in each input. Let $U$ be the first input and $V$ the second. The digit sequence of $U$ is its radix-$2^b$ digits, least significant first, so $U$ has $m$ digits, each between $0$ and $2^b-1$. The digit sequence of $V$ is defined the same way.

Multiplication reduces to [Cyclic convolution](cyclic-convolution.md) of short integer coefficients. Pad both digit sequences with zeros to length $r \ge 2m-1$. The convolution of two length-$m$ sequences has $2m-1$ terms, so no term wraps around and mixes with another. The paper opens with this reduction. <cite data-source="paper">Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients.</cite>

For example, in radix $4$ ($b=2$), $U=13$ has digits $(1,3)$ and $V=11$ has digits $(3,2)$, since $13=1+3\cdot 4$ and $11=3+2\cdot 4$. Their convolution has coefficients $(3,11,6)$: the coefficient of $4^0$ is $1\cdot 3$, that of $4^1$ is $1\cdot 2+3\cdot 3$, and that of $4^2$ is $3\cdot 2$. The coefficient $11$ is larger than a digit, so the result is not yet in binary. Carrying evaluates the coefficient list at $4=2^b$: $3+11\cdot 4+6\cdot 16=143=13\cdot 11$.

The point of short coefficients is size, so that the transform machinery can work on small fixed-size records instead of whole integers. Each coefficient is a sum of at most $m$ products of $b$-bit digits, so it is at most $m(2^b-1)^2 < 2^{2b+\lceil \lg m\rceil}$ and fits in $2b+\lceil \lg m\rceil$ bits. A transform layer handles the coefficients as records of $r$ entries, each of this bounded width, and its arithmetic on a record uses numbers of that width. What grows with the input length is the number of records, not their width, and the width grows only logarithmically in $m$. The carry into binary is done once, at the end, on the whole integer.

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

Write the body to `exegenius/tasks/0176-write-convolution-reduction.answer.md` and the JSON to `exegenius/tasks/0176-write-convolution-reduction.answer.json`, then run `exegenius submit 0176-write-convolution-reduction` in the project directory. If submit rejects the answer, fix the answer and submit again.
