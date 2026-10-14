# exegenius task 0032-write-transform-layout

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e5/N5` (paths below are relative to it)

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

For these sources: The reader has an undergraduate computer science education: discrete mathematics (sets, permutations, modular arithmetic, gcd and the Chinese remainder theorem, induction, binomial coefficients), the algorithms course (asymptotic notation, recurrences, Karatsuba, the FFT and FFT-based polynomial multiplication, bit-reversal, binary counters, stacks), introductory computability (Turing machines with multiple tapes and constant-factor simulations), and the supporting mathematics of a CS degree: calculus with limits, exponentials and Newton's method, complex numbers, and a first linear algebra course (matrices, rank, invertibility, subspaces, dimension, dot products and orthogonality over the reals, Gaussian elimination). They have not studied bilinear forms over general fields, tensor products of operators, Bruhat factorizations, algebraic complexity of integer multiplication beyond Karatsuba and the basic FFT, or research-level fast multiplication (Schönhage–Strassen, Fürer, Harvey–van der Hoeven, Nussbaumer transforms, Gaussian resampling), nor index coding or the Frankl–Wilson construction.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine
- n log n optimality conjecture (also: Schönhage–Strassen conjecture)
- Harvey–van der Hoeven O(n log n) multiplier
- Normalized discrete Fourier transform (also: DFT, Fourier transform)
- Multidimensional Fourier transform
- Arrays on tape and logical volume (also: logical volume, row field)
- Elementary stream operations
- Controlled shifts and rational scalings (also: ordered affine updates)
- Linear network with wire roles (also: role, scratch wires)
- Restoration of arbitrary scratch values (also: transparent computation)
- Triple-intersection bank exchange (also: bit construction, complex construction, three-stage bank exchange)
- Frames and the common-frame identity (also: frame)
- Nested subspace labels and orthogonal residuals
- Rank deficit s < Wm
  - $s$ (smaller-call count): The total number of smaller recursive calls needed on all network edges (sum of edge ranks or residual dimensions).
  - $W$ (wire count): The number of wires (roles) in the fixed network, including scratch wires.
  - $m$ (label dimension): The dimension of the ambient label space, the number of address fields per chunk handled by one recursion level (here 10⁶).
- Recursive power saving
- Lower triangular factorization (also: Bruhat factorization)
- Address shear (also: matrix shear)
- Bit network interface
- Fast address-chunk interchange (also: chunk swap, address interchange)
- Normalized butterfly H₀ (also: butterfly)
  - $H_0$ (normalized butterfly): The 2×2 map sending a pair (u,v) to ((u+v)/2,(u−v)/2).
- Gaussian dyadic numbers
- Polynomial ring modulo y^r + 1 (also: negacyclic ring)
  - $y$ (polynomial variable): The indeterminate of the polynomial records, whose powers act as roots of unity.
  - $r$ (record length): The number of complex coefficients in each polynomial record, a power of two.
- Fixed-point disk grid and truncation (also: disk grid, precision p)
- Binary phase frames (also: complex phase network)
- Simultaneous butterfly layer
- Synthetic polynomial transform (also: Nussbaumer transform)
- Signed Kronecker packing (also: Kronecker substitution)
- Gaussian resampling with retained permutations
- Fixed rational parameters and cost table
- Asymptotic notation beyond big-O (also: Omega notation, Theta notation, little-o, o(n log n), Ω, Θ)
- Logarithms and exponents (also: log, lg, log base 2, binary logarithm, ceiling of log)
- Floor and ceiling (also: floor function, ceiling function, ⌊x⌋, ⌈x⌉, integer part)
- Binary representation of integers (also: base-2 representation, binary numeral, most significant bit, least significant bit, bin_k, bit string value, radix-q digits, positional notation)
- Schoolbook integer arithmetic with carries (also: grade-school multiplication, long multiplication, carry propagation, ripple-carry addition, binary addition)
- Two's complement and signed integers (also: signed binary integers, sign bit, negative numbers in binary)
- XOR and arithmetic modulo 2 (also: exclusive or, bitwise XOR, addition mod 2, parity, F_2 arithmetic, GF(2))
- Modular arithmetic (also: congruence modulo n, residues, mod, Z/nZ, integers modulo q^b, modular inverse, residue ring)
- Prime numbers and gcd (also: primes, greatest common divisor, coprime, relatively prime, prime to q)
- Euclidean algorithm (also: extended Euclidean algorithm, Bezout coefficients, computing modular inverses)
- Chinese remainder theorem (also: CRT, Chinese remaindering)
- Binomial coefficients and subsets (also: n choose k, binom, k-element subsets, combinations, set intersection, Cartesian product)
- Permutations (also: bijection, reordering, permutation of indices, inverse permutation, address permutation)
- Lexicographic order (also: dictionary order, row-major order, mixed-radix ordering)
- Vectors and matrices (also: matrix multiplication, matrix-vector product, identity matrix, diagonal matrix, transpose, row-major matrix, permutation matrix, triangular matrix)
- Linear maps and invertibility (also: linear transformation, linear operator, inverse matrix, invertible matrix, composition of linear maps, linear combination)
- Vector spaces, subspaces and dimension (also: subspace, span, basis, dimension, linear independence, nested subspaces)
- Rank of a matrix (also: matrix rank, column rank, row rank, full rank)
- Dot product and orthogonality (also: inner product, orthogonal vectors, orthonormal vectors, orthogonal complement, perpendicular)
- Gaussian elimination (also: row reduction, LU decomposition, elimination)
- Fields and rings (also: field, ring, rational numbers Q, integers Z, finite field, F_2)
- Fast Fourier transform (also: FFT, Cooley–Tukey FFT, radix-two FFT, inverse FFT)
- Polynomial multiplication via evaluation and interpolation (also: FFT-based polynomial multiplication, convolution theorem, coefficient vs point-value representation, multiplying polynomials with the FFT)
- Bit-reversal permutation (also: bit-reversed order, bit reversal)
- Karatsuba multiplication (also: Karatsuba algorithm, Karatsuba–Ofman)
- Divide-and-conquer recurrences (also: recurrence relation, master theorem, recursion tree, T(n)=aT(n/b)+f(n))
- Mathematical induction (also: proof by induction, induction on n, strong induction)
- Geometric series (also: geometric sum, sum of a geometric progression)
- Limits (also: limit, limit inferior, liminf, tends to infinity, asymptotically)
- Exponential function and Gaussians (also: exp, e^x, Gaussian function, e^{-x²}, Euler's formula, complex exponential)
- Absolute value and the triangle inequality (also: modulus of a complex number, |z|, triangle inequality, error bound)
- Rounding to the nearest integer (also: rounding, round-off, truncation error)
- Newton's method (also: Newton iteration, Newton–Raphson)
- Integer division and square root (also: quotient and remainder, division with remainder, floor of square root)
- Deterministic algorithm and worst-case running time (also: worst-case time, time complexity, deterministic, bit complexity, running time T(n))
- Stacks (also: push and pop, LIFO)
- Binary counter (also: counter increment, amortized counter, ripple counter)
- Hamming weight (also: popcount, number of ones, wt, bit count)
- Matrix transposition (also: transpose a matrix, transposition)
- Turing machine alphabet and simulation constants (also: tape alphabet, tracks, constant-factor simulation, finite control)

## This page

Concept: Fast synthetic transform layout
Gloss: A tape layout placing the selected bits of participating axes at a common offset in consecutive K-bit chunks so simultaneous butterfly layers apply, with chunk interchanges paying for the movement.

## This page in the argument

The step: Synthetic transforms over $\mathbb C[y]/(y^r+1)$ on $d-1$ power-of-two axes, with outputs kept in a stored frequency order, cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$ with error below $\sqrt2\ell\,2^{-p}$.
How: compute Nussbaumer's decimation-in-frequency recursion, group each round into a parallel butterfly plus a monomial, and lay the selected bits out in common-offset chunks for the simultaneous layer
Why: The simultaneous layer applies only to selected bits at a common offset in consecutive K-bit chunks, so a layout must be built and its movement charged. (the sources say so: "To apply Proposition~\ref{prop:simultaneous-layer} in a transform round, we must place the selected bits of the participating axes at a common offset in consecutive $K$-bit chunks." (paper))

Its sub-steps, in order:

- With root $\omega_t=y^{2r/t}$, decimation-in-frequency butterflies and signed shifts compute $B_tF_t^-$, writing the outputs directly in bit-reversed frequency order. (on [Synthetic polynomial transform](synthetic-transform.md))
- Each round on several axes is a parallel butterfly $\mathcal H$ followed by one recordwise monomial $J_E$.
- Moving prefix slots and interchanging chunks into the layout, and applying one simultaneous layer per round, gives the stated cost including layout construction and restoration.

It serves these steps, from the main result down:

- A single deterministic fixed-alphabet multitape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.; how: speed up address movement and butterfly arithmetic by recursive linear-network procedures, plug them into Harvey and van der Hoeven's reduction of multiplication to synthetic polynomial transforms, and bound the total cost (on [Integer multiplication below n log n](main-theorem.md))
- Cyclic convolution on distinct prime axes is computed from synthetic transforms over $\mathbb C[y]/(y^r+1)$, Gaussian resampling with retained permutations, and Bluestein chirps.; how: evaluate the needed transforms as synthetic polynomial transforms on a layout where the fast layers apply, and connect them to the prime-length transforms by resampling and chirps

## Steps this page derives

The argument gives this page these sub-steps of its step (S6.2, S6.3). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S6.2**: Each round on several axes is a parallel butterfly $\mathcal H$ followed by one recordwise monomial $J_E$.
Source: "Consequently the individual axis steps may be grouped as a parallel butterfly $\mathcal H$, followed by one recordwise monomial operation $J_E$." (paper)
> For $D$ axes of lengths $t_1,\ldots,t_D$, put \[ M=\prod_{i=1}^D t_i,\qquad F_{\boldsymbol t}^\pm=\bigotimes_{i=1}^D F_{t_i}^\pm, \qquad B=\bigotimes_{i=1}^D B_{t_i}. \] A round applies one current $H_0$ on each participating axis. The twiddle for axis $i$ depends only on that axis's address bits. The two entries paired by another axis's butterfly have the same axis-$i$ address, so that twiddle commutes with the other butterfly. Consequently the individual axis steps may be grouped as a parallel butterfly $\mathcal H$, followed by one recordwise monomial operation $J_E$. At each address, $J_E$ multiplies the record by \begin{equation} y^{E},\qquad E=-\sum_{i\ \mathrm{participating}} \frac{2r}{u_i}\,b_i k_i\pmod{2r}. \label{eq:combined-twiddle} \end{equation} Here $u_i$ is that axis's current recursive length, $b_i$ its newly written branch bit, and $0\leq k_i<u_i/2$ is encoded by its still unprocessed named slots. The exponent depends on the address, not on coefficient values. In the opposite direction the grouped round is $\mathcal HJ_E^{-1}$: apply $y^{-E}$ first and the parallel butterfly second. Each $\mathcal H$ is a contraction and each $J_E$ is an isometry, so every completed round is a contraction.

**S6.3**: Moving prefix slots and interchanging chunks into the layout, and applying one simultaneous layer per round, gives the stated cost including layout construction and restoration.
Source: "Both layout construction and final restoration are charged in this bound." (paper)
> The procedure constructs an explicit positional layout permutation $L$ of record addresses, preserving their polynomial suffixes, and transforms disk grid arrays of $M$ contiguous degree-less-than-$r$ polynomial records. Its exact counterpart is $LB F_{\boldsymbol t}^-$. Its opposite procedure consumes that order and has exact counterpart $F_{\boldsymbol t}^+B^{-1}L^{-1}$. Each procedure has error less than $\sqrt2\ell\,2^{-p}$, returns disk grid coefficients in the same component format, and costs \begin{equation} O\left(Tp\left[dK+pK^{\tau-1}+\ell d^{\lambda'}\right]\right). \label{eq:synthetic-transform-cost} \end{equation} Both layout construction and final restoration are charged in this bound. The forward procedure may retain its output layout for a pointwise product and the following opposite procedure. \end{lemma} \begin{proof} Put $D=d-1$ and write $a_i=\log_2t_i$. The supplied encoding has $2w=\Theta(p)$ bits per coefficient, so the logical bit volume is $\Theta(Tp)$. Call an axis long if $a_i=\ell$ and short if $a_i=\ell-1$. Name the original bit slots of axis $i$ by $(i,h)$, $a_i-1\geq h\geq0$. Initially these slots are in axis order and, within each axis, in decreasing $h$. The coefficients of each polynomial form a contiguous suffix. Put \[ b=(\ell-1)\bmod K, \qquad q=\lfloor(\ell-1)/K\rfloor. \] Form a list of the slots to move to a prefix. First list $(i,\ell-1)

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S6.1 (on [Synthetic polynomial transform](synthetic-transform.md)): With root $\omega_t=y^{2r/t}$, decimation-in-frequency butterflies and signed shifts compute $B_tF_t^-$, writing the outputs directly in bit-reversed frequency order.

### Other pages these steps use

Link each where the derivation uses it, stating what it gives; do not derive its results again.

- [Multidimensional Fourier transform](multidimensional-transform.md)
- [Fixed rational parameters and cost table](parameter-choice.md)

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Synthetic polynomial transform](synthetic-transform.md): Nussbaumer's Fourier transform over ℂ[y]/(y^r+1) using ω_t = y^{2r/t} as root of unity, computed by decimation-in-frequency butterflies and signed shifts, with outputs left in bit-reversed frequency order.
  Shown as: Fast synthetic transform layout *<predicate>* Synthetic polynomial transform
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): Applying H₀ on the same bit position in each of up to d equal-width address chunks costs O(V·d^λ′) with λ′ < 1, by recursing through the complex network's phase frames, with exact dyadic intermediates and one final truncation.
  Shown as: Fast synthetic transform layout *<predicate>* Simultaneous butterfly layer
- [Fast address-chunk interchange](fast-address-interchange.md): Interchanging two disjoint contiguous address fields of u bits in an array costs O(V·u^τ) with τ = 1 − 2⁻⁵⁰, realized by recursively applying the bit network and computing XOR combinations of data.
  Shown as: Fast synthetic transform layout *<predicate>* Fast address-chunk interchange

## Pages that build on this one

- Normalized convolution over the polynomial ring: Cyclic convolution of arrays with values in ℂ[y]/(y^r+1), computed by two forward synthetic transforms kept in stored frequency order, packed pointwise ring products, and the opposite transform.

## Other pages you may link to

- [n log n optimality conjecture](nlogn-conjecture.md)
- [Harvey–van der Hoeven O(n log n) multiplier](harvey-hoeven-multiplier.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring.md)
- [Normalized butterfly H₀](normalized-butterfly.md)
- [Gaussian dyadic numbers](gaussian-dyadics.md)
- [Linear network with wire roles](linear-network.md)
- [Frames and the common-frame identity](frames.md)
- [Arrays on tape and logical volume](tape-array-layout.md)
- [Elementary stream operations](elementary-streams.md)
- [Controlled shifts and rational scalings](controlled-shifts.md)
- [Restoration of arbitrary scratch values](scratch-restoration.md)
- [Triple-intersection bank exchange](triple-intersection-construction.md)
- [Nested subspace labels and orthogonal residuals](subspace-labels.md)
- [Rank deficit s < Wm](rank-deficit.md)
- [Recursive power saving](recursive-saving.md)
- [Binary phase frames](phase-frames.md)
- [Lower triangular factorization](triangular-factorization.md)
- [Address shear](address-shear.md)
- [Bit network interface](bit-network-interface.md)
- [Fixed-point disk grid and truncation](fixed-point-precision.md)
- [Signed Kronecker packing](signed-kronecker-packing.md)
- [Normalized discrete Fourier transform](discrete-fourier-transform.md)
- [Multidimensional Fourier transform](multidimensional-transform.md)
- [Gaussian resampling with retained permutations](gaussian-resampling.md)
- [Fixed rational parameters and cost table](parameter-choice.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Radix-digit reduction to convolution](radix-digit-convolution.md)
- [Chinese-remainder address map](crt-address-map.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Coefficient twist](coefficient-twist.md)
- [Normalized convolution over the polynomial ring](synthetic-convolution.md)
- [Exact coefficient recovery and carries](exact-recovery.md)
- [Integer multiplication below n log n](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "we must place the selected bits of the participating axes at a common offset in consecutive $K$-bit chunks." (paper)

  > To apply Proposition~\ref{prop:simultaneous-layer} in a transform round, we must place the selected bits of the participating axes at a common offset in consecutive $K$-bit chunks. We now construct that layout, keeping each polynomial's coefficients in a contiguous suffix. The layout uses the single-bit moves of Lemma~\ref{lem:elementary-streams} and the chunk interchanges of Lemma~\ref{lem:chunk-swap}; each movement is included in the transform cost. The layer then supplies one truncated contraction per round, and its temporary rows and work streams are removed before the next round begins.


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

Write the body to `exegenius/tasks/0032-write-transform-layout.answer.md` and the JSON to `exegenius/tasks/0032-write-transform-layout.answer.json`, then run `exegenius submit 0032-write-transform-layout` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0032-write-transform-layout`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
