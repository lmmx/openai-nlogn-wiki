# exegenius task 0086-write-main-theorem

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
- Discrete Fourier transform
- Cyclic convolution and the convolution theorem
- Integer product as convolution of radix digits
- Butterfly (decimation-in-frequency) transform
- Multidimensional transforms (tensor products)
- Chinese-remainder map to distinct prime axes
- Fixed-point complex grid and truncation
- Contractions and error accumulation
- Gaussian resampling (also: Gaussian gridding)
- Bluestein chirp identity (also: chirp identity)
- Resampling with the permutations left in the transform
- Polynomial ring modulo yʳ + 1
  - $y$ (ring variable): The formal polynomial variable, which satisfies y^r = -1 and serves as a root of unity.
  - $r$ (record length): The number of complex coefficients in a ring element, a power of two.
  - $\mathbb C$ (complex numbers): The field of complex numbers from which the coefficients are drawn.
- Synthetic polynomial transform (also: polynomial transform)
- Phase twist from cyclic to negacyclic wrap
- Signed packing (Kronecker substitution) of ring products
- Exact recovery by rounding and carry propagation
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
- Phase frames reduce a butterfly layer to C kernels
- Packed addition of selected address bits
- Simultaneous butterfly layer in O(V d^λ′) time
  - $V$ (stored bit volume): The number of stored data bits in the array of polynomial records.
  - $d$ (axis count): The number of address chunks (axes) on which the butterfly acts simultaneously.
  - $\lambda'$ (layer exponent): A fixed constant below 1, here 1-2^{-54}, bounding the cost growth in d.
- Synthetic transform layout and retained frequency order
- Normalized convolution over the ring from the retained layout
- Complex cyclic convolution via the coefficient twist
- Computed source transform
- Parameter choices, padded box and prime source lengths
- The multiplication algorithm
- Cost table and the κ margin
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

Concept: Integer multiplication in O(n (lg n)^(1−κ)) time
Gloss: A single deterministic multitape Turing machine multiplies two n-bit integers exactly in O(n (lg n)^{1−κ}) time with κ=2^{-182}, refuting the n log n optimality conjecture in this model; it works by fast address interchanges and fast simultaneous butterfly layers inside a Gaussian-resampling/Bluestein/synthetic-transform reduction.
Heading: Integer multiplication in $O(n(\lg n)^{1-\kappa})$ time

The symbols in this page's heading denote (say so on the page):

- $n$ (operand length): The number of bits in each of the two integers being multiplied.
- $\kappa$ (saving exponent): The fixed positive constant 2^{-182} giving the power saving in the logarithmic factor.

## This page in the argument

The step: A single deterministic multitape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.
How: reduce multiplication to a convolution computed by Gaussian-resampling, Bluestein and synthetic transforms, accelerate the address movement and butterfly layers by two network-based tape procedures, and add up the costs
Why: Scanning the array at each of $\Theta(\log n)$ transform levels already costs $\Theta(n\log n)$, so both the movement and the arithmetic of the transforms must be made cheaper. (the sources say so: "We therefore need savings in both movement and arithmetic." (paper))
Striking feature: The saving is a power $(\lg n)^{-\kappa}$ of the logarithmic factor, not just a smaller constant, with the tiny exponent $\kappa=2^{-182}$ set by the smallest margin in the cost table. (explain why it holds, from the method)

Its sub-steps, in order:

