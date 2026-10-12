# exegenius task 0161-write-synthetic-transform

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
- Multiplication as convolution of digits (also: radix-digit convolution)
- Polynomial ring modulo yʳ + 1 (also: negacyclic ring, signed shift)
  - $y$ (ring indeterminate): The variable of the polynomial ring whose powers serve as roots of unity in the remaining axes.
  - $r$ (coefficient count): The number of coefficients in the coefficient list of one polynomial record, a power of two.
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

Concept: Synthetic polynomial transform
Gloss: A transform over a polynomial ring in which the roots of unity are powers of y, so that each transform stage uses only signed shifts and butterfly additions.
Also called: Nussbaumer polynomial transform, synthetic transform

## This page in the argument

The step: The two forward synthetic transforms keep the same frequency order through their pointwise product, and the opposite transform consumes that order.
How: run synthetic transforms whose roots of unity are powers of $y$ and whose layers use signed shifts and butterflies
Why: Powers of $y$ as roots of unity make each transform stage a signed shift plus butterfly additions. (the sources leave this for the reader to work out: spell it out)

Its sub-steps, in order:

- The two forward synthetic transforms keep the same frequency order through their pointwise product.

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
- $n$ (sequence length), bound on [Discrete Fourier transform](fourier-transform.md): The number of entries in the input and output sequences, the length of the transform; it is also the order of $\omega$.
- $a$ (input sequence), bound on [Discrete Fourier transform](fourier-transform.md): The input sequence, a list of $n$ complex numbers $a_0,\dots,a_{n-1}$.
- $\hat a$ (output sequence), bound on [Discrete Fourier transform](fourier-transform.md): The DFT of $a$, whose entries $\hat a_k$ are given by the formula below.
- $j$ (input index), bound on [Discrete Fourier transform](fourier-transform.md): The index of an input entry $a_j$, running from $0$ to $n-1$.
- $k$ (output index), bound on [Discrete Fourier transform](fourier-transform.md): The index of an output entry $\hat a_k$, running from $0$ to $n-1$.
- $p$ (coefficient polynomial), bound on [Discrete Fourier transform](fourier-transform.md): The polynomial $p(x)=\sum_{j} a_j x^j$ whose coefficient list is $a$.
- $x$ (formal variable), bound on [Discrete Fourier transform](fourier-transform.md): The formal variable of $p$, a placeholder for a number to be substituted.
- $u$ (first input value), bound on [Butterfly operation](butterfly-operation.md): The first of the two input values that the butterfly maps.
- $v$ (second input value), bound on [Butterfly operation](butterfly-operation.md): The second of the two input values that the butterfly maps.
- $H_0$ (butterfly map), bound on [Butterfly operation](butterfly-operation.md): The two-point map sending a pair of values to its half-sum and half-difference.
- $I$ (identity matrix), bound on [Butterfly operation](butterfly-operation.md): The $2\times 2$ identity matrix, which leaves every pair unchanged.
- $x$ (formal variable), bound on [Cyclic convolution](cyclic-convolution.md): A formal variable, an indeterminate not evaluated at any number, used as the placeholder of the polynomials a(x) and b(x).
- $r$ (sequence length), bound on [Cyclic convolution](cyclic-convolution.md): The number of complex coefficients in each input sequence, so both sequences have length r.
- $b$ (second input sequence), bound on [Cyclic convolution](cyclic-convolution.md): The second of the two input sequences, a list of r complex numbers.
- $c$ (cyclic convolution), bound on [Cyclic convolution](cyclic-convolution.md): The cyclic convolution of a and b, a sequence of r complex coefficients.
- $l$ (term index of b), bound on [Cyclic convolution](cyclic-convolution.md): An index running over 0 to r-1 that labels the terms of b in the reduced product.
- $b$ (digit width), bound on [Multiplication as convolution of digits](convolution-reduction.md): The number of bits in one digit, so each digit lies between 0 and 2^b-1.
- $m$ (digit count), bound on [Multiplication as convolution of digits](convolution-reduction.md): The number of digits in each input, the count of radix-2^b digits of each integer.
- $U$ (first input integer), bound on [Multiplication as convolution of digits](convolution-reduction.md): The first of the two integers being multiplied.
- $V$ (second input integer), bound on [Multiplication as convolution of digits](convolution-reduction.md): The second of the two integers being multiplied.
- $y$ (ring indeterminate), bound on [Polynomial ring modulo yʳ + 1](polynomial-ring-y.md): The variable of the polynomial ring, an indeterminate that is not evaluated at any number.
- $r$ (coefficient count), bound on [Polynomial ring modulo yʳ + 1](polynomial-ring-y.md): The number of complex coefficients in the list of one element of the ring, a power of two.
- $\theta$ (twist factor), bound on [Polynomial ring modulo yʳ + 1](polynomial-ring-y.md): A complex $2r$-th root of unity with $\theta^r=-1$, by which the phase twist multiplies the entries of a coefficient list.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Polynomial ring modulo yʳ + 1](polynomial-ring-y.md): The ring of complex polynomials in y reduced modulo y^r + 1, where multiplying by a power of y is a signed cyclic shift of the coefficient list.
  Shown as: Synthetic polynomial transform *<predicate>* Polynomial ring modulo yʳ + 1
