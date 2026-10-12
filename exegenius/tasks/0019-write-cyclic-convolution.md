# exegenius task 0019-write-cyclic-convolution

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

For these sources: The reader has completed an undergraduate computer science degree, so they know big-O and related asymptotic notation, polynomials, complex numbers (roots of unity, polar form), and Turing machines with tapes. They also know the discrete mathematics and first linear algebra that every such degree teaches: modular arithmetic, gcd and primes, sets, permutations, binary and radix notation, XOR over GF(2), induction, recurrences and geometric sums, and vector spaces, matrices and Gaussian elimination over a field, with basic sorting. They have not met the Chinese remainder theorem, the FFT, tensor products, bilinear forms, Gaussian integers, prime-number estimates, or operator norms and Neumann series.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes (also: multitape Turing machine)
- Exact integer multiplication
- Radix-digit convolution
- Discrete Fourier transform (also: normalized Fourier transform)
- Gaussian resampling (also: Harvey–van der Hoeven resampling)
- Big-Theta, big-Omega and little-o notation (also: Theta notation, Omega notation, little-o, asymptotic tight bound, asymptotic lower bound, Θ, Ω, o-notation)
- Logarithms (also: log, log2, binary logarithm, lg, natural logarithm, ln, change of base)
- Floor and ceiling (also: integer part, floor function, ceiling function, round down, round up)
- Mathematical induction (also: induction, proof by induction, strong induction, inductive step)
- Recurrence relations (also: recurrence, recursive inequality, unrolling a recurrence, divide-and-conquer recurrence)
- Geometric series (also: geometric sum, finite geometric sum, geometric progression)
- Sets, intersections and indicator vectors (also: set intersection, intersection size, indicator vector, characteristic vector, k-subsets, three-element subsets)
- Permutations (also: bijection of a finite set, reordering, permutation of coordinates, cyclic shift)
- Lexicographic order (also: dictionary order, lexicographic order on tuples, lexicographic order)
- Positional (radix) notation (also: radix representation, base-b expansion, binary representation, mixed-radix representation, digits, bits, binary string)
- Hamming weight (also: popcount, number of ones, population count, weight of a binary string)
- Two's complement and signed binary (also: twos complement, signed binary numbers, sign extension, sign bit)
- Fixed-point binary numbers (also: fixed-point arithmetic, binary point, fractional bits, guard bits, fixed-width arithmetic)
- Modular arithmetic (also: congruence, congruent modulo n, integers modulo n, Z/nZ, residues, modulo, modular inverse)
- Greatest common divisor and coprimality (also: gcd, coprime, relatively prime, pairwise coprime, Euclid's algorithm, Euclidean algorithm)
- Prime numbers (also: primes, prime factorization, trial division, primality)
- Binary field GF(2) and XOR (also: F2, GF(2), binary field, XOR, exclusive or, addition modulo 2, parity)
- Roots of unity (also: n-th roots of unity, primitive root of unity, primitive n-th root of unity, omega)
- Polar form and Euler's formula (also: modulus and argument, Euler's identity, complex exponential, complex conjugate, unit circle, argument of a complex number)
- Vector spaces over a field (also: linear space, vector space, subspace, span, basis, dimension, linear independence, field)
- Matrices, rank and invertibility (also: matrix inverse, invertible matrix, nonsingular matrix, rank, identity matrix, matrix product, linear map, linear transformation)
- Gaussian elimination and triangular factorization (also: row reduction, elementary row operations, pivot, lower triangular matrix, upper triangular matrix, LU decomposition)
- Eigenvalues and eigenvectors (also: eigenvalue, eigenvector, characteristic polynomial, spectrum)
- Newton's method (also: Newton iteration, Newton-Raphson method, Newton's root-finding method)
- Stable sorting and radix sort (also: stable sort, stable sorting, radix sort, least-significant-digit radix sort, LSD radix sort, counting sort)

## This page

