# exegenius task 0065-write-signed-packing

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
- Matrix rank, subspaces and orthogonal complements
- Tensor products of operators and arrays
- Array order and elementary stream scans
- Controlled cyclic shifts and fixed rational scalings
- Polynomial ring modulo yʳ + 1 (also: negacyclic ring)
  - $y$ (ring indeterminate): The formal variable of the polynomials, a root of −1 raised to the r-th power, whose powers serve as roots of unity.
  - $r$ (polynomial length): The number of complex coefficients in a stored polynomial, a power of two.
- Linear exchange network with restored scratch wires (also: finite network, motif)
- Frames: changing array representation along network edges (also: common-frame identity)
- Nested subspace labels and the total-rank saving (also: rank deficit, orthogonal residual)
- Bit-network rational matrix interface
- Lower triangular factorization of a matrix (also: Bruhat factorization)
- Cost of a rational matrix shear
- Depth-first schedule of recursive calls on fixed tapes
- Recursive power-width chunk interchange
- Fast interchange of address chunks (also: address interchange, chunk swap)
- Packed selected-bit addition on one rectangle (also: packed change of address bits)
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

Concept: Signed packing of polynomial products (Kronecker substitution)
Gloss: Evaluating integer polynomials at B₀ = 2^{4p} to get integers, multiplying them with the established multiplier, and extracting signed coefficients by centered residues, then reducing modulo y^r + 1, to multiply ring elements in O(rp log(rp)).

## This page in the argument

The step: Ring elements are multiplied by signed Kronecker packing at $B_0=2^{4p}$ and the established multiplier, in $O(rp\log(rp))$ time.

It serves these steps, from the main result down:

- One deterministic multitape Turing machine multiplies $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$, using fast address interchange, fast simultaneous butterfly layers, and the resampling, chirp and synthetic-convolution reduction.; how: supply the two fast tape procedures, then insert them into a reduction from the integer product to polynomial-ring convolution, and add up every cost (on [Power-saving integer multiplication theorem](main-theorem.md))
- Radix-$2^b$ digit convolution on $S$ distinct prime axes, computed by transform, pointwise product and opposite transform at precision $p$ in a padded box of $T$ entries, gives the exact $2n$-bit product after scaling, rounding and carries.; how: reduce the integer product to a cyclic convolution of radix digits, move it to prime axes by a CRT map, replace each prime-length transform by power-of-two transforms through Gaussian resampling and a chirp, and solve the remaining ring convolution by synthetic transforms (on [The multiplication algorithm: digits to transform, pointwise product and back](multiplication-algorithm.md))
- The normalized convolution $\mathcal M_r(f,g)=(f*g)/T$ over $\mathcal R_r$ on $d-1$ power-of-two axes is computed from the retained transform layout with error below $\sqrt2\,M(3\ell+1)2^{-p}$.; how: forward synthetic transforms of both operands, pointwise ring products in the retained stored order, and the opposite transform (on [Convolution over the polynomial ring from the retained transform layout](synthetic-convolution.md))

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Established O(n log n) multiplier (Harvey–van der Hoeven)](harvey-hoeven-multiplier.md): The previously known fixed-tape algorithm multiplying N-bit integers in O(N log N) time, used here only as an ordinary subroutine on short records and never recursively on the improved theorem.
  Shown as: Signed packing of polynomial products (Kronecker substitution) *<predicate>* Established O(n log n) multiplier (Harvey–van der Hoeven)
- [Polynomial ring modulo yʳ + 1](polynomial-ring-mod.md): The ring of complex polynomials of degree less than r with y^r = −1, where multiplying by a power of y permutes the coefficients with sign changes (a signed shift) and so acts as an isometry in the max coefficient norm.
  Shown as: Signed packing of polynomial products (Kronecker substitution) *<predicate>* Polynomial ring modulo yʳ + 1

## Pages that build on this one

- Convolution over the polynomial ring from the retained transform layout: Normalized convolution M_r(f,g) = (f*g)/(rM): two forward synthetic transforms, pointwise ring products by signed packing in the retained stored order, and the opposite transform, with error below √2·M(3ℓ+1)·2^{−p}.

## Other pages you may link to

- [Exact integer multiplication on a multitape Turing machine](integer-multiplication-problem.md)
- [Schönhage–Strassen n log n optimality conjecture](optimality-conjecture.md)
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
- [Normalized discrete Fourier transform](dft.md)
- [Two-point butterfly and radix-2 fast Fourier transform](fft-butterfly.md)
- [Two-point phase kernel C](phase-kernel.md)
- [Binary phase interface of the complex network](phase-frame-interface.md)
- [Disk-grid fixed-point arithmetic, contractions and error](fixed-point-disk-arithmetic.md)
- [Exact Gaussian dyadic evaluation with guard bits](guard-width-exactness.md)
- [Simultaneous normalized butterfly layer](simultaneous-butterfly-layer.md)
- [Cyclic convolution and the convolution theorem](cyclic-convolution.md)
- [Integer multiplication as convolution of radix digits](multiplication-by-convolution.md)
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
- [Precision, rounding and carry propagation](precision-exact-recovery.md)
- [The multiplication algorithm: digits to transform, pointwise product and back](multiplication-algorithm.md)
- [Time-bound accounting and the exponent κ](time-bound-accounting.md)
- [Power-saving integer multiplication theorem](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "reduction is a signed form of Kronecker substitution; compare" (paper)

  > To multiply the polynomial records, we use the fixed-tape integer multiplier of Harvey and van der Hoeven~\cite[Theorem~1.1]{HarveyHoeven2021}, with cost $O(N\log(2N))$ on $N$-bit inputs. This is an independent subroutine. Its inputs below have $O(rp)$ bits, and we include the conversions between coefficient streams and signed integers in the cost. The reduction is a signed form of Kronecker substitution; compare \cite[Lemma~2.5]{HarveyHoeven2021}. We specify the packing and recovery of coefficients to include negative values and the required tape format.

- "Signed packing and normalized ring multiplication" (paper)

  > \begin{lemma}[Signed packing and normalized ring multiplication] \label{lem:signed-ring-product} Let $r=2^\ell<2^p$ with integers $\ell\geq1$ and $p\geq2$, and fix $C_w>1$. Let $w$ be an integer with $p+2\leq w\leq C_wp$. The input supplies $\Gamma(p)\Gamma(r)\Gamma(w)$ and two disk grid polynomials $f,g\in\mathcal R_r$ in the component format of Proposition~\ref{prop:simultaneous-layer} with width $w$. One can compute the exact Gaussian integer numerators of $fg$, and then return $Q_p(fg/r)$ in that same format, in time $O(rp\log(rp))$ on a fixed number of tapes. The output is a disk grid polynomial with error less than $\sqrt2\,2^{-p}$ from $fg/r$. \end{lemma} \begin{proof} The supplied power of two $r$ determines $\ell=\log_2r$. Write \[ f=2^{-p}(a+ib),\qquad g=2^{-p}(c+ie


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

Write the body to `exegenius/tasks/0065-write-signed-packing.answer.md` and the JSON to `exegenius/tasks/0065-write-signed-packing.answer.json`, then run `exegenius submit 0065-write-signed-packing` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0065-write-signed-packing`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
