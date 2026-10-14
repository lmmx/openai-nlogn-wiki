# exegenius task 0021-write-cyclic-convolution

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F3V` (paths below are relative to it)

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

For these sources: The reader is an undergraduate in computer science who has taken discrete mathematics, data structures and algorithms, introductory theory of computation, and the linear algebra and calculus that accompany such a degree. They are fluent with asymptotic analysis, recurrences, binary representation and bitwise operations, modular arithmetic, matrices and rank, vector spaces over the reals, and complex numbers including roots of unity; they know the schoolbook and Karatsuba multiplication algorithms and what a Turing machine with tapes is. They have not studied abstract algebra beyond basics, the FFT's algebraic variants, number-theoretic transforms, finite fields beyond arithmetic mod 2, analytic number theory, numerical analysis of rounding error, or any bit-complexity multiplication algorithm.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine
- Schönhage–Strassen optimality conjecture
- Harvey–van der Hoeven O(n log n) multiplier
- Contractions and error accumulation
- Polynomial ring modulo y^r + 1 (also: negacyclic ring, R_r)
  - $y$ (ring variable): The formal polynomial variable, satisfying y^r = −1 in the ring.
  - $r$ (ring length): The number of complex coefficients in a ring element, a power of two.
- Signed Kronecker packing
- Arrays and elementary stream operations on tape
- Controlled shifts and rational scalings
- Bank-exchange network with restored scratch wires
- Frames on network wires
- Nested subspace labels and orthogonal residuals
- Strict rank saving
- Lower-triangular factorization of a matrix
- Cost of a matrix shear on address fields
- Power-width chunk interchange
- Address chunk interchange
  - $V$ (stored bit volume): The number of data bits stored in the array being permuted.
  - $u$ (chunk width): The number of bits in each of the two interchanged address chunks.
  - $\tau$ (interchange exponent): A fixed constant below one, 1 − 2^{−50}, bounding the power of the width in the cost.
- Packed selected-bit addition
- Exact dyadic intermediates with one truncation
- Asymptotic notation beyond big-O (also: Omega notation, Theta notation, little-o, o(...), Ω, Θ, asymptotically smaller, worst-case running time)
- Limits and limit inferior (also: liminf, limsup, limit of a ratio, lim inf, eventually, for all sufficiently large n)
- Logarithms, exponentials, floors and ceilings (also: log base 2, lg n, log_2, natural logarithm, floor function, ceiling function, powers of two, iterated logarithm, log star)
- Recurrences and geometric sums (also: recurrence relation, solving recurrences, geometric series, geometric sum, unrolling a recurrence, divide and conquer)
- Positional number systems and carries (also: binary representation, radix representation, base-b digits, bit string, most significant bit, carry propagation, schoolbook addition, padding with leading zeros)
- Schoolbook and Karatsuba multiplication (also: grade-school multiplication, long multiplication, Karatsuba, divide-and-conquer multiplication, Toom-Cook, quadratic multiplication)
- Bitwise operations and XOR (also: exclusive or, XOR, bitwise exclusive or, addition modulo 2, bit flip, parity, bit shift, bit mask)
- Modular arithmetic (also: integers modulo q, Z/qZ, congruence, residues, units modulo q, invertible residues, arithmetic mod q, Chinese remainder theorem for integers)
- Primes, coprimality and the extended Euclidean algorithm (also: prime numbers, relatively prime, pairwise coprime, gcd, greatest common divisor, Euclid's algorithm, Bezout identity, modular inverse, odd primes, primality testing by trial division)
- Roots of unity (also: primitive root of unity, nth roots of unity, e^{2πi/n}, unit complex numbers, complex exponential, Euler's formula, twiddle factor, N-th root of unity)
- Matrices and linear maps (also: matrix multiplication, matrix inverse, invertible matrix, linear operator, linear transformation, identity matrix, diagonal matrix, unitary or involution matrix, matrix-vector product, linear combination)
- Vector spaces, subspaces, dimension and rank (also: subspace, span, basis, linear independence, dimension, rank of a matrix, rank-nullity, kernel, image, column space, direct sum, quotient space)
- Inner products, bilinear forms and orthogonal complements (also: bilinear form, dot product, orthogonality, orthogonal complement, orthogonal subspace, nondegenerate pairing, inner product space, pairing)
- Gaussian elimination and triangular matrices (also: row reduction, LU decomposition, lower triangular matrix, upper triangular matrix, elementary row operations, back substitution, unit triangular matrix, row echelon form)
- Permutations, bijections and permutation matrices (also: permutation, bijection, one-to-one correspondence, inverse permutation, partial permutation, reordering of an array, sorting network, transposition of indices, permutation matrix)
- Arithmetic modulo 2 and linear algebra over F_2 (also: F_2, GF(2), binary field, field with two elements, matrices over F_2, GL(m, F_2), mod 2 arithmetic, boolean linear algebra)
- Finite sets, subsets and counting (also: Cartesian product, subset intersection, set cardinality, binomial coefficient, inclusion-exclusion, product of index sets, power set, three-element subsets, pigeonhole)
- Circuits and directed acyclic graphs (also: arithmetic circuit, linear circuit, wires and gates, directed graph, DAG, network of gates, fan-in, source and sink nodes, layered network)
- Vector norms and the triangle inequality (also: sup norm, maximum norm, infinity norm, ‖·‖_∞, modulus bound, triangle inequality, operator norm, error bound, disk bound)
- Fixed-point numbers, dyadic rationals and rounding (also: fixed point arithmetic, dyadic rational, binary fraction, rounding to nearest integer, truncation, round-off error, precision in bits, numbers with p fractional bits, grid of spacing 2^{-p})
- Row-major order and matrix transposition (also: row-major layout, array layout, transposing a matrix, matrix transpose, k×k binary matrix, lexicographic address, two-dimensional array as a list)
- Subroutines and reductions between problems (also: black-box subroutine, reduction, calling a subroutine, oracle call, problem reduction, conditional lower bound, composition of algorithms, uniform algorithm)
- Convolution of sequences (also: linear convolution, polynomial multiplication as convolution, product of coefficient sequences, discrete convolution, convolution theorem)

## This page

Concept: Cyclic convolution
Gloss: For arrays indexed by a product of cyclic groups, the product whose entry at address j is the sum of u_k v_{j−k} with all indices taken modulo the axis lengths.

## Where the argument relies on this page

- For arrays on $\prod_i\mathbb Z/t_i\mathbb Z$ with entries in $\mathcal R_r$, the normalised convolution $\mathcal M_r(f,g)=(f*g)/T$ is computed with error below $\sqrt2\,M(3\ell+1)2^{-p}$ by two forward synthetic transforms, pointwise polynomial products by Kronecker packing, and the opposite transform on the retained order. (on [Convolution over the polynomial ring](ring-convolution.md))
- The source Fourier transform $RF_{\boldsymbol s}$ on prime-length axes equals $2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ with cheap Gaussian contractions $\mathcal A,\mathcal B_0$ between the prime axes and the power-of-two axes, and the retained coordinate permutations never need to be executed.
- The factor $QF_{\boldsymbol t}$ equals $\overline a\cdot(a*(\overline a\cdot u))/T$ for the chirp $a_{\boldsymbol j}=\exp(-\pi i\sum_is_ij_i^2/t_i)$, and the retained source permutation cancels: $(RF^+_{\boldsymbol s})[(RF_{\boldsymbol s}u)\cdot(RF_{\boldsymbol s}v)]=(u*v)/S^2$ with $S=\prod_is_i$. (on [Retained permutations cancel in a convolution](permutation-cancellation.md))
- Digits of $x$ and $y$ are placed on prime cyclic axes by the Chinese-remainder map, transformed by Gaussian resampling around a chirp convolution over $\mathbb C[y]/(y^r+1)$, multiplied pointwise, transformed with opposite sign, rescaled, rounded and carried to give the exact $2n$-bit product. (on [The multiplication algorithm](multiplication-algorithm.md))
- Splitting $x$ and $y$ into $q=\lceil n/b\rceil$ radix-$2^b$ digits turns the product into a convolution of digit sequences with degree below $S$, so cyclic convolution of length $S$ has no wraparound, and every coefficient is below $2^{3b}$. (on [Integer product as digit convolution](radix-digit-convolution.md))
- The assignment $x\mapsto\prod_ix_i^{\mu_i}$ with $\mu_i=P_i^{-1}\bmod s_i$ is an algebra isomorphism from $\mathbb C[x]/(x^S-1)$ to $\mathbb C[x_1,\dots,x_d]/(x_i^{s_i}-1)$, carrying cyclic convolution of length $S=s_1\cdots s_d$ to convolution on the product of cyclic axes, and its action on padded addresses is a sequence of triangular controlled shifts costing $O(Tp\,d^2(1+\ell^\tau))$. (on [Chinese-remainder map to prime axes](crt-axis-map.md))
- With $\zeta=e^{\pi i/r}$, the map $x_d\mapsto\zeta y$ multiplies coefficient $k$ by $\zeta^k$ and is an isomorphism $\mathbb C[x_d]/(x_d^r-1)\to\mathbb C[y]/(y^r+1)$; the negative wrap of the negacyclic product gives exactly the cyclic wrap once the twist is removed. (on [Coefficient phase twist](phase-twist.md))

## Pages that build on this one

- Integer product as digit convolution: Splitting two integers into radix-2^b digits turns their product into a convolution of the digit sequences followed by carry propagation.
- Coefficient phase twist: Substituting x_d ↦ ζy with ζ = e^{πi/r} multiplies coefficient k by ζ^k and turns cyclic convolution of length r into negacyclic polynomial multiplication, exactly undone by untwisting.
- Discrete Fourier transform: The normalized transform (F_q u)_k = (1/q) Σ_j u_j e^{−2πi jk/q} (and its opposite-sign version) that turns cyclic convolution into pointwise multiplication.
- Bluestein chirp identity: A Fourier transform of even length t can be written as pointwise multiplication by a chirp phase a, a cyclic convolution with a, and another chirp multiplication.
- Multidimensional transform: The tensor product of one-dimensional transforms applied along each axis of an array whose axis lengths are t_1,…,t_D; convolution on the product of cyclic groups becomes pointwise multiplication.
- Chinese-remainder map to prime axes: An algebra isomorphism from cyclic convolution of length S = s_1⋯s_d (pairwise coprime) to convolution on the product of cyclic axes of lengths s_i, implemented by triangular controlled shifts.

## Other pages you may link to

- [Schönhage–Strassen optimality conjecture](schonhage-strassen-conjecture.md)
- [Harvey–van der Hoeven O(n log n) multiplier](hh-multiplier.md)
- [Arrays and elementary stream operations on tape](tape-stream-operations.md)
- [Controlled shifts and rational scalings](controlled-shift.md)
- [Bank-exchange network with restored scratch wires](exchange-network.md)
- [Frames on network wires](frames.md)
- [Nested subspace labels and orthogonal residuals](subspace-labels.md)
- [Strict rank saving](rank-saving.md)
- [Lower-triangular factorization of a matrix](matrix-factorization.md)
- [Cost of a matrix shear on address fields](matrix-shear.md)
- [Power-width chunk interchange](power-width-interchange.md)
- [Address chunk interchange](chunk-interchange.md)
- [Packed selected-bit addition](packed-selected-bit-addition.md)
- [Polynomial ring modulo y^r + 1](negacyclic-ring.md)
- [Signed Kronecker packing](kronecker-packing.md)
- [Contractions and error accumulation](contraction-error.md)
- [Exact dyadic intermediates with one truncation](guard-bits.md)
- [Integer product as digit convolution](radix-digit-convolution.md)
- [Coefficient phase twist](phase-twist.md)
- [Exact recovery by rounding and carries](exact-recovery.md)
- [Discrete Fourier transform](dft.md)
- [Two-point butterfly and radix-two recursion](fft-butterfly.md)
- [Bluestein chirp identity](chirp-identity.md)
- [Phase frames and the two-point kernel C](phase-frames.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Multidimensional transform](multidimensional-transform.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Stored bit-reversed frequency order](bit-reversed-order.md)
- [Transform layout and cost](transform-layout.md)
- [Convolution over the polynomial ring](ring-convolution.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Retained permutations cancel in a convolution](permutation-cancellation.md)
- [Chinese-remainder map to prime axes](crt-axis-map.md)
- [Prime axis lengths near powers of two](prime-axis-lengths.md)
- [Parameter choice for the multiplier](parameter-choice.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Complete time bound](time-bound.md)
- [Sub-n-log-n integer multiplication](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "cyclic convolution on the product of the coordinate groups" (paper)

  > The factor $QF_{\boldsymbol t}$ in \eqref{eq:no-sort-tensor} can be computed from a cyclic convolution and two pointwise phase multiplications. The chirp identity below performs the frequency change in $Q$ without applying $Q$ as a separate permutation of the array. The second identity shows how the retained source permutation $R$ cancels when computing a convolution. Here $*$ denotes cyclic convolution on the product of the coordinate groups and a dot denotes coordinatewise multiplication.


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

Write the body to `exegenius/tasks/0021-write-cyclic-convolution.answer.md` and the JSON to `exegenius/tasks/0021-write-cyclic-convolution.answer.json`, then run `exegenius submit 0021-write-cyclic-convolution` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0021-write-cyclic-convolution`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