Concept: Cyclic convolution
Gloss: The product of two sequences in which indices wrap around modulo the sequence length.

## This page in the argument

The step: The retained source permutation cancels: $RF_s^{+}R(F_su\cdot F_sv)=(u\ast v)/S^2$ with $S=\prod_i s_i$.
How: use that the permutation is its own inverse against the opposite transform, commute it through pointwise products, then apply the normalized convolution rule
Why: A coordinate permutation commutes with pointwise products, and the normalized convolution rule turns the product of transforms into a convolution. (the sources leave this for the reader to work out: spell it out)
Striking feature: the permutation $R$ disappears exactly, leaving no residual reordering of the convolution (explain why it holds, from the method)

Its sub-steps, in order:

- $F_s^{+}R=R^{-1}F_s^{+}$, hence $RF_s^{+}R=F_s^{+}$.
- $(RF_su)\cdot(RF_sv)=R(F_su\cdot F_sv)$, since a permutation commutes with pointwise products.
- $F_s(u\ast v)=S(F_su)\cdot(F_sv)$ and $F_s^{+}F_s=I/S$, the normalized convolution rule.

It serves these steps, from the main result down:

- With both coordinate permutations kept in the formula, $P_sF_s = 2^{2\alpha^2}B_0P_tF_tA$, and the retained source permutation cancels across a convolution, so no sort is executed.; how: keep the permutations in the Gaussian resampling identity, then cancel the source permutation through the convolution (on [Transform identity with retained permutations](transform-identity.md))

## Symbols already bound on earlier pages

The symbols in the names of the concepts the reader knows are listed with those concepts above.

