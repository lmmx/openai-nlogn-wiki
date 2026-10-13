# exegenius task 0016-write-address-interchange

Project directory: `/home/user/openai-nlogn-wiki/runs/B1` (paths below are relative to it)

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

For these sources: The reader has done an undergraduate computer science degree: asymptotic analysis and recurrences, basic algorithms (including schoolbook and Karatsuba multiplication and the idea of the FFT), discrete mathematics (modular arithmetic, primes, the Chinese remainder theorem, permutations, bit operations), and first-year linear algebra (matrices, rank, invertibility, subspaces). They know complex numbers, polynomials and basic Turing machines with tapes. They have not studied abstract algebra beyond rings as a name, tensor products, Nussbaumer or Schönhage–Strassen transforms, or any research-level multiplication algorithm.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes
- Fixed multitape Turing machine model
- Schönhage–Strassen n log n optimality conjecture
  - $n$ (input length): The number of bits in each input integer.
- Multiplication as convolution of digit lists
- Polynomial ring modulo y^r + 1
  - $y$ (polynomial variable): The indeterminate of the polynomials.
  - $r$ (ring degree): The number of complex coefficients in a polynomial, a power of two.
- Chinese-remainder address map onto prime axes
- Linear networks with roles and frames
- Three-element-subset finite networks
  - $s$ (number of calls): The number of smaller calls the network makes.
  - $W$ (number of roles): The number of wires (roles) of the network.
  - $m$ (space dimension): The dimension of the fixed space whose subspaces label the network.
- Scratch-restoring exchange network
- Recursive power saving
  - $s$ (number of calls): The number of smaller calls.
  - $W$ (number of roles): The number of roles of the network.
  - $m$ (parameter multiplier): The factor by which the recursive parameter grows.
- Elementary scans and controlled shifts
- Lower triangular factorization
  - $m$ (matrix size): The number of rows and columns of the matrix.
  - $a$ (matrix rank): The rank of the matrix.
- Rational matrix shear of address fields
- Logarithms and iterated logarithms (also: lg, log base 2, log n, lg n)
- Binary representation and bit operations (also: bits, XOR, bit position, binary expansion, radix representation)
- Schoolbook and Karatsuba multiplication (also: grade-school multiplication, long multiplication, quadratic multiplication, Karatsuba)
- Fast Fourier transform algorithm (also: FFT, Cooley-Tukey, fast Fourier transform)
- Convolution (also: cyclic convolution, product of coefficient sequences, polynomial multiplication as convolution)
- Modular arithmetic and congruences (also: mod, residues, congruence classes, cyclic group Z/n)
- Primes and coprimality (also: distinct primes, relatively prime, gcd, greatest common divisor, prime number theorem)
- Chinese remainder theorem (also: CRT)
- Matrices, rank and invertibility (also: linear maps, matrix product, invertible matrix, lower triangular matrix, matrix rank, identity matrix)
- Vector spaces and subspaces (also: change of basis, linear subspace, linear independence, basis)
- Permutations (also: permutation matrix, partial permutation, bijection of indices)
- Floor, ceiling and rounding (also: nearest integer, floor function, integer part)
- Recursion and recurrence relations (also: divide and conquer, recurrence, master theorem, recursive calls)
- Fixed-point and dyadic arithmetic (also: fixed-point numbers, dyadic rationals, truncation error, rounding error)
- Complex conjugate and modulus (also: conjugate, absolute value of complex number, Gaussian integers)
- Cartesian products and multi-indexing (also: multidimensional array, tuple indices, product of index sets)
- Linear-time scans and tape sorting (also: sorting on tapes, copying a tape, linear scan, tape reversal)
- Deterministic computation and time complexity classes (also: deterministic algorithm, running time, step count, worst-case time)
- Geometric and power-of-two parameter manipulation (also: powers of two, geometric series, exponent inequalities)

## This page

