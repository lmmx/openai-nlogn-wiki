# exegenius task 0036-write-transform-identity

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
- Cyclic convolution
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

Concept: Transform identity with retained permutations
Gloss: The Gaussian resampling identity in which the source and target coordinate permutations are kept as part of the formula, so that they cancel across a convolution instead of being executed as sorts.

## This page in the argument

The step: With both coordinate permutations kept in the formula, $P_sF_s = 2^{2\alpha^2}B_0P_tF_tA$, and the retained source permutation cancels across a convolution, so no sort is executed.
How: keep the permutations in the Gaussian resampling identity, then cancel the source permutation through the convolution
Why: Keeping the permutations in the formula lets the two sorts disappear instead of being executed as full passes over each coordinate. (the sources say so: "the source and target coordinate permutations in the transform identity, so they need not be" (paper))

Its sub-steps, in order:

- The one-dimensional Gaussian resampling identity $P_sF_s = 2^{2\alpha^2}B_0P_tF_tA$ holds with contractions $A$ and $B_0$. (on [Gaussian resampling](gaussian-resampling.md))
- The retained source permutation cancels: $RF_s^{+}R(F_su\cdot F_sv)=(u\ast v)/S^2$ with $S=\prod_i s_i$. (on [Cyclic convolution](cyclic-convolution.md))

## Symbols already bound on earlier pages

The symbols in the names of the concepts the reader knows are listed with those concepts above.

