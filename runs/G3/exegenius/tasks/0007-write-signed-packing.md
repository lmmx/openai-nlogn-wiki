# exegenius task 0007-write-signed-packing

Project directory: `/home/user/openai-nlogn-wiki/runs/G3` (paths below are relative to it)

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

For these sources: The reader has finished an undergraduate computer science degree: algorithm analysis with asymptotic notation and recurrences, discrete mathematics (induction, divisibility, gcd, primes, permutations, summations, modular arithmetic at the level of residues), the schoolbook and divide-and-conquer integer arithmetic algorithms, sorting, and the fast Fourier transform as an O(n log n) convolution algorithm. They have taken linear algebra (matrices, linear maps, rank, inverses, vector norms) and complex numbers, and know basic multitape Turing machines and bit-level data representation. They have not studied abstract algebra beyond what the existing concepts give, finite-field linear algebra, tensor products of vector spaces, analytic number theory, or the research literature on fast multiplication.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine
- History of fast multiplication and the n log n conjecture
- Integer product as digit-polynomial convolution
- Negacyclic ring ℂ[y]/(yʳ + 1)
  - $\mathbb C$ (complex numbers): The field of complex numbers from which the polynomial coefficients are taken.
  - $y$ (ring variable): The indeterminate of the polynomials, whose powers act as roots of unity.
  - $r$ (coefficient count): The number of complex coefficients in a ring element, which is a power of two.
- Binary representation of integers and radix expansions (also: binary numbers, base-b representation, radix-b digits, bit string value, most significant bit, padding with leading zeros)
- Schoolbook arithmetic and carries (also: long multiplication, grade-school multiplication, carry propagation, long division, linear-time integer addition)
- Fast Fourier transform and the convolution theorem (also: FFT, Cooley-Tukey algorithm, FFT-based multiplication, convolution theorem)
- Linear maps and matrices (also: matrix-vector product, matrix inverse, matrix rank, linear operator, diagonal matrix, identity matrix, invertible matrix, rational matrix)
- Vector norms and the triangle inequality (also: max norm, sup norm, infinity norm, operator norm, norm of a linear map, triangle inequality)
- Permutations of indices (also: coordinate permutation, bijection on indices, rearrangement of a list, permutation matrix, bit reversal permutation)
- Divisibility, gcd and coprime integers (also: greatest common divisor, relatively prime, Euclidean algorithm, division with remainder, quotient and remainder, modular inverse, units modulo n)
- Prime numbers and primality testing by trial division (also: primes, odd primes, trial division, prime search, finding primes in an interval)
- Floor, ceiling, rounding and logarithms (also: floor function, ceiling function, round to nearest integer, binary logarithm, lg, natural logarithm, integer part)
- Bitwise XOR and Hamming weight (also: exclusive or, XOR, addition modulo 2, parity, Hamming weight, population count, bit flip)
- Asymptotic notation beyond big-O (also: Theta, Omega, little-o, big-Theta, big-Omega, tight bound, lower bound)
- Recurrences, induction and geometric series (also: recurrence relation, proof by induction, geometric series, master theorem, unrolling a recurrence, telescoping sum)
- Sorting and its O(N log N) cost (also: merge sort, sorting on tapes, label and sort, comparison sorting)
- Summation, product and index notation (also: sigma notation, indicator function, Kronecker delta, Cartesian product of index sets, subscripts modulo q, ordered tuples)
- Integers, rationals and Gaussian integers (also: Z[i], dyadic rationals, Gaussian dyadics, integers modulo, rational numbers, real and imaginary parts)
- Euler's formula and complex exponentials (also: e^{i theta}, unit circle, modulus of a complex number, complex conjugate, polar form)
- Time and bit complexity of Turing machine computation (also: bit complexity, worst-case running time, sequential tape scan, head movement cost, finite-state control, unit-cost versus bit cost)

## This page

Concept: Signed packing of polynomial products
Gloss: A Kronecker-substitution reduction that evaluates polynomials at 2^{4p}, multiplies the resulting integers with the established O(N log N) multiplier, and extracts signed coefficients to get exact products in the negacyclic ring.

## This page in the argument

The step: Two disk-grid polynomials in the negacyclic ring multiply exactly by evaluating at $2^{4p}$, multiplying the resulting integers with the established multiplier and extracting signed coefficients, in $O(rp\log(rp))$ time.

It serves these steps, from the main result down:

- A single deterministic multitape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ worst-case time with $\kappa=2^{-182}$, refuting the $n\log n$ optimality conjecture in this model.; how: Reduce the product to a cyclic convolution of radix digits, evaluate it with Fourier-type transforms whose data movement and butterfly layers are accelerated by two power-saving tape procedures, recover the exact integers by rounding and carries, and add up the costs. (on [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md))
- The normalized cyclic convolution of arrays of polynomials over $\mathbb C[y]/(y^r+1)$ on power-of-two axes is computed from the retained transform layout in time $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}+\log(rp)])$.; how: Compute two forward synthetic transforms on a layout where every round is a simultaneous butterfly layer, multiply the transformed records pointwise by signed packing in the stored frequency order, and apply the opposite transform. (on [Convolution from the retained transform layout](synthetic-convolution.md))

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Negacyclic ring ℂ[y]/(yʳ + 1)](negacyclic-ring.md): The ring of complex polynomials of degree below r taken modulo yʳ + 1, in which multiplying by a power of y is a signed shift of the coefficient list.
  Shown as: Signed packing of polynomial products *<predicate>* Negacyclic ring ℂ[y]/(yʳ + 1)