- $n$ (input length), bound on [Exact integer multiplication](exact-integer-multiplication.md): The number of bits in each input, so each input has $n$ bits.
- $x$ (first input), bound on [Exact integer multiplication](exact-integer-multiplication.md): A binary string of length $n$, the first of the two inputs.
- $y$ (second input), bound on [Exact integer multiplication](exact-integer-multiplication.md): A binary string of length $n$, the second of the two inputs.
- $\mathrm{val}$ (integer value), bound on [Exact integer multiplication](exact-integer-multiplication.md): The nonnegative integer value of a binary string, with the leftmost bit most significant.
- $k$ (padded width), bound on [Exact integer multiplication](exact-integer-multiplication.md): The number of bits of the padded binary representation.
- $z$ (integer to represent), bound on [Exact integer multiplication](exact-integer-multiplication.md): The integer whose padded binary representation is taken, with $0 \le z < 2^k$.
- $\mathrm{bin}_k$ (padded binary representation), bound on [Exact integer multiplication](exact-integer-multiplication.md): The binary representation of $z$ padded on the left with zeros to exactly $k$ bits.
- $B$ (radix), bound on [Radix-digit convolution](radix-digit-convolution.md): The base of the digit expansion, an integer at least 2.
- $x$ (first input), bound on [Radix-digit convolution](radix-digit-convolution.md): The first integer to multiply.
- $y$ (second input), bound on [Radix-digit convolution](radix-digit-convolution.md): The second integer to multiply.
- $d$ (digit count), bound on [Radix-digit convolution](radix-digit-convolution.md): The number of radix-B digits of each input, a count.
- $x_i$ (digit of x), bound on [Radix-digit convolution](radix-digit-convolution.md): The i-th radix-B digit of x, counting from the least significant digit.
- $y_j$ (digit of y), bound on [Radix-digit convolution](radix-digit-convolution.md): The j-th radix-B digit of y, counting from the least significant digit.
- $u$ (digit vector of x), bound on [Radix-digit convolution](radix-digit-convolution.md): The vector (x_0, ..., x_{d-1}) of the digits of x.
- $v$ (digit vector of y), bound on [Radix-digit convolution](radix-digit-convolution.md): The vector (y_0, ..., y_{d-1}) of the digits of y.
- $u\ast v$ (convolution of digit vectors), bound on [Radix-digit convolution](radix-digit-convolution.md): The convolution of u and v, whose m-th entry is the sum of u_i v_j over i+j=m.
- $q$ (transform length), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The number of complex entries in the vector the transform acts on, a count of entries.
- $\omega$ (primitive root of unity), bound on [Discrete Fourier transform](discrete-fourier-transform.md): A primitive $q$-th root of unity, a complex number whose powers $\omega^0, \dots, \omega^{q-1}$ are all distinct and whose $q$-th power is 1.
- $a$ (input vector), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The input vector $(a_0, \dots, a_{q-1})$ of $q$ complex numbers that the transform maps.
- $s$ (source length), bound on [Gaussian resampling](gaussian-resampling.md): The number of coordinates of a source vector.
- $t$ (target length), bound on [Gaussian resampling](gaussian-resampling.md): The number of coordinates of a target vector, with s < t and gcd(s,t) = 1.
- $\alpha$ (Gaussian width parameter), bound on [Gaussian resampling](gaussian-resampling.md): The integer width parameter of the Gaussian weights.
- $F_s$ (normalized Fourier transform), bound on [Gaussian resampling](gaussian-resampling.md): The normalized Fourier transform of length s.
- $F_t$ (normalized Fourier transform), bound on [Gaussian resampling](gaussian-resampling.md): The normalized Fourier transform of length t.
- $P_s$ (source coordinate permutation), bound on [Gaussian resampling](gaussian-resampling.md): The coordinate permutation of length-s vectors given by (P_s u)_j = u_{tj}.
- $P_t$ (target coordinate permutation), bound on [Gaussian resampling](gaussian-resampling.md): The coordinate permutation of length-t vectors given by (P_t v)_k = v_{-sk}.
- $A$ (source-to-target contraction), bound on [Gaussian resampling](gaussian-resampling.md): A linear contraction from vectors of length s to vectors of length t.
- $B_0$ (target-to-source contraction), bound on [Gaussian resampling](gaussian-resampling.md): A linear contraction from vectors of length t to vectors of length s.
- $S$ (Gaussian map S), bound on [Gaussian resampling](gaussian-resampling.md): A Gaussian-weighted map from vectors of length s to vectors of length t.
- $T$ (Gaussian map T), bound on [Gaussian resampling](gaussian-resampling.md): A Gaussian-weighted map from vectors of length s to vectors of length t.
- $D$ (Gaussian diagonal map), bound on [Gaussian resampling](gaussian-resampling.md): The diagonal map on length-s vectors that multiplies coordinate j by a Gaussian factor.
- $C$ (coordinate selection map), bound on [Gaussian resampling](gaussian-resampling.md): The map that selects from a length-t vector the coordinates at the indices nearest tj/s, for each j.
- $N$ (near-identity map), bound on [Gaussian resampling](gaussian-resampling.md): The map CTD, which is close to the identity.

## Pages that build on this one

- Transform identity with retained permutations: The Gaussian resampling identity in which the source and target coordinate permutations are kept as part of the formula, so that they cancel across a convolution instead of being executed as sorts.

## Other pages you may link to

- [Exact integer multiplication](exact-integer-multiplication.md)
- [Radix-digit convolution](radix-digit-convolution.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Transform identity with retained permutations](transform-identity.md)

## Evidence from the sources, with the paragraph around each quote

- "denote cyclic convolution in the displayed axes" (paper)

  > i Z/ti Z with values in Rr , let ∗ denote cyclic convolution in the displayed axes and


## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Length

At most 350 words, not counting mathematics and citations: submit rejects a longer page.

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

Write the body to `exegenius/tasks/0019-write-cyclic-convolution.answer.md` and the JSON to `exegenius/tasks/0019-write-cyclic-convolution.answer.json`, then run `exegenius submit 0019-write-cyclic-convolution` in the project directory. If submit rejects the answer, fix the answer and submit again.