- $x$ (first input), bound on [Exact integer multiplication](exact-integer-multiplication.md): A binary string of length n, the first of the two inputs.
- $y$ (second input), bound on [Exact integer multiplication](exact-integer-multiplication.md): A binary string of length n, the second of the two inputs.
- $n$ (input bit count), bound on [Exact integer multiplication](exact-integer-multiplication.md): The number of bits in each input string.
- $\mathrm{val}$ (value function), bound on [Exact integer multiplication](exact-integer-multiplication.md): The function mapping a binary string to its nonnegative integer value, with the leftmost bit most significant.
- $k$ (padded bit width), bound on [Exact integer multiplication](exact-integer-multiplication.md): The number of bits of the padded binary representation.
- $z$ (integer to encode), bound on [Exact integer multiplication](exact-integer-multiplication.md): An integer with 0 at most z and z less than 2 to the power k, which is encoded by bin_k.
- $\mathrm{bin}_k$ (padded binary representation), bound on [Exact integer multiplication](exact-integer-multiplication.md): The function giving the binary representation of an integer z, padded on the left with zeros to exactly k bits.
- $B$ (radix), bound on [Radix-digit convolution](radix-digit-convolution.md): The base of the digit expansion, an integer at least 2.
- $x$ (first input), bound on [Radix-digit convolution](radix-digit-convolution.md): The first integer to multiply.
- $y$ (second input), bound on [Radix-digit convolution](radix-digit-convolution.md): The second integer to multiply.
- $d$ (digit count), bound on [Radix-digit convolution](radix-digit-convolution.md): The number of radix-B digits of each input, a count.
- $x_i$ (digit of x), bound on [Radix-digit convolution](radix-digit-convolution.md): The i-th radix-B digit of x, counting from the least significant digit.
- $y_j$ (digit of y), bound on [Radix-digit convolution](radix-digit-convolution.md): The j-th radix-B digit of y, counting from the least significant digit.
- $u$ (digit vector of x), bound on [Radix-digit convolution](radix-digit-convolution.md): The vector (x_0, ..., x_{d-1}) of the digits of x.
- $v$ (digit vector of y), bound on [Radix-digit convolution](radix-digit-convolution.md): The vector (y_0, ..., y_{d-1}) of the digits of y.
- $u\ast v$ (convolution of digit vectors), bound on [Radix-digit convolution](radix-digit-convolution.md): The convolution of u and v, whose m-th entry is the sum of u_i v_j over i+j=m.
- $q$ (entry count), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The number of entries in the input vector, a count.
- $\omega$ (primitive root of unity), bound on [Discrete Fourier transform](discrete-fourier-transform.md): A primitive q-th root of unity, whose powers weight the entries in the transform.
- $a$ (input vector), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The list of q complex input entries a_0 through a_{q-1}.
- $\hat a$ (transformed vector), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The discrete Fourier transform of a, a list of q entries.
- $j$ (input index), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The index of an input entry, running over the input positions 0 to q-1.
- $k$ (output index), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The index of an output entry, running over the output positions 0 to q-1; on this page it replaces the padded width.
- $s$ (source length), bound on [Gaussian resampling](gaussian-resampling.md): The number of coordinates of a source vector.
- $t$ (target length), bound on [Gaussian resampling](gaussian-resampling.md): The number of coordinates of a target vector.
- $\alpha$ (Gaussian width), bound on [Gaussian resampling](gaussian-resampling.md): The integer width parameter of the Gaussian weights.
- $F_s$ (source transform), bound on [Gaussian resampling](gaussian-resampling.md): The normalized Fourier transform of length s.
- $F_t$ (target transform), bound on [Gaussian resampling](gaussian-resampling.md): The normalized Fourier transform of length t.
- $P_s$ (source permutation), bound on [Gaussian resampling](gaussian-resampling.md): The coordinate permutation on vectors of length s, sending g to the vector with j-th entry g_{tj}.
- $P_t$ (target permutation), bound on [Gaussian resampling](gaussian-resampling.md): The coordinate permutation on vectors of length t, sending h to the vector with m-th entry h_{-sm}.
- $g$ (source vector), bound on [Gaussian resampling](gaussian-resampling.md): A vector of length s, the input of P_s.
- $h$ (target vector), bound on [Gaussian resampling](gaussian-resampling.md): A vector of length t, the input of P_t.
- $j$ (coordinate index), bound on [Gaussian resampling](gaussian-resampling.md): An index of a coordinate of a vector.
- $m$ (target coordinate index), bound on [Gaussian resampling](gaussian-resampling.md): An index of a coordinate of a target-length vector.
- $I$ (identity map), bound on [Gaussian resampling](gaussian-resampling.md): The identity map, which leaves every vector unchanged.
- $S$ (source Gaussian map), bound on [Gaussian resampling](gaussian-resampling.md): A Gaussian-weighted map from vectors of length s to vectors of length t.
- $T$ (target Gaussian map), bound on [Gaussian resampling](gaussian-resampling.md): A Gaussian-weighted map from vectors of length s to vectors of length t.
- $D$ (Gaussian diagonal map), bound on [Gaussian resampling](gaussian-resampling.md): The diagonal map on vectors of length s that multiplies coordinate j by a Gaussian factor.
- $C$ (selection map), bound on [Gaussian resampling](gaussian-resampling.md): The map from vectors of length t to vectors of length s that selects the coordinates at the indices nearest tj/s.
- $N$ (near-identity map), bound on [Gaussian resampling](gaussian-resampling.md): The map CTD from vectors of length s to themselves, which is close to the identity.
- $r$ (series index), bound on [Gaussian resampling](gaussian-resampling.md): The summation index of the Neumann series for N inverse.
- $A$ (scaled source map), bound on [Gaussian resampling](gaussian-resampling.md): The map S/2, a contraction from vectors of length s to vectors of length t.
- $B_0$ (scaled inverse map), bound on [Gaussian resampling](gaussian-resampling.md): The map 2^{-(2 alpha^2-2)} D N^{-1} C / 2, a contraction from vectors of length t to vectors of length s.
- $\ast$ (cyclic convolution), bound on [Cyclic convolution](cyclic-convolution.md): The cyclic convolution of two vectors of equal length, whose indices wrap around modulo the length.
- $i$ (entry index), bound on [Cyclic convolution](cyclic-convolution.md): An index of a vector entry, an element of $\mathbb{Z}/s\mathbb{Z}$.
- $j$ (entry index), bound on [Cyclic convolution](cyclic-convolution.md): A second index of a vector entry, an element of $\mathbb{Z}/s\mathbb{Z}$.
- $m$ (output index), bound on [Cyclic convolution](cyclic-convolution.md): The index of an entry of the cyclic convolution, an element of $\mathbb{Z}/s\mathbb{Z}$.
- $S$ (entry count), bound on [Cyclic convolution](cyclic-convolution.md): The number of entries of an array indexed by the axes $s_1,\dots,s_d$, namely $s_1 s_2\cdots s_d$.
- $R$ (retained source permutation), bound on [Cyclic convolution](cyclic-convolution.md): The coordinate permutation of the source vectors that is kept in the formula and cancels across the convolution.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Gaussian resampling](gaussian-resampling.md): A technique that replaces a Fourier transform of arbitrary length by transforms whose axis lengths are powers of two, using Gaussian weights to move between the two sets of frequencies.
  Shown as: Transform identity with retained permutations *<predicate>* Gaussian resampling
