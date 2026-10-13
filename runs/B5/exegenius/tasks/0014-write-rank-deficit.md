# exegenius task 0014-write-rank-deficit

Project directory: `/home/user/openai-nlogn-wiki/runs/B5` (paths below are relative to it)

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

For these sources: An undergraduate computer science reader who has studied algorithm analysis (big-O, recurrences, sorting, divide and conquer including Karatsuba-style multiplication), discrete mathematics (modular arithmetic, gcd and coprimality, the Chinese remainder theorem in its basic form, permutations, binary representation), and calculus and linear algebra through matrices, Gaussian elimination and basic vector spaces. They know complex numbers and polynomials, and have seen simple Turing machines with tapes. They have not met the fast Fourier transform in depth beyond its name, finite-field or group-theoretic structure beyond Z/n, Kronecker products, or any research-level multiplication algorithms.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine
- The n log n conjecture and its history
  - $n$ (input length): The number of bits in each of the two integers being multiplied.
- Arrays on tape, address fields and volume
- Elementary stream operations
- Controlled shifts and rational scalings
- Rank, subspaces and orthogonal complements
- Cyclic convolution
- Integer product as digit convolution
- Bank-exchanging linear network with restored scratch
- Frames and the common-frame invariant
- Subspace labels from triple indicator vectors
- Logarithms and exponentials (also: lg, log base 2, log n, exp, powers of two)
- Floor and ceiling (also: floor function, ceiling function, rounding to nearest integer)
- Modular arithmetic (also: congruence, Z/nZ, integers modulo q, residues, remainder)
- Greatest common divisor and coprimality (also: gcd, relatively prime, pairwise coprime, units modulo q)
- Prime numbers (also: primes, prime factorization, odd prime, distribution of primes)
- Chinese remainder theorem (also: CRT)
- Binary representation and bit operations (also: bits, XOR, exclusive or, two's complement, bitwise operations, carries)
- Positional radix representation (also: base b digits, digit expansion, radix)
- Permutations (also: bijections, partial permutation, permutation matrix, transposition)
- Matrices and matrix products (also: matrix multiplication, invertible matrix, identity matrix, triangular matrix, transpose, Gaussian elimination)
- Vector spaces and linear maps (also: linear independence, dimension, kernel, image, basis, dot product)
- Finite field F2 (also: GF(2), integers mod 2, binary field)
- Euler's formula and complex exponentials (also: e^{i theta}, roots of unity, modulus, unit circle, Euler identity)
- Geometric series (also: sum of powers, geometric sum, sum of roots of unity)
- Gaussian function (also: Gaussian, bell curve, exp(-x^2), Gaussian weights)
- Basic calculus and inequalities (also: Taylor series, triangle inequality, Cauchy-Schwarz, limits, bounds on error)
- Fixed-point and rounding arithmetic (also: approximation error, truncation, precision bits, numerical error)
- Cartesian product and tuples (also: product of index sets, multi-index, d-dimensional array, lexicographic order)
- Cyclic groups and direct products (also: Z/n, additive group, group isomorphism, cyclic shift)
- Sorting (also: merge sort, sorting by key, comparison sort, O(N log N) sorting)
- Divide and conquer recurrences (also: master theorem, recurrence relation, recursion tree, induction)
- Karatsuba and schoolbook multiplication (also: long multiplication, grade-school multiplication, O(n^2) multiplication, Karatsuba algorithm)
- Fast Fourier transform idea (also: FFT, Cooley-Tukey, fast polynomial multiplication, evaluation and interpolation)
- Sums and indexed notation (also: summation, product notation, indicator function, Kronecker delta, subsets and set notation)

## This page

Concept: Rank deficit and the recursive power saving
Gloss: The edge residual dimensions sum to s<Wm, so a recursive call on m times more parameter uses s calls on 1/W of the volume, giving cost exponent below 1.
Heading: Rank deficit $s<Wm$

The symbols in this page's heading denote (say so on the page):

- $s$ (total smaller calls): The number of smaller recursive calls, equal to the sum of ranks of edge differences.
- $W$ (wire count): The number of wires in the fixed network.
- $m$ (label dimension): The number of coordinates of the fixed label space.

## This page in the argument

The step: Two fixed linear networks exchange two banks of values with signs and restore every auxiliary wire, and their edge residual dimensions sum to $s<Wm$, which gives the recursive power saving.
How: build a scalar exchange network, lift it to arrays with common frames, choose nested subspace labels that make each edge cheap, then compare the total residual with $Wm$
Why: The saving over plain scanning comes only from a network whose total edge rank is strictly below the number of wires times $m$. (the sources say so: "is the source of the power saving." (paper))
Striking feature: The saving is strict but tiny: the relative rank deficit is about 1e-11, so the power saving 1-2^{-50} is nonzero only because s<Wm strictly; the page should explain why the decreasing central-wire edges make the sum fall below Wm. (explain why it holds, from the method)

Its sub-steps, in order:

- Three stages of gather, side-injection and scatter send $(X_a,Y_a)$ to $(-Y_a,X_a)$ and restore all scratch wires, whatever their initial values. (on [Bank-exchanging linear network with restored scratch](scalar-network.md))
- With a common invertible frame at each gate, pointwise gates commute with it, so intermediate frames cancel and only the endpoint operators remain. (on [Frames and the common-frame invariant](frames.md))
- Labels built from three-element subsets are nested nondegenerate subspaces whose only decreasing edges are the central-wire edges, so edge residuals are small. (on [Subspace labels from triple indicator vectors](labels.md))
- The bit network with rational matrices at gates has endpoint difference $I_m$ on every role, giving the shear $H\gets H+D$ with total rank $s_{\rm b}<W_{\rm b}m$. (on [Bit network and rational shear interface](bit-interface.md))
- The complex network with binary labels has phase-frame changes that are products of kernels $aI+bX_v$ and telescope to $C^{\otimes m}$ on every role, with $s_{\rm c}<W_{\rm c}m$. (on [Phase frames and the kernel C=aI+bX](phase-interface.md))
- Both relative rank deficits are positive and large enough that $s/W<m^\tau$ for the fixed exponent $\tau=\sigma=1-2^{-50}$.

It serves these steps, from the main result down:

- Integer multiplication of $n$-bit integers takes $O(n(\lg n)^{1-\kappa})$ time on one deterministic fixed-tape machine, disproving the $n\log n$ conjecture.; how: build the fast tape primitives (address interchange and simultaneous butterfly layers), then the synthetic transform and convolution machinery, then the resampling reductions and the assembly with its cost table (on [Integer multiplication in O(n (lg n)^(1−κ))](main-theorem.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S1.6). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S1.6**: Both relative rank deficits are positive and large enough that $s/W<m^\tau$ for the fixed exponent $\tau=\sigma=1-2^{-50}$.
Source: "For both recurrences we may use the fixed rational exponent" (paper)
> The relative rank deficits are \[ \eta_{\rm b}=\frac{W_{\rm b}m-s_{\rm b}}{W_{\rm b}m} =\frac{339}{22587335000000},\qquad \eta_{\rm c}=\frac{W_{\rm c}m-s_{\rm c}}{W_{\rm c}m} =\frac{73}{19906842167500}. \] For both recurrences we may use the fixed rational exponent \begin{equation} \tau=\sigma=1-2^{-50}. \label{eq:explicit-motif-exponents} \end{equation} Both exact deficits displayed above are greater than $20\cdot2^{-50}$. Since $m<2^{20}$ and $\log 2<1$, we have $\log m<20$, whence \[ m^{1-2^{-50}} =m\exp(-2^{-50}\log m) >m(1-20\cdot2^{-50})>m(1-\eta) \] for either $\eta=\eta_{\rm b}$ or $\eta=\eta_{\rm c}$. Consequently \[ \frac{s_{\rm b}}{W_{\rm b}}<m^\tau, \qquad \frac{s_{\rm c}}{W_{\rm c}}<m^\sigma, \qquad 0<\tau=\sigma<1. \] Here $\sigma$ is a rational upper bound for the logarithmic exponent of the complex recurrence. \section{Faster interchange of address chunks} \label{sec:tape-interchange}

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S1.1 (on [Bank-exchanging linear network with restored scratch](scalar-network.md)): Three stages of gather, side-injection and scatter send $(X_a,Y_a)$ to $(-Y_a,X_a)$ and restore all scratch wires, whatever their initial values.
- S1.2 (on [Frames and the common-frame invariant](frames.md)): With a common invertible frame at each gate, pointwise gates commute with it, so intermediate frames cancel and only the endpoint operators remain.
- S1.3 (on [Subspace labels from triple indicator vectors](labels.md)): Labels built from three-element subsets are nested nondegenerate subspaces whose only decreasing edges are the central-wire edges, so edge residuals are small.
- S1.4 (on [Bit network and rational shear interface](bit-interface.md)): The bit network with rational matrices at gates has endpoint difference $I_m$ on every role, giving the shear $H\gets H+D$ with total rank $s_{\rm b}<W_{\rm b}m$.
- S1.5 (on [Phase frames and the kernel C=aI+bX](phase-interface.md)): The complex network with binary labels has phase-frame changes that are products of kernels $aI+bX_v$ and telescope to $C^{\otimes m}$ on every role, with $s_{\rm c}<W_{\rm c}m$.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Subspace labels from triple indicator vectors](labels.md): Nested nondegenerate subspaces built from three-element subsets of a fixed set, attached to gates so each edge's frame change costs its residual dimension.
  Shown as: Rank deficit and the recursive power saving *<predicate>* Subspace labels from triple indicator vectors

## Pages that build on this one

- Bit network and rational shear interface: The XOR network with rational matrices at gates whose endpoint difference is the identity, yielding the same shear H←H+D on every role.
- Phase frames and the kernel C=aI+bX: The Gaussian-dyadic network whose frame changes are products of translation kernels aI+bX_v, ending in C⊗m on every role.

## Other pages you may link to

- [The n log n conjecture and its history](nlogn-conjecture.md)
- [Cyclic convolution](convolution.md)
- [Integer product as digit convolution](radix-digit-mult.md)
- [Arrays on tape, address fields and volume](array-layout.md)
- [Elementary stream operations](stream-ops.md)
- [Controlled shifts and rational scalings](controlled-shifts.md)
- [Rank, subspaces and orthogonal complements](linear-algebra.md)
- [Bank-exchanging linear network with restored scratch](scalar-network.md)
- [Frames and the common-frame invariant](frames.md)
- [Bit network and rational shear interface](bit-interface.md)
- [Lower triangular factorization](bruhat.md)
- [Cost of a rational matrix shear](matrix-shear.md)
- [Power-width chunk interchange](power-interchange.md)
- [Fast interchange of address chunks](chunk-swap.md)
- [Packed selected-bit addition](packed-addition.md)
- [Polynomial ring modulo y^r+1](synthetic-ring.md)
- [Signed packing for ring products](signed-packing.md)
- [Discrete Fourier transform](dft.md)
- [Two-point butterfly](butterfly.md)
- [Phase frames and the kernel C=aI+bX](phase-interface.md)
- [Simultaneous butterfly layer](butterfly-layer.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Transform layout and cost](transform-layout.md)
- [Convolution from retained transform layout](synthetic-convolution.md)
- [Chinese-remainder address map](crt-map.md)
- [Coefficient phase twist](coefficient-twist.md)
- [Fixed-point error control](fixed-point-errors.md)
- [Gaussian resampling](resampling.md)
- [Multidimensional resampling](tensor-resampling.md)
- [Bluestein chirp and permutation cancellation](chirp.md)
- [Parameter choices and cost table](parameters-cost.md)
- [Integer multiplication in O(n (lg n)^(1−κ))](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "increases the recursive contribution by $s/W<m$." (paper)

  > A recursive call at parameter $mf$ therefore uses $s$ calls at parameter $f$, each on a stream of volume $V/W$. The parameter counts field digits for address interchange and selected axes for a numerical layer. After dividing cost by volume, multiplying the parameter by $m$ increases the recursive contribution by $s/W<m$. This strict inequality is the source of the power saving. The later tape and arithmetic estimates preserve it, including the work of changing numerical address coordinates. Those changes are implemented by whole-chunk moves and controlled shifts, followed by a deterministic correction of the explicitly identified exceptional addresses.


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

Write the body to `exegenius/tasks/0014-write-rank-deficit.answer.md` and the JSON to `exegenius/tasks/0014-write-rank-deficit.answer.json`, then run `exegenius submit 0014-write-rank-deficit` in the project directory. If submit rejects the answer, fix the answer and submit again.
