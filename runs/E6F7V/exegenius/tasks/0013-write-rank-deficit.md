# exegenius task 0013-write-rank-deficit

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F7V` (paths below are relative to it)

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
- Subspaces, orthogonality and rank
- Linear network exchanging two banks with restored scratch values
- Frames: changing the representation along a network
- Subspace labels from three-element subsets
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

Concept: Rank deficit s < W m
Gloss: The sum s of ranks of all edge differences (the number of smaller calls) is strictly less than W·m, where W is the number of wires and m the label-space dimension; the deficit comes from the loss L on decreasing edges being below N/2.

## This page in the argument

The step: In each of the two networks, with $W$ wires and an $m$-dimensional label space, the nested labels make the total rank $s$ of all edge differences (the number of smaller calls) strictly less than $Wm$, because the loss $L$ on decreasing edges is below $N/2$.
How: Label every gate and terminal by a nested nondegenerate subspace so that an edge changes the stored array by one smaller operation per unit of residual dimension; build the exchanging network, the frames and the labels, then count the total dimension change.
Why: A frame change along an edge costs one smaller call per dimension of its orthogonal residual, so s is a sum of dimension changes; the whole saving reduces to the signed sum $Wm-2N$ and the small loss on decreasing edges. (the sources say so: "The saving will come from keeping the total dimension lost on decreasing" (paper))
Striking feature: The deficit is minute (a relative deficit of about $10^{-11}$) but strictly positive: all decreasing edges are the single return of the central wires from time 3 to time 4, which loses only $h=100$ dimensions per invocation, so $L/N$ is $100/539$ or $101/539$, below $1/2$, and that is exactly enough to leave $s<Wm$ after the $N$ extra source ranks. (explain why it holds, from the method)

Its sub-steps, in order:

- A fixed linear network on two data banks $X,Y$ and scratch wires maps $(X,Y)$ to $(-Y,X)$ in three stages and returns every scratch wire to its arbitrary initial value. (on [Linear network exchanging two banks with restored scratch values](xor-linear-network.md))
- Giving every source, gate and sink an invertible frame $D_v$ and applying $D_vD_u^{-1}$ along each edge makes the network implement $D_{\rm out}\mathsf S D_{\rm in}^{-1}$, so only the endpoint frames matter. (on [Frames: changing the representation along a network](frames.md))
- Nested nondegenerate subspaces of a tensor cube, built from indicator vectors of three-element subsets of $[100]$, can be attached to all gates and terminals so that every edge joins comparable labels and the only decreasing edges are the central-wire edges from time 3 to time 4. (on [Subspace labels from three-element subsets](subset-labels.md))
- The sum of the absolute changes of label dimension over all edges is $Wm-2N+2L$, and the loss $L$ on decreasing edges is below $N/2$.

It serves these steps, from the main result down:

- One deterministic fixed-tape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$, refuting the $n\log n$ optimality conjecture in this model.; how: Build the two accelerated tape procedures (address interchange and simultaneous butterfly layers), use them inside synthetic transforms and Gaussian resampling to compute a convolution, assemble the multiplication algorithm with exact recovery, and total the cost. (on [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md))
- Two tape procedures cost less than a pass per level: interchanging two disjoint $u$-bit address fields of a volume-$V$ array costs $O(Vu^\tau)$ and a simultaneous butterfly layer on $D\le d$ chunks costs $O(Vd^{\lambda'})$, for fixed $\tau,\lambda'<1$.; how: Give each procedure its own fixed linear network that exchanges two banks of values and restores all scratch values, with total number $s$ of smaller calls below $Wm$, then run the network recursively on role streams of volume $V/W$ (interchange of address fields first, numerical layers second).

## Steps this page derives

The argument gives this page these sub-steps of its step (S1.1.4). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S1.1.4**: The sum of the absolute changes of label dimension over all edges is $Wm-2N+2L$, and the loss $L$ on decreasing edges is below $N/2$.
How: Telescope the signed dimension changes at each gate (source dimensions sum to $N$, sink dimensions to $Wm-N$), then add twice the total loss on decreasing edges; evaluate $L$ from the number of central wires.
- S1.1.4.1: The signed change of label dimension over all edges telescopes to $Wm-2N$.
  Source: "The signed increase is therefore $Wm-2N$." (paper)
  > The signed sum of dimension changes telescopes at every gate: each touched wire has one incoming and one outgoing incidence with the same gate label. The sum of source dimensions is $N$, while the sum of sink dimensions is $Wm-N$. The signed increase is therefore $Wm-2N$. There are $Ic$ decreasing edges, each of loss $h$; replacing signed changes by absolute changes adds $2L$.
- S1.1.4.2: There are $Ic$ decreasing edges, each of loss $h$, so $L=Ich$ and replacing signed by absolute changes adds $2L$.
  Source: "There are $Ic$ decreasing edges, each of loss $h$; replacing signed" (paper)
  > The signed sum of dimension changes telescopes at every gate: each touched wire has one incoming and one outgoing incidence with the same gate label. The sum of source dimensions is $N$, while the sum of sink dimensions is $Wm-N$. The signed increase is therefore $Wm-2N$. There are $Ic$ decreasing edges, each of loss $h$; replacing signed changes by absolute changes adds $2L$.
- S1.1.4.3: The loss ratios are exactly $L_{\rm b}/N=100/539$ and $L_{\rm c}/N=101/539$.
  Source: "\frac{L_{\rm b}}{N}=\frac{100}{539},\qquad" (paper)
  > The loss ratios have the exact values \[ \frac{L_{\rm b}}{N}=\frac{100}{539},\qquad \frac{L_{\rm c}}{N}=\frac{101}{539}. \] In particular, both are smaller than $1/2$. We now turn the dimension count into the two interfaces needed later.
- S1.1.4.4: Both loss ratios $L/N$ are below $1/2$, so after the $N$ extra source ranks the total edge rank is $s=Wm-N+2L<Wm$ in the bit network.
  Source: "In particular, both are smaller than $1/2$." (paper)
  > The loss ratios have the exact values \[ \frac{L_{\rm b}}{N}=\frac{100}{539},\qquad \frac{L_{\rm c}}{N}=\frac{101}{539}. \] In particular, both are smaller than $1/2$. We now turn the dimension count into the two interfaces needed later.

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S1.1.1 (on [Linear network exchanging two banks with restored scratch values](xor-linear-network.md)): A fixed linear network on two data banks $X,Y$ and scratch wires maps $(X,Y)$ to $(-Y,X)$ in three stages and returns every scratch wire to its arbitrary initial value.
- S1.1.2 (on [Frames: changing the representation along a network](frames.md)): Giving every source, gate and sink an invertible frame $D_v$ and applying $D_vD_u^{-1}$ along each edge makes the network implement $D_{\rm out}\mathsf S D_{\rm in}^{-1}$, so only the endpoint frames matter.
- S1.1.3 (on [Subspace labels from three-element subsets](subset-labels.md)): Nested nondegenerate subspaces of a tensor cube, built from indicator vectors of three-element subsets of $[100]$, can be attached to all gates and terminals so that every edge joins comparable labels and the only decreasing edges are the central-wire edges from time 3 to time 4.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Subspace labels from three-element subsets](subset-labels.md): Frankl–Wilson style construction: indicator vectors of three-element subsets of [100] give intersection-size inner products; tensor cubes of these lines label gates by nested nondegenerate subspaces so that edge changes are small orthogonal residuals.
  Shown as: Rank deficit s < W m *<predicate>* Subspace labels from three-element subsets
- [Frames: changing the representation along a network](frames.md): An invertible operator D_v on an array chosen at each source, gate and sink; every edge applies D_vD_u^{-1}, a common frame commutes with the pointwise linear gate, so the network implements D_out S D_in^{-1} and the endpoint frames fix the operator on every role.
  Shown as: Rank deficit s < W m *<predicate>* Frames: changing the representation along a network

## Pages that build on this one

- Recursive power saving from the rank deficit: A call at parameter m·f makes s calls at parameter f on streams of volume V/W, giving F_k ≤ (s/W)F_{k−1}+O(1) with s/W < m, so the normalized cost is O(parameter^τ) for some τ < 1.
- Address shear from the bit network: Using the permutation frame Φ_M that moves the entry at (H,D) to (H+MD,D), the bit network's endpoint matrices differ by the identity, so it implements the shear H ← H+D on every role, with total edge rank s_b < W_b·m.
- Complex phase network and two-point kernels: The same network over Gaussian dyadic values with binary labels and phase frames C_U = H^{⊗m} diag(i^{wt(P_U x) mod 4}) H^{⊗m}; each edge change is a product of two-point kernels C = aI+bX (a=(1+i)/2, b=(1−i)/2), and telescoping gives C^{⊗m} on every role with s_c < W_c·m kernel factors.

## Other pages you may link to

- [Multiplication complexity and the n log n conjecture](nlogn-history.md)
- [Fixed finite-alphabet multitape model](fixed-tape-model.md)
- [Established O(n log n) multiplier (subroutine)](established-multiplier.md)
- [Array order and elementary stream operations](stream-operations.md)
- [Controlled shifts](controlled-shifts.md)
- [Subspaces, orthogonality and rank](linear-algebra-prelims.md)
- [Linear network exchanging two banks with restored scratch values](xor-linear-network.md)
- [Recursive power saving from the rank deficit](power-saving-recurrence.md)
- [Address shear from the bit network](bit-shear-interface.md)
- [Lower-triangular (Bruhat) factorization](lower-triangular-factorization.md)
- [Cost of a rational matrix shear](matrix-shear-cost.md)
- [Recursive power-width address interchange](power-width-interchange.md)
- [Address-chunk interchange in time O(V u^τ)](arbitrary-width-interchange.md)
- [Packed selected-bit addition](packed-selected-bit-addition.md)
- [Polynomial ring modulo y^r + 1](negacyclic-ring.md)
- [Fixed-point complex coefficients and truncation](fixed-point-disk.md)
- [Signed packing of ring products](signed-packing-product.md)
- [Contractions and error accounting](error-accounting.md)
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

- "number $s$ of smaller calls satisfies $s<Wm$." (paper)

  > The finite construction in Section~\ref{sec:finite-networks} attaches subspaces of a fixed $m$-dimensional space to its gates and terminals. The subspaces at adjacent vertices are nested. Their dimension changes count the smaller operations needed on an edge, with an additional source contribution in the bit construction. The construction uses three-element subsets: gather and scatter create coefficients depending on intersection size, and auxiliary wires cancel the unwanted coefficients. Orthogonality of the corresponding indicator vectors permits the subspace assignments. The decisive property is that the total number $s$ of smaller calls satisfies $s<Wm$.

- "\frac{L_{\rm b}}{N}=\frac{100}{539},\qquad" (paper)

  > The loss ratios have the exact values \[ \frac{L_{\rm b}}{N}=\frac{100}{539},\qquad \frac{L_{\rm c}}{N}=\frac{101}{539}. \] In particular, both are smaller than $1/2$. We now turn the dimension count into the two interfaces needed later.


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

Write the body to `exegenius/tasks/0013-write-rank-deficit.answer.md` and the JSON to `exegenius/tasks/0013-write-rank-deficit.answer.json`, then run `exegenius submit 0013-write-rank-deficit` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0013-write-rank-deficit`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
