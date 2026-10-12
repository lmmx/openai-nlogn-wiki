# exegenius task 0057-write-polynomial-ring-y

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

Concept: Polynomial ring modulo yʳ + 1
Gloss: The ring of complex polynomials in y reduced modulo y^r + 1, where multiplying by a power of y is a signed cyclic shift of the coefficient list.
Also called: negacyclic ring, signed shift
Heading: Polynomial ring modulo $y^r + 1$

The symbols in this page's heading denote (say so on the page):

- $y$ (ring indeterminate): The variable of the polynomial ring whose powers serve as roots of unity in the remaining axes.
- $r$ (coefficient count): The number of coefficients in the coefficient list of one polynomial record, a power of two.

## This page in the argument

The step: The last cyclic coordinate becomes a polynomial modulo $y^r+1$, so that its wrap is a signed shift.
How: apply a phase twist to the last cyclic coordinate
Why: Multiplying by a power of $y$ is a signed cyclic shift, so the twisted coordinate needs no general multiplication. (the sources leave this for the reader to work out: spell it out)

Its sub-steps, in order:

- A phase twist changes the last cyclic coordinate into a polynomial modulo $y^r+1$.

It serves these steps, from the main result down:

- Two $n$-bit integers can be multiplied exactly in $O(n(\lg n)^{1-\kappa})$ worst-case time on a deterministic multitape Turing machine, for a fixed $\kappa=2^{-182}$.; how: reduce the product to a digit convolution, compute that convolution through transform layers whose tape cost saves a power, and recover the exact product by rounding (on [Integer multiplication in O(n(lg n)^(1-κ)) time](integer-multiplication-target.md))

## Symbols already bound on earlier pages

The symbols in the names of the concepts the reader knows are listed with those concepts above.

- $n$ (input bit length), bound on [Schönhage–Strassen n log n conjecture](nlogn-conjecture.md): The number of bits in each input integer; the count of bits of each of the two integers being multiplied.
- $n$ (input length), bound on [Harvey–van der Hoeven O(n log n) multiplication](harvey-hoeven-multiplier.md): The number of bits in each input integer.
- $n$ (root order), bound on [Primitive roots of unity](roots-of-unity.md): A positive integer, the order of the root of unity.
- $\omega$ (primitive root), bound on [Primitive roots of unity](roots-of-unity.md): A complex number that is a primitive $n$-th root of unity.
- $k$ (power index), bound on [Primitive roots of unity](roots-of-unity.md): An integer exponent, the power of $\omega$ being tested against 1.
- $n$ (sequence length), bound on [Discrete Fourier transform](fourier-transform.md): The number of entries in the input sequence, which is also the number of output values.
- $a$ (input sequence), bound on [Discrete Fourier transform](fourier-transform.md): The length-$n$ list of complex numbers that the transform is applied to.
- $\omega$ (primitive root), bound on [Discrete Fourier transform](fourier-transform.md): A primitive n-th root of unity, whose powers give the points at which the transform evaluates.
- $\hat{a}$ (output sequence), bound on [Discrete Fourier transform](fourier-transform.md): The discrete Fourier transform of the input sequence, a list of n values.
- $j$ (input index), bound on [Discrete Fourier transform](fourier-transform.md): An index of an input entry, running from 0 to n-1.
- $k$ (output index), bound on [Discrete Fourier transform](fourier-transform.md): An index of an output entry, running from 0 to n-1.
- $H_0$ (two-point butterfly), bound on [Butterfly operation](butterfly-operation.md): The map sending a pair of values to its scaled sum and scaled difference.
- $u$ (first input value), bound on [Butterfly operation](butterfly-operation.md): The first of the two input values of the butterfly.
- $v$ (second input value), bound on [Butterfly operation](butterfly-operation.md): The second of the two input values of the butterfly.
- $r$ (sequence length), bound on [Cyclic convolution](cyclic-convolution.md): The number of complex coefficients in each sequence being convolved.
- $a$ (first sequence), bound on [Cyclic convolution](cyclic-convolution.md): The first input sequence, a list of r complex coefficients a_0 through a_{r-1}.
- $b$ (second sequence), bound on [Cyclic convolution](cyclic-convolution.md): The second input sequence, a list of r complex coefficients b_0 through b_{r-1}.
- $c$ (cyclic convolution), bound on [Cyclic convolution](cyclic-convolution.md): The cyclic convolution of a and b, a sequence of length r.
- $k$ (output index), bound on [Cyclic convolution](cyclic-convolution.md): The index of an output coefficient of the cyclic convolution, running from 0 to r-1.
- $j$ (summation index), bound on [Cyclic convolution](cyclic-convolution.md): The index of a term in the sum for one output coefficient, running from 0 to r-1.
- $x$ (formal variable), bound on [Cyclic convolution](cyclic-convolution.md): A formal variable (indeterminate) used to write the sequences as polynomials; it is not evaluated at any number.
- $b$ (digit width), bound on [Multiplication as convolution of digits](convolution-reduction.md): The number of bits in one digit, so that digits are taken in radix $2^b$.
- $m$ (digits per input), bound on [Multiplication as convolution of digits](convolution-reduction.md): The number of radix-$2^b$ digits in each input.
- $u$ (first input), bound on [Multiplication as convolution of digits](convolution-reduction.md): The first of the two integers being multiplied.
- $v$ (second input), bound on [Multiplication as convolution of digits](convolution-reduction.md): The second of the two integers being multiplied.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Cyclic convolution](cyclic-convolution.md): The product of two sequences in which indices are taken modulo a fixed length, so each coefficient of the result is a sum of products over residues.
  Shown as: Polynomial ring modulo yʳ + 1 *<predicate>* Cyclic convolution

