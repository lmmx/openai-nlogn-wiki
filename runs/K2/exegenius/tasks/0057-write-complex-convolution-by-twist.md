# exegenius task 0057-write-complex-convolution-by-twist

Project directory: `/home/user/openai-nlogn-wiki/runs/K2` (paths below are relative to it)

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

For these sources: The reader has an undergraduate computer science degree: discrete mathematics (sets, counting, induction, modular arithmetic, gcd and primes), calculus and a first linear algebra course (matrix rank and row reduction), an algorithms course (asymptotic notations, recurrences, sorting, schoolbook arithmetic), and a theory course on Turing machines and their running time. Complex numbers are known through polar form and roots of unity, and binary and two's-complement representation through computer organization. Each subject is taken only to first-course depth: no abstract algebra beyond the fields and rings that linear algebra uses, no Fourier analysis beyond the finite transform, no number theory beyond gcd, primes and modular inverses, and nothing from coding theory, circuit complexity or the specialist finite-network material.

The reader already understands these concepts:

- Big-O notation (also: O-notation)
- Polynomials
- Complex numbers
- Basic Turing machines and tapes
- Fixed-tape Turing machine model (also: fixed finite-tape model)
- Schönhage–Strassen optimality conjecture (also: n log n conjecture)
- Established fixed-tape integer multiplier (also: Harvey–van der Hoeven multiplier)
- Elementary stream operations
- Logical volume
- Address fields and rows
- Row splitting into role streams
- Controlled cyclic shifts
- Linear algebra over a field
- Restoration of arbitrary scratch values
- Triple-subset exchange network
- Frames on network vertices
- Subspace labels and orthogonal residuals
- Rank saving s < Wm (also: rank deficit)
  - $s$ (smaller-call count): The number of smaller calls made by one network invocation, the sum of the rational ranks of all edge matrix differences.
  - $W$ (wire count): The number of wires in the network, including its scratch wires.
  - $m$ (label dimension): The dimension of the ambient label space, which is h cubed for the set size h = 100.
- Volume-normalized recursion
- Lower-triangular factorization
- Matrix shear of address fields
- Finite circuit as address permutation
- Power-width chunk interchange
- Arbitrary-width chunk interchange
- Gaussian dyadic
- Guard bits
- Normalized two-point butterfly
- Two-point phase kernel
- Binary phase frames
- Packed selected-bit XOR
- Disk-grid arrays
- Truncation to the precision grid
- Approximate roots of unity
- Simultaneous butterfly layer
- Polynomial ring modulo y^r + 1 (also: negacyclic polynomial ring)
  - $y$ (polynomial variable): The formal variable of the ring, whose powers serve as roots of unity in the transforms.
  - $r$ (record length): The number of complex coefficients in a record, which is a power of two.
