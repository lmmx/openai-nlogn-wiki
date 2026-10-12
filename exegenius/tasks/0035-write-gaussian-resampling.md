# exegenius task 0035-write-gaussian-resampling

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

Concept: Gaussian resampling
Gloss: A technique that replaces a Fourier transform of arbitrary length by transforms whose axis lengths are powers of two, using Gaussian weights to move between the two sets of frequencies.
Also called: Harvey–van der Hoeven resampling

## This page in the argument

The step: The one-dimensional Gaussian resampling identity $P_sF_s = 2^{2\alpha^2}B_0P_tF_tA$ holds with contractions $A$ and $B_0$.
How: resample Fourier transform through Gaussian weights onto the other length, invert the near-identity factor by a Neumann series, and absorb the normalizations
Why: The source transform length and the target length are coprime, so the Fourier transform of one length must be moved onto the power-of-two frequencies of the other; Gaussian weights move between the two sets of frequencies. (the sources say so: "Gaussian resampling connects these two shapes." (paper))
Striking feature: the factors $A$ and $B_0$ are contractions, with norm below one, for all admissible $s<t$ and $\alpha$ (explain why it holds, from the method)

Its sub-steps, in order:

- $TP_sF_s = P_tF_tS$, the Gaussian resampling identity before normalization.
- $\|N-I\|<1/2$, so $N$ is invertible.
- $DN^{-1}CP_tF_tS = P_sF_s$, using the left inverse of $CT$.
- $B_0P_tF_tA = 2^{-2\alpha^2}P_sF_s$, after the normalizations of $A$, $B_0$ are absorbed.

It serves these steps, from the main result down:

- With both coordinate permutations kept in the formula, $P_sF_s = 2^{2\alpha^2}B_0P_tF_tA$, and the retained source permutation cancels across a convolution, so no sort is executed.; how: keep the permutations in the Gaussian resampling identity, then cancel the source permutation through the convolution (on [Transform identity with retained permutations](transform-identity.md))

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

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Discrete Fourier transform](discrete-fourier-transform.md): The map sending a vector of q values to its q values weighted by powers of a q-th root of unity, normalized by 1/q.
  Shown as: Gaussian resampling *<predicate>* Discrete Fourier transform
- [Radix-digit convolution](radix-digit-convolution.md): Writing both integers as polynomials in a power of two whose coefficients are their digits, so that their product is a polynomial convolution of short coefficients.
  Shown as: Gaussian resampling *<predicate>* Radix-digit convolution

## Pages that build on this one

- Transform identity with retained permutations: The Gaussian resampling identity in which the source and target coordinate permutations are kept as part of the formula, so that they cancel across a convolution instead of being executed as sorts.

## Other pages you may link to

- [Exact integer multiplication](exact-integer-multiplication.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Transform identity with retained permutations](transform-identity.md)

## Evidence from the sources, with the paragraph around each quote

- "it replaces the Fourier transforms needed for this convolution by multidimensional transforms whose" (paper)

  > Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients. Our starting point is the Gaussian-resampling reduction of Harvey and van der Hoeven [15]: it replaces the Fourier transforms needed for this convolution by multidimensional transforms whose axis lengths are powers of two. After a further conversion to convolution, one coordinate is stored as the coefficient list of a polynomial modulo y r + 1, with r a power of two. Powers of y then serve as roots of unity in the remaining axes, and multiplication by such a root is a signed shift of the coefficient list. These are the synthetic polynomial transforms of Nussbaumer and Quandalle and Nussbaumer [21, 20]. In this representation, the transform calculation consists of address rearrangements, signed shifts, and two-point butterfly operations. Scanning an array of Θ(n) stored bits at each of Θ(log n) transform levels already costs Θ(n log n). We therefore need savings in both movem


## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The quotation does not support the claim it is attached to (unsupported): "First, $TP_sF_s=P_tF_tS$ holds before normalization, as an exact Gaussian identity" cites "[15, Theorem 4.2 and Lemma 4.6]": The quotation is only a citation to Theorem 4.2 and Lemma 4.6 with no content; it does not state any Gaussian identity relating TP_sF_s to P_tF_tS. Say only what the source supports, or cite the passage that supports the claim.

