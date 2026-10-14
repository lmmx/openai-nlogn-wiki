# exegenius task 0015-write-triple-intersection-construction

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
- Arrays on tape and logical volume (also: logical volume, row field)
- Elementary stream operations
- Controlled shifts and rational scalings (also: ordered affine updates)
- Linear network with wire roles (also: role, scratch wires)
- Restoration of arbitrary scratch values (also: transparent computation)
- Frames and the common-frame identity (also: frame)
- Normalized butterfly H₀ (also: butterfly)
  - $H_0$ (normalized butterfly): The 2×2 map sending a pair (u,v) to ((u+v)/2,(u−v)/2).
- Gaussian dyadic numbers
- Polynomial ring modulo y^r + 1 (also: negacyclic ring)
  - $y$ (polynomial variable): The indeterminate of the polynomial records, whose powers act as roots of unity.
  - $r$ (record length): The number of complex coefficients in each polynomial record, a power of two.
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

Concept: Triple-intersection bank exchange
Gloss: Two networks indexed by three-element subsets of [100], where gather/scatter through central wires produce coefficients depending on intersection size and side wires cancel the unwanted ones, giving y ← y + x; three stages then exchange banks (X,Y) ↦ (−Y,X).
Also called: bit construction, complex construction, three-stage bank exchange

## This page in the argument

The step: Gather/scatter through central wires gives coefficients depending on $|S\cap T|$, side wires cancel the unwanted ones so each invocation is $y\gets y+x$, and three stages give $(X,Y)\mapsto(-Y,X)$.

It serves these steps, from the main result down:

- A single deterministic fixed-alphabet multitape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.; how: speed up address movement and butterfly arithmetic by recursive linear-network procedures, plug them into Harvey and van der Hoeven's reduction of multiplication to synthetic polynomial transforms, and bound the total cost (on [Integer multiplication below n log n](main-theorem.md))
- Address-field interchange costs $O(Vu^\tau)$ and a simultaneous butterfly layer costs $O(Vd^{\lambda'})$, with fixed $\tau,\lambda'<1$, where $V$ is the stored bit volume.; how: turn a strict rank deficit of two finite linear networks into recursive power savings for both tape procedures
- There are two fixed linear networks, one over $\mathbb F_2$ and one over $\mathbb Z[i,1/2]$, each with $W$ wires, that exchange two banks of values, restore all scratch values, and admit nested subspace labels whose edge changes need only $s<Wm$ smaller calls in total.; how: build the scalar networks from triple-intersection gather/scatter with scratch restoration, lift them to arrays by frames, and count the residual dimensions of nested subspace labels (on [Rank deficit s < Wm](rank-deficit.md))

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Restoration of arbitrary scratch values](scratch-restoration.md): An eight-row schedule that subtracts the effect of old scratch values, adds the source's effect, then undoes the copies, so the net change y ← y + x is independent of the scratch contents, which are restored.
  Shown as: Triple-intersection bank exchange *<predicate>* Restoration of arbitrary scratch values

## Pages that build on this one

- Nested subspace labels and orthogonal residuals: Each gate and terminal is labelled by a nondegenerate subspace of a fixed m-dimensional bilinear space, nested along edges; the orthogonal residual of an edge measures how many smaller operations its frame change needs.

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
- [Nested subspace labels and orthogonal residuals](subspace-labels.md)
- [Rank deficit s < Wm](rank-deficit.md)
- [Recursive power saving](recursive-saving.md)
- [Binary phase frames](phase-frames.md)
- [Lower triangular factorization](triangular-factorization.md)
- [Address shear](address-shear.md)
- [Bit network interface](bit-network-interface.md)
- [Fast address-chunk interchange](fast-address-interchange.md)
- [Fixed-point disk grid and truncation](fixed-point-precision.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Signed Kronecker packing](signed-kronecker-packing.md)
- [Normalized discrete Fourier transform](discrete-fourier-transform.md)
- [Multidimensional Fourier transform](multidimensional-transform.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Gaussian resampling with retained permutations](gaussian-resampling.md)
- [Fixed rational parameters and cost table](parameter-choice.md)
- [Fast synthetic transform layout](transform-layout.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Radix-digit reduction to convolution](radix-digit-convolution.md)
- [Chinese-remainder address map](crt-address-map.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Coefficient twist](coefficient-twist.md)
- [Normalized convolution over the polynomial ring](synthetic-convolution.md)
- [Exact coefficient recovery and carries](exact-recovery.md)
- [Integer multiplication below n log n](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "The construction uses three-element subsets: gather and scatter create coefficients depending on intersection size, and auxiliary wires cancel the unwanted coefficients." (paper)

  > The finite construction in Section~\ref{sec:finite-networks} attaches subspaces of a fixed $m$-dimensional space to its gates and terminals. The subspaces at adjacent vertices are nested. Their dimension changes count the smaller operations needed on an edge, with an additional source contribution in the bit construction. The construction uses three-element subsets: gather and scatter create coefficients depending on intersection size, and auxiliary wires cancel the unwanted coefficients. Orthogonality of the corresponding indicator vectors permits the subspace assignments. The decisive property is that the total number $s$ of smaller calls satisfies $s<Wm$.

- "and restores every auxiliary value.  In the bit construction this is the permutation exchanging $X_a$ and $Y_a$." (paper)

  > \begin{lemma}\label{lem:scalar-motifs} For arbitrary initial values of its auxiliary wires, a forward invocation changes $y_S$ to $y_S+x_S$ and leaves every other value unchanged. Performing a forward invocation from $X$ to $Y$ at stage 1, the inverse forward schedule from $Y$ to $X$ at stage 2, and a forward invocation from $X$ to $Y$ at stage 3 sends \[ (X_a,Y_a)\longmapsto(-Y_a,X_a) \] and restores every auxiliary value. In the bit construction this is the permutation exchanging $X_a$ and $Y_a$. \end{lemma}


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

Write the body to `exegenius/tasks/0015-write-triple-intersection-construction.answer.md` and the JSON to `exegenius/tasks/0015-write-triple-intersection-construction.answer.json`, then run `exegenius submit 0015-write-triple-intersection-construction` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0015-write-triple-intersection-construction`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
