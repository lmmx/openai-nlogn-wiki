# exegenius task 0026-write-power-width-interchange

Project directory: `/home/user/openai-nlogn-wiki/runs/P4` (paths below are relative to it)

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

For these sources: The reader has finished a standard undergraduate computer science degree: discrete mathematics (induction, counting, modular arithmetic, primes, gcd, permutations, basic graphs), algorithms (asymptotic notation, divide and conquer, recurrences, sorting including radix sort, the idea of the FFT and Karatsuba multiplication at survey level), calculus and basic real analysis (limits, logarithms, exponentials, floors and ceilings, inequalities), introductory linear algebra and probability, and the basics of Turing machines and complexity. They have not studied abstract algebra beyond arithmetic mod n, coding theory, or number-theoretic transforms in depth, and have not met the multitape fast-multiplication literature (Schönhage–Strassen, Fürer, Harvey–van der Hoeven), Gaussian resampling, or Nussbaumer polynomial transforms.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes
- Fixed-tape Turing machine model
- The n log n optimality conjecture
- Established near-linear integer multiplier
- Matrices, rank, subspaces and projections
- Tensor products of vectors, spaces and operators
- Binary vectors, XOR and Hamming weight
- Nondegenerate bilinear forms and orthogonal complements
- Streaming fixed-point and Gaussian dyadic arithmetic
- Arrays, address fields, rows and logical volume
- Linear-time stream operations
- Controlled cyclic shifts and rational scalings
- Depth-first recursion schedule on fixed tapes
- Triple-intersection pairing formulas
- Linear network exchanging two banks with restored scratch
- Frames and the common-frame identity
- Nested subspace labels and the rank deficit
- Address shear
- Bit network and rational shear interface
- Lower-triangular factorization of a matrix
- Cost of a rational matrix shear
- Strict rank deficit gives a power saving
- Rows distributed cyclically among wire roles
- Asymptotic notation beyond big-O (also: Theta, Omega, little-o, Θ, Ω, o(1), liminf, eventual lower bound)
- Logarithms, exponentials, floors and ceilings (also: log base 2, lg n, floor, ceiling, change of base, iterated logarithm)
- Binary and radix-b representation of integers (also: positional notation, base-b digits, mixed radix, bit length, val(x))
- Schoolbook multiplication and Karatsuba (also: grade-school multiplication, long multiplication, quadratic multiplication, Karatsuba-Ofman, Toom-Cook)
- Divisibility, primes and gcd (also: coprime, relatively prime, greatest common divisor, Euclidean algorithm, trial division, prime number)
- Modular arithmetic and residue classes (also: integers mod n, Z/nZ, congruence, mod Q, remainder, division with remainder, residue ring)
- Roots of unity (also: primitive root of unity, n-th roots of unity, e^{2πi/n}, twiddle factors)
- Recurrences and geometric series (also: divide-and-conquer recurrence, master theorem, solving recurrences, geometric sum, T(n) = aT(n/b) + f(n))
- Induction and elementary proof technique (also: proof by induction, structural induction, contradiction, pigeonhole principle)
- Elementary counting and the union bound (also: binomial coefficients, counting subsets, inclusion–exclusion, union bound, fraction of a finite set, Boole's inequality)
- Sorting and radix sort (also: stable sort, radix sort, counting sort, sorting by key, bucket sort)
- Permutations and bijections (also: index permutation, bit reversal, inverse permutation, permutation matrix, one-to-one correspondence)
- Sets, products of ranges and lexicographic order (also: Cartesian product, index set [n], multi-index, lexicographic order, row-major order)
- Matrix transposition and row-major storage (also: transpose, k×k binary matrix, row-major matrix)
- Triangle inequality and error bounds (also: absolute error, rounding error, approximation error, supremum, modulus inequality, rounding to nearest integer)
- Boolean and arithmetic circuits as networks (also: logic gates, XOR gate, circuit, wires and gates, directed acyclic graph, fan-in and fan-out)
- Graphs, paths and neighbors (also: directed graph, edges and vertices, adjacent vertices, route in a graph)
- Stacks and recursion (also: call stack, LIFO, push and pop, depth-first traversal, recursive procedure)
- Fast Fourier transform and Karatsuba as survey knowledge (also: FFT multiplication, Schönhage–Strassen, polynomial multiplication via evaluation, evaluation and interpolation)
- Real and imaginary parts, rounding and truncation (also: Re and Im, truncate toward zero, nearest integer, fixed-point numbers)
- Dot product, vectors over the rationals and orthonormal bases (also: inner product, orthogonal vectors, standard basis, Gram–Schmidt, bilinear pairing)

## This page

Concept: Power-width interchange with rows
Gloss: Using the bit network on W role streams with address shears applied recursively on every edge, two chunks of e = m^k digits are interchanged in O(V e^τ) time, via the XOR combinations of intermediate data whose net effect is an exact permutation.

## This page in the argument

The step: Two disjoint chunks of $e=m^k$ radix-$q$ digits each can be interchanged in $O(Ve^\tau)$ time, provided a preceding row field has length divisible by $W^k$.
How: Perform the interchange as the three shears $D\leftarrow D-H$, $H\leftarrow H+D$, $D\leftarrow H-D$ and run the middle shear through the bit network on $W$ role streams, applying an address shear to every edge by recursive smaller interchanges.
Why: An edge matrix of rank $a$ needs only $a$ smaller interchanges and the total rank is below the number of wires times $m$, so the recurrence saves a power of the chunk width. (the sources say so: "Because the sum of these ranks is less than the number of wires times" (paper))
Striking feature: Although the intermediate steps form XOR combinations of data, the net effect is an exact permutation, and it is exact for arbitrary initial contents of the scratch role streams. (explain why it holds, from the method)

Its sub-steps, in order:

- The shear $(H,D)\mapsto(H+AD,D)$ over $\mathbb Z/q^b\mathbb Z$ with a rational matrix $A$ of rank $a$ is performed with exactly $a$ interchanges of $b$-digit fields plus $O(V)$ further work. (on [Cost of a rational matrix shear](matrix-shear-cost.md))
- Whole rows can be dealt cyclically into $W$ role streams, with the row count padded per prefix to a multiple of $W$, so that each stream has volume $V/W$ and the same remaining shape and gates act pointwise on matching addresses. (on [Rows distributed cyclically among wire roles](row-splitting-roles.md))
- On every circuit edge apply the address shear $\Phi_{A_e}$ to that role stream, and execute every gate pointwise; the endpoint matrices then give $H\leftarrow H+D$ on every row.
- Two further updates that target the later group, $D\leftarrow D-H$ and $D\leftarrow H-D$, complete the interchange of the two full chunks around the shear.
- If a call at width $e=mf$ makes $s$ calls at width $f$, each on a stream of volume $V/W$, then the normalized cost satisfies $F_k\le(s/W)F_{k-1}+O(1)$, and since $s/W<m^\tau$ with $\tau<1$ this solves to $F_k=O(e^\tau)$. (on [Strict rank deficit gives a power saving](rank-deficit-recurrence.md))
- Recursive calls on $W$ role streams can be run on one fixed set of tapes by parking the inactive streams on a stack, copying the active stream to the child and restoring afterwards, at cost $O(V)$ per node. (on [Depth-first recursion schedule on fixed tapes](fixed-tape-dfs-schedule.md))

It serves these steps, from the main result down:

- A single deterministic fixed-tape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.; how: Reduce multiplication to convolution over $\mathbb C[y]/(y^r+1)$ through radix digits, Chinese-remainder axes, Gaussian resampling and chirps, speed up the data movement and the butterfly arithmetic with two network-based tape procedures with a strict rank saving, recover the exact product by rounding and carries, and add up the costs. (on [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md))
- Two tape procedures exist for fixed exponents $\tau,\lambda'<1$: one interchanges two disjoint address chunks of $u$ bits in $O(Vu^\tau)$ time, and one applies a normalized butterfly layer on up to $d$ address chunks in $O(Vd^{\lambda'})$ time, where $V$ is the logical bit volume.; how: Obtain both from one fixed linear network that exchanges two banks of values and restores every auxiliary value, whose edge frame changes are smaller calls of the same procedure; the strict inequality $s<Wm$ on their number gives a recursion with a power saving.
- There is a fixed $\tau<1$ and one fixed multitape procedure that interchanges two disjoint address chunks of $u$ bits, $(p,h,g,d,z)\mapsto(p,d,g,h,z)$, in $O(Vu^\tau)$ steps on an arbitrary bit array of volume $V$.; how: Peel off the top digits of both chunks to supply rows, pad the rows to a multiple of $W^k$, decompose the remaining width in base $m$ and apply the power-width interchange to each piece, then remove padding and reverse the high-digit moves. (on [Fast address-chunk interchange](chunk-swap.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (C1.1.a, C1.1.b). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**C1.1.a**: On every circuit edge apply the address shear $\Phi_{A_e}$ to that role stream, and execute every gate pointwise; the endpoint matrices then give $H\leftarrow H+D$ on every row.
Source: "On every circuit edge apply" (paper)
> For a rational matrix $M$, let $\Phi_M$ act on an array by moving its entry at address $(H,D)$ to $(H+MD,D)$, with every spectator unchanged. Thus $\Phi_M$ is the array permutation induced by that address map. Its inverse is $\Phi_{-M}$ and $\Phi_{M'}\Phi_M=\Phi_{M'+M}$. On every circuit edge apply $\Phi_{A_e}$ to that role stream; implement it by Lemma~\ref{lem:matrix-shear}, recursively interchanging each pivot pair of $b$-digit fields. Execute each circuit gate pointwise at matching addresses of its role streams.

**C1.1.b**: Two further updates that target the later group, $D\leftarrow D-H$ and $D\leftarrow H-D$, complete the interchange of the two full chunks around the shear.
Source: "To interchange the two full chunks, perform" (paper)
> To interchange the two full chunks, perform \[ D\leftarrow D-H,\qquad H\leftarrow H+D,\qquad D\leftarrow H-D, \] componentwise. Only the middle shear uses the circuit. The other two updates target the later group and have linear cost. The transformation sends $(H,D)$ to $(D,H)$.

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- C1.1.2 (on [Cost of a rational matrix shear](matrix-shear-cost.md)): The shear $(H,D)\mapsto(H+AD,D)$ over $\mathbb Z/q^b\mathbb Z$ with a rational matrix $A$ of rank $a$ is performed with exactly $a$ interchanges of $b$-digit fields plus $O(V)$ further work.
- C1.1.3 (on [Rows distributed cyclically among wire roles](row-splitting-roles.md)): Whole rows can be dealt cyclically into $W$ role streams, with the row count padded per prefix to a multiple of $W$, so that each stream has volume $V/W$ and the same remaining shape and gates act pointwise on matching addresses.
- C1.1.4 (on [Strict rank deficit gives a power saving](rank-deficit-recurrence.md)): If a call at width $e=mf$ makes $s$ calls at width $f$, each on a stream of volume $V/W$, then the normalized cost satisfies $F_k\le(s/W)F_{k-1}+O(1)$, and since $s/W<m^\tau$ with $\tau<1$ this solves to $F_k=O(e^\tau)$.
- C1.1.5 (on [Depth-first recursion schedule on fixed tapes](fixed-tape-dfs-schedule.md)): Recursive calls on $W$ role streams can be run on one fixed set of tapes by parking the inactive streams on a stack, copying the active stream to the child and restoring afterwards, at cost $O(V)$ per node.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Bit network and rational shear interface](bit-network-interface.md): The bit-valued network (XOR gates, W_b wires) with rational projection matrices on gates so that every route's endpoint difference is the identity (the shear H ← H+D) while the total rank of edge differences s_b is below W_b·m.
  Shown as: Power-width interchange with rows *<predicate>* Bit network and rational shear interface
- [Cost of a rational matrix shear](matrix-shear-cost.md): The shear (H,D)↦(H+AD,D) of rank a is performed with exactly a interchanges of b-digit fields plus O(V) further work, using triangular factors as linear-time controlled shifts and one interchange per pivot.
  Shown as: Power-width interchange with rows *<predicate>* Cost of a rational matrix shear
- [Rows distributed cyclically among wire roles](row-splitting-roles.md): To run the network on an array, whole rows are dealt cyclically into W role streams (padding the row count to a multiple of W per prefix), each of volume V/W with identical remaining shape, and gates act pointwise on matching addresses.
  Shown as: Power-width interchange with rows *<predicate>* Rows distributed cyclically among wire roles
- [Strict rank deficit gives a power saving](rank-deficit-recurrence.md): If a call at parameter m·f makes s calls at parameter f, each on a stream of volume V/W, then normalized cost obeys F_k ≤ (s/W)F_{k−1}+O(1); since s/W < m^τ with τ<1 the solution is O(e^τ), a power-of-the-width saving.
  Shown as: Power-width interchange with rows *<predicate>* Strict rank deficit gives a power saving
- [Depth-first recursion schedule on fixed tapes](fixed-tape-dfs-schedule.md): Recursive calls on W role streams are run on one fixed set of tapes by parking the inactive streams on a stack, copying the active stream to the child, and restoring afterwards, costing O(V) per node.
  Shown as: Power-width interchange with rows *<predicate>* Depth-first recursion schedule on fixed tapes

## Pages that build on this one

- Fast address-chunk interchange: Arbitrary-width interchange of two disjoint address chunks of u bits in O(V u^τ) with fixed τ<1: peel off top digits to supply rows, pad rows, decompose the rest in base m and apply the power-width interchange to each piece.

## Other pages you may link to

- [Fixed-tape Turing machine model](multitape-model.md)
- [The n log n optimality conjecture](nlogn-conjecture.md)
- [Streaming fixed-point and Gaussian dyadic arithmetic](fixed-point-arithmetic.md)
- [Established near-linear integer multiplier](established-multiplier.md)
- [Arrays, address fields, rows and logical volume](address-fields-volume.md)
- [Linear-time stream operations](stream-ops.md)
- [Controlled cyclic shifts and rational scalings](controlled-shifts.md)
- [Matrices, rank, subspaces and projections](linear-algebra-basics.md)
- [Tensor products of vectors, spaces and operators](tensor-products.md)
- [Address shear](address-shear.md)
- [Binary vectors, XOR and Hamming weight](f2-vectors.md)
- [Nondegenerate bilinear forms and orthogonal complements](bilinear-orthogonality.md)
- [Triple-intersection pairing formulas](subset-pairing-formulas.md)
- [Linear network exchanging two banks with restored scratch](scalar-exchange-network.md)
- [Frames and the common-frame identity](network-frames.md)
- [Nested subspace labels and the rank deficit](subspace-labels-rank-saving.md)
- [Lower-triangular factorization of a matrix](lower-factorization.md)
- [Fast address-chunk interchange](chunk-swap.md)
- [Carry-free packed controlled rotations](packed-rotations.md)
- [Deterministic repair of exceptional addresses](exceptional-address-repair.md)
- [Packed selected-bit addition on one rectangle](packed-selected-bit-addition.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring-negacyclic.md)
- [Discrete Fourier transform](dft.md)
- [Synthetic root of unity ω_t = y^{2r/t}](synthetic-roots.md)
- [Butterfly step and decimation-in-frequency recursion](fft-butterfly.md)
- [Phase kernel C = aI + bX](phase-kernel.md)
- [Complex phase network interface](complex-network-interface.md)
- [Recursive phase-frame layer on slots](phase-frame-layer.md)
- [Multidimensional transform and cyclic convolution on a product of axes](multidim-dft.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Retained stored frequency order](frequency-order.md)
- [Max-modulus norm, contractions and error propagation](contraction-error-budget.md)
- [Disk grid and truncation](disk-grid-truncation.md)
- [Guard width for exact intermediate values](guard-width.md)
- [Simultaneous normalized butterfly layer](simultaneous-layer.md)
- [Transform layout and cost](transform-layout.md)
- [Signed Kronecker packing for ring products](signed-packing.md)
- [Gaussian resampling with retained permutations](gaussian-resampling.md)
- [Tensor interface for resampling](tensor-resampling.md)
- [Cyclic convolution and the convolution theorem](cyclic-convolution.md)
- [Integer multiplication as convolution of radix digits](multiplication-as-convolution.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Cancellation of the source permutation](source-permutation-cancel.md)
- [Convolution from the retained transform layout](synthetic-convolution.md)
- [Size parameters of the algorithm](parameter-choice.md)
- [Chinese-remainder map to prime cyclic axes](crt-address-map.md)
- [Distinct prime source lengths near powers of two](prime-lengths.md)
- [Coefficient twist from cyclic to negacyclic](coefficient-twist.md)
- [Middle transform computed by chirp and complex convolution](chirp-transform.md)
- [Source transform procedure](source-transform.md)
- [Exact recovery by rounding and carry propagation](exact-recovery.md)
- [The complete multiplication algorithm](multiplication-algorithm.md)
- [Cost analysis and the exponent κ](cost-analysis.md)
- [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "The chunks can be interchanged in $O(Ve^\tau)$ time" (paper)

  > \begin{proposition}[Power-width interchange with rows] \label{prop:power-interchange} Assume the fixed circuit data satisfy \eqref{eq:finite-shear-contract}, and let $q$ be a prime as in Lemma~\ref{lem:matrix-shear} for its edge matrices, also avoiding the denominators of every assigned terminal and gate matrix $M$. Choose a rational number $\tau\in(0,1)$ with $s/W<m^\tau$. For every $e=m^k$, $k\ge0$, consider two disjoint contiguous address chunks of $e$ radix-$q$ digits each. Suppose a row field preceding both chunks has length divisible by $W^k$. There may be additional fields before and after the row field, between the chunks, and after them. The chunks can be interchanged in $O(Ve^\tau)$ time, preserving every other address field, on a fixed number of finite-alphabet tapes. The constant is independent of all field lengths and of the data. \end{proposition}

- "Although its final effect is an exact permutation, its intermediate
steps form pointwise XOR combinations of data." (paper)

  > The first procedure interchanges two disjoint contiguous address fields of $u$ bits in an array whose addresses form a complete Cartesian product. Its cost is $O(Vu^\tau)$ for a fixed $\tau<1$. Although its final effect is an exact permutation, its intermediate steps form pointwise XOR combinations of data. The final permutation is exact for arbitrary initial auxiliary values.


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

Write the body to `exegenius/tasks/0026-write-power-width-interchange.answer.md` and the JSON to `exegenius/tasks/0026-write-power-width-interchange.answer.json`, then run `exegenius submit 0026-write-power-width-interchange` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0026-write-power-width-interchange`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