## Previous version (revise it)

It has 396 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 495 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

Gaussian resampling is a technique that replaces a [Discrete Fourier transform](discrete-fourier-transform.md) of arbitrary length by transforms whose axis lengths are powers of two, which the integer multiplier needs. It moves values between the two sets of frequencies with Gaussian weights, which are exponential factors that decay quadratically with distance.

It replaces the Fourier transforms needed for a [radix-digit convolution](radix-digit-convolution.md) by transforms whose axis lengths are powers of two. The integer product needs pairwise coprime transform lengths, but the synthetic transforms use powers of two. <cite data-source="paper">Gaussian resampling connects these two shapes</cite>.

Here $s$ is the number of coordinates of a source vector, and $t$ is the number of coordinates of a target vector, with $s<t$ and $\gcd(s,t)=1$. The integer $\alpha$ is the width parameter of the Gaussian weights. $F_s$ and $F_t$ are the normalized Fourier transforms of length $s$ and $t$. $P_s$ and $P_t$ are the coordinate permutations $(P_s g)_j=g_{tj}$ and $(P_t h)_m=h_{-sm}$ on vectors $g$ of length $s$ and $h$ of length $t$, with $j$ and $m$ the coordinate indices and subscripts taken modulo the length. $I$ is the identity map.

The operator norm $\|\cdot\|$ of a linear map is the largest factor by which the map stretches a vector, where vectors are measured in the maximum-modulus norm, the largest absolute value of a coordinate. A map is a contraction when its operator norm is at most $1$.

The identity rests on two Gaussian-weighted maps $S$ and $T$ from vectors of length $s$ to vectors of length $t$. $D$ is the diagonal map on vectors of length $s$ that multiplies coordinate $j$ by a Gaussian factor, and $C$ selects from a length-$t$ vector the coordinates at the indices nearest $tj/s$, for $0\le j<s$. Put $N=CTD$, a map close to $I$.

The argument has four steps.

First, $TP_sF_s=P_tF_tS$ holds before normalization, as an exact Gaussian identity <cite data-source="paper">[15, Theorem 4.2 and Lemma 4.6]</cite>.

Second, the source gives $\|N-I\|<1/2$ <cite data-source="paper">∥N − I∥ < 1/2, so N is invertible by the Neumann series</cite>, so $N$ is invertible. Its inverse is the Neumann series $N^{-1}=\sum_{r\ge 0}(I-N)^r$, where $r$ is the summation index. Each term has norm at most $2^{-r}$, so the series converges, and multiplying its partial sums by $N$ leaves $I$ minus a power of $I-N$, which tends to $0$.

Third, since $N=CTD$, we have $CT=ND^{-1}$. Hence $(DN^{-1}C)T=DN^{-1}ND^{-1}=I$, so $DN^{-1}C$ is a left inverse of $T$. Applying it to the first identity gives $DN^{-1}CP_tF_tS=P_sF_s$.

Fourth, set $A=S/2$ and $B_0=2^{-(2\alpha^2-2)}DN^{-1}C/2$. The scale factors multiply to $2^{-2\alpha^2}$, so $B_0P_tF_tA=2^{-2\alpha^2}P_sF_s$. Multiplying by $2^{2\alpha^2}$ gives $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$.

Both factors are contractions. $N-I$ is small because $D$ cancels the Gaussian factor at each selected coordinate, leaving only the small Gaussian weights of the other coordinates. The source bounds $\|S/2\|<3/4$ and $\|N^{-1}/2\|<7/8$, and $\|2^{-(2\alpha^2-2)}D\|<1$ <cite data-source="paper">∥D′ ∥ < 1</cite>. Since $\|C\|=1$, the product $B_0$ has norm below $1$.

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

Write the body to `exegenius/tasks/0035-write-gaussian-resampling.answer.md` and the JSON to `exegenius/tasks/0035-write-gaussian-resampling.answer.json`, then run `exegenius submit 0035-write-gaussian-resampling` in the project directory. If submit rejects the answer, fix the answer and submit again.
