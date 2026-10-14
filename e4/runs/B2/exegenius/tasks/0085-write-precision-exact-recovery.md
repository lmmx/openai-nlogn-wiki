# exegenius task 0085-write-precision-exact-recovery

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e4/B2` (paths below are relative to it)

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

For these sources: The reader is an undergraduate computer science student: they have taken programming, data structures, an algorithms course (asymptotic analysis, divide and conquer, sorting), discrete mathematics (sets, functions, induction, modular arithmetic, basic number theory) and an introductory linear algebra and complex numbers course, plus an introductory theory-of-computation course covering Turing machines. They have not met the Fourier transform beyond what the wiki explains, nor rings of polynomials modulo a polynomial, analytic number theory (prime density estimates), finite fields beyond bits, or any research-level complexity results on integer multiplication. Everything specific to the paper's fixed-tape constructions, networks, frames and numerical precision must be explained.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine
- Bitwise XOR and arithmetic mod 2
- Exact integer multiplication on a multitape Turing machine
- Schönhage–Strassen n log n optimality conjecture (also: n log n conjecture)
- Established O(n log n) multiplier (Harvey–van der Hoeven)
- Normalized discrete Fourier transform (also: Fourier transform)
- Cyclic convolution and the convolution theorem (also: convolution)
- Integer multiplication as convolution of radix digits
- Two-point butterfly and radix-2 fast Fourier transform (also: butterfly, FFT)
- Matrix rank, subspaces and orthogonal complements
- Tensor products of operators and arrays
- Multidimensional transform on a tensor of axes
- Disk-grid fixed-point arithmetic, contractions and error (also: disk grid, truncation Q_p)
- Array order and elementary stream scans
- Controlled cyclic shifts and fixed rational scalings
- Chinese-remainder address map to distinct prime axes (also: Agarwal–Cooley map, Φ)
- Gaussian resampling with permutations left in the transform (also: Gaussian resampling)
- Bluestein chirp identity (also: chirp identity)
- Source permutation cancellation
- Polynomial ring modulo yʳ + 1 (also: negacyclic ring)
  - $y$ (ring indeterminate): The formal variable of the polynomials, a root of −1 raised to the r-th power, whose powers serve as roots of unity.
  - $r$ (polynomial length): The number of complex coefficients in a stored polynomial, a power of two.
- Coefficient twist from cyclic to negacyclic wrap
- Synthetic polynomial transform (also: Nussbaumer polynomial transform)
- Signed packing of polynomial products (Kronecker substitution)
- Linear exchange network with restored scratch wires (also: finite network, motif)
- Frames: changing array representation along network edges (also: common-frame identity)
- Nested subspace labels and the total-rank saving (also: rank deficit, orthogonal residual)
- Bit-network rational matrix interface
- Lower triangular factorization of a matrix (also: Bruhat factorization)
- Cost of a rational matrix shear
- Depth-first schedule of recursive calls on fixed tapes
- Recursive power-width chunk interchange
- Fast interchange of address chunks (also: address interchange, chunk swap)
- Two-point phase kernel C
- Binary phase interface of the complex network (also: phase frames)
- Packed selected-bit addition on one rectangle (also: packed change of address bits)
- Exact Gaussian dyadic evaluation with guard bits
- Simultaneous normalized butterfly layer (also: parallel butterfly layer)
- Transform layout on which parallel layers apply
- Convolution over the polynomial ring from the retained transform layout
- Parameter choice: precision, dimension, axis lengths and prime source lengths
- Asymptotic notation Omega, Theta and little-o (also: Ω, Θ, Big-Omega, Big-Theta, tight bound, lower bound notation)
- Logarithms, floors and ceilings (also: log base 2, lg, natural logarithm, floor function, ceiling function, ⌈x⌉, ⌊x⌋)
- Binary representation of integers (also: binary numbers, bit strings, radix representation, most significant bit, least significant bit, base-2 numerals, n-bit integer)
- Schoolbook binary addition with carries (also: carry propagation, ripple carry, grade-school multiplication, long addition, long multiplication)
- Divide and conquer multiplication (Karatsuba, Toom-Cook) (also: Karatsuba algorithm, Toom-Cook, Karatsuba-Ofman, divide-and-conquer, O(n^{log_2 3}))
- Recurrences, induction and geometric sums (also: recurrence relation, proof by induction, geometric series, unrolling a recurrence, master theorem)
- Sets, functions, bijections and permutations (also: Cartesian product, bijection, permutation, involution, function composition, injective, surjective, index set, indicator function)
- Binomial coefficients (also: n choose k, combinations, C(n,k), counting subsets)
- Modular arithmetic and congruences (also: integers mod n, Z/nZ, residues, congruence, a mod q, cyclic group of integers mod n, modular inverse)
- Greatest common divisor and the Euclidean algorithm (also: gcd, coprime, relatively prime, extended Euclidean algorithm, Bezout identity, modular inverse computation)
- Prime numbers (also: primes, prime factorization, primality testing, sieve of Eratosthenes, distinct primes)
- Chinese remainder theorem (also: CRT, Chinese remainder, residues modulo coprime moduli)
- Roots of unity (also: primitive root of unity, nth roots of unity, e^{2πi/n}, unit-modulus roots, twiddle factor)
- Matrices, matrix products and inverses (also: matrix multiplication, identity matrix, invertible matrix, diagonal matrix, permutation matrix, triangular matrix, transpose, linear map, dot product, inner product)
- Gaussian elimination and row operations (also: row reduction, elementary row operations, row addition, row swap, pivot)
- Vectors and matrices over the two-element field (also: F_2, GF(2), binary vectors, linear algebra mod 2, Hamming weight, binary matrices, GL(m, F_2))
- Vector norms and the triangle inequality (also: max norm, sup norm, infinity norm, absolute value bound, error bound, triangle inequality, modulus bound)
- Two's complement and fixed-width signed integers (also: signed binary, twos complement, signed words, dyadic rationals, binary fixed-point)
- Stacks and queues (also: push and pop, LIFO, stack discipline, last-in first-out, queue)
- Sorting and radix sort (also: stable sort, radix sorting, merge sort, sorting by keys, binary radix sort, merging sorted lists)
- Binary counters and finite-state bookkeeping (also: finite residue counter, counting with a counter, finite control counting, ripple counting)

## This page

Concept: Precision, rounding and carry propagation
Gloss: Tracks scales (the two factors S and 2^{2b+4}) and disk margins to show the recovered convolution coefficients have error below 1/2, rounds to nearest integers, and propagates radix-2^b carries to output the exact 2n-bit product.

## This page in the argument

The step: The recovered coefficients have error below $1/2$, so rounding gives the exact integer convolution coefficients and carries give the exact $2n$-bit product.

It serves these steps, from the main result down:

- One deterministic multitape Turing machine multiplies $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$, using fast address interchange, fast simultaneous butterfly layers, and the resampling, chirp and synthetic-convolution reduction.; how: supply the two fast tape procedures, then insert them into a reduction from the integer product to polynomial-ring convolution, and add up every cost (on [Power-saving integer multiplication theorem](main-theorem.md))
- Radix-$2^b$ digit convolution on $S$ distinct prime axes, computed by transform, pointwise product and opposite transform at precision $p$ in a padded box of $T$ entries, gives the exact $2n$-bit product after scaling, rounding and carries.; how: reduce the integer product to a cyclic convolution of radix digits, move it to prime axes by a CRT map, replace each prime-length transform by power-of-two transforms through Gaussian resampling and a chirp, and solve the remaining ring convolution by synthetic transforms (on [The multiplication algorithm: digits to transform, pointwise product and back](multiplication-algorithm.md))

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Disk-grid fixed-point arithmetic, contractions and error](fixed-point-disk-arithmetic.md): Complex numbers with real and imaginary parts that are multiples of 2^{−p} in the unit disk, stored as two signed two's-complement words; Q_p truncates toward zero, linear contractions do not increase the max norm, and errors of composed approximations add.
  Shown as: Precision, rounding and carry propagation *<predicate>* Disk-grid fixed-point arithmetic, contractions and error
- [Integer multiplication as convolution of radix digits](multiplication-by-convolution.md): Write each operand as a polynomial in 2^b with radix-2^b digit coefficients; the product coefficients are a convolution of digit lists (each below 2³ᵇ), padded so cyclic convolution has no wraparound, and carries recover the integer product.
  Shown as: Precision, rounding and carry propagation *<predicate>* Integer multiplication as convolution of radix digits

## Pages that build on this one

- The multiplication algorithm: digits to transform, pointwise product and back: Convert operands to digit lists on a padded prime-axis box via Φ, apply the source transform (resample, chirp convolution through the twist, resample) to each, multiply pointwise, apply the opposite transform, scale by S and 2^{2b+4}, undo Φ, round and propagate carries.

## Other pages you may link to

- [Exact integer multiplication on a multitape Turing machine](integer-multiplication-problem.md)
- [Schönhage–Strassen n log n optimality conjecture](optimality-conjecture.md)
- [Established O(n log n) multiplier (Harvey–van der Hoeven)](harvey-hoeven-multiplier.md)
- [Polynomial ring modulo yʳ + 1](polynomial-ring-mod.md)
- [Linear exchange network with restored scratch wires](scalar-exchange-network.md)
- [Array order and elementary stream scans](elementary-streams.md)
- [Controlled cyclic shifts and fixed rational scalings](controlled-cyclic-shifts.md)
- [Matrix rank, subspaces and orthogonal complements](linear-algebra-basics.md)
- [Frames: changing array representation along network edges](frames.md)
- [Tensor products of operators and arrays](tensor-product.md)
- [Nested subspace labels and the total-rank saving](subspace-labels-rank-saving.md)
- [Bit-network rational matrix interface](rational-matrix-interface.md)
- [Lower triangular factorization of a matrix](lower-triangular-factorization.md)
- [Cost of a rational matrix shear](address-shear-cost.md)
- [Depth-first schedule of recursive calls on fixed tapes](fixed-tape-recursion-schedule.md)
- [Recursive power-width chunk interchange](power-width-interchange.md)
- [Fast interchange of address chunks](chunk-interchange.md)
- [Packed selected-bit addition on one rectangle](packed-selected-bit-addition.md)
- [Signed packing of polynomial products (Kronecker substitution)](signed-packing.md)
- [Normalized discrete Fourier transform](dft.md)
- [Two-point butterfly and radix-2 fast Fourier transform](fft-butterfly.md)
- [Two-point phase kernel C](phase-kernel.md)
- [Binary phase interface of the complex network](phase-frame-interface.md)
- [Exact Gaussian dyadic evaluation with guard bits](guard-width-exactness.md)
- [Simultaneous normalized butterfly layer](simultaneous-butterfly-layer.md)
- [Cyclic convolution and the convolution theorem](cyclic-convolution.md)
- [Multidimensional transform on a tensor of axes](multidimensional-transform.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Coefficient twist from cyclic to negacyclic wrap](coefficient-twist.md)
- [Chinese-remainder address map to distinct prime axes](crt-address-map.md)
- [Transform layout on which parallel layers apply](synthetic-transform-layout.md)
- [Convolution over the polynomial ring from the retained transform layout](synthetic-convolution.md)
- [Gaussian resampling with permutations left in the transform](gaussian-resampling.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Source permutation cancellation](permutation-cancellation.md)
- [Parameter choice: precision, dimension, axis lengths and prime source lengths](parameter-choice.md)
- [The multiplication algorithm: digits to transform, pointwise product and back](multiplication-algorithm.md)
- [Time-bound accounting and the exponent κ](time-bound-accounting.md)
- [Power-saving integer multiplication theorem](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "Propagate radix-$2^b$ carries in increasing coefficient order." (paper)

  > exactly by $S$, retaining the denominator $2^p$ and writing each component in signed width $w_{\rm c}+b$. Denote the represented dyadic array by $\widetilde w$. \item Multiply the grid numerators of $\widetilde w$ exactly by $2^{2b+4}S$, again retaining the denominator $2^p$, and write each component in signed width $w_{\rm c}+4b+4$. Round the represented real values to the nearest integers. At each valid address, write the rounded coefficient in one signed $(3b+1)$-bit word, most significant bit first; at every padded address, write a zero word of that width. Supply this local payload width to $\Phi^{-1}$ and apply it, including removal of the address padding, to restore the ordinary coefficient order. \item Propagate radix-$2^b$ carries in increasing coefficient order. Write the resulting bits from least to most significant on a work tape, then reverse that stream and output exactly $2n$ bits in most-significant-first order. \end{enumerate}

- "k_{j+1}=\left\lfloor\frac{c_j+k_j}{Q_0}\right\rfloor" (paper)

  > To propagate carries, let $Q_0=2^b$. The recovered ordinary coefficients are the $c_j$ in \eqref{eq:capacity}; they are zero for $2q-2<j<S$. With $q=\lceil n/b\rceil$ as above, use the recurrence for $0\le j<S$: \[ k_0=0,\qquad d_j=(c_j+k_j)\bmod Q_0,\qquad k_{j+1}=\left\lfloor\frac{c_j+k_j}{Q_0}\right\rfloor. \] The carries satisfy $0\le k_j\le q(Q_0-1)<Q_0^2$. If this holds at $j$, then \[ c_j+k_j\le q(Q_0-1)^2+q(Q_0-1)=qQ_0(Q_0-1), \] which proves the next carry bound. The defining relation $c_j+k_j=d_j+Q_0k_{j+1}$ also gives the exact invariant \[ \sum_{h<j}c_hQ_0^h =\sum_{h<j}d_hQ_0^h+k_jQ_0^j. \] It holds for $j=0$, and the defining relation proves its next instance. The unprocessed terms are multiples of $Q_0^j$, so the identity fixes the first $j$ radix digits of the full product. The value $k_j$ is the carry from the processed coefficients into the remaining positions.


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

Write the body to `exegenius/tasks/0085-write-precision-exact-recovery.answer.md` and the JSON to `exegenius/tasks/0085-write-precision-exact-recovery.answer.json`, then run `exegenius submit 0085-write-precision-exact-recovery` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0085-write-precision-exact-recovery`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