- [Primitive roots of unity](roots-of-unity.md): A complex number ω is a primitive n-th root of unity when ω^n = 1 and no smaller positive power equals 1.
  Shown as: Synthetic polynomial transform *<predicate>* Primitive roots of unity
- [Discrete Fourier transform](fourier-transform.md): The map sending a length-n sequence to its values at the n-th roots of unity, i.e. the sums of the sequence weighted by powers of a root of unity.
  Shown as: Synthetic polynomial transform *<predicate>* Discrete Fourier transform

## Pages that build on this one

- Exact recovery by rounding: The step in which the approximate convolution coefficients are rounded to integers, provided the error is strictly below 1/2, and carries are then propagated to give the exact binary product.
- Integer multiplication in O(n(lg n)^(1-κ)) time: A deterministic multitape Turing machine that multiplies two n-bit integers exactly in O(n(lg n)^(1-κ)) worst-case time for a fixed κ = 2^(-182) > 0, beating the n log n conjecture in this model.

## Other pages you may link to

- [Schönhage–Strassen n log n conjecture](nlogn-conjecture.md)
- [Harvey–van der Hoeven O(n log n) multiplication](harvey-hoeven-multiplier.md)
- [Butterfly operation](butterfly-operation.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Multiplication as convolution of digits](convolution-reduction.md)
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

- "These are the synthetic polynomial transforms of Nussbaumer and Quandalle" (paper)

  > Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients. Our starting point is the Gaussian-resampling reduction of Harvey and van der Hoeven \cite{HarveyHoeven2021}: it replaces the Fourier transforms needed for this convolution by multidimensional transforms whose axis lengths are powers of two. After a further conversion to convolution, one coordinate is stored as the coefficient list of a polynomial modulo $y^r+1$, with $r$ a power of two. Powers of $y$ then serve as roots of unity in the remaining axes, and multiplication by such a root is a signed shift of the coefficient list. These are the synthetic polynomial transforms of Nussbaumer and Quandalle and Nussbaumer~\cite{NussbaumerQuandalle1978,Nussbaumer1980}.


## Sources (read from disk as needed)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- $x$ means input sequence here, but formal variable on [Discrete Fourier transform](fourier-transform.md), which this page builds on: On synthetic-transform, the input sequence x clashes with the formal variable x of the Fourier and cyclic convolution pages. Use another letter for the input sequence (e.g. u).
- $x$ means input sequence here, but formal variable on [Cyclic convolution](cyclic-convolution.md), which this page builds on: On synthetic-transform, the input sequence x clashes with the formal variable x of cyclic-convolution. Use another letter for the input sequence (e.g. u).

## Previous version (revise it)

It has 387 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 483 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

