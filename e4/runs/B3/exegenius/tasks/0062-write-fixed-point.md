# exegenius task 0062-write-fixed-point

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e4/B3` (paths below are relative to it)

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

For these sources: The reader is an undergraduate computer scientist: fluent with big-O and basic algorithm analysis (recurrences, divide and conquer, sorting and merging, schoolbook multiplication), discrete mathematics (sets, binomial coefficients, permutations, modular arithmetic, primes, gcd), and introductory linear algebra and complex numbers including roots of unity and polynomial arithmetic. They have seen single-tape and multitape Turing machines and tapes as a cost model, but not the discrete Fourier transform, FFT, fast integer multiplication, abstract algebra beyond residues, number-theoretic estimates such as the prime number theorem, or any research-level multiplication technique.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine
- Integer multiplication complexity and the n log n conjecture
- Subspaces, rank, orthogonal complements and bilinear forms
- Arrays on tape and elementary stream operations
- Controlled cyclic shifts and fixed rational scalings
- Polynomial ring modulo yʳ + 1
  - $y$ (ring variable): The formal polynomial variable, which satisfies y^r = -1 and serves as a root of unity.
  - $r$ (record length): The number of complex coefficients in a ring element, a power of two.
  - $\mathbb C$ (complex numbers): The field of complex numbers from which the coefficients are drawn.
- Linear exchange network with restored scratch wires (also: finite network)
- Three-element-subset gather/scatter gadget
- Frames: changing the representation along network edges
- Subspace labels and the rank saving s < Wm
  - $s$ (total rank): The sum over all network edges of the rank of the frame difference, equal to the number of smaller calls needed.
  - $W$ (wire count): The number of wires, including scratch wires, in the fixed network.
  - $m$ (label dimension): The dimension of the fixed space whose subspaces label the gates.
- Bit network and the address shear
- Lower-triangular (Bruhat) factorization (also: Bruhat factorization)
- Cost of a rational matrix shear
- Power-width chunk interchange and the recursive saving
- Chunk interchange in O(V uᵗ) time
  - $V$ (stored bit volume): The number of stored data bits in the array being rearranged.
  - $u$ (chunk width): The number of bits in each of the two address chunks being interchanged.
  - $\tau$ (interchange exponent): A fixed constant below 1, here 1-2^{-50}, controlling the saving.
- Complex phase network and the C kernel
- Packed addition of selected address bits
- Binary representation of integers (also: binary expansion, bit string, bits, radix representation, base-b digits, val(x))
- Modular arithmetic (also: congruence, residues mod m, mod, residue ring Z/mZ, centered residue, modular inverse)
- Primes, divisibility, coprimality and gcd (also: prime numbers, relatively prime, coprime, pairwise coprime, greatest common divisor, Euclidean algorithm, extended Euclidean algorithm, trial division)
- Logarithms, floors and ceilings (also: log base 2, lg, binary logarithm, floor, ceiling, natural logarithm, powers of two)
- Divide and conquer and recurrences (also: recursion, recurrence relation, master theorem, geometric series, unrolling a recurrence, induction)
- Sorting, merging and radix sort (also: merge sort, stable sort, radix sorting, counting sort, merge, sorting by keys)
- Schoolbook multiplication and carries (also: long multiplication, grade-school multiplication, carry propagation, quadratic multiplication, Karatsuba)
- Permutations (also: permutation of coordinates, bijection, reordering, partial permutation, transposition, inverse permutation)
- Sets, subsets and binomial coefficients (also: n choose k, binomial coefficient, counting subsets, cardinality, intersection of sets, indicator vector, ground set)
- XOR and mod 2 arithmetic (also: bitwise XOR, exclusive or, GF(2) addition, addition mod 2, bitwise operations, F2 arithmetic)
- Hamming weight (also: wt(x), population count, popcount, number of one bits)
- Matrices and matrix-vector products (also: matrix multiplication, identity matrix, invertible matrix, transpose, diagonal matrix, lower-triangular matrix, Gaussian elimination, block matrix)
- Vector norms and the triangle inequality (also: maximum norm, sup norm, absolute value of a complex number, modulus, triangle inequality, operator norm)
- Lexicographic order and mixed-radix indexing (also: lexicographic order, dictionary order, row-major order, multi-index, mixed radix, Cartesian product, most significant coordinate)
- Two's complement and signed integers (also: signed integer encoding, sign-magnitude, sign extension)
- Dyadic and rational numbers (also: dyadic rational, rational numbers, fractions with power-of-two denominator, exact arithmetic)
- Euler's formula and complex conjugation (also: e^{i theta}, complex conjugate, unit circle, real and imaginary parts, Gaussian integers)
- Tape-based subroutines and stacks (also: subroutine call, call stack, program counter, work tape, scanning a tape, tape copying and reversal)
- Constant factors versus asymptotic dominance (also: little-o, Theta notation, Omega notation, o(1), for sufficiently large n, polylogarithmic, dominant term)

## This page

Concept: Fixed-point complex grid and truncation
Gloss: Complex numbers are stored as pairs of signed two's-complement integers scaled by 2^{-p}; the truncation Q_p rounds each part toward zero to this grid with error below √2·2^{-p}.

## Where the argument relies on this page

- Applying $H_0$ to the same bit position in $d$ address chunks of polynomial records at once, exactly in Gaussian dyadics with a single final truncation, costs $O(Vd^{\lambda'})$ with $\lambda'<1$. (on [Simultaneous butterfly layer in O(V d^λ′) time](simultaneous-layer.md))
- Intermediate values of a layer stay exact Gaussian dyadics of width $O(p)$ with explicit guard bits, so only one final truncation is needed.
- The procedure returns $Q_p(\mathcal Hz)$ with error below $\sqrt2\,2^{-p}$ in $O(Vd^{\lambda'})$ time.
- Polynomials with small signed coefficients are evaluated at a large power of two, multiplied with the established $O(N\log N)$ integer multiplier, and recovered by centered residues, giving normalized ring products in $O(rp\log(rp))$. (on [Signed packing (Kronecker substitution) of ring products](signed-packing.md))
- The source transform $RF_{\boldsymbol s}$ is computed by the Gaussian map $\mathcal A$ on each line, the chirp transform by complex convolution, the Gaussian map $\mathcal B_0$, and scaling by $2^\gamma$; the opposite sign comes by complex conjugation. (on [Computed source transform](source-transform.md))
- After removing the known scales each recovered digit-convolution coefficient has error below $1/2$, so rounding gives the exact integer coefficients and radix-$2^b$ carries give the $2n$-bit product. (on [Exact recovery by rounding and carry propagation](exact-recovery.md))

## Pages that build on this one

- Signed packing (Kronecker substitution) of ring products: Polynomials with small signed coefficients are evaluated at a large power of two to give integers, multiplied by the established O(N log N) integer multiplier as a subroutine, and the product coefficients are recovered by centered residues, giving normalized ring products in O(rp log(rp)).
- Simultaneous butterfly layer in O(V d^λ′) time: Applying H₀ to the same bit position in d address chunks of polynomial records at once, exactly in Gaussian dyadics with guard bits and one final truncation, costs O(V d^{λ′}) with λ′<1 instead of d passes.
- Contractions and error accumulation: A linear map that does not increase the maximum coefficient norm is a contraction; errors of composed approximations add, and for a bilinear contraction the error is bounded by ‖Δf‖‖g′‖+‖f‖‖Δg‖.
- Exact recovery by rounding and carry propagation: After removing the known scales, each recovered digit-convolution coefficient has error below 1/2, so rounding gives the exact integer coefficients and radix-2^b carries give the 2n-bit product.

## Other pages you may link to

- [Integer multiplication complexity and the n log n conjecture](history.md)
- [Arrays on tape and elementary stream operations](stream-ops.md)
- [Controlled cyclic shifts and fixed rational scalings](controlled-shift.md)
- [Subspaces, rank, orthogonal complements and bilinear forms](linear-algebra.md)
- [Linear exchange network with restored scratch wires](linear-network.md)
- [Frames: changing the representation along network edges](frames.md)
- [Three-element-subset gather/scatter gadget](subset-gadget.md)
- [Subspace labels and the rank saving s < Wm](rank-saving.md)
- [Bit network and the address shear](bit-network-shear.md)
- [Complex phase network and the C kernel](complex-phase-network.md)
- [Lower-triangular (Bruhat) factorization](triangular-factorization.md)
- [Cost of a rational matrix shear](matrix-shear.md)
- [Power-width chunk interchange and the recursive saving](power-width-interchange.md)
- [Chunk interchange in O(V uᵗ) time](chunk-interchange.md)
- [Packed addition of selected address bits](packed-bit-addition.md)
- [Polynomial ring modulo yʳ + 1](ring-mod-yr.md)
- [Signed packing (Kronecker substitution) of ring products](signed-packing.md)
- [Discrete Fourier transform](dft.md)
- [Butterfly (decimation-in-frequency) transform](butterfly-fft.md)
- [Phase frames reduce a butterfly layer to C kernels](phase-frame-reduction.md)
- [Simultaneous butterfly layer in O(V d^λ′) time](simultaneous-layer.md)
- [Contractions and error accumulation](contraction-error.md)
- [Cyclic convolution and the convolution theorem](convolution.md)
- [Multidimensional transforms (tensor products)](multidim-transform.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Chinese-remainder map to distinct prime axes](crt-map.md)
- [Bluestein chirp identity](bluestein.md)
- [Phase twist from cyclic to negacyclic wrap](phase-twist.md)
- [Synthetic transform layout and retained frequency order](transform-layout.md)
- [Normalized convolution over the ring from the retained layout](ring-convolution.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Resampling with the permutations left in the transform](retained-permutations.md)
- [Integer product as convolution of radix digits](integer-as-convolution.md)
- [Exact recovery by rounding and carry propagation](exact-recovery.md)
- [Parameter choices, padded box and prime source lengths](parameters.md)
- [Complex cyclic convolution via the coefficient twist](complex-convolution-twist.md)
- [Computed source transform](source-transform.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Cost table and the κ margin](cost-accounting.md)
- [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "$p$-bit grid array has real and imaginary coefficient parts in" (paper)

  > For an integer $r\geq 2$ that is a power of two, put \[ \mathcal R_r=\mathbb C[y]/(y^r+1),\qquad \left\|\sum_{k=0}^{r-1}z_k y^k\right\|_\infty =\max_{0\leq k<r}|z_k|. \] We always use representatives of degree less than $r$. Multiplication by $y^a$, for any integer $a$, permutes the coefficients and changes some signs; consequently it is an isometry for this norm. For arrays over $\mathcal R_r$, the same notation denotes the maximum over all coefficients in all entries. A disk array has norm at most one. A $p$-bit grid array has real and imaginary coefficient parts in $2^{-p}\mathbb Z$. For any array, let $Q_p$ truncate each real and imaginary coefficient part toward zero to this grid. Then \begin{equation} \|Q_p z-z\|_\infty<\sqrt2\,2^{-p},\qquad \|Q_p z\|_\infty\leq\|z\|_\infty. \label{eq:transform-truncate} \end{equation}

- "\|Q_p z-z\|_\infty<\sqrt2\,2^{-p}" (paper)

  > For an integer $r\geq 2$ that is a power of two, put \[ \mathcal R_r=\mathbb C[y]/(y^r+1),\qquad \left\|\sum_{k=0}^{r-1}z_k y^k\right\|_\infty =\max_{0\leq k<r}|z_k|. \] We always use representatives of degree less than $r$. Multiplication by $y^a$, for any integer $a$, permutes the coefficients and changes some signs; consequently it is an isometry for this norm. For arrays over $\mathcal R_r$, the same notation denotes the maximum over all coefficients in all entries. A disk array has norm at most one. A $p$-bit grid array has real and imaginary coefficient parts in $2^{-p}\mathbb Z$. For any array, let $Q_p$ truncate each real and imaginary coefficient part toward zero to this grid. Then \begin{equation} \|Q_p z-z\|_\infty<\sqrt2\,2^{-p},\qquad \|Q_p z\|_\infty\leq\|z\|_\infty. \label{eq:transform-truncate} \end{equation}


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

Write the body to `exegenius/tasks/0062-write-fixed-point.answer.md` and the JSON to `exegenius/tasks/0062-write-fixed-point.answer.json`, then run `exegenius submit 0062-write-fixed-point` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0062-write-fixed-point`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