- The tape toolkit: elementary stream scans, controlled shifts, and the finite exchange networks with rank saving are available on a fixed number of tapes.
- Interchanging two disjoint $u$-bit address fields of an array in which all address combinations occur costs $O(Vu^\tau)$ for a fixed $\tau<1$. (on [Chunk interchange in O(V uᵗ) time](chunk-interchange.md))
- Applying $H_0$ to the same bit position in $d$ address chunks of polynomial records at once, exactly in Gaussian dyadics with a single final truncation, costs $O(Vd^{\lambda'})$ with $\lambda'<1$. (on [Simultaneous butterfly layer in O(V d^λ′) time](simultaneous-layer.md))
- Normalized cyclic convolution over $\mathbb C[y]/(y^r+1)$ on the remaining axes is computed with the fast layers, using synthetic transforms in a retained frequency order and signed packing for pointwise ring products. (on [Normalized convolution over the ring from the retained layout](ring-convolution.md))
- The two coordinate permutations of Gaussian resampling are kept in the transform formula rather than executed, with the chirp absorbing the target permutation and the source permutation cancelling. (on [Resampling with the permutations left in the transform](retained-permutations.md))
- The multiplication algorithm, with its parameters and exact recovery, multiplies two $n$-bit integers exactly. (on [The multiplication algorithm](multiplication-algorithm.md))
- Dividing costs by $Tp=\Theta(n)$, the seven dominant terms have powers of $p$ at most $1-2\kappa$, so every polylogarithmic loss is absorbed and the total is $O(n(\log n)^{1-\kappa})$. (on [Cost table and the κ margin](cost-accounting.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S1). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S1**: The tape toolkit: elementary stream scans, controlled shifts, and the finite exchange networks with rank saving are available on a fixed number of tapes.
How: collect the stream operations and the finite networks that both tape procedures use

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S2 (on [Chunk interchange in O(V uᵗ) time](chunk-interchange.md)): Interchanging two disjoint $u$-bit address fields of an array in which all address combinations occur costs $O(Vu^\tau)$ for a fixed $\tau<1$.
- S3 (on [Simultaneous butterfly layer in O(V d^λ′) time](simultaneous-layer.md)): Applying $H_0$ to the same bit position in $d$ address chunks of polynomial records at once, exactly in Gaussian dyadics with a single final truncation, costs $O(Vd^{\lambda'})$ with $\lambda'<1$.
- S4 (on [Normalized convolution over the ring from the retained layout](ring-convolution.md)): Normalized cyclic convolution over $\mathbb C[y]/(y^r+1)$ on the remaining axes is computed with the fast layers, using synthetic transforms in a retained frequency order and signed packing for pointwise ring products.
- S5 (on [Resampling with the permutations left in the transform](retained-permutations.md)): The two coordinate permutations of Gaussian resampling are kept in the transform formula rather than executed, with the chirp absorbing the target permutation and the source permutation cancelling.
- S6 (on [The multiplication algorithm](multiplication-algorithm.md)): The multiplication algorithm, with its parameters and exact recovery, multiplies two $n$-bit integers exactly.
- S7 (on [Cost table and the κ margin](cost-accounting.md)): Dividing costs by $Tp=\Theta(n)$, the seven dominant terms have powers of $p$ at most $1-2\kappa$, so every polylogarithmic loss is absorbed and the total is $O(n(\log n)^{1-\kappa})$.
- S1.1 (on [Arrays on tape and elementary stream operations](stream-ops.md)): An array with a product address set, stored in lexicographic order, supports digit permutation, digit move, splitting on a digit with a pointwise map and merging, and cyclic row splitting into streams, each in $O(V)$ time on a fixed number of tapes.
- S1.2 (on [Controlled cyclic shifts and fixed rational scalings](controlled-shift.md)): Updating a later address field $y$ by $y+a(\text{controls})$ modulo $q^b$, or multiplying it by a fixed rational unit, costs $O(V)$.
- S1.3 (on [Linear exchange network with restored scratch wires](linear-network.md)): A fixed linear network on $W$ wires exchanges two banks with signs and restores every scratch wire, and its gates can be labelled so that the total rank $s$ of the edge changes of representation satisfies $s<Wm$.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [The multiplication algorithm](multiplication-algorithm.md): Form radix-2^b digits, apply the CRT map Φ, compute two forward source transforms, multiply pointwise, apply the opposite transform, rescale by S and 2^{2b+4}S, round, invert Φ, and propagate carries to output the 2n-bit product.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* The multiplication algorithm
- [Cost table and the κ margin](cost-accounting.md): Dividing costs by Tp=Θ(n), seven dominant terms have powers of p at most 1−2κ (smallest margin 2^{-181}), so every polylogarithmic loss is absorbed and the total is O(n (log n)^{1−κ}).
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Cost table and the κ margin
- [Integer multiplication complexity and the n log n conjecture](history.md): Schönhage–Strassen gave O(n log n log log n) on multitape Turing machines and conjectured n log n optimal; Harvey–van der Hoeven reached O(n log n), which this paper's algorithm beats.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Integer multiplication complexity and the n log n conjecture

## Other pages you may link to

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
- [Fixed-point complex grid and truncation](fixed-point.md)
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

## Evidence from the sources, with the paragraph around each quote

- "computes this exact product for every $n\ge1$ and every pair of $n$-bit" (paper)

  > \begin{theorem}\label{thm:main} There is one deterministic Turing machine $A$, with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, that computes this exact product for every $n\ge1$ and every pair of $n$-bit inputs. Its worst-case running time satisfies \[ T_A(n)=O\!\left(n(\lg n)^{1-\kappa}\right), \qquad \kappa=2^{-182}. \] \end{theorem}

- "T_A(n)=O\!\left(n(\lg n)^{1-\kappa}\right)," (paper)

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

Write the body to `exegenius/tasks/0086-write-main-theorem.answer.md` and the JSON to `exegenius/tasks/0086-write-main-theorem.answer.json`, then run `exegenius submit 0086-write-main-theorem` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0086-write-main-theorem`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
