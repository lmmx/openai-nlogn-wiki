# exegenius task 0032-write-fixed-point-numerics

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F5B` (paths below are relative to it)

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

For these sources: The reader has an undergraduate computer science education: discrete mathematics (sets, counting, induction, primes, gcd), a first algorithms course (divide and conquer, recurrences, sorting, Karatsuba multiplication, schoolbook arithmetic) and complexity (big-O family, single- and multitape Turing machines), together with calculus (exponentials, logarithms, series), linear algebra over the reals and complex numbers, and polynomials. They have not met Fourier transforms or the FFT in depth, finite fields beyond arithmetic mod 2, bilinear forms over arbitrary fields, number-theoretic estimates such as prime density, or any research-level multiplication algorithm; those are what the wiki must explain.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes
- Binary integers
- Modular arithmetic
- Matrices, rank and linear maps
- Fixed-tape Turing machine model
- Arrays, address fields and logical volume
- Elementary stream operations
- Controlled cyclic shifts and rational scalings
- Cyclic convolution
- Normalized discrete Fourier transform
- Multidimensional transforms and convolution on several axes
- Integer multiplication as digit convolution
- Established O(n log n) integer multiplier
- The n log n optimality conjecture
- Polynomial ring modulo y^r + 1
  - $y$ (ring variable): The formal variable of the polynomials, which satisfies y^r = −1 in the quotient.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Synthetic polynomial transform
- Decimation-in-frequency butterflies and bit-reversed frequency order
- Bluestein chirp identity
- Role networks and frames
- Restoring arbitrary scratch values
- Three-subset gather and scatter network
- Nondegenerate subspaces and orthogonal residuals
- Subspace labels and the rank budget
- Rank saving and the power-saving recurrence
- Lower-triangular factorization of a matrix
- Cost of a rational matrix shear
- Bit network as an address shear
- Power-width address interchange
- Fast interchange of address chunks
- Two-point butterfly H₀ and the kernel C
- Binary phase frames
- Packed selected-bit addition
- Big-Theta, big-Omega and little-o notation (also: Theta, Omega, Θ, Ω, little-o, o(1), asymptotic notation)
- Divide-and-conquer recurrences (also: recurrence relation, master theorem, recursion tree, solving recurrences)
- Schoolbook and Karatsuba multiplication (also: long multiplication, Karatsuba, Toom-Cook, grade-school multiplication)
- Positional notation in any radix and mixed radix (also: radix-q digits, base-q representation, mixed-radix expansion, digit string, most significant digit)
- Bitwise operations, XOR and Hamming weight (also: XOR, exclusive or, addition mod 2, bit parity, wt, popcount, Hamming weight)
- Floor, ceiling and rounding (also: ⌊x⌋, ⌈x⌉, round to nearest integer, integer part)
- Exponential and logarithm functions (also: log base 2, lg, natural logarithm, ln, exp, e^x, Gaussian function)
- Convergent series and the geometric series (also: absolutely convergent sum, infinite sum, geometric series, tail bound, series convergence)
- Prime numbers, coprimality and trial division (also: relatively prime, pairwise coprime, gcd, odd prime, primality by trial division, unique factorization)
- Extended Euclidean algorithm (also: Euclid's algorithm, Bezout identity, computing modular inverses)
- Counting subsets and binomial coefficients (also: n choose k, binomial coefficient, k-subsets, inclusion-exclusion, ground set)
- Permutations and permutation matrices (also: bijection of indices, reordering of coordinates, involution, permutation of positions, partial permutation)
- Lexicographic order and Cartesian products of index sets (also: lexicographic order, product of ranges, multi-index, tuple addressing, row-major order)
- Vector norms, inner products and orthogonality (also: maximum norm, sup norm, infinity norm, triangle inequality, dot product, orthonormal basis, orthogonal complement, isometry)
- Gaussian elimination (also: row reduction, row operations, elementary matrices, echelon form)
- Dyadic rationals and binary fractions (also: dyadic numbers, numbers m/2^k, binary point, fixed-point numbers, Gaussian dyadics, Gaussian integers)
- Stable radix sort and counting sort (also: bit sorting, stable sorting, radix sorting, sorting by a key digit)
- Mathematical induction (also: induction on k, proof by induction, recursive construction)

## This page

Concept: Fixed-point complex arithmetic and truncation error
Gloss: Complex values are stored as pairs of signed integers over a 2^p grid inside the unit disk, truncated toward zero by Q_p; contractions pass errors through unchanged and errors of composed steps add.

## Where the argument relies on this page

- Two $n$-bit integers are multiplied exactly by one deterministic fixed-tape Turing machine in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$. (on [Integer multiplication below n log n](main-theorem.md))
- One $H_0$ butterfly can be applied at the same bit offset in $D\le d$ address chunks at once, computed exactly with a single final truncation, in $O(Vd^{\lambda'})$ time. (on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md))
- Normalized convolution over $\mathbb C[y]/(y^r+1)$ is computed by two forward synthetic transforms, pointwise polynomial products in the retained frequency order, and the opposite transform, with explicit error bound. (on [Convolution from the retained transform layout](ring-convolution.md))
- A positional permutation moves selected bits of the $d-1$ axes of an array of $M$ polynomial records to a common offset in $K$-bit chunks so each transform round is one simultaneous layer, giving forward and opposite synthetic transforms costing $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$ that keep the frequency order for a pointwise product. (on [Transform layout and cost](transform-layout.md))
- A product of two disk-grid polynomials is computed exactly by evaluating their integer parts at the base $2^{4p}$, multiplying the resulting integers with the $O(N\log N)$ multiplier, and reading centered coefficients back out, then wrapping modulo $y^r+1$. (on [Signed packing (Kronecker substitution)](signed-packing.md))
- There are linear contractions $A$ and $B_0$ with $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$, computable by fixed multitape algorithms with error below $p^2$ in time $O(tp^{3/2+\delta}\alpha)$, which expresses a transform of coprime length $s$ through one of length $t$. (on [Gaussian resampling](gaussian-resampling.md))
- Applying the one-dimensional maps line by line along each axis of a zero-padded power-of-two box gives $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ with error below $dp^2$, at cost $O(dTp^{3/2+\delta}\alpha)$ plus the chunk interchanges that expose the axes. (on [Tensor resampling on a padded box](tensor-resampling-box.md))
- Multiplying coefficient $k$ by $\zeta^k$ with $\zeta=e^{\pi i/r}$ maps $\mathbb C[x]/(x^r-1)$ isomorphically onto $\mathbb C[y]/(y^r+1)$, so the last cyclic axis is convolved over the ring and then untwisted. (on [Phase twist from cyclic to negacyclic](coefficient-twist.md))
- The computed source transform applies the linewise Gaussian map $A$, the chirp transform done by complex convolution through the twist, the linewise map $B_0$, and an exact $2^\gamma$ rescale, approximating $RF_{\boldsymbol s}$. (on [Source Fourier transform procedure](source-transform.md))
- Split the operands into radix-$2^b$ digits, map them by $\Phi$ to prime axes, apply the source transform to each, multiply pointwise, apply the opposite transform, rescale by $S$ and $2^{2b+4}$, round to integers, undo $\Phi$ and propagate carries. (on [The multiplication algorithm](multiplication-algorithm.md))
- Disk-margin and error bookkeeping show that the recovered coefficient error stays below $1/2$, so rounding gives the exact integer convolution coefficients and carries give the exact binary product. (on [Precision and exact recovery](exact-recovery.md))

## Pages that build on this one

- Simultaneous butterfly layer: One H₀ butterfly applied at the same bit offset in D ≤ d address chunks at once, computed exactly via the phase network with recursive calls on 1/m of the axes and a single final truncation, in O(V d^{λ'}) time with λ' < 1.
- Signed packing (Kronecker substitution): A product of two disk-grid polynomials is computed exactly by evaluating their integer parts at a large base 2^{4p}, multiplying the resulting integers with the O(N log N) multiplier, and reading centered coefficients back out, then wrapping modulo y^r + 1.
- Gaussian resampling: Harvey–van der Hoeven's method expressing a Fourier transform of coprime length s through one of a nearby power-of-two length t via Gaussian-weighted contractions A and B₀, with the two coordinate permutations left inside the identity.
- Source Fourier transform procedure: The computed transform for a coprime-length source: linewise Gaussian map A, the chirp transform done by complex convolution through the phase twist, linewise map B₀, and an exact 2^γ rescale, approximating R F_s.
- Precision and exact recovery: Disk-margin and error bookkeeping shows the recovered coefficient error stays below 1/2, so rounding gives the exact integer convolution coefficients and carries give the exact binary product.

## Other pages you may link to

- [Two-point butterfly H₀ and the kernel C](two-point-butterfly.md)
- [Fixed-tape Turing machine model](multitape-model.md)
- [Established O(n log n) integer multiplier](nlogn-multiplier.md)
- [The n log n optimality conjecture](nlogn-conjecture.md)
- [Arrays, address fields and logical volume](array-layout.md)
- [Role networks and frames](gate-network-frames.md)
- [Elementary stream operations](elementary-streams.md)
- [Controlled cyclic shifts and rational scalings](controlled-shifts.md)
- [Restoring arbitrary scratch values](scratch-restoration.md)
- [Three-subset gather and scatter network](subset-intersection-network.md)
- [Nondegenerate subspaces and orthogonal residuals](nondegenerate-subspaces.md)
- [Subspace labels and the rank budget](subspace-labels.md)
- [Rank saving and the power-saving recurrence](rank-saving-recurrence.md)
- [Bit network as an address shear](bit-network-interface.md)
- [Binary phase frames](phase-interface.md)
- [Lower-triangular factorization of a matrix](lower-triangular-factorization.md)
- [Cost of a rational matrix shear](matrix-shear-cost.md)
- [Power-width address interchange](power-width-interchange.md)
- [Fast interchange of address chunks](chunk-interchange.md)
- [Packed selected-bit addition](packed-selected-bit-addition.md)
- [Polynomial ring modulo y^r + 1](negacyclic-ring.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Integer multiplication as digit convolution](radix-digit-convolution.md)
- [Normalized discrete Fourier transform](discrete-fourier-transform.md)
- [Multidimensional transforms and convolution on several axes](multidimensional-transform.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Decimation-in-frequency butterflies and bit-reversed frequency order](butterfly-recursion.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Transform layout and cost](transform-layout.md)
- [Signed packing (Kronecker substitution)](signed-packing.md)
- [Convolution from the retained transform layout](ring-convolution.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Cancellation of the retained source permutation](permutation-cancellation.md)
- [Tensor resampling on a padded box](tensor-resampling-box.md)
- [Choosing prime source lengths](prime-lengths.md)
- [Size parameters of the multiplication](size-parameters.md)
- [Chinese-remainder map to prime cyclic axes](crt-prime-axes.md)
- [Phase twist from cyclic to negacyclic](coefficient-twist.md)
- [Source Fourier transform procedure](source-transform.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Precision and exact recovery](exact-recovery.md)
- [Cost table and the saving exponent κ](time-accounting.md)
- [Integer multiplication below n log n](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "\mathbb D_p=\{2^{-p}(a+ib):a,b\in\mathbb Z,\ a^2+b^2\leq 2^{2p}\}" (paper)

  > For an integer $q\geq 1$, write \[ (F_q u)_k=\frac1q\sum_{j=0}^{q-1}u_j e^{-2\pi i jk/q}, \qquad (F_q^+ u)_k=\frac1q\sum_{j=0}^{q-1}u_j e^{2\pi i jk/q}. \] All subscripts on a vector of length $q$ are taken modulo $q$. The vector norm is the maximum modulus of its coordinates. All operator norms are induced by this norm: $\|L\|=\sup_{\|u\|\leq1}\|Lu\|$. Each normalized Fourier transform above is a contraction, since each output averages inputs multiplied by complex numbers of modulus one. Coordinate permutations preserve the norm. For an integer precision $p\geq1$, put \[ \mathbb D_p=\{2^{-p}(a+ib):a,b\in\mathbb Z,\ a^2+b^2\leq 2^{2p}\}. \] For storage between completed scalar routines, put $w_{\rm c}=p+2$. Represent $2^{-p}(a+ib)\in\mathbb D_p$ by a signed $w_{\rm c}$-bit two's-complement word for $a$, followed by one for $b$, with each word written most significant bit first. A coordinate list is the concatenation of these fixed-length records in its stated order. Since $|a|,|b|\leq2^p<2^{w_{\rm c}-1}$, this format includes both signs of every permitted numerator, including $-2^p$ and $2^p$. An approximation $\widetilde L:\mathbb D_p^a\to\mathbb D_p^b$ to a linear contraction $L:\mathbb C^a\to\mathbb C^b$ has error $E$ if $2^p\|\widetilde L u-Lu\|<E$ for every input in $\mathbb D_p^a$. The approximation itself need not be linear. Composi

- "Composing such algorithms adds their errors" (paper)

  > 2+b^2\leq 2^{2p}\}. \] For storage between completed scalar routines, put $w_{\rm c}=p+2$. Represent $2^{-p}(a+ib)\in\mathbb D_p$ by a signed $w_{\rm c}$-bit two's-complement word for $a$, followed by one for $b$, with each word written most significant bit first. A coordinate list is the concatenation of these fixed-length records in its stated order. Since $|a|,|b|\leq2^p<2^{w_{\rm c}-1}$, this format includes both signs of every permitted numerator, including $-2^p$ and $2^p$. An approximation $\widetilde L:\mathbb D_p^a\to\mathbb D_p^b$ to a linear contraction $L:\mathbb C^a\to\mathbb C^b$ has error $E$ if $2^p\|\widetilde L u-Lu\|<E$ for every input in $\mathbb D_p^a$. The approximation itself need not be linear. Composing such algorithms adds their errors: at each step, insert the exact map at the computed input and use its contraction bound on the accumulated input error.


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

Write the body to `exegenius/tasks/0032-write-fixed-point-numerics.answer.md` and the JSON to `exegenius/tasks/0032-write-fixed-point-numerics.answer.json`, then run `exegenius submit 0032-write-fixed-point-numerics` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0032-write-fixed-point-numerics`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
