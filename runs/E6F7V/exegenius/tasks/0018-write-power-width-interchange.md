# exegenius task 0018-write-power-width-interchange

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
- Rank deficit s < W m
- Recursive power saving from the rank deficit
- Lower-triangular (Bruhat) factorization
- Address shear from the bit network
- Cost of a rational matrix shear
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

Concept: Recursive power-width address interchange
Gloss: Two address chunks of m^k digits are interchanged in O(V e^τ) by splitting rows into W role streams, running the bit network whose edges are shears (smaller interchanges), and finishing with D←D−H, H←H+D, D←H−D; a depth-first schedule on fixed tapes realizes the recursion.

## This page in the argument

The step: For $e=m^k$ digits, two address chunks of $e$ digits are interchanged in $O(Ve^\tau)$ time, provided a preceding row field has length divisible by $W^k$.
How: Split rows into $W$ role streams, run the bit network whose edges $\Phi_{A_e}$ are shears done by smaller interchanges (Lemma on matrix shears), undo the role permutation to obtain $H\leftarrow H+D$ on all roles, finish with $D\leftarrow D-H$, $H\leftarrow H+D$, $D\leftarrow H-D$, and schedule the recursion depth-first on fixed tapes.
Why: The bit network turns an interchange of width $e$ into $s$ interchanges of width $e/m$ on streams $1/W$ as large, which is the recurrence $F_k\le(s/W)F_{k-1}+O(1)$; the only thing to check besides the frames is that the recursion fits on a fixed number of tapes. (the sources leave this for the reader to work out: spell it out)
Striking feature: The interchange is an exact permutation of the data, yet it is computed through XOR combinations of role streams, and it comes out right for arbitrary initial contents of the scratch roles because the transparent-computation schedule restores them. (explain why it holds, from the method)

Its sub-steps, in order:

- Split whole rows cyclically into $W$ role streams, each of volume $V/W$ with the same remaining shape.
- Applying $\Phi_{A_e}$ on every edge and the gates pointwise yields $H\leftarrow H+D$ on every original row, including rows assigned to scratch roles.
- The interchange follows from the shear by the three updates $D\leftarrow D-H$, $H\leftarrow H+D$, $D\leftarrow H-D$, only the middle one using the circuit.
- The number of recursive calls is the sum of the edge ranks, exactly $s$, each on a stream of volume $V/W$.
- Parking the inactive role streams on a stack makes each push, pop and copy cost $O(V)$ at a parent node, so scheduling the $s$ calls on fixed tapes adds only $O(V)$.

It serves these steps, from the main result down:

- One deterministic fixed-tape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$, refuting the $n\log n$ optimality conjecture in this model.; how: Build the two accelerated tape procedures (address interchange and simultaneous butterfly layers), use them inside synthetic transforms and Gaussian resampling to compute a convolution, assemble the multiplication algorithm with exact recovery, and total the cost. (on [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md))
- Two tape procedures cost less than a pass per level: interchanging two disjoint $u$-bit address fields of a volume-$V$ array costs $O(Vu^\tau)$ and a simultaneous butterfly layer on $D\le d$ chunks costs $O(Vd^{\lambda'})$, for fixed $\tau,\lambda'<1$.; how: Give each procedure its own fixed linear network that exchanges two banks of values and restores all scratch values, with total number $s$ of smaller calls below $Wm$, then run the network recursively on role streams of volume $V/W$ (interchange of address fields first, numerical layers second).
- Two disjoint contiguous address fields of $u$ bits (any width, any gaps, even one-bit payload) in an array of volume $V$ are interchanged in $O(Vu^\tau)$ time for a fixed $\tau=1-2^{-50}<1$; the intermediate steps are XOR combinations although the result is an exact permutation.; how: Interchange fields of power width $m^k$ recursively by the bit network with shears as edges, then reduce arbitrary widths to power widths by peeling off high digits to make rows, padding the row count, and splitting the width in base $m$. (on [Address-chunk interchange in time O(V u^τ)](arbitrary-width-interchange.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S2.3.1, S2.3.2, S2.3.3, S2.3.4, S2.3.5). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S2.3.1**: Split whole rows cyclically into $W$ role streams, each of volume $V/W$ with the same remaining shape.
Source: "Split whole rows cyclically into $W$ role streams within each prefix" (paper)
> Split whole rows cyclically into $W$ role streams within each prefix preceding the row field. Write the original row number as $r=Wg+(w-1)$ with $1\le w\le W$; stream $w$ has row number $g$. These streams have exactly the same remaining shape, including the full ranges of $H$ and $D$. Each has logical volume $V/W$, and its row count is divisible by $W^{k-1}$.

**S2.3.2**: Applying $\Phi_{A_e}$ on every edge and the gates pointwise yields $H\leftarrow H+D$ on every original row, including rows assigned to scratch roles.
Source: "is $H\leftarrow H+D$ on every original row, including rows assigned" (paper)
> The row split supplies the common address set used in the frame identity~\eqref{eq:common-frame-identity}. Here the frame at a vertex with matrix $M$ is the address permutation $\Phi_M$, and every edge changes it by $\Phi_{M'-M}$. The same invariant proof applies because a common address permutation commutes with every pointwise bit gate. For the physical input arrays $f_w$, the logical arrays are $g_w=\Phi_{-M_{\mathrm{in}(w)}}f_w$; this only specifies their interpretation, with no initial tape operation. The logical circuit routes $g_w$ to role $\rho(w)$. Thus its physical output satisfies \[ f'_{\rho(w)} =\Phi_{M_{\mathrm{out}(\rho(w))}} \Phi_{-M_{\mathrm{in}(w)}}f_w =\Phi_{I_m}f_w, \] by~\eqref{eq:finite-shear-contract}. Merge by returning row $g$ of output role $\rho(w)$ to the original row $Wg+(w-1)$ within the same preceding prefix. This undoes $\rho$ and restores row order. The result is $H\leftarrow H+D$ on every original row, including rows assigned to scratch roles, whose initial values were arbitrary.

**S2.3.3**: The interchange follows from the shear by the three updates $D\leftarrow D-H$, $H\leftarrow H+D$, $D\leftarrow H-D$, only the middle one using the circuit.
Source: "D\leftarrow D-H,\qquad H\leftarrow H+D,\qquad D\leftarrow H-D," (paper)
> To interchange the two full chunks, perform \[ D\leftarrow D-H,\qquad H\leftarrow H+D,\qquad D\leftarrow H-D, \] componentwise. Only the middle shear uses the circuit. The other two updates target the later group and have linear cost. The transformation sends $(H,D)$ to $(D,H)$.

**S2.3.4**: The number of recursive calls is the sum of the edge ranks, exactly $s$, each on a stream of volume $V/W$.
Source: "The number of recursive calls is the sum of the edge ranks, exactly $s$." (paper)
> The number of recursive calls is the sum of the edge ranks, exactly $s$. Each acts on one role stream of volume $V/W$, retaining all other fields as spectators. Splitting, merging, gates, and triangular operations have total cost $O(V)$ because their number is fixed. Below we verify that scheduling the recursive calls on fixed tapes also costs $O(V)$ at this node. Thus if $F_k$ is a uniform upper bound for time divided by logical volume, then \begin{equation} \label{eq:swap-recurrence} F_0=O(1),\qquad F_k\le(s/W)F_{k-1}+O(1). \end{equation} For $a=s/W<m^\tau$ the geometric sum $\sum_{j=0}^k a^j$ is $O(m^{k\tau})$. If $a\le1$, the sum is at most $k+1=O(m^{k\tau})$; if $a>1$, it is $O(a^k)$. Hence $F_k=O(e^\tau)$.

**S2.3.5**: Parking the inactive role streams on a stack makes each push, pop and copy cost $O(V)$ at a parent node, so scheduling the $s$ calls on fixed tapes adds only $O(V)$.
Source: "Each push, pop, copy, positioning operation, or erasure moves $O(V)$" (paper)
> Each push, pop, copy, positioning operation, or erasure moves $O(V)$ symbols at a parent node. There are only the fixed number $s$ of child calls. This gives precisely the additional $O(V)$ term claimed above, even though each child itself has volume $V/W$. Temporary storage is therefore not substituted for logical volume in the factor $s/W$.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Cost of a rational matrix shear](matrix-shear-cost.md): For a rational matrix A of rank a, the shear (H,D) ↦ (H+AD,D) over ℤ/q^bℤ is done with exactly a interchanges of b-digit fields and O(V) other work, using triangular updates as controlled shifts.
  Shown as: Recursive power-width address interchange *<predicate>* Cost of a rational matrix shear
- [Recursive power saving from the rank deficit](power-saving-recurrence.md): A call at parameter m·f makes s calls at parameter f on streams of volume V/W, giving F_k ≤ (s/W)F_{k−1}+O(1) with s/W < m, so the normalized cost is O(parameter^τ) for some τ < 1.
  Shown as: Recursive power-width address interchange *<predicate>* Recursive power saving from the rank deficit
- [Array order and elementary stream operations](stream-operations.md): Arrays are stored in lexicographic address order on a tape; digit moves, digit swaps, pointwise maps on split streams and cyclic splitting of rows into W streams all take O(V) steps for volume V on fixed tapes.
  Shown as: Recursive power-width address interchange *<predicate>* Array order and elementary stream operations

## Pages that build on this one

- Address-chunk interchange in time O(V u^τ): Exchanging two disjoint contiguous address fields of u bits (any width, any gaps, even one-bit payload) in O(V u^τ) for a fixed τ = 1 − 2^{−50} < 1, by peeling off high digits to make rows, padding, and splitting the width in base m; the intermediate steps are XOR combinations though the result is an exact permutation.

## Other pages you may link to

- [Multiplication complexity and the n log n conjecture](nlogn-history.md)
- [Fixed finite-alphabet multitape model](fixed-tape-model.md)
- [Established O(n log n) multiplier (subroutine)](established-multiplier.md)
- [Controlled shifts](controlled-shifts.md)
- [Subspaces, orthogonality and rank](linear-algebra-prelims.md)
- [Linear network exchanging two banks with restored scratch values](xor-linear-network.md)
- [Subspace labels from three-element subsets](subset-labels.md)
- [Frames: changing the representation along a network](frames.md)
- [Rank deficit s < W m](rank-deficit.md)
- [Address shear from the bit network](bit-shear-interface.md)
- [Lower-triangular (Bruhat) factorization](lower-triangular-factorization.md)
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

- "The chunks can be interchanged in $O(Ve^\tau)$ time, preserving every" (paper)

  > \begin{proposition}[Power-width interchange with rows] \label{prop:power-interchange} Assume the fixed circuit data satisfy \eqref{eq:finite-shear-contract}, and let $q$ be a prime as in Lemma~\ref{lem:matrix-shear} for its edge matrices, also avoiding the denominators of every assigned terminal and gate matrix $M$. Choose a rational number $\tau\in(0,1)$ with $s/W<m^\tau$. For every $e=m^k$, $k\ge0$, consider two disjoint contiguous address chunks of $e$ radix-$q$ digits each. Suppose a row field preceding both chunks has length divisible by $W^k$. There may be additional fields before and after the row field, between the chunks, and after them. The chunks can be interchanged in $O(Ve^\tau)$ time, preserving every other address field, on a fixed number of finite-alphabet tapes. The constant is independent of all field lengths and of the data. \end{proposition}

- "D\leftarrow D-H,\qquad H\leftarrow H+D,\qquad D\leftarrow H-D," (paper)

  > To interchange the two full chunks, perform \[ D\leftarrow D-H,\qquad H\leftarrow H+D,\qquad D\leftarrow H-D, \] componentwise. Only the middle shear uses the circuit. The other two updates target the later group and have linear cost. The transformation sends $(H,D)$ to $(D,H)$.


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

Write the body to `exegenius/tasks/0018-write-power-width-interchange.answer.md` and the JSON to `exegenius/tasks/0018-write-power-width-interchange.answer.json`, then run `exegenius submit 0018-write-power-width-interchange` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0018-write-power-width-interchange`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
