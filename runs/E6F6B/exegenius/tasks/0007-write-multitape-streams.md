# exegenius task 0007-write-multitape-streams

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F6B` (paths below are relative to it)

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
- Established O(n log n) integer multiplier
- Integer multiplication as convolution of radix digits
- Polynomial ring modulo y^r + 1
  - $y$ (ring variable): The indeterminate of the polynomials, whose powers act as roots of unity because y^r = −1.
  - $r$ (record length): The number of complex coefficients in a polynomial of the ring, a power of two.
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

Concept: Fixed-tape model and elementary stream scans
Gloss: The fixed-alphabet, fixed-number-of-tapes machine model in which arrays are streams in lexicographic order, and splitting, merging, digit moves and row splits cost O(V) for volume V.

## This page in the argument

The step: Splitting, merging, digit moves and row splits on an array of volume $V$ in lexicographic order cost $O(V)$ steps on a fixed number of tapes.

It serves these steps, from the main result down:

- A single deterministic fixed-tape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.; how: Provide two fast tape procedures, place them inside the Gaussian-resampling and synthetic-transform reduction of the integer product to a convolution, then check precision and exact recovery and add up the costs of all phases. (on [Integer multiplication below n log n](multiplication-below-nlogn.md))
- There are two fast tape procedures: an interchange of two address fields of $u$ bits in $O(Vu^\tau)$ time and a simultaneous butterfly layer over $d$ address chunks in $O(Vd^{\lambda'})$ time, with $\tau,\lambda'<1$ and $V$ the stored bit volume.; how: Set up the elementary stream and controlled-shift tools, then build each of the two procedures from its own rank-saving linear network that recurses on smaller calls of itself.

## Pages that build on this one

- Controlled cyclic shifts and rational scalings: Updating a target address field by an offset computed from earlier control fields (a cyclic rotation of blocks), or multiplying it by a unit modulo q^b, in O(V) time.
- Power-width chunk interchange with rows: Interchanging two chunks of e = m^k digits by splitting rows into W role streams, running the bit network with shear edges implemented by smaller interchanges, then applying D←D−H, H←H+D, D←H−D; cost O(V e^τ).

## Other pages you may link to

- [Integer multiplication as convolution of radix digits](convolution-multiplication.md)
- [Polynomial ring modulo y^r + 1](negacyclic-ring.md)
- [Established O(n log n) integer multiplier](hvdh-multiplier.md)
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
- [Fixed-point disk-grid arrays and truncation](fixed-point-precision.md)
- [Exact Gaussian dyadics and guard width](guard-bits.md)
- [Signed packing of polynomial products](signed-kronecker-packing.md)
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

- "A machine has one fixed finite alphabet and one fixed finite number of one-dimensional tapes." (paper)

  > A machine has one fixed finite alphabet and one fixed finite number of one-dimensional tapes. A step reads and writes at most one cell on each tape and moves each head by at most one cell. Fixed tracks and finitely many work tapes change time by a fixed factor. We distinguish moving one digit in a fixed radix, which needs a bounded number of scans, from interchanging fields whose numbers of digits grow. The latter permutation will be realized in Section~\ref{sec:tape-interchange} by computing XOR combinations of intermediate data streams. The present section supplies the elementary scans it uses. Every scan includes its counters and the return of its tape heads.

- "is the number of stored data bits" (paper)

  > For a positive integer $a$ write $[a]=\{0,\ldots,a-1\}$. An array with address set $[a_1]\times\cdots\times[a_t]$ is stored in lexicographic order, with the first coordinate most significant. Its entries are bits unless a record width is specified. A trailing record of $B$ bits can equivalently be regarded as a final address field $[B]$. An address is implicit in an entry's position in this ordered stream; it is not stored beside every data bit. The \emph{logical volume} $V$ is the number of stored data bits. Work tapes and duplicate streams are charged in time but do not increase $V$ in recurrences. All the fields discussed below are nonempty. A call with an empty array is handled directly.

- "Each of the following operations on an array of volume $V$ takes $O(V)$ steps on a fixed number of one-dimensional tapes" (paper)

  > \begin{lemma}[Elementary stream operations] \label{lem:elementary-streams} Fix a radix $q\ge2$. Each of the following operations on an array of volume $V$ takes $O(V)$ steps on a fixed number of one-dimensional tapes: \begin{enumerate} \item any fixed permutation of the pair of digit values at two specified radix-$q$ positions, whether or not the positions are adjacent; \item moving one specified radix-$q$ digit to another position, preserving the order of the intervening positions; \item splitting on a specified radix-$q$ digit, applying a fixed pointwise map to aligned streams, and merging them back; \item for positive integers $P,R,B$, within each prefix of an array on $[P]\times[R]\times[B]$, splitting whole rows cyclically into a fixed number $W$ of streams, and, when $W$ divides $R$, merging those streams in any fixed order of the row classes. \end{enumerate} The bounds include shape preparation, counter initialization and resets, and returning or clearing the visited portions of work tapes. Their constants may depend on the fixed radix, the fixed pointwise map, and the fixed number of row classes. \end{lemma}


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

Write the body to `exegenius/tasks/0007-write-multitape-streams.answer.md` and the JSON to `exegenius/tasks/0007-write-multitape-streams.answer.json`, then run `exegenius submit 0007-write-multitape-streams` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0007-write-multitape-streams`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
