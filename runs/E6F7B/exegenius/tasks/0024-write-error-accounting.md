# exegenius task 0024-write-error-accounting

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F7B` (paths below are relative to it)

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

For these sources: The reader has an undergraduate computer science education: discrete mathematics (sets, functions, permutations, modular arithmetic, primes and gcd), calculus-level analysis (limits, sums, Newton's method), first-course linear algebra (matrices, inverses, Gaussian elimination, vectors) and complex numbers up to roots of unity, algorithm analysis (recursion, recurrences, big-O with its relatives Omega, Theta, little-o) and basic Turing machines. The reader knows binary representation and bitwise operations, and the textbook schoolbook multiplication. The reader has not studied abstract algebra beyond what the existing concepts introduce (rings and quotient rings, zero divisors, group characters), number-theory estimates on primes, numerical analysis of rounding errors, fast multiplication algorithms beyond the basics, or any coding-theory or quantum-computing notation, so those are explained in the wiki.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine
- Multiplication complexity and the n log n conjecture
- Fixed finite-alphabet multitape model
- Established O(n log n) multiplier (subroutine)
- Array order and elementary stream operations
- Controlled shifts
- Fixed-point complex coefficients and truncation
- Polynomial ring modulo y^r + 1 (also: negacyclic ring)
  - $y$ (ring variable): The formal variable of the polynomials, satisfying y^r = −1.
  - $r$ (coefficient count): The number of complex coefficients of each polynomial, a power of two.
- Signed packing of ring products
- Subspaces, orthogonality and rank
- Linear network exchanging two banks with restored scratch values
- Frames: changing the representation along a network
- Subspace labels from three-element subsets
- Rank deficit s < W m
- Recursive power saving from the rank deficit
- Lower-triangular (Bruhat) factorization
- Address shear from the bit network
- Cost of a rational matrix shear
- Recursive power-width address interchange
- Address-chunk interchange in time O(V u^τ)
  - $V$ (stored bit volume): The number of data bits stored in the array being rearranged.
  - $u$ (chunk width): The number of bits in each of the two interchanged address chunks.
  - $\tau$ (interchange exponent): A fixed constant strictly below one (1 − 2^{−50}) bounding the growth of the cost with the chunk width.
- Packed selected-bit addition
- Asymptotic notation beyond big-O (also: Omega, Theta, little-o, Ω(f), Θ(f), o(f), liminf, limit of a ratio, asymptotic lower bound, asymptotic equivalence)
- Logarithms, exponentials, floor and ceiling (also: lg, log base 2, log2, natural logarithm, ln, floor, ceiling, ⌊x⌋, ⌈x⌉, powers of two, iterated logarithm)
- Binary representation and bitwise operations (also: binary numbers, positional notation, radix representation, base-b digits, most significant bit, bit string, XOR, exclusive or, bitwise addition mod 2, two's complement, leading zeroes, carry)
- Schoolbook integer arithmetic (also: grade-school multiplication, long multiplication, long division, quadratic-time multiplication, integer division with remainder, quotient and remainder, Euclidean division)
- Modular arithmetic (also: congruence, residues, mod q, integers modulo n, ℤ/qℤ, units modulo q, modular inverse, multiplicative inverse mod q, residue ring)
- Primes, coprimality and gcd (also: prime numbers, pairwise coprime, relatively prime, greatest common divisor, gcd, extended Euclidean algorithm, Euclid's algorithm, trial division, odd prime, divisibility, prime to q)
- Sets, functions, Cartesian products and bijections (also: index set, [n] = {0,...,n-1}, product set, Cartesian product, injective surjective bijective, inverse map, indexing, lexicographic order, mixed-radix index)
- Permutations (also: permutation of positions, bit-reversal permutation, involution, composition of permutations, permutation matrix, cyclic shift, swap, partial permutation)
- Matrices and linear maps (also: matrix multiplication, identity matrix, invertible matrix, matrix inverse, transpose, matrix transposition, Gaussian elimination, row operations, linear operator, diagonal matrix, lower triangular matrix, GL(m), row-major order, linearity)
- Roots of unity (also: nth roots of unity, primitive root of unity, e^{2πi/n}, character sum, sum of roots of unity vanishes, geometric sum of roots of unity)
- Summation, geometric series and products (also: sigma notation, geometric sum, geometric series, arithmetic series, sum of a geometric progression, product notation, telescoping sum, telescoping)
- Recursion and divide-and-conquer recurrences (also: recurrence relation, master theorem, recursion depth, solving recurrences, recursive call, unrolling a recurrence, divide and conquer)
- Worst-case running time and subroutines (also: deterministic algorithm, worst-case time, black box, subroutine call, reduction, time complexity, exact computation, bit complexity, depth-first schedule)
- Triangle inequality and norms (also: triangle inequality, absolute value of a sum, max norm, sup norm, operator norm, |z+w| ≤ |z|+|w|, error bound, absolute error)
- Rational numbers and rounding (also: fractions, dyadic rational, rounding to nearest integer, truncation toward zero, denominator, reals, real and imaginary parts)
- Newton's method (also: Newton iteration, Newton-Raphson, quadratic convergence, reciprocal iteration, square root iteration)
- Tapes, scanning and sorting as basic machine procedures (also: scan a tape, linear scan, copying a tape, merge, sorting, work tape, head movement, tape reversal)

## This page

Concept: Contractions and error accounting
Gloss: Normalized transforms and averaged convolutions are contractions in the max-modulus norm, so errors of composed approximate steps add (bilinear steps add the two operand errors) and a final error below 1/2 permits rounding to integers.

## Where the argument relies on this page

- On arrays over $\mathbb C[y]/(y^r+1)$ with $M$ records, the normalized convolution $(f*g)/T$ is computed with error below $\sqrt2 M(3\ell+1)2^{-p}$ in time $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}+\log(rp)])$. (on [Convolution from the retained transform layout](synthetic-convolution.md))
- Both forward transforms are performed in the common order $LB$, the ring products are formed pointwise, the opposite procedure consumes that order, and the result is multiplied exactly by $M=T/r$.
- For coprime $s<t$ there are contractions $A$ and $B_0$ with $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$, computed on a line of length $t$ in time $O(tp^{3/2+\delta}\alpha)$ without executing the permutations. (on [Gaussian resampling](gaussian-resampling.md))
- The computed complex convolution twists both operands, calls the synthetic convolution, untwists, and truncates, each step with tracked disk and error bounds.
- The source transform $RF_{\boldsymbol s}$ is computed as $2^\gamma\mathcal B_0 Q F_{\boldsymbol t}\mathcal A$ from Gaussian expansion, a chirp transform and Gaussian compression, with tracked errors. (on [Computed source transform](source-transform.md))
- Each recovered convolution coefficient lies within $1/2$ of its true integer value, which is below $2^{3b}$, so rounding and carry propagation give the exact product. (on [Precision budget and exact recovery](exact-recovery.md))
- The final absolute error is below $448b\,2^{-b+\gamma}\le 448b\,2^{-3b/4}<1/2$.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Fixed-point complex coefficients and truncation](fixed-point-disk.md): Complex numbers stored as 2^{−p}(a+ib) with integer a, b inside the unit disk, written as signed two's-complement words; Q_p truncates real and imaginary parts toward zero to this grid, with error below √2·2^{−p} and no increase of norm.
  Shown as: Contractions and error accounting *<predicate>* Fixed-point complex coefficients and truncation

## Pages that build on this one

- Convolution from the retained transform layout: Two forward synthetic transforms in layout order, a pointwise ring product divided by r, the opposite transform and an exact scaling by M compute the normalized convolution (f*g)/T over the negacyclic ring with error below √2 M(3ℓ+1)2^{−p}.
- Gaussian resampling: Harvey–van der Hoeven technique that expresses a Fourier transform of coprime length s through a transform of the larger length t (a power of two) using Gaussian-weighted contractions A and B₀ and a Neumann-series inverse; the sorting permutations stay inside the transform identity.
- Precision budget and exact recovery: Scale bookkeeping (the two factors S) and the error bound 448 b 2^{−b+γ} < 1/2 show that each recovered convolution coefficient rounds to the true integer, which is below 2^{3b}, so carries give the exact product.

## Other pages you may link to

- [Multiplication complexity and the n log n conjecture](nlogn-history.md)
- [Fixed finite-alphabet multitape model](fixed-tape-model.md)
- [Established O(n log n) multiplier (subroutine)](established-multiplier.md)
- [Array order and elementary stream operations](stream-operations.md)
- [Controlled shifts](controlled-shifts.md)
- [Subspaces, orthogonality and rank](linear-algebra-prelims.md)
- [Linear network exchanging two banks with restored scratch values](xor-linear-network.md)
- [Subspace labels from three-element subsets](subset-labels.md)
- [Frames: changing the representation along a network](frames.md)
- [Rank deficit s < W m](rank-deficit.md)
- [Recursive power saving from the rank deficit](power-saving-recurrence.md)
- [Address shear from the bit network](bit-shear-interface.md)
- [Lower-triangular (Bruhat) factorization](lower-triangular-factorization.md)
- [Cost of a rational matrix shear](matrix-shear-cost.md)
- [Recursive power-width address interchange](power-width-interchange.md)
- [Address-chunk interchange in time O(V u^τ)](arbitrary-width-interchange.md)
- [Packed selected-bit addition](packed-selected-bit-addition.md)
- [Polynomial ring modulo y^r + 1](negacyclic-ring.md)
- [Signed packing of ring products](signed-packing-product.md)
- [Discrete Fourier transform](dft.md)
- [Two-point butterfly](butterfly.md)
- [Complex phase network and two-point kernels](phase-frame-network.md)
- [Simultaneous butterfly layer in time O(V d^λ′)](simultaneous-butterfly-layer.md)
- [Cyclic convolution and the convolution theorem](cyclic-convolution.md)
- [Multidimensional transforms and convolutions](multidimensional-dft.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Retained (bit-reversed) frequency order](retained-frequency-order.md)
- [Transform layout and cost](transform-layout.md)
- [Convolution from the retained transform layout](synthetic-convolution.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Tensor resampling on the padded box](padded-box-tensor-resampling.md)
- [Retained permutations and their cancellation](permutation-cancellation.md)
- [Integer multiplication as radix-digit convolution](radix-digit-convolution.md)
- [Chinese-remainder map to prime cyclic axes](crt-map.md)
- [Parameter choices and prime axis lengths](prime-axis-parameters.md)
- [Coefficient twist from cyclic to negacyclic](phase-twist.md)
- [Computed source transform](source-transform.md)
- [Precision budget and exact recovery](exact-recovery.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Complete time bound and power margins](cost-accounting.md)
- [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "adds their errors: at each step, insert the exact map at the computed" (paper)

  > een completed scalar routines, put $w_{\rm c}=p+2$. Represent $2^{-p}(a+ib)\in\mathbb D_p$ by a signed $w_{\rm c}$-bit two's-complement word for $a$, followed by one for $b$, with each word written most significant bit first. A coordinate list is the concatenation of these fixed-length records in its stated order. Since $|a|,|b|\leq2^p<2^{w_{\rm c}-1}$, this format includes both signs of every permitted numerator, including $-2^p$ and $2^p$. An approximation $\widetilde L:\mathbb D_p^a\to\mathbb D_p^b$ to a linear contraction $L:\mathbb C^a\to\mathbb C^b$ has error $E$ if $2^p\|\widetilde L u-Lu\|<E$ for every input in $\mathbb D_p^a$. The approximation itself need not be linear. Composing such algorithms adds their errors: at each step, insert the exact map at the computed input and use its contraction bound on the accumulated input error.

- "\|\mathcal M_r(f,g)\|_\infty" (paper)

  > For arrays on $\prod_i\mathbb Z/t_i\mathbb Z$ with values in $\mathcal R_r$, let $*$ denote cyclic convolution in the displayed axes and define \[ \mathcal M_r(f,g)=\frac{f*g}{rM}=\frac{f*g}{T}. \] For a fixed output coefficient, each of the $M$ first cyclic addresses determines one second address, and each of the $r$ first polynomial indices determines one second index modulo $r$. The negacyclic wrap supplies the sign. Thus that coefficient averages $rM$ signed scalar products, and $\mathcal M_r$ is a bilinear contraction: \[ \|\mathcal M_r(f,g)\|_\infty \leq\|f\|_\infty\|g\|_\infty. \] If the other operand is a disk array, replacing one operand changes the output by at most the norm distance between its two values.

- "For a bilinear contraction $\mathcal M$, replacing its operands gives" (paper)

  > Put $h_p=2^{-p}$, and use the coefficient sup norm throughout this subsection. An error of $a$ will mean absolute error less than $ah_p$. A linear contraction propagates an input error without increasing it. For a bilinear contraction $\mathcal M$, replacing its operands gives \[ \|\mathcal M(f',g')-\mathcal M(f,g)\| \le \|f'-f\|\,\|g'\|+\|f\|\,\|g'-g\|. \] When all four operands are in the disk, their two errors therefore add.


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

Write the body to `exegenius/tasks/0024-write-error-accounting.answer.md` and the JSON to `exegenius/tasks/0024-write-error-accounting.answer.json`, then run `exegenius submit 0024-write-error-accounting` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0024-write-error-accounting`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