- Polynomial roots of unity
- Cyclic convolution
- Normalized discrete Fourier transform
- Contraction
- Synthetic polynomial transform (also: Nussbaumer polynomial transform)
- Positional layout of transform axes
- Synthetic transform on fixed tapes
- Retained frequency order
- Phase twist of the last coordinate
- Signed coefficient packing
- Normalized polynomial-ring product
- Normalized ring convolution
- Gaussian resampling
- Resampling with permutations left in the transform
- Prime source lengths
- Multidimensional Gaussian resampling
- Cancellation of the source permutation
- Bluestein chirp identity
- Chinese-remainder coefficient map
- Radix-digit convolution
- Fixed rational exponent choices
- Size parameters for the input length
- Arithmetic modulo n (also: congruence arithmetic, residue classes, integers mod n, Z/nZ, modular inverse, reduction modulo n)
- The field with two elements (also: GF(2), F_2, binary field, field of two elements, arithmetic mod 2)
- Greatest common divisor and coprimality (also: gcd, relatively prime, coprime, Euclid's algorithm, extended Euclidean algorithm, Bezout's identity)
- Prime numbers and trial division (also: primes, primality test, trial division, prime factorization)
- Positional (radix) number representation (also: base-b representation, radix representation, binary representation, digit expansion, bit string, most significant bit first)
- Two's-complement integers (also: two's complement, 2's complement, signed binary integer, sign-extension)
- Bitwise operations (also: exclusive or, XOR, bitwise AND, bit shift, cyclic rotation, Boolean logic gates)
- Hamming weight (also: Hamming weight of a bit string, population count, popcount, number of ones, parity of a bit string)
- Floor, ceiling, logarithms and exponentials (also: floor function, ceiling function, lg, base-2 logarithm, natural logarithm, exponential function, exp)
- Theta, Omega and little-o notation (also: Big-Theta, Big-Omega, little-o, tight asymptotic bound, asymptotic lower bound, eventual inequality)
- Geometric series (also: geometric sum, sum of powers of a ratio, geometric progression sum, convergent geometric series)
- Recurrence relations (also: recurrence, unrolling a recurrence, divide-and-conquer recurrence, difference equation, master theorem)
- Mathematical induction and proof by contradiction (also: induction, strong induction, proof by induction on n, reductio ad absurdum, contradiction)
- Sets, Cartesian products and lexicographic order (also: Cartesian product, product set, intersection of sets, lexicographic order, dictionary order, lex order, indicator vector)
- Permutations and permutation matrices (also: bijection of a finite set, permutation of coordinates, permutation matrix, cycle notation, symmetric group)
- Binomial coefficients and counting subsets (also: binomial coefficient, n choose k, combinations, choose function, counting argument)
- Polar form, Euler's formula and roots of unity (also: polar form, Euler's formula, de Moivre's formula, complex roots of unity, unit circle, argument of a complex number, e^(i theta))
- Matrix rank and Gaussian elimination (also: rank of a matrix, column rank, row rank, row reduction, elementary row operations, row echelon form, invertible matrix, nonsingular matrix)
- Directed graphs (also: digraph, directed acyclic graph, DAG, sources and sinks of a digraph, in-degree and out-degree, directed path)
- Worst-case time complexity of Turing machines (also: running time, worst-case running time, step complexity, time complexity class, TIME(f(n)), time bound)
- Sorting, stability and radix sort (also: comparison sort, stable sort, stable sorting, radix sort, sorting by keys)
- Schoolbook multiplication and long division (also: schoolbook multiplication, long multiplication, long division, quadratic-time multiplication, grade-school algorithm)

## This page

Concept: Complex cyclic convolution by twist
Gloss: The normalized complex cyclic convolution obtained from the normalized ring convolution by applying the phase twist to each operand and its inverse to the result, which is the convolution the chirp identity needs.

## This page in the argument

The step: The normalized complex cyclic convolution $(f*g)/T$ is computed by twisting each operand by powers of $\zeta$, applying the ring convolution, and untwisting.
How: apply a diagonal phase twist on the last coordinate, which turns cyclic into negacyclic convolution over $\mathcal R_r$
Why: The complex convolution is taken from the synthetic ring convolution by a coefficient twist. (the sources say so: "obtained from the synthetic convolution by a coefficient twist." (paper))

Its sub-steps, in order:

- The substitution $x_d\mapsto\zeta y$ with $\zeta=e^{\pi i/r}$ is well defined on $\mathbb C[x_d]/(x_d^r-1)$ and multiplies coefficient $k$ by $\zeta^k$. (on [Phase twist of the last coordinate](negacyclic-twist.md))
- The normalized complex cyclic convolution is $D_-\iota^{-1}\mathcal M_r(\iota D_+f,\iota D_+g)=(f*g)/T$.
- Disk-grid approximations to $\zeta^{k}$ and $\zeta^{-k}$ with error below $2\,2^{-p}$ are obtained for every $0\le k<r$. (on [Approximate roots of unity](approximate-roots-of-unity.md))

It serves these steps, from the main result down:

