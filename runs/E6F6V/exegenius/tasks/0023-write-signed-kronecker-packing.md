# exegenius task 0023-write-signed-kronecker-packing

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F6V` (paths below are relative to it)

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

For these sources: The reader is an undergraduate computer scientist: asymptotic analysis and recurrences, discrete mathematics (induction, sets, functions, permutations, logarithms, floor and ceiling, modular arithmetic, primes, gcd and the Euclidean algorithm), introductory linear algebra (matrices, invertibility, rank, Gaussian elimination, vectors and inner products), basic algorithms (grade-school multiplication, divide and conquer, number representations in binary, bitwise XOR) and the basics of Turing machines with several tapes. They have met complex numbers and polynomials, but not the FFT in depth, abstract algebra beyond basic rings or quotient constructions, number-theoretic results such as prime density, numerical error analysis, or any research on fast integer multiplication.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes
- Fixed-tape model and elementary stream scans
- Controlled cyclic shifts and rational scalings
- Established O(n log n) integer multiplier
- Integer multiplication as convolution of radix digits
- Polynomial ring modulo y^r + 1
  - $y$ (ring variable): The indeterminate of the polynomials, whose powers act as roots of unity because y^r = −1.
  - $r$ (record length): The number of complex coefficients in a polynomial of the ring, a power of two.
- Fixed-point disk-grid arrays and truncation
- Subspaces, orthogonal complements and projections
- Lower-triangular (Bruhat) factorization
- Linear network exchanging two banks with restored scratch wires
- Frames and the common-frame identity
- Nested subspace labels with a rank deficit
- Recursive power saving from s < Wm
- Rational matrix interface and address shear
- Cost of a rational matrix shear
- Power-width chunk interchange with rows
- Fast interchange of address chunks
- Phase frames and the two-point kernel C
- Packed changes of selected address bits
- Exact Gaussian dyadics and guard width
- Modular arithmetic and congruences (also: integers mod n, Z/nZ, residues, congruence, mod q^b)
- Primes, coprimality and gcd (also: prime numbers, relatively prime, coprime, prime to q, greatest common divisor, gcd)
- Euclidean algorithm and modular inverses (also: extended Euclidean algorithm, Euclid's algorithm, Bezout identity, inverse modulo q)
- Trial division and primality search (also: finding a prime by scanning, testing divisibility, trial division)
- Binary representation, bit strings and XOR (also: binary expansion, bit string, bits, exclusive or, XOR, addition mod 2, most significant bit)
- Radix representation and carry propagation (also: base-b digits, radix, carries, grade-school addition, schoolbook multiplication, digit expansion)
- Logarithms, floor and ceiling (also: lg, log base 2, natural logarithm, floor function, ceiling function, power of two)
- Recurrences and induction (also: proof by induction, recurrence relations, unrolling a recurrence, geometric series)
- Divide-and-conquer multiplication (also: Karatsuba, schoolbook algorithm, O(n^2) multiplication, Toom-Cook)
- Permutations and bijections (also: permutation of coordinates, permutation matrix, partial permutation, bit reversal, bijection)
- Matrices, invertibility and rank (also: matrix product, invertible matrix, rank of a matrix, linear map, diagonal matrix, identity matrix, matrix inverse, linear combination)
- Gaussian elimination (also: row reduction, elementary row operations, row echelon form)
- Vector spaces, bases and dimension (also: basis, span, linear independence, dimension, coordinates, standard basis)
- Cartesian products and lexicographic order (also: product of sets, tuples, lexicographic ordering, multi-index, d-dimensional array indexing, row-major order)
- Rational numbers and dyadic fractions (also: dyadic rationals, binary fractions, denominators, numerators, rational coefficients, lowest terms)
- Norms, absolute value and triangle inequality (also: modulus, sup norm, maximum norm, triangle inequality, unit disk, Euclidean norm, contraction, error bound)
- Euler's formula and roots of unity (also: e^(i theta), primitive root of unity, cis, complex exponential, unit circle)
- Rounding and square roots (also: nearest integer, rounding to integer, square root, truncation toward zero)
- Polynomial time and computational cost on tapes (also: polynomial in p, linear time, worst-case running time, single scan of a tape, fixed alphabet, finite control)
- Fast Fourier transform as a known algorithm (also: FFT, Cooley-Tukey, divide-and-conquer FFT, fast polynomial multiplication)

## This page

Concept: Signed packing of polynomial products
Gloss: Computing products of ring polynomials exactly by evaluating each at a large power of two (signed Kronecker substitution), multiplying the resulting integers with the established multiplier and unpacking the coefficients.

## This page in the argument

The step: Products of ring polynomials are computed exactly by signed Kronecker substitution, using the established multiplier as a subroutine, in time $O(rp\log(rp))$.

It serves these steps, from the main result down:

- A single deterministic fixed-tape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.; how: put fast address interchange and simultaneous butterfly layers inside the Gaussian-resampling and synthetic-transform reduction of multiplication to convolution, then verify exactness and cost (on [Integer multiplication below n log n](multiplication-below-nlogn.md))
- Convolution over the polynomial ring $\mathbb C[y]/(y^r+1)$ on several axes runs in time dominated by simultaneous layers and chunk interchanges.; how: evaluate the convolution by synthetic transforms laid out on tape so that each round is one simultaneous layer

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Polynomial ring modulo y^r + 1](negacyclic-ring.md): Complex polynomials of degree below r with y^r = −1, so multiplying by a power of y is a signed cyclic shift of the coefficient list and powers of y serve as roots of unity.
  Shown as: Signed packing of polynomial products *<predicate>* Polynomial ring modulo y^r + 1
- [Established O(n log n) integer multiplier](hvdh-multiplier.md): The Harvey–van der Hoeven multitape algorithm multiplying N-bit integers in O(N log N) time, used here only as an ordinary subroutine on short inputs.
  Shown as: Signed packing of polynomial products *<predicate>* Established O(n log n) integer multiplier
- [Fixed-point disk-grid arrays and truncation](fixed-point-precision.md): Complex coefficients of modulus at most 1 stored with p fractional bits per component; truncation Q_p toward zero costs error below √2·2^(−p) and never increases the norm.
  Shown as: Signed packing of polynomial products *<predicate>* Fixed-point disk-grid arrays and truncation

## Pages that build on this one

- Convolution over the polynomial ring from retained frequency order: Convolving arrays over the ring by transforming both operands, multiplying pointwise in the retained stored frequency order, and applying the opposite transform, with error below √2·M(3ℓ+1)·2^(−p).
- Cost table and exponent margins: Dividing each phase's cost by Tp = Θ(n) gives seven dominant powers of p, each at most 1−2κ for the fixed rational exponents, so the total is O(n (log n)^(1−κ)).

## Other pages you may link to

- [Integer multiplication as convolution of radix digits](convolution-multiplication.md)
- [Fixed-tape model and elementary stream scans](multitape-streams.md)
- [Controlled cyclic shifts and rational scalings](controlled-shifts.md)
- [Linear network exchanging two banks with restored scratch wires](bank-exchange-network.md)
- [Subspaces, orthogonal complements and projections](linear-algebra-spaces.md)
- [Frames and the common-frame identity](frames-on-arrays.md)
- [Nested subspace labels with a rank deficit](subspace-labels.md)
- [Recursive power saving from s < Wm](recursive-power-saving.md)
- [Rational matrix interface and address shear](bit-shear-interface.md)
- [Lower-triangular (Bruhat) factorization](lower-triangular-factorization.md)
- [Cost of a rational matrix shear](matrix-shear-cost.md)
- [Power-width chunk interchange with rows](power-width-interchange.md)
- [Fast interchange of address chunks](chunk-interchange.md)
- [Phase frames and the two-point kernel C](phase-frames.md)
- [Packed changes of selected address bits](packed-selected-bit-addition.md)
- [Exact Gaussian dyadics and guard width](guard-bits.md)
- [Normalized discrete Fourier transform and convolution theorem](discrete-fourier-transform.md)
- [Radix-two FFT butterflies](radix-two-fft.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Synthetic transform layout on tape](synthetic-transform-layout.md)
- [Convolution over the polynomial ring from retained frequency order](synthetic-convolution.md)
- [Cyclic-to-negacyclic coefficient twist](coefficient-twist.md)
- [Gaussian resampling without sorting](gaussian-resampling.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Cancellation of the retained source permutation](permutation-cancellation.md)
- [Tensor resampling on the padded box](tensor-resampling.md)
- [Chinese-remainder map to distinct prime cyclic axes](crt-cyclic-convolution.md)
- [Size parameters and prime axis lengths](parameter-choice.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Precision, rounding and carry recovery](exact-recovery.md)
- [Cost table and exponent margins](time-bound-accounting.md)
- [Integer multiplication below n log n](multiplication-below-nlogn.md)

## Evidence from the sources, with the paragraph around each quote

- "The reduction is a signed form of Kronecker substitution" (paper)

  > To multiply the polynomial records, we use the fixed-tape integer multiplier of Harvey and van der Hoeven~\cite[Theorem~1.1]{HarveyHoeven2021}, with cost $O(N\log(2N))$ on $N$-bit inputs. This is an independent subroutine. Its inputs below have $O(rp)$ bits, and we include the conversions between coefficient streams and signed integers in the cost. The reduction is a signed form of Kronecker substitution; compare \cite[Lemma~2.5]{HarveyHoeven2021}. We specify the packing and recovery of coefficients to include negative values and the required tape format.

- "One can compute the exact Gaussian integer numerators of $fg$" (paper)

  > \begin{lemma}[Signed packing and normalized ring multiplication] \label{lem:signed-ring-product} Let $r=2^\ell<2^p$ with integers $\ell\geq1$ and $p\geq2$, and fix $C_w>1$. Let $w$ be an integer with $p+2\leq w\leq C_wp$. The input supplies $\Gamma(p)\Gamma(r)\Gamma(w)$ and two disk grid polynomials $f,g\in\mathcal R_r$ in the component format of Proposition~\ref{prop:simultaneous-layer} with width $w$. One can compute the exact Gaussian integer numerators of $fg$, and then return $Q_p(fg/r)$ in that same format, in time $O(rp\log(rp))$ on a fixed number of tapes. The output is a disk grid polynomial with error less than $\sqrt2\,2^{-p}$ from $fg/r$. \end{lemma} \begin{proof} The supplied power of two $r$ determines $\ell=\log_2r$. Write \[ f=2^{-p}(a+ib),\qquad g=2^{-p}(c+ie), \] where $a,b,c,e\in\mathbb Z[y]$ have degree less than $r$ and coefficients of absolute value at most $2^p$. Set $B_0=2^{4p}$ and, for $u\in\{a,b,c,e\}$, define the signed evaluation integer \[ A_u=u(B_0)=\sum_{j=0}^{r-1}u_jB_0^j. \] The bound \[ |A_u|\leq2^p\frac{B_0^r-1}{B_0-1}<B_0^r/2 \] shows that each magnitude fits in $4pr$ bits. Multiply the four pairs of absolute values usin


## Sources (read from disk as needed)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Length

At most 350 words, not counting mathematics and citations: submit rejects a longer page.

## Answer

The answer is two files: the page body as markdown (not JSON), and a JSON object with the symbols the page binds and its relations to its prerequisite pages. In JSON strings, write each backslash of LaTeX twice (`"\\kappa"`). The JSON follows this schema:

```json
{
  "$defs": {
    "Derivation": {
      "additionalProperties": false,
      "description": "Where the page derives one of the steps the argument gives it.",
      "properties": {
        "quote": {
          "description": "The passage on this page that derives the step, copied exactly: a sentence or more,\noutside citations.",
          "type": "string"
        },
        "step": {
          "description": "The step's id, as listed under \"Steps this page derives\".",
          "type": "string"
        }
      },
      "required": [
        "step",
        "quote"
      ],
      "type": "object"
    },
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
    "derivations": {
      "default": [],
      "description": "For each step listed under \"Steps this page derives\", the passage on the page that\nderives it. Empty if the task lists none.",
      "items": {
        "$ref": "#/$defs/Derivation"
      },
      "type": "array"
    },
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

Write the body to `exegenius/tasks/0023-write-signed-kronecker-packing.answer.md` and the JSON to `exegenius/tasks/0023-write-signed-kronecker-packing.answer.json`, then run `exegenius submit 0023-write-signed-kronecker-packing` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0023-write-signed-kronecker-packing`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