Concept: Fast address-field interchange
Gloss: Interchanges two disjoint address fields of u bits via pointwise XOR combinations that end as an exact permutation, in O(V u^τ) with τ<1.
Heading: Address interchange in time $O(Vu^\tau)$

The symbols in this page's heading denote (say so on the page):

- $V$ (bit volume): The number of stored bits.
- $u$ (field width): The number of bits in each interchanged address field.
- $\tau$ (saving exponent): A fixed constant below 1.

## This page in the argument

The step: Two disjoint address fields of $u$ bits are interchanged in $O(Vu^\tau)$ steps for a fixed $\tau<1$ (fast address interchange).
How: build a linear network that exchanges two banks of values with restored auxiliaries, turn each edge into smaller interchanges, and recurse
Why: Scanning $\Theta(n)$ bits at each of $\Theta(\log n)$ levels costs $n\log n$; a recurrence whose calls total fewer than the width times the parameter gains a power. (the sources say so: "is the source of the power saving." (paper))
Striking feature: The final effect is an exact permutation although the intermediate steps are XOR combinations of data, correct for arbitrary initial auxiliary values; and the exponent is strictly below 1. (explain why it holds, from the method)

Its sub-steps, in order:

- A fixed eight-row network of copy, gather, scatter and side-injection gates adds $x_S$ to $y_S$ for arbitrary initial scratch values, and three stages exchange $(X,Y)$ to $(-Y,X)$. (on [Scratch-restoring exchange network](scalar-motif-network.md))
- Giving each gate an invertible frame on the arrays, the intermediate frames cancel, so a route applies only the endpoint operator. (on [Linear networks with roles and frames](linear-network-frames.md))
- Three-element-subset networks with nested subspaces at the gates have total edge rank $s<Wm$ for $W$ wires and dimension $m$. (on [Three-element-subset finite networks](subset-network.md))
- A recursive call at parameter $mf$ uses $s$ calls at parameter $f$ on volume $V/W$, adding $s/W<m$ per level, which gives a power saving. (on [Recursive power saving](recursive-saving.md))
- Every rational matrix of rank $a$ factors as $E_1\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\Pi$ a partial permutation with $a$ ones, so it can be applied in tape order. (on [Lower triangular factorization](lower-triangular-factorization.md))
- A shear $(H,D)\mapsto(H+AD,D)$ of rank $a$ costs $a$ interchanges of $b$-digit fields plus $O(V)$ work. (on [Rational matrix shear of address fields](matrix-shear.md))
- Chunks of $e=m^k$ digits can be interchanged in $O(Ve^\tau)$ time by recursion on the network.
- Removing the power and row restrictions, two $u$-bit address fields are interchanged in $O(Vu^\tau)$ steps for a fixed $\tau<1$.

It serves these steps, from the main result down:

- Integer multiplication of $n$-bit integers takes $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$ on one fixed multitape machine.; how: reduce to digit convolution, build the fast tape and ring-transform tools bottom up, then assemble reductions, precision and cost (on [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md))
- The two tape procedures, fast address interchange and simultaneous butterfly layers, exist with power savings.; how: construct each procedure from its own fixed linear network, after the elementary scans

## Steps this page derives

The argument gives this page these sub-steps of its step (S2.2.7, S2.2.8). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S2.2.7**: Chunks of $e=m^k$ digits can be interchanged in $O(Ve^\tau)$ time by recursion on the network.
Source: "The chunks can be interchanged in $O(Ve^\tau)$ time, preserving every" (paper)
> \begin{proposition}[Power-width interchange with rows] \label{prop:power-interchange} Assume the fixed circuit data satisfy \eqref{eq:finite-shear-contract}, and let $q$ be a prime as in Lemma~\ref{lem:matrix-shear} for its edge matrices, also avoiding the denominators of every assigned terminal and gate matrix $M$. Choose a rational number $\tau\in(0,1)$ with $s/W<m^\tau$. For every $e=m^k$, $k\ge0$, consider two disjoint contiguous address chunks of $e$ radix-$q$ digits each. Suppose a row field preceding both chunks has length divisible by $W^k$. There may be additional fields before and after the row field, between the chunks, and after them. The chunks can be interchanged in $O(Ve^\tau)$ time, preserving every other address field, on a fixed number of finite-alphabet tapes. The constant is independent of all field lengths and of the data. \end{proposition}