- On one deterministic machine with a fixed finite alphabet and a fixed number of one-dimensional tapes, two $n$-bit integers multiply exactly in worst-case time $O(n(\lg n)^{1-\kappa})$, with $\kappa=2^{-182}$.; how: show that the fixed-tape tools are cheap and accurate, show that the transform pipeline returns the exact product, then bound its total cost (on [Deterministic integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md))
- On input $x\#y$ the procedure outputs exactly the $2n$-bit binary product of $\operatorname{val}(x)$ and $\operatorname{val}(y)$.; how: fix the sizes, reduce to a radix-digit convolution, evaluate it through the approximate transforms with chirp and twist, recover the integers by rounding, then propagate carries (on [Multiplication algorithm by transforms](digit-convolution-algorithm.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S2.4.2). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S2.4.2**: The normalized complex cyclic convolution is $D_-\iota^{-1}\mathcal M_r(\iota D_+f,\iota D_+g)=(f*g)/T$.
Source: "\mathcal M_r(\iota D_+f,\iota D_+g)" (paper)
> Put $M=\prod_{i<d}t_i=T/r$. For a complex array $f$ on $\prod_{i=1}^d\mathbb Z/t_i\mathbb Z$, with $t_d=r$, define \[ (\iota f)_{\boldsymbol j} =\sum_{k=0}^{r-1}f_{\boldsymbol j,k}y^k, \qquad \boldsymbol j\in\prod_{i<d}\mathbb Z/t_i\mathbb Z. \] This identifies the scalar tensor with an array of $M$ records in $\mathcal R$. As maps of values, $\iota$ and $\iota^{-1}$ preserve norms and grids. Write $(D_\pm f)_{\boldsymbol j,k}=\zeta^{\pm k}f_{\boldsymbol j,k}$. The linewise extension of $\Theta$ is $\iota D_+$, with inverse $D_-\iota^{-1}$. Consequently, with $\mathcal M_r$ from Section~\ref{sec:exact-ring-products}, normalized complex cyclic convolution is \[ \mathcal M_{\mathbb C}(f,g) :=D_-\iota^{-1} \mathcal M_r(\iota D_+f,\iota D_+g) =\frac{f*g}{T}. \] Here $\mathcal M_r$ convolves the first $d-1$ axes over $\mathcal R$, whereas $*$ on the right convolves all $d$ scalar axes. The division by $T$ is already part of $\mathcal M_r$. The maps $D_\pm$ and $\iota^{\pm1}$ are isometries, so $\mathcal M_{\mathbb C}$ is also a bilinear contraction.

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S2.4.1 (on [Phase twist of the last coordinate](negacyclic-twist.md)): The substitution $x_d\mapsto\zeta y$ with $\zeta=e^{\pi i/r}$ is well defined on $\mathbb C[x_d]/(x_d^r-1)$ and multiplies coefficient $k$ by $\zeta^k$.
- S2.4.3 (on [Approximate roots of unity](approximate-roots-of-unity.md)): Disk-grid approximations to $\zeta^{k}$ and $\zeta^{-k}$ with error below $2\,2^{-p}$ are obtained for every $0\le k<r$.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Phase twist of the last coordinate](negacyclic-twist.md): The isomorphism from the cyclic group algebra of length r to the polynomial ring that sends x to ζy with ζ = e^(πi/r), implemented by multiplying coefficient k by ζ^k and undone by multiplying by ζ^(−k).
  Shown as: Complex cyclic convolution by twist *<predicate>* Phase twist of the last coordinate
- [Normalized ring convolution](normalized-ring-convolution.md): The bilinear contraction M_r(f, g) = (f ∗ g)/(rM) = (f ∗ g)/T on arrays over the polynomial ring, computed as two forward synthetic transforms, a pointwise ring product and an opposite transform.
  Shown as: Complex cyclic convolution by twist *<predicate>* Normalized ring convolution
- [Approximate roots of unity](approximate-roots-of-unity.md): Disk-grid approximations of the roots of unity e^(2πi j/k) with error below 2^(−p), computable in time O(max(p, log k)^(1+δ)) and used for the phase twists.
  Shown as: Complex cyclic convolution by twist *<predicate>* Approximate roots of unity

## Pages that build on this one

- Computed chirp transform: The chirp identity evaluated with approximate phases, a computed complex convolution and final truncations, mapping a disk-grid array of norm at most 0.6 to an approximation of QF_t x with error below 8TL·2^(−p).

## Other pages you may link to