- [History of fast multiplication and the n log n conjecture](mult-history.md): Schönhage–Strassen (1971) multiplied n-bit integers in O(n log n log log n) on multitape Turing machines and conjectured n log n optimal; Fürer and later work reduced the extra factor, and Harvey and van der Hoeven reached O(n log n).
  Shown as: Signed packing of polynomial products *<predicate>* History of fast multiplication and the n log n conjecture

## Pages that build on this one

- Convolution from the retained transform layout: Two forward synthetic transforms keep their common stored frequency order, the ring records are multiplied pointwise by signed packing, and the opposite transform consumes that order to give normalized convolution over the negacyclic ring.
- Cost accounting and the exponent κ: Dividing every step's cost by the volume Tp gives seven dominant powers of p, each at most 1 − 2κ, which with κ = 2^{−182} yields total time O(n (lg n)^{1−κ}).

## Other pages you may link to

- [Integer product as digit-polynomial convolution](radix-convolution.md)
- [Elementary stream scans on tapes](stream-scans.md)
- [Subspaces, orthogonal complements and bilinear forms](linear-spaces.md)
- [Frames and pointwise gates](common-frame.md)
- [Scratch-restoring bank-exchange network](scratch-network.md)
- [Nested subspace labels and the rank saving](subspace-labels.md)
- [Phase frames and the two-point kernel C](phase-frames.md)
- [Fixed-point complex numbers on a disk grid](fixed-point-grid.md)
- [Discrete Fourier transform and cyclic convolution](dft-convolution.md)
- [Multidimensional transforms on product axes](multidim-transform.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Bluestein chirp identity](chirp-identity.md)
- [Radix-2 butterflies and stored frequency order](butterfly-order.md)
- [Contractions and error accumulation](contraction-error.md)
- [Modular arithmetic and the Chinese remainder theorem](modular-crt.md)
- [Controlled cyclic shifts of an address field](controlled-shifts.md)
- [Chinese-remainder address map to prime axes](crt-prime-axes.md)
- [Matrix shears and triangular factorization](matrix-shear.md)
- [Recursion with a strict rank saving](rank-saving-recurrence.md)
- [Fast address chunk interchange](address-interchange.md)
- [Packed addition on selected address bits](packed-bit-addition.md)
- [Fast simultaneous butterfly layer](butterfly-layer.md)
- [Tape layout for synthetic transforms](transform-layout.md)
- [Convolution from the retained transform layout](synthetic-convolution.md)
- [Phase twist from cyclic to negacyclic wrap](phase-twist.md)
- [Gaussian resampling with permutations retained](gaussian-resampling.md)
- [Source permutation cancellation](permutation-cancel.md)
- [Parameter choices and prime source lengths](parameter-choice.md)
- [Exact recovery by rounding and carries](exact-recovery.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Cost accounting and the exponent κ](cost-table.md)
- [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "reduction is a signed form of Kronecker substitution" (paper)

  > To multiply the polynomial records, we use the fixed-tape integer multiplier of Harvey and van der Hoeven~\cite[Theorem~1.1]{HarveyHoeven2021}, with cost $O(N\log(2N))$ on $N$-bit inputs. This is an independent subroutine. Its inputs below have $O(rp)$ bits, and we include the conversions between coefficient streams and signed integers in the cost. The reduction is a signed form of Kronecker substitution; compare \cite[Lemma~2.5]{HarveyHoeven2021}. We specify the packing and recovery of coefficients to include negative values and the required tape format.

- "Calls to the established $O(n\log n)$ multiplier are ordinary subroutine calls" (paper)

  > More specifically, the proof adapts Harvey and van der Hoeven's Gaussian-resampling identity, contraction bounds, and short-convolution procedures~\cite[Theorem~4.2, Proposition~4.7 and Lemmas~4.8--4.12]{HarveyHoeven2021}. Their framework already permits arbitrary dimension. Here the source and target permutations remain in the transform identity, while the faster tape procedures perform the required axis movements. Bluestein's conversion to convolution~\cite{Bluestein1970} and the synthetic-root convolution algorithm are retained; the latter follows the polynomial-transform construction in~\cite[Section~2.4 and Section~3]{HarveyHoeven2021}. Signed coefficient packing is a form of Kronecker substitution, with the fixed-tape version of~\cite[Lemma~2.5]{HarveyHoeven2021} as a direct antecedent. Calls to the established $O(n\log n)$ multiplier are ordinary subroutine calls; they do not invoke the improved theorem recursively.


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

Write the body to `exegenius/tasks/0007-write-signed-packing.answer.md` and the JSON to `exegenius/tasks/0007-write-signed-packing.answer.json`, then run `exegenius submit 0007-write-signed-packing` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0007-write-signed-packing`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