**S2.2.8**: Removing the power and row restrictions, two $u$-bit address fields are interchanged in $O(Vu^\tau)$ steps for a fixed $\tau<1$.
Source: "in $O(Vu^\tau)$ steps, where $V=PG B\,2^{2u}$." (paper)
> \begin{lemma}[Arbitrary-width interchange] \label{lem:chunk-swap} There exist fixed $0<\tau<1$ and one fixed finite-alphabet multitape procedure with the following property. For positive integers $P,G,B$ and $u\ge1$, it transforms an arbitrary bit array on \[ [P]\times[2^u]\times[G]\times[2^u]\times[B] \] by the address permutation \[ (p,h,g,d,z)\longmapsto(p,d,g,h,z) \] in $O(Vu^\tau)$ steps, where $V=PG B\,2^{2u}$. The integers specifying the shape are part of the input. The time includes their processing, all padding and unpadding, and fixed-tape workspace cleanup. In particular, $B=1$ is allowed. \end{lemma}

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S2.2.1 (on [Scratch-restoring exchange network](scalar-motif-network.md)): A fixed eight-row network of copy, gather, scatter and side-injection gates adds $x_S$ to $y_S$ for arbitrary initial scratch values, and three stages exchange $(X,Y)$ to $(-Y,X)$.
- S2.2.2 (on [Linear networks with roles and frames](linear-network-frames.md)): Giving each gate an invertible frame on the arrays, the intermediate frames cancel, so a route applies only the endpoint operator.
- S2.2.3 (on [Three-element-subset finite networks](subset-network.md)): Three-element-subset networks with nested subspaces at the gates have total edge rank $s<Wm$ for $W$ wires and dimension $m$.
- S2.2.4 (on [Recursive power saving](recursive-saving.md)): A recursive call at parameter $mf$ uses $s$ calls at parameter $f$ on volume $V/W$, adding $s/W<m$ per level, which gives a power saving.
- S2.2.5 (on [Lower triangular factorization](lower-triangular-factorization.md)): Every rational matrix of rank $a$ factors as $E_1\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\Pi$ a partial permutation with $a$ ones, so it can be applied in tape order.
- S2.2.6 (on [Rational matrix shear of address fields](matrix-shear.md)): A shear $(H,D)\mapsto(H+AD,D)$ of rank $a$ costs $a$ interchanges of $b$-digit fields plus $O(V)$ work.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Linear networks with roles and frames](linear-network-frames.md): A fixed linear network of gates exchanging banks of values with signs, restoring auxiliary values; each wire is a role and each gate has an invertible frame so intermediate frames cancel.
  Shown as: Fast address-field interchange *<predicate>* Linear networks with roles and frames
- [Recursive power saving](recursive-saving.md): Recursing at parameter mf with s calls of parameter f on volume V/W adds s/W<m per level, a strict inequality that gives a power saving.
  Shown as: Fast address-field interchange *<predicate>* Recursive power saving
- [Rational matrix shear of address fields](matrix-shear.md): The frame Φ_M moving the entry at address (H,D) to (H+MD,D); a shear of rank a costs a smaller interchanges.
  Shown as: Fast address-field interchange *<predicate>* Rational matrix shear of address fields
- [Scratch-restoring exchange network](scalar-motif-network.md): Eight-row schedule of copy, gather, scatter and side-injection gates adding x_S to y_S for arbitrary initial scratch values; three stages give the exchange (X,Y) → (−Y,X).
  Shown as: Fast address-field interchange *<predicate>* Scratch-restoring exchange network

## Pages that build on this one