- [Polynomial ring modulo y^r + 1](polynomial-ring.md)
- [Polynomial roots of unity](polynomial-roots-of-unity.md)
- [Normalized two-point butterfly](two-point-butterfly.md)
- [Gaussian dyadic](gaussian-dyadic.md)
- [Linear algebra over a field](linear-algebra.md)
- [Fixed-tape Turing machine model](fixed-tape-machine.md)
- [Schönhage–Strassen optimality conjecture](schonhage-strassen-conjecture.md)
- [Logical volume](logical-volume.md)
- [Address fields and rows](address-fields.md)
- [Elementary stream operations](elementary-stream-operations.md)
- [Row splitting into role streams](row-splitting.md)
- [Controlled cyclic shifts](controlled-shifts.md)
- [Restoration of arbitrary scratch values](scratch-restoration.md)
- [Triple-subset exchange network](triple-subset-exchange-network.md)
- [Frames on network vertices](frames.md)
- [Subspace labels and orthogonal residuals](subspace-labels.md)
- [Rank saving s < Wm](rank-saving.md)
- [Volume-normalized recursion](volume-normalized-recursion.md)
- [Lower-triangular factorization](lower-triangular-factorization.md)
- [Matrix shear of address fields](matrix-shear-interchange.md)
- [Finite circuit as address permutation](circuit-to-address-permutation.md)
- [Power-width chunk interchange](power-width-chunk-interchange.md)
- [Arbitrary-width chunk interchange](arbitrary-width-chunk-interchange.md)
- [Two-point phase kernel](two-point-phase-kernel.md)
- [Binary phase frames](binary-phase-frames.md)
- [Packed selected-bit XOR](packed-selected-bit-xor.md)
- [Guard bits](guard-bits.md)
- [Disk-grid arrays](disk-grid-arrays.md)
- [Truncation to the precision grid](grid-truncation.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Positional layout of transform axes](transform-layout.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Radix-digit convolution](radix-digit-convolution.md)
- [Chinese-remainder coefficient map](crt-coefficient-map.md)
- [Normalized discrete Fourier transform](discrete-fourier-transform.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Synthetic transform on fixed tapes](synthetic-transform-on-tapes.md)
- [Retained frequency order](frequency-order-retention.md)
- [Established fixed-tape integer multiplier](hvdh-multiplier.md)
- [Signed coefficient packing](signed-coefficient-packing.md)
- [Normalized polynomial-ring product](ring-product.md)
- [Contraction](contraction.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Fixed rational exponent choices](fixed-exponent-choices.md)
- [Size parameters for the input length](size-parameters.md)
- [Prime source lengths](prime-source-lengths.md)
- [Resampling with permutations left in the transform](permutation-free-resampling.md)
- [Multidimensional Gaussian resampling](tensor-resampling.md)
- [Cancellation of the source permutation](source-permutation-cancellation.md)
- [Computed chirp transform](chirp-transform-procedure.md)
- [Source transform](source-transform.md)
- [Multiplication algorithm by transforms](digit-convolution-algorithm.md)
- [Carry propagation](carry-propagation.md)
- [Precision and exact recovery](precision-and-exact-recovery.md)
- [Cost accounting for the dominant terms](cost-exponent-accounting.md)
- [Deterministic integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "obtained from the synthetic convolution by a coefficient twist" (paper)

  > The power-of-two complex convolution used in the chirp identity is obtained from the synthetic convolution by a coefficient twist. Put $\mathcal R=\mathcal R_r=\mathbb C[y]/(y^r+1)$ and $\zeta=e^{\pi i/r}$. The map \[ \Theta:\mathbb C[x_d]/(x_d^r-1)\longrightarrow\mathcal R, \qquad x_d\longmapsto\zeta y \] is well defined, since $(\zeta y)^r=(-1)(-1)=1$. On the bases $(x_d^k)_{0\le k<r}$ and $(y^k)_{0\le k<r}$ it is diagonal, multiplying coefficient $k$ by the nonzero number $\zeta^k$. It is therefore an isomorphism, with inverse multiplying that coefficient by $\zeta^{-k}$. Both exact maps preserve the coefficient sup norm. For an explicit check on the wrap, write $k+l=j+hr$, where $h\in\{0,1\}$. A product term after twisting and negacyclic reduction has factor \[ \zeta^{k+l}(-1)^h=\zeta^j(\zeta^r)^h(-1)^h=\zeta^j. \] Untwistin


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

Write the body to `exegenius/tasks/0057-write-complex-convolution-by-twist.answer.md` and the JSON to `exegenius/tasks/0057-write-complex-convolution-by-twist.answer.json`, then run `exegenius submit 0057-write-complex-convolution-by-twist` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0057-write-complex-convolution-by-twist`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
