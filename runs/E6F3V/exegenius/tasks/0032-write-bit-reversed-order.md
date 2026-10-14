# exegenius task 0032-write-bit-reversed-order

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
- Cyclic convolution
- Integer product as digit convolution
- Discrete Fourier transform (also: Fourier transform, F_q)
- Multidimensional transform
- Two-point butterfly and radix-two recursion (also: H₀, butterfly layer)
- Contractions and error accumulation
- Bluestein chirp identity
- Polynomial ring modulo y^r + 1 (also: negacyclic ring, R_r)
  - $y$ (ring variable): The formal polynomial variable, satisfying y^r = −1 in the ring.
  - $r$ (ring length): The number of complex coefficients in a ring element, a power of two.
- Coefficient phase twist
- Synthetic polynomial transform
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
- Phase frames and the two-point kernel C
- Packed selected-bit addition
- Exact dyadic intermediates with one truncation
- Simultaneous butterfly layer
- Exact recovery by rounding and carries
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

Concept: Stored bit-reversed frequency order
Gloss: The recursion writes outputs in bit-reversed order (record permutation B_t), and the opposite transform consumes that same order, so no reordering is needed between the forward transforms and the inverse.

## This page in the argument

The step: The recursion writes entry $j$ of $F_t^-z$ at slot $\operatorname{rev}_a(j)$ (the record permutation $B_t$) and the opposite procedure reads the same order, so the two procedures implement $B_tF_t^-$ and $F_t^+B_t^{-1}$ and no reordering is ever executed.
How: Track which address bits hold frequency bits after each level, then run the recursion backwards for the opposite transform and use $H_0^2=I/2$ to identify it with $F_t^+B_t^{-1}$.
Why: The frequency order in which entries are stored matters because the opposite transform consumes that same order after the pointwise product. (the sources say so: "We also specify where each frequency entry
is stored, because the opposite transform consumes that same order
after a pointwise product." (paper))
Striking feature: No reordering is ever executed: the bit-reversal permutation produced by the forward recursion is exactly the order the opposite recursion consumes, so the pointwise product sits between the two in the stored order. (explain why it holds, from the method)

Its sub-steps, in order:

- After all $a$ rounds the named slots from high to low contain the frequency bits from low to high, so entry $(F_t^-z)_j$ occupies slot $\operatorname{rev}_a(j)$.
- The consuming procedure traverses the recursion in reverse: first the two smaller branches, then the inverse monomial on the second branch, and finally $H_0$.
- Since $H_0^2=I/2$ the reversed level is half the inverse of the forward level, so the two exact procedures implement $B_tF_t^-$ and $F_t^+B_t^{-1}$.

It serves these steps, from the main result down:

- One deterministic multitape Turing machine multiplies $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$, refuting the $n\log n$ optimality conjecture in this model.; how: Reduce the product to a convolution of short digits evaluated by Fourier transforms, speed up the two costly ingredients (moving data between addresses, and butterfly arithmetic) by a power of a block size using one recursive saving, and total every cost term. (on [Sub-n-log-n integer multiplication](main-theorem.md))
- For arrays on $\prod_i\mathbb Z/t_i\mathbb Z$ with entries in $\mathcal R_r$, the normalised convolution $\mathcal M_r(f,g)=(f*g)/T$ is computed with error below $\sqrt2\,M(3\ell+1)2^{-p}$ by two forward synthetic transforms, pointwise polynomial products by Kronecker packing, and the opposite transform on the retained order.; how: Transform both operands, multiply the polynomial records pointwise in the retained stored order (the same record permutation on both operands), and apply the opposite transform to that order; each ingredient is a separate procedure. (on [Convolution over the polynomial ring](ring-convolution.md))
- With the selected bits of the $d-1$ participating axes placed at a common offset in consecutive $K$-bit chunks, the forward synthetic transform $LBF^-_{\boldsymbol t}$ of $M$ polynomial records of degree below $r=2^\ell$ runs in $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$ time with error below $\sqrt2\,\ell\,2^{-p}$.; how: Move the prefix slots by single-bit moves, bring the remaining chunks into aligned rounds by chunk exchanges, then run each round as one simultaneous butterfly layer followed by a signed-shift monomial and a single truncation. (on [Transform layout and cost](transform-layout.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S4.1.2.1, S4.1.2.2, S4.1.2.3). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S4.1.2.1**: After all $a$ rounds the named slots from high to low contain the frequency bits from low to high, so entry $(F_t^-z)_j$ occupies slot $\operatorname{rev}_a(j)$.
Source: "After all $a$ rounds, the named slots from high to low therefore
contain the frequency bits from low to high.  If
$\operatorname{rev}_a(j)$ reverses the $a$ binary digits of $j$, the
entry $(F_t^-z)_j$ occupies slot $\operatorname{rev}_a(j)$." (paper)
> After all $a$ rounds, the named slots from high to low therefore contain the frequency bits from low to high. If $\operatorname{rev}_a(j)$ reverses the $a$ binary digits of $j$, the entry $(F_t^-z)_j$ occupies slot $\operatorname{rev}_a(j)$. Let $B_t$ denote this record permutation: it moves the entry at $j$ to $\operatorname{rev}_a(j)$. The recursion writes its outputs directly in this order; it does not move whole frequency indices.

**S4.1.2.2**: The consuming procedure traverses the recursion in reverse: first the two smaller branches, then the inverse monomial on the second branch, and finally $H_0$.
Source: "The procedure consuming this stored order traverses the recursion in
reverse: first process the two smaller branches, then apply the inverse
monomial to the second branch, and finally apply $H_0$." (paper)
> The procedure consuming this stored order traverses the recursion in reverse: first process the two smaller branches, then apply the inverse monomial to the second branch, and finally apply $H_0$. Each forward level is invertible, since both its butterfly and its monomial are invertible. As $H_0^2=I/2$, the reversed level is half the inverse of the corresponding forward level. There are $a=\log_2t$ levels, so the reverse procedure composed with $B_tF_t^-$ is $2^{-a}I=I/t$. Lemma~\ref{lem:synthetic-characters} gives the same composite for $F_t^+B_t^{-1}$ with $B_tF_t^-$. The forward procedure is invertible, so these two reverse operators agree. Thus the two exact procedures implement \begin{equation} B_tF_t^-,\qquad F_t^+B_t^{-1}, \label{eq:stored-opposite} \end{equation} respectively.

**S4.1.2.3**: Since $H_0^2=I/2$ the reversed level is half the inverse of the forward level, so the two exact procedures implement $B_tF_t^-$ and $F_t^+B_t^{-1}$.
Source: "Thus the two
exact procedures implement
\begin{equation}
       B_tF_t^-,\qquad F_t^+B_t^{-1}," (paper)
> The procedure consuming this stored order traverses the recursion in reverse: first process the two smaller branches, then apply the inverse monomial to the second branch, and finally apply $H_0$. Each forward level is invertible, since both its butterfly and its monomial are invertible. As $H_0^2=I/2$, the reversed level is half the inverse of the corresponding forward level. There are $a=\log_2t$ levels, so the reverse procedure composed with $B_tF_t^-$ is $2^{-a}I=I/t$. Lemma~\ref{lem:synthetic-characters} gives the same composite for $F_t^+B_t^{-1}$ with $B_tF_t^-$. The forward procedure is invertible, so these two reverse operators agree. Thus the two exact procedures implement \begin{equation} B_tF_t^-,\qquad F_t^+B_t^{-1}, \label{eq:stored-opposite} \end{equation} respectively.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Synthetic polynomial transform](synthetic-transform.md): A Fourier transform over the negacyclic ring using ω_t = y^{2r/t} as root of unity, so each twiddle multiplication is a signed shift and only butterflies cost arithmetic.
  Shown as: Stored bit-reversed frequency order *<predicate>* Synthetic polynomial transform

## Pages that build on this one

- Transform layout and cost: Placing the selected bits of all participating axes at a common offset in K-bit chunks, so each round of the synthetic transform uses the simultaneous layer, at total normalized cost dK + pK^{τ−1} + ℓd^{λ′}.
- Convolution over the polynomial ring: Normalized convolution of arrays with entries in the negacyclic ring: forward synthetic transforms, pointwise polynomial products by Kronecker packing, and the opposite transform in the retained order.

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
- [Cyclic convolution](cyclic-convolution.md)
- [Integer product as digit convolution](radix-digit-convolution.md)
- [Coefficient phase twist](phase-twist.md)
- [Exact recovery by rounding and carries](exact-recovery.md)
- [Discrete Fourier transform](dft.md)
- [Two-point butterfly and radix-two recursion](fft-butterfly.md)
- [Bluestein chirp identity](chirp-identity.md)
- [Phase frames and the two-point kernel C](phase-frames.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Multidimensional transform](multidimensional-transform.md)
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

- "Let $B_t$ denote this record permutation" (paper)

  > After all $a$ rounds, the named slots from high to low therefore contain the frequency bits from low to high. If $\operatorname{rev}_a(j)$ reverses the $a$ binary digits of $j$, the entry $(F_t^-z)_j$ occupies slot $\operatorname{rev}_a(j)$. Let $B_t$ denote this record permutation: it moves the entry at $j$ to $\operatorname{rev}_a(j)$. The recursion writes its outputs directly in this order; it does not move whole frequency indices.

- "B_tF_t^-,\qquad F_t^+B_t^{-1}," (paper)

  > The procedure consuming this stored order traverses the recursion in reverse: first process the two smaller branches, then apply the inverse monomial to the second branch, and finally apply $H_0$. Each forward level is invertible, since both its butterfly and its monomial are invertible. As $H_0^2=I/2$, the reversed level is half the inverse of the corresponding forward level. There are $a=\log_2t$ levels, so the reverse procedure composed with $B_tF_t^-$ is $2^{-a}I=I/t$. Lemma~\ref{lem:synthetic-characters} gives the same composite for $F_t^+B_t^{-1}$ with $B_tF_t^-$. The forward procedure is invertible, so these two reverse operators agree. Thus the two exact procedures implement \begin{equation} B_tF_t^-,\qquad F_t^+B_t^{-1}, \label{eq:stored-opposite} \end{equation} respectively.


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

Write the body to `exegenius/tasks/0032-write-bit-reversed-order.answer.md` and the JSON to `exegenius/tasks/0032-write-bit-reversed-order.answer.json`, then run `exegenius submit 0032-write-bit-reversed-order` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0032-write-bit-reversed-order`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