A synthetic polynomial transform generalizes the [discrete Fourier transform](fourier-transform.md) to a polynomial ring whose roots of unity are powers of $y$. It transforms the cyclic convolution that a multiplication of digits reduces to, and each of its stages needs only signed shifts and additions.

It works in the [polynomial ring modulo yʳ + 1](polynomial-ring-y.md). It is built on $y$ as a [primitive root of unity](roots-of-unity.md) of order $2r$: $y^r=-1$, so $y^{2r}=1$, and no smaller positive power of $y$ equals $1$.

Let $x_0,\dots,x_{2r-1}$ be a sequence of ring elements; here $x$ names a sequence, not the formal variable of earlier pages. Let $t$ be the input position and $s$ the frequency index, $s=0,\dots,2r-1$. Its transform has entries $\hat x_s=\sum_{t=0}^{2r-1} y^{st}x_t$.

Split the inputs into the halves $t<r$ and $t+r$. Write $i$ for the index of the pair of frequencies $2i$ and $2i+1$, so $i$ runs over $0,\dots,r-1$. Since $y^{s(t+r)}=(-1)^s y^{st}$ (because $y^r=-1$), we get $\hat x_{2i}=\sum_{t<r} y^{2it}(x_t+x_{t+r})$ and $\hat x_{2i+1}=\sum_{t<r} y^{2it}\,y^t(x_t-x_{t+r})$. One stage therefore forms, for each pair $(x_t,x_{t+r})$, the sum and the difference times the twiddle factor $y^t$, the power of $y$ that multiplies that difference. The even and odd entries are then transforms of length $r$ of these two lists, with root $y^2$.

Multiplying by a power of $y$ is a signed shift of the coefficient list <cite data-source="paper">multiplication by such a root is a signed shift of the coefficient list</cite>. So each stage needs only signed shifts and butterfly additions. For $r=4$, $y^3(1+2y)=y^3+2y^4=-2+y^3$, since $y^4=-1$: the coefficient list $(1,2,0,0)$ becomes $(-2,0,0,1)$.

The inverse is $x_t=\frac{1}{2r}\sum_{s=0}^{2r-1} y^{-st}\hat x_s$, with $y^{-1}=y^{2r-1}$. This holds because $\sum_{s=0}^{2r-1} y^{su}$ equals $2r$ when $u\equiv 0 \pmod{2r}$ and $0$ otherwise, where $u$ is an integer exponent of $y$ (here $u$ does not denote the butterfly input of earlier pages). Since $r$ is a power of two, $y^r+1$ has $r$ distinct roots, all primitive $2r$-th roots of unity. A ring element of degree below $r$ that vanishes at all of them is zero, and at each root the sum is an ordinary geometric sum, which vanishes when the root's $u$-th power is not $1$.

Both forward transforms use the same index convention, so their outputs share the frequency order $s=0,\dots,2r-1$. Let $z_0,\dots,z_{2r-1}$ be a second sequence of ring elements, with transform $\hat z_s=\sum_{q=0}^{2r-1} y^{sq}z_q$, where $q$ is the input position in $z$. The entrywise products $\hat x_s\hat z_s$ therefore pair equal frequencies, and the inverse reads them in that order.

Expanding, $\hat x_s\hat z_s=\sum_{t,q} y^{s(t+q)}x_tz_q$. Let $x\ast z$ be the cyclic convolution of $x$ and $z$, with entries $(x\ast z)_h=\sum_{t+q\equiv h \pmod{2r}} x_tz_q$, where $h$ is the output position. Since $y^{2r}=1$, the exponent depends only on $h\equiv t+q \pmod{2r}$, so $\hat x_s\hat z_s=\sum_h y^{sh}(x\ast z)_h$. The inverse transform therefore returns $x\ast z$: transforms turn entrywise products into a cyclic convolution.

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

Write the body to `exegenius/tasks/0161-write-synthetic-transform.answer.md` and the JSON to `exegenius/tasks/0161-write-synthetic-transform.answer.json`, then run `exegenius submit 0161-write-synthetic-transform` in the project directory. If submit rejects the answer, fix the answer and submit again.