- [Cyclic convolution](cyclic-convolution.md): The product of two sequences in which indices wrap around modulo the sequence length.
  Shown as: Transform identity with retained permutations *<predicate>* Cyclic convolution

## Other pages you may link to

- [Exact integer multiplication](exact-integer-multiplication.md)
- [Radix-digit convolution](radix-digit-convolution.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)

## Evidence from the sources, with the paragraph around each quote

- "We retain both permutations in the transform formula" (paper)

  > The transform lengths needed for the integer product are pairwise coprime, whereas the synthetic transforms use powers of two. Gaussian resampling connects these two shapes. Its usual implementation sorts twice on each coordinate. We retain both permutations in the transform formula and compute that formula directly. This section proves the resulting interface, including its tape cost when the number of coordinates grows. For an integer q ≥ 1, write q−1


## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- $g$ means second source-box array here, but source vector on [Gaussian resampling](gaussian-resampling.md), which this page builds on: g here is a vector of length s (the input of P_s), not the multi-dimensional array over the source box of transform-identity. Use another letter for the length-s source vector on gaussian-resampling, or state explicitly that g there is a length-s vector and not the box array of the earlier page.

## Previous version (revise it)

It has 249 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 311 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

Transform identity with retained permutations is the form of the identity from [Gaussian resampling](gaussian-resampling.md) that keeps the source and target coordinate permutations inside the formula instead of executing them as sorts. On the way to exact integer multiplication, its job is to let the source permutation cancel across a convolution.

The identity rests on [Gaussian resampling](gaussian-resampling.md): its one-dimensional form $P_sF_s = 2^{2\alpha^2}B_0P_tF_tA$ holds with linear contractions $A$ and $B_0$. A contraction is a linear map that does not increase the norm, a measure of a vector's length.

The usual implementation sorts twice on each coordinate. Keeping both permutations in the formula means those sorts are never executed. <cite data-source="paper">We retain both permutations in the transform formula</cite>.

The cancellation concerns the source side alone: the retained source permutation cancels across a [cyclic convolution](cyclic-convolution.md). Let $R$ be the source permutation $P_s$ applied along every source axis, and let $F_s^{+}$ be the opposite transform, the transform with the sign of its roots of unity reversed. Let $f$ and $g$ be arrays indexed by the source box, which has $M=\prod_i s_i$ entries, where $s_i$ is the length of source axis $i$. Writing $\cdot$ for coordinatewise multiplication and $\ast$ for cyclic convolution on the box,
$$RF_s^{+}R\bigl(F_sf\cdot F_sg\bigr)=\frac{f\ast g}{M^2}.$$

Each $t_i$ is a unit modulo $s_i$ because $\gcd(s,t)=1$, so $RF_s^{+}R=F_s^{+}$. Since $R$ commutes with pointwise products, the left side is $F_s^{+}(F_sf\cdot F_sg)$. The normalizations give $F_s^{+}F_s=I/M$, where $I$ is the identity map on the box, and $F_s(f\ast g)=M\,(F_sf)\cdot(F_sg)$. Hence $F_s^{+}(F_sf\cdot F_sg)=(f\ast g)/M^2$.

So the retained permutation is undone inside the opposite transform, and the product of two retained transforms yields the convolution directly, scaled by $1/M^2$. No sort is needed to bring the result into natural order.

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

Write the body to `exegenius/tasks/0036-write-transform-identity.answer.md` and the JSON to `exegenius/tasks/0036-write-transform-identity.answer.json`, then run `exegenius submit 0036-write-transform-identity` in the project directory. If submit rejects the answer, fix the answer and submit again.