## Pages that build on this one

- Synthetic polynomial transform: A transform over a polynomial ring in which the roots of unity are powers of y, so that each transform stage uses only signed shifts and butterfly additions.
- Signed Kronecker packing: Encoding a polynomial with bounded signed coefficients as an integer by evaluating it at a large power of two, so that polynomial products become integer products.
- Integer multiplication in O(n(lg n)^(1-κ)) time: A deterministic multitape Turing machine that multiplies two n-bit integers exactly in O(n(lg n)^(1-κ)) worst-case time for a fixed κ = 2^(-182) > 0, beating the n log n conjecture in this model.

## Other pages you may link to

- [Schönhage–Strassen n log n conjecture](nlogn-conjecture.md)
- [Harvey–van der Hoeven O(n log n) multiplication](harvey-hoeven-multiplier.md)
- [Primitive roots of unity](roots-of-unity.md)
- [Discrete Fourier transform](fourier-transform.md)
- [Butterfly operation](butterfly-operation.md)
- [Multiplication as convolution of digits](convolution-reduction.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Signed Kronecker packing](kronecker-packing.md)
- [Matrix rank](matrix-rank.md)
- [Linear network with restored auxiliary values](linear-network-exchange.md)
- [Lower-triangular factorization](lower-triangular-factorization.md)
- [Address shear](address-shear.md)
- [Fast address interchange](address-interchange.md)
- [Chinese-remainder address map](chinese-remainder-address-map.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein's chirp identity](bluestein-chirp.md)
- [Tensor product](tensor-product.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Recursive power saving](recursive-power-saving.md)
- [Exact recovery by rounding](rounding-recovery.md)
- [Integer multiplication in O(n(lg n)^(1-κ)) time](integer-multiplication-target.md)

## Evidence from the sources, with the paragraph around each quote

- "one coordinate is stored as the coefficient list of a polynomial modulo $y^r+1$" (paper)

  > Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients. Our starting point is the Gaussian-resampling reduction of Harvey and van der Hoeven \cite{HarveyHoeven2021}: it replaces the Fourier transforms needed for this convolution by multidimensional transforms whose axis lengths are powers of two. After a further conversion to convolution, one coordinate is stored as the coefficient list of a polynomial modulo $y^r+1$, with $r$ a power of two. Powers of $y$ then serve as roots of unity in the remaining axes, and multiplication by such a root is a signed shift of the coefficient list. These are the synthetic polynomial transforms of Nussbaumer and Quandalle and Nussbaumer~\cite{NussbaumerQuandalle1978,Nussbaumer1980}.


## Sources (read from disk as needed)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The reader cannot follow this step: "The step applies a phase twist to the last cyclic coordinate, which makes that coordinate a polynomial modulo $y^r+1$." (The page asserts that the twist turns the coordinate into a polynomial modulo y^r+1 but never shows how a twist by roots of unity produces that reduction rule, so the reader cannot check it.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "Multiplication by a power of $y$ is therefore a signed cyclic shift (cited), so the twisted coordinate needs no general multiplication." (The worked example shows only one multiplication by y. The page generalises it to every power of y and draws the conclusion about the twisted coordinate without showing how that follows. The cited claim is also the basis of the step, and the page does not say how it applies to the twisted coordinate.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- Explain "last cyclic coordinate of the transform" in a sentence where it is first used.
- Explain "phase twist" in a sentence where it is first used.

## Previous version (revise it)

It has 260 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 325 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

Here $y$ is the variable of the ring, whose powers serve as roots of unity in the remaining axes. $r$ is the number of coefficients in the coefficient list of one polynomial record, a power of two.

The polynomial ring modulo $y^r+1$ is the set of complex polynomials in $y$ in which $y^r$ is replaced by $-1$, so each element is stored as its list of $r$ complex coefficients, from degree $0$ up to degree $r-1$. It is where the last cyclic coordinate of the transform is stored, so that wrap-around in that coordinate becomes a sign change rather than a general multiplication.

Adding two elements adds their coefficient lists entrywise. Multiplying them takes the ordinary polynomial product and then uses $y^r=-1$ to rewrite every power of $y$ of degree $r$ or more as a negated lower power. In this ring, products are computed by a signed form of [Cyclic convolution](cyclic-convolution.md): the coefficient lists are convolved, and any term that wraps past index $r-1$ returns with a minus sign.

Take $r=4$ and the polynomial $1+2y+3y^2+4y^3$, stored as $(1,2,3,4)$. Multiplying by $y$ gives $y+2y^2+3y^3+4y^4$, and since $y^4=-1$ this equals $-4+y+2y^2+3y^3$. So $(1,2,3,4)$ becomes $(-4,1,2,3)$: each entry moves up one place, and the entry that wraps round is negated.

The step applies a phase twist to the last cyclic coordinate, which makes that coordinate a polynomial modulo $y^r+1$. Its method rests on the example: multiplying by a power of $y$ moves the coefficient list up by that many places, and each entry that wraps round comes back negated. Multiplication by a power of $y$ is therefore a signed cyclic shift <cite data-source="paper">multiplication by such a root is a signed shift of the coefficient list</cite>, so the twisted coordinate needs no general multiplication.

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

Write the body to `exegenius/tasks/0057-write-polynomial-ring-y.answer.md` and the JSON to `exegenius/tasks/0057-write-polynomial-ring-y.answer.json`, then run `exegenius submit 0057-write-polynomial-ring-y` in the project directory. If submit rejects the answer, fix the answer and submit again.