- Simultaneous butterfly layers: Applies H₀ at the same bit position of up to d address chunks at once on complex fixed-point records, in O(V d^λ′) with λ′<1.
- Retained frequency order and transform layout: Selected bits of the participating axes are placed at a common offset in K-bit chunks so the simultaneous layers apply, and the frequency order is retained through the pointwise product.
- Tensor interface for growing dimension: Applies the one-dimensional resampling maps line by line along d axes, using chunk swaps to move axes, giving R F_s = 2^γ B₀ Q F_t A.
- Fixed rational parameter choice: The fixed exponents (τ=σ=1−2⁻⁵⁰, λ′=1−2⁻⁵⁴, ε=2⁻⁷⁵, κ=2⁻¹⁸²) and size parameters p=6b, d=⌊b^ε⌋ making all costs fit the theorem.
- Integer multiplication in O(n (lg n)^(1−κ)) time: Deterministic fixed-tape machine multiplying n-bit integers in O(n (lg n)^(1−κ)), κ=2^−182: digit convolution, CRT prime axes, Gaussian resampling and chirps, synthetic transforms over the y^r+1 ring, accelerated by fast address interchange and butterfly layers.

## Other pages you may link to

- [Multiplication as convolution of digit lists](convolution-reduction.md)
- [Polynomial ring modulo y^r + 1](polyring-mod.md)
- [Chinese-remainder address map onto prime axes](chinese-remainder-map.md)
- [Fixed multitape Turing machine model](multitape-model.md)
- [Schönhage–Strassen n log n optimality conjecture](nlogn-conjecture.md)
- [Elementary scans and controlled shifts](controlled-shifts.md)
- [Three-element-subset finite networks](subset-network.md)
- [Lower triangular factorization](lower-triangular-factorization.md)
- [Signed packing (Kronecker substitution)](signed-packing.md)
- [Established O(n log n) multiplier as subroutine](hvdh-subroutine.md)
- [Discrete Fourier transform](fourier-transform.md)
- [Multidimensional transform](multidim-transform.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Two-point butterfly H₀](butterfly.md)
- [Phase frames for the butterfly layer](phase-frames.md)
- [Simultaneous butterfly layers](fast-butterfly-layer.md)
- [Fixed-point precision and exact recovery](exact-recovery.md)
- [Synthetic character cancellation](synthetic-character-cancellation.md)
- [Retained frequency order and transform layout](transform-layout.md)
- [Normalized convolution over the ring](normalized-convolution.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Resampling without executing permutations](resampling-lemma.md)
- [Tensor interface for growing dimension](tensor-resampling.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Chirp and permutation cancellation](chirp-permutation-cancellation.md)
- [Fixed rational parameter choice](parameter-choice.md)
- [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "The chunks can be interchanged in $O(Ve^\tau)$ time" (paper)

  > \begin{proposition}[Power-width interchange with rows] \label{prop:power-interchange} Assume the fixed circuit data satisfy \eqref{eq:finite-shear-contract}, and let $q$ be a prime as in Lemma~\ref{lem:matrix-shear} for its edge matrices, also avoiding the denominators of every assigned terminal and gate matrix $M$. Choose a rational number $\tau\in(0,1)$ with $s/W<m^\tau$. For every $e=m^k$, $k\ge0$, consider two disjoint contiguous address chunks of $e$ radix-$q$ digits each. Suppose a row field preceding both chunks has length divisible by $W^k$. There may be additional fields before and after the row field, between the chunks, and after them. The chunks can be interchanged in $O(Ve^\tau)$ time, preserving every other address field, on a fixed number of finite-alphabet tapes. The constant is independent of all field lengths and of the data. \end{proposition}

- "Its cost is $O(Vu^\tau)$ for a fixed $\tau<1$." (paper)

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

Write the body to `exegenius/tasks/0016-write-address-interchange.answer.md` and the JSON to `exegenius/tasks/0016-write-address-interchange.answer.json`, then run `exegenius submit 0016-write-address-interchange` in the project directory. If submit rejects the answer, fix the answer and submit again.
