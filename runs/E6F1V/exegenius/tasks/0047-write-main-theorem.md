# exegenius task 0047-write-main-theorem

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F1V` (paths below are relative to it)

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

For these sources: The reader has an undergraduate computer science education: asymptotic analysis (O, Theta, Omega), recursion and induction, discrete mathematics (sets, functions, permutations, graphs, modular arithmetic, primes and gcd, elementary combinatorics), and single-variable calculus. They have taken linear algebra at the level of vectors, matrices, bases, dimension and dot products, and have met complex numbers, polynomials, binary representation, Boolean gates and basic multitape Turing machines. They have not studied abstract algebra beyond residues and the two-element field, Fourier analysis, the FFT, fast integer multiplication, tensor products, or any research-level algorithms or complexity.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes
- Fixed finite-tape machine model
- The n log n optimality conjecture
- Established O(n log n) multiplier (Harvey–van der Hoeven)
- Arrays in lexicographic tape order with address fields
- Elementary stream operations
- Controlled cyclic shifts and rational scalings
- Matrix rank, subspaces and orthogonal complements
- Discrete Fourier transform
- Cyclic convolution
- Convolution theorem for normalized transforms
- Multidimensional (tensor) transforms
- Integer multiplication as digit convolution
- Fixed-point disk grid and error propagation
- Polynomial ring modulo y^r + 1
  - $y$ (ring variable): The polynomial variable, which satisfies y^r = −1 and serves as a root of unity.
  - $r$ (coefficient count): The number of complex coefficients in a polynomial record, a power of two.
- Two-point butterfly and radix-2 FFT order
- Synthetic polynomial transform
- Chinese-remainder address map
- Gaussian resampling with retained permutations
- Bluestein chirp identity
- Source-permutation cancellation
- Coefficient twist to negacyclic ring
- Linear exchange network with restored scratch wires
- Frames and the common-frame identity
- Three-element-subset subspace labels
- Rank deficit s < Wm
- Bit exchange network with shear interface
- Complex phase network
- Lower-triangular factorization of matrices
- Rational matrix shear as field interchanges
- Power-saving recurrence
- Power-width address interchange with rows
- Fast interchange of address chunks
  - $u$ (chunk width): The number of bits in each of the two address chunks being interchanged.
  - $V$ (stored bit volume): The number of data bits stored in the array.
  - $\tau$ (interchange exponent): A fixed constant with 0 < τ < 1 (here 1 − 2^{-50}) in the exponent of the cost.
- Packed selected-bit addition with deterministic repair
- Simultaneous butterfly layer
  - $H_0$ (two-point butterfly): The matrix ((1,1),(1,−1))/2 sending (u,v) to ((u+v)/2,(u−v)/2).
  - $D$ (axis count): The number of address chunks, one selected bit in each, on which the butterfly acts simultaneously.
- Synthetic transform layout and stored frequency order
- Signed packing (Kronecker substitution)
- Convolution over the polynomial ring from the retained layout
- Complex cyclic convolution by coefficient twist
- Source transform procedure
- Choice of prime source lengths
- Parameter choice and cost balance
- Rounding and carry propagation to the exact product
- The multiplication algorithm
- Asymptotic notation beyond big-O (also: Theta notation, Omega notation, little-o, Big-Theta, Big-Omega, Θ, Ω, o(1))
- Logarithms and exponentials (also: lg, log base 2, log n, log log n, powers of two, exponent laws)
- Floor, ceiling and rounding (also: floor function, ceiling function, round to nearest integer, truncation toward zero, integer part)
- Proof by induction and recursion (also: mathematical induction, recursive definition, recurrence relation, geometric series, divide and conquer)
- Sets, subsets and basic combinatorics (also: subset, intersection of sets, cardinality, binomial coefficient, counting, indicator vector, characteristic vector, pigeonhole)
- Functions, bijections and permutations (also: permutation, bijection, composition of functions, inverse function, permutation matrix, one-to-one correspondence)
- Graphs (also: vertices and edges, graph, neighbors, adjacency, directed edge, path in a graph)
- Modular arithmetic (also: residues, congruence, integers mod n, Z/nZ, mod q, remainder, cyclic group of residues)
- Primes, coprimality and gcd (also: prime number, relatively prime, coprime, greatest common divisor, Euclidean algorithm, modular inverse, Chinese remainder theorem, prime factorization)
- Binary field F2 and XOR (also: GF(2), F_2, exclusive or, XOR, mod 2 arithmetic, bitwise xor, parity)
- Positional number representation and carries (also: radix, base-b digits, binary representation, digit expansion, carry propagation, schoolbook multiplication, bit length, most significant digit)
- Dyadic rationals and binary fractions (also: dyadic numbers, binary fraction, fixed-point number, fixed-point arithmetic, scaling by a power of two, shift)
- Exponential function and Gaussian function (also: e^x, Euler's formula, Gaussian function, e^{-x^2}, bell curve, exponential decay, calculus bounds, Taylor series)
- Vectors, matrices and linear maps (also: matrix multiplication, invertible matrix, linear transformation, dot product, inner product, linear independence, basis, dimension, identity matrix, diagonal matrix, transpose, lower triangular matrix, linear combination)
- Vector norms and error bounds (also: norm, Euclidean norm, triangle inequality, operator norm, contraction, sup norm, absolute error, modulus of a complex number)
- Boolean gates and circuits (also: logic gate, wire, circuit, XOR gate, AND gate, fan-out, gate network)
- Determinism and exact versus approximate computation (also: deterministic algorithm, exact arithmetic, rational arithmetic, approximation error, worst-case running time, constant-factor overhead)

## This page

Concept: Integer multiplication in O(n (lg n)^(1−κ)) time
Gloss: There is one deterministic fixed-alphabet, fixed-tape Turing machine multiplying n-bit integers exactly in O(n (lg n)^{1−κ}) time with κ = 2^{−182}, disproving the n log n optimality conjecture in this model.
Heading: Integer multiplication in $O(n(\lg n)^{1-\kappa})$ time

The symbols in this page's heading denote (say so on the page):

- $n$ (operand length): The number of bits in each of the two integers being multiplied.
- $\kappa$ (saving exponent): The fixed constant 2^{-182} by which the logarithmic factor is reduced.

## This page in the argument

The step: There is one deterministic fixed-alphabet, fixed-tape Turing machine multiplying $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.
How: Reduce the product to a digit convolution computed with Fourier-type transforms on power-of-two axes, and accelerate the transforms' address rearrangements and butterfly layers by a power of the logarithm.
Why: Scanning the array at each of the logarithmically many transform levels already costs $n\log n$, so a power saving needs the movement and the arithmetic per level to be cheaper than a scan. (the sources say so: "$\Theta(\log n)$ transform levels already costs $\Theta(n\log n)$." (paper))

Its sub-steps, in order:

- There are two fixed-tape procedures whose cost beats a full scan per level by a power: an address-chunk interchange in $O(Vu^\tau)$ and a simultaneous butterfly layer in $O(Vd^{\lambda'})$.
- The normalized convolution over power-of-two axes needed by the multiplication is available, with every cost and error bound, from the synthetic transforms.
- The transform of pairwise coprime lengths $s_i$ is expressible through power-of-two tensor transforms, a chirp convolution, and a cancellation of the retained permutation.
- With $p=6b$, $d=\lfloor b^\epsilon\rfloor$, $K$, $r$, $T$ and the tiny exponents fixed, the multiplication algorithm is correct and runs in $O(n(\lg n)^{1-\kappa})$ time. (on [Parameter choice and cost balance](parameter-balance.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (T, X, G). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**T**: There are two fixed-tape procedures whose cost beats a full scan per level by a power: an address-chunk interchange in $O(Vu^\tau)$ and a simultaneous butterfly layer in $O(Vd^{\lambda'})$.
How: Build each procedure from a fixed linear network that exchanges two banks of values and restores its scratch values, and apply it recursively with a strict rank deficit.

**X**: The normalized convolution over power-of-two axes needed by the multiplication is available, with every cost and error bound, from the synthetic transforms.
How: Build the polynomial-ring convolution from the retained-order synthetic transforms and the signed packing multiplication.

**G**: The transform of pairwise coprime lengths $s_i$ is expressible through power-of-two tensor transforms, a chirp convolution, and a cancellation of the retained permutation.
How: Retain the source and target coordinate permutations in the identity instead of executing sorts, and use Bluestein's chirp for the middle transform.

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- PB (on [Parameter choice and cost balance](parameter-balance.md)): With $p=6b$, $d=\lfloor b^\epsilon\rfloor$, $K$, $r$, $T$ and the tiny exponents fixed, the multiplication algorithm is correct and runs in $O(n(\lg n)^{1-\kappa})$ time.
- T.1 (on [Elementary stream operations](stream-ops.md)): Fixed-radix digit permutations, digit moves, splits by a digit, pointwise maps, merges and cyclic row splitting into a fixed number of streams each take $O(V)$ steps.
- T.2 (on [Controlled cyclic shifts and rational scalings](controlled-shifts.md)): Updating a target field by an offset computed from earlier control fields modulo $q^b$, or multiplying it by a fixed rational unit, costs $O(V)$.
- R1 (on [Fast interchange of address chunks](chunk-interchange.md)): Two disjoint address chunks of $u$ bits, with any prefix, gap and suffix, can be interchanged in $O(Vu^\tau)$ tape steps for a fixed $\tau<1$.
- R2 (on [Simultaneous butterfly layer](simultaneous-layer.md)): Applying $H_0=\frac12\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ at one bit position in each of $D\le d$ equal-width address chunks costs $O(Vd^{\lambda'})$ for a fixed $\lambda'<1$, with one final truncation.
- R3 (on [Synthetic polynomial transform](synthetic-transform.md)): Normalized Fourier-type transforms of arrays of polynomials modulo $y^r+1$, with roots of unity $\omega_t=y^{2r/t}$, need arithmetic only in butterflies, leave outputs in bit-reversed slot order, and have an opposite transform that consumes that order.
- R4 (on [Convolution over the polynomial ring from the retained layout](ring-convolution.md)): The normalized convolution $\mathcal M_r(f,g)=(f*g)/T$ of arrays over $\mathbb C[y]/(y^r+1)$ is computed with error below $\sqrt2\,M(3\ell+1)2^{-p}$ in $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}+\log(rp)])$ time.
- G.1 (on [Gaussian resampling with retained permutations](gaussian-resampling.md)): For coprime $s<t$ with $t/s-1>p/\alpha^4$ there are contractions $A,B_0$ with $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$, and tensoring over $d$ axes gives $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ with the permutations $R,Q$ retained.
- G.2 (on [Bluestein chirp identity](chirp-identity.md)): For the chirp array $a_{\boldsymbol j}=\exp(-\pi i\sum_i s_ij_i^2/t_i)$, the permuted transform is $QF_{\boldsymbol t}u=\overline a\cdot\bigl(a*(\overline a\cdot u)\bigr)/T$.
- G.3 (on [Source-permutation cancellation](permutation-cancellation.md)): The retained source permutation cancels: $(RF_{\boldsymbol s}^+)\bigl[(RF_{\boldsymbol s}u)\cdot(RF_{\boldsymbol s}v)\bigr]=(u*v)/S^2$ with $S=\prod_is_i$, so no sort is executed.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [The multiplication algorithm](mult-algorithm.md): Splits both inputs into digits, applies the coefficient-address map, computes the source transform of each, multiplies pointwise, applies the opposite-sign transform with scalings, rounds and propagates carries.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* The multiplication algorithm
- [Parameter choice and cost balance](parameter-balance.md): Fixes p = Θ(log n), d = ⌊b^ε⌋ axes, chunk size K, ring dimension r = 2^{Θ(p/d)} and the tiny exponents so that every row of the cost table has normalized power of p at most 1 − 2κ, giving total O(n (log n)^{1−κ}).
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Parameter choice and cost balance
- [The n log n optimality conjecture](nlogn-conjecture.md): Schönhage and Strassen's proposal that n log n is the optimal order of growth for multiplying n-bit integers on multitape Turing machines.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* The n log n optimality conjecture
- [Established O(n log n) multiplier (Harvey–van der Hoeven)](nlogn-multiplier.md): The known fixed-tape integer multiplier running in O(N log N) time on N-bit inputs, used here only as an ordinary subroutine on short records.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Established O(n log n) multiplier (Harvey–van der Hoeven)

## Other pages you may link to

- [Fixed finite-tape machine model](fixed-tape-model.md)
- [Arrays in lexicographic tape order with address fields](array-order.md)
- [Elementary stream operations](stream-ops.md)
- [Controlled cyclic shifts and rational scalings](controlled-shifts.md)
- [Matrix rank, subspaces and orthogonal complements](matrix-basics.md)
- [Linear exchange network with restored scratch wires](network.md)
- [Frames and the common-frame identity](frames.md)
- [Three-element-subset subspace labels](subset-labels.md)
- [Rank deficit s < Wm](rank-saving.md)
- [Bit exchange network with shear interface](bit-network.md)
- [Lower-triangular factorization of matrices](lower-triangular.md)
- [Rational matrix shear as field interchanges](matrix-shear.md)
- [Power-saving recurrence](power-saving-recurrence.md)
- [Power-width address interchange with rows](power-interchange.md)
- [Fast interchange of address chunks](chunk-interchange.md)
- [Packed selected-bit addition with deterministic repair](packed-bit-addition.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring-mod.md)
- [Signed packing (Kronecker substitution)](kronecker-packing.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Integer multiplication as digit convolution](int-as-convolution.md)
- [Discrete Fourier transform](dft.md)
- [Two-point butterfly and radix-2 FFT order](butterfly-fft.md)
- [Complex phase network](phase-network.md)
- [Fixed-point disk grid and error propagation](fixed-point-disk-grid.md)
- [Coefficient twist to negacyclic ring](negacyclic-twist.md)
- [Simultaneous butterfly layer](simultaneous-layer.md)
- [Convolution theorem for normalized transforms](convolution-theorem.md)
- [Multidimensional (tensor) transforms](multidim-transform.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Gaussian resampling with retained permutations](gaussian-resampling.md)
- [Bluestein chirp identity](chirp-identity.md)
- [Source-permutation cancellation](permutation-cancellation.md)
- [Synthetic transform layout and stored frequency order](transform-layout.md)
- [Convolution over the polynomial ring from the retained layout](ring-convolution.md)
- [Chinese-remainder address map](crt-axis-map.md)
- [Choice of prime source lengths](prime-lengths.md)
- [Complex cyclic convolution by coefficient twist](complex-convolution.md)
- [Source transform procedure](source-transform.md)
- [Rounding and carry propagation to the exact product](exact-recovery.md)

## Evidence from the sources, with the paragraph around each quote

- "There is one deterministic Turing machine $A$, with a fixed finite alphabet and a fixed finite number of one-dimensional tapes" (paper)

  > \begin{theorem}\label{thm:main} There is one deterministic Turing machine $A$, with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, that computes this exact product for every $n\ge1$ and every pair of $n$-bit inputs. Its worst-case running time satisfies \[ T_A(n)=O\!\left(n(\lg n)^{1-\kappa}\right), \qquad \kappa=2^{-182}. \] \end{theorem}

- "T_A(n)=O\!\left(n(\lg n)^{1-\kappa}\right)" (paper)

  > \begin{theorem}\label{thm:main} There is one deterministic Turing machine $A$, with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, that computes this exact product for every $n\ge1$ and every pair of $n$-bit inputs. Its worst-case running time satisfies \[ T_A(n)=O\!\left(n(\lg n)^{1-\kappa}\right), \qquad \kappa=2^{-182}. \] \end{theorem}


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

Write the body to `exegenius/tasks/0047-write-main-theorem.answer.md` and the JSON to `exegenius/tasks/0047-write-main-theorem.answer.json`, then run `exegenius submit 0047-write-main-theorem` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0047-write-main-theorem`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
